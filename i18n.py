from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path

from PyQt6.QtCore import QEvent, QLibraryInfo, QObject, QTranslator
from PyQt6.QtWidgets import (
    QAbstractButton, QAbstractSpinBox, QApplication, QComboBox, QGroupBox,
    QLabel, QMenu, QMessageBox, QProgressBar, QTabWidget, QTableWidget, QWidget,
)


LANGUAGES = ("pt-BR", "es", "en")
_CATALOG_PATH = Path(__file__).resolve().parent / "translations" / "ui.json"
_WEEKDAYS = {
    "pt-BR": ("seg", "ter", "qua", "qui", "sex", "sáb", "dom"),
    "es": ("lun", "mar", "mié", "jue", "vie", "sáb", "dom"),
    "en": ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"),
}
_MONTHS = {
    "pt-BR": (
        "jan", "fev", "mar", "abr", "mai", "jun",
        "jul", "ago", "set", "out", "nov", "dez",
    ),
    "es": (
        "ene", "feb", "mar", "abr", "may", "jun",
        "jul", "ago", "sep", "oct", "nov", "dic",
    ),
    "en": (
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
    ),
}


def _load_catalog() -> dict[str, dict[str, str]]:
    data = json.loads(_CATALOG_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or any(
        language not in data or not isinstance(data[language], dict)
        for language in LANGUAGES
    ):
        raise ValueError(f"Invalid interface translation catalog: {_CATALOG_PATH}")
    for language in LANGUAGES:
        for source, translated in data[language].items():
            if not isinstance(source, str) or not isinstance(translated, str):
                raise ValueError(f"Invalid {language} translation entry in {_CATALOG_PATH}")
            if set(re.findall(r"\{([a-zA-Z_]\w*)\}", source)) != set(
                re.findall(r"\{([a-zA-Z_]\w*)\}", translated)
            ):
                raise ValueError(f"Translation placeholders differ for {language}: {source}")
    return data


class LanguageManager(QObject):
    def __init__(self, app: QApplication, language: str = "pt-BR"):
        super().__init__(app)
        if language not in LANGUAGES:
            raise ValueError(f"Unsupported interface language: {language}")
        previous = app.property("_jtia_language_manager")
        if isinstance(previous, LanguageManager) and previous is not self:
            previous._detach()
        self._app = app
        self._catalog = _load_catalog()
        self._language = language
        self._patterns: dict[str, list[tuple[re.Pattern[str], str]]] = {}
        self._reverse: dict[str, str] = {}
        for catalog in self._catalog.values():
            for source, translated in catalog.items():
                self._reverse.setdefault(translated, source)
        self._translating = False
        self._qt_translator: QTranslator | None = None
        self._set_qt_language(language)
        app.installEventFilter(self)
        app.setProperty("_jtia_language_manager", self)

    @property
    def language(self) -> str:
        return self._language

    def translate(self, text: str) -> str:
        catalog = self._catalog[self._language]
        # Widgets may be created with an already translated _t(...) value.
        text = self._reverse.get(text, text) if text not in catalog else text
        translated = catalog.get(text)
        if translated is not None:
            return translated

        patterns = self._patterns.get(self._language)
        if patterns is None:
            patterns = []
            for source, target in catalog.items():
                if "{" not in source:
                    continue
                escaped = re.escape(source)
                fields: set[str] = set()

                def field_pattern(match: re.Match[str]) -> str:
                    name = match.group(1)
                    if name in fields:
                        return rf"(?P={name})"
                    fields.add(name)
                    return rf"(?P<{name}>.*?)"

                pattern = re.sub(
                    r"\\\{([a-zA-Z_]\w*)\\\}",
                    field_pattern,
                    escaped,
                )
                patterns.append((re.compile(f"^{pattern}$", re.DOTALL), target))
            for other_language, other_catalog in self._catalog.items():
                if other_language == self._language:
                    continue
                for source, rendered in other_catalog.items():
                    if "{" not in rendered or source not in catalog:
                        continue
                    fields = set()
                    pattern = re.sub(
                        r"\\\{([a-zA-Z_]\w*)\\\}", field_pattern, re.escape(rendered),
                    )
                    patterns.append((
                        re.compile(f"^{pattern}$", re.DOTALL), catalog[source],
                    ))
            self._patterns[self._language] = patterns

        for pattern, target in patterns:
            match = pattern.fullmatch(text)
            if match:
                return target.format(**match.groupdict())
        return text

    def format_date(self, value: datetime) -> str:
        weekday = _WEEKDAYS[self._language][value.weekday()]
        month = _MONTHS[self._language][value.month - 1]
        return f"{weekday} {value.day:02d} {month} {value.year}"

    def set_language(self, language: str) -> None:
        if language not in LANGUAGES:
            raise ValueError(f"Unsupported interface language: {language}")
        self._language = language
        self._set_qt_language(language)
        for widget in self._app.allWidgets():
            self.translate_widget(widget)
            widget.updateGeometry()
            widget.update()

    def _set_qt_language(self, language: str) -> None:
        if self._qt_translator is not None:
            self._app.removeTranslator(self._qt_translator)
            self._qt_translator.deleteLater()
            self._qt_translator = None
        if language == "en":
            return
        locale = {"pt-BR": "pt_BR", "es": "es"}[language]
        translator = QTranslator(self)
        directory = QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
        if translator.load(f"qtbase_{locale}", directory):
            self._app.installTranslator(translator)
            self._qt_translator = translator
        else:
            translator.deleteLater()
            print(
                f"[i18n] Qt translation qtbase_{locale} unavailable in {directory}; "
                "built-in Qt controls may remain in English."
            )

    def _detach(self) -> None:
        if self._qt_translator is not None:
            self._app.removeTranslator(self._qt_translator)
            self._qt_translator.deleteLater()
            self._qt_translator = None
        self._app.removeEventFilter(self)

    def translate_widget(self, widget: QWidget) -> None:
        if self._translating:
            return
        self._translating = True
        try:
            if isinstance(widget, (QAbstractButton, QLabel, QMessageBox)):
                self._translate_value(widget, "text", "setText", "text")
            if isinstance(widget, (QGroupBox, QMenu)):
                self._translate_value(widget, "title", "setTitle", "title")
            if isinstance(widget, QMessageBox):
                self._translate_value(
                    widget, "informativeText", "setInformativeText", "informative"
                )
            if isinstance(widget, QAbstractSpinBox):
                self._translate_value(widget, "prefix", "setPrefix", "prefix")
                self._translate_value(widget, "suffix", "setSuffix", "suffix")
                self._translate_value(
                    widget, "specialValueText", "setSpecialValueText", "special_value"
                )
            if isinstance(widget, QProgressBar):
                self._translate_value(widget, "format", "setFormat", "format")
            self._translate_value(
                widget, "placeholderText", "setPlaceholderText", "placeholder"
            )
            self._translate_value(widget, "toolTip", "setToolTip", "tooltip")
            self._translate_value(
                widget, "windowTitle", "setWindowTitle", "window_title"
            )
            for action in widget.actions():
                self._translate_value(action, "text", "setText", "text")
                self._translate_value(action, "toolTip", "setToolTip", "tooltip")
            if isinstance(widget, QTableWidget):
                for count, getter in (
                    (widget.columnCount(), widget.horizontalHeaderItem),
                    (widget.rowCount(), widget.verticalHeaderItem),
                ):
                    for index in range(count):
                        item = getter(index)
                        if item is not None:
                            self._translate_value(item, "text", "setText", "text")

            if isinstance(widget, QComboBox):
                sources = getattr(widget, "_i18n_item_sources", {})
                rendered = getattr(widget, "_i18n_item_rendered", {})
                signals_were_blocked = widget.blockSignals(True)
                try:
                    for index in range(widget.count()):
                        current = widget.itemText(index)
                        old_source = sources.get(index)
                        old_rendered = rendered.get(index)
                        source = (
                            old_source
                            if old_source is not None
                            and current in (old_source, old_rendered)
                            else current
                        )
                        translated = self.translate(source)
                        sources[index] = source
                        rendered[index] = translated
                        if translated != current:
                            widget.setItemText(index, translated)
                finally:
                    widget.blockSignals(signals_were_blocked)
                widget._i18n_item_sources = sources
                widget._i18n_item_rendered = rendered

            if isinstance(widget, QTabWidget):
                sources = getattr(widget, "_i18n_tab_sources", {})
                rendered = getattr(widget, "_i18n_tab_rendered", {})
                for index in range(widget.count()):
                    current = widget.tabText(index)
                    old_source = sources.get(index)
                    old_rendered = rendered.get(index)
                    source = (
                        old_source
                        if old_source is not None
                        and current in (old_source, old_rendered)
                        else current
                    )
                    translated = self.translate(source)
                    sources[index] = source
                    rendered[index] = translated
                    if translated != current:
                        widget.setTabText(index, translated)
                widget._i18n_tab_sources = sources
                widget._i18n_tab_rendered = rendered
        finally:
            self._translating = False

    def _translate_value(
        self, widget: object, getter_name: str, setter_name: str, slot: str
    ) -> None:
        getter = getattr(widget, getter_name, None)
        setter = getattr(widget, setter_name, None)
        if not callable(getter) or not callable(setter):
            return
        current = getter()
        if not current:
            return

        source_attr = f"_i18n_{slot}_source"
        rendered_attr = f"_i18n_{slot}_rendered"
        old_source = getattr(widget, source_attr, None)
        old_rendered = getattr(widget, rendered_attr, None)
        source = (
            old_source
            if old_source is not None and current in (old_source, old_rendered)
            else current
        )
        translated = self.translate(source)
        setattr(widget, source_attr, source)
        setattr(widget, rendered_attr, translated)
        if translated != current:
            setter(translated)

    def eventFilter(self, watched, event) -> bool:
        if not self._translating and event.type() in (
            QEvent.Type.Show,
            QEvent.Type.Paint,
            QEvent.Type.ToolTip,
        ) and isinstance(watched, QWidget):
            self.translate_widget(watched)
        return super().eventFilter(watched, event)
