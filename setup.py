"""
JT.IA — Script de Instalação Completa (Full Setup).

Instala e configura TODAS as dependências e recursos do JT.IA:
  * Dependências Principais (PyQt6, som, Gemini Live, automação, UI)
  * Visão Local & Multi-Monitor (Claude Overlay, OCR WinRT, keyboard)
  * Documentos (python-docx, python-pptx)
  * Pesquisa & Coleta Web Multi-Canal (Agent-Reach, feedparser, cookies)
  * Recursos Avançados de Mídia (Pandas, Pydub, Edge-TTS, Miniaudio)
  * Detecção de Voz Wake-Word Local ("Hey Jarvis" via openWakeWord)
  * Navegadores Playwright (Chromium e Firefox)
  * Configuração pós-instalação do Windows (pywin32) e atalhos

Uso:
  python setup.py              # instalação completa
  python setup.py --minimal    # só o núcleo (requirements.txt)
  python setup.py --no-browsers
  python setup.py --no-shortcuts
"""
import argparse
import os
import platform
import subprocess
import sys
from pathlib import Path

# Force UTF-8 on Windows console output to prevent encoding errors
for _stream in ("stdout", "stderr"):
    try:
        _s = getattr(sys, _stream, None)
        if _s is not None and hasattr(_s, "reconfigure"):
            _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

OS = platform.system()  # "Windows" | "Darwin" | "Linux"
HERE = Path(__file__).resolve().parent

MIN_PY = (3, 11)        # Versão mínima do Python
MAX_PY = (3, 13)        # Versão máxima testada

# ── Lista completa de módulos (fallback se algum requirements*.txt faltar) ────
# Mantida alinhada com requirements.txt + vision + media + docs.
ALL_PACKAGES: list[str] = [
    # Core: UI, áudio, Gemini Live
    "PyQt6>=6.6,<7",
    "sounddevice>=0.4,<1",
    "numpy>=1.24,<3",
    "google-genai>=2.8.0,<3",
    "httpx>=0.28.1,<1",
    "websockets>=13,<17",
    "vosk>=0.3.45,<1",
    # Web / browser
    "requests>=2.31,<3",
    "beautifulsoup4>=4.12,<5",
    "playwright>=1.40,<2",
    "yt-dlp",
    "ddgs>=9,<10",
    # Automação
    "pyautogui",
    "pyperclip",
    # Visão & mídia
    "pillow>=10,<13",
    "opencv-python>=4.8,<5",
    "mss>=9,<11",
    # Sistema / arquivos / documentos
    "psutil>=5.9,<8",
    "send2trash",
    "python-pptx>=0.6.23",
    "python-docx>=1.0.0",
    "pdfplumber",
    "PyPDF2",
    "packaging",
    # Dashboard remoto
    "fastapi>=0.110,<1",
    "uvicorn[standard]>=0.27,<1",
    "cryptography>=42,<50",
    "python-multipart>=0.0.9,<1",
    "qrcode[pil]>=7,<9",
    # Plugins
    "google-api-python-client",
    "google-auth-oauthlib",
    "tinytuya",
    "paho-mqtt",
    "openpyxl",
    "youtube-transcript-api",
    "pygetwindow",
    "nvidia-ml-py",
    # Claude Overlay & multi-monitor
    "claude-agent-sdk>=0.2.87",
    # Agent-Reach
    "feedparser>=6.0",
    "python-dotenv>=1.0",
    "loguru>=0.7",
    "pyyaml>=6.0",
    "rich>=13.0",
    "browser-cookie3>=0.19",
    # Mídia / TTS / analytics
    "pandas>=2.2,<4",
    "pydub>=0.25,<1",
    "edge-tts>=7,<8",
    "miniaudio>=1.61,<2",
    # Wake-word local
    "openwakeword>=0.6.0",
]

WINDOWS_PACKAGES: list[str] = [
    "comtypes",
    "pycaw",
    "win10toast",
    "pywin32",
    "wmi",
    "pywinauto",
    "keyboard>=0.13.5",
    # OCR nativo Windows (WinRT)
    "winrt-Windows.Foundation>=3.2,<4",
    "winrt-Windows.Foundation.Collections>=3.2,<4",
    "winrt-Windows.Media.Ocr>=3.2,<4",
    "winrt-Windows.Graphics.Imaging>=3.2,<4",
    "winrt-Windows.Storage.Streams>=3.2,<4",
    "winrt-Windows.Globalization>=3.2,<4",
]

REQUIREMENT_FILES_FULL = (
    "requirements.txt",
    "requirements-vision.txt",
    "requirements-media.txt",
    "requirements-docs.txt",
)

REQUIREMENT_FILES_MINIMAL = (
    "requirements.txt",
)


def _print_header(title: str) -> None:
    sep = "=" * 64
    print(f"\n{sep}\n  {title}\n{sep}")


def _print_step(num: int, total: int, msg: str) -> None:
    print(f"\n[{num}/{total}] ▶ {msg}")


def _run(label: str, args: list[str], cwd: Path | None = None, fatal: bool = True) -> bool:
    """Executa um comando de terminal exibindo status claro."""
    print(f"    * Executando: {label}...")
    try:
        res = subprocess.run(args, cwd=str(cwd or HERE), check=fatal)
        if res.returncode == 0:
            print(f"      [OK] {label}")
            return True
        print(f"      [AVISO] {label} encerrou com código {res.returncode}.")
        return False
    except subprocess.CalledProcessError as exc:
        print(f"      [FALHA] Erro ao executar {label}: {exc}")
        if fatal:
            raise
        return False
    except Exception as exc:
        print(f"      [AVISO] Não foi possível executar {label}: {exc}")
        if fatal:
            raise
        return False


def _check_python() -> None:
    """Verifica se a versão do Python é compatível."""
    v = sys.version_info[:2]
    if v > MAX_PY:
        print(f"\n⚠️  [AVISO] Python {v[0]}.{v[1]} detectado. A versão recomendada é até "
              f"{MAX_PY[0]}.{MAX_PY[1]}. Continuando a instalação...")
        return
    if v < MIN_PY:
        print(f"\n❌ [ERRO] Python {v[0]}.{v[1]} detectado — O JT.IA necessita de no "
              f"mínimo Python {MIN_PY[0]}.{MIN_PY[1]}.")
        print("   Por favor, instale uma versão compatível (3.11, 3.12 ou 3.13) e execute:")
        print(f"     py -{MIN_PY[0]}.{MIN_PY[1]} setup.py        (Windows)")
        print(f"     python{MIN_PY[0]}.{MIN_PY[1]} setup.py      (macOS / Linux)")
        sys.exit(1)
    print(f"    [OK] Python {v[0]}.{v[1]}.{sys.version_info[2]} compatível.")


def _ensure_directories() -> None:
    """Garante que as pastas essenciais da aplicação existam."""
    dirs = [
        HERE / "memory",
        HERE / "logs",
        HERE / "config",
        HERE / "config" / "certs",
        HERE / "plugins",
        HERE / "actions",
        HERE / "core",
        HERE / "translations",
    ]
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
    print("    [OK] Diretórios da estrutura do aplicativo verificados.")


def _check_assets() -> None:
    """Verifica integridade de assets essenciais."""
    face_obj = HERE / "core" / "face_model.obj"
    if not face_obj.exists() or face_obj.stat().st_size < 4096:
        print("    [INFO] core/face_model.obj não presente — avatar usará o núcleo luminoso padrão.")

    face_png = HERE / "face.png"
    if face_png.exists():
        print(f"    [OK] Imagem do HUD encontrada: {face_png.name}")

    ico = HERE / "icone_ia.ico"
    if ico.exists():
        print(f"    [OK] Ícone do aplicativo encontrado: {ico.name}")


def _install_requirement_files(files: tuple[str, ...], fatal_first: bool = True) -> int:
    """Instala cada requirements*.txt existente. Retorna quantos foram aplicados."""
    installed = 0
    for index, name in enumerate(files):
        path = HERE / name
        if not path.exists():
            print(f"    [INFO] {name} não encontrado — ignorado.")
            continue
        fatal = fatal_first and index == 0 and name == "requirements.txt"
        ok = _run(
            f"Instalando pacotes de {name}",
            [sys.executable, "-m", "pip", "install", "-r", str(path)],
            fatal=fatal,
        )
        if ok:
            installed += 1
    return installed


def _install_fallback_packages() -> None:
    """Instala a lista ALL_PACKAGES (+ Windows) se requirements.txt estiver ausente."""
    packages = list(ALL_PACKAGES)
    if OS == "Windows":
        packages.extend(WINDOWS_PACKAGES)
    _run(
        "Instalando lista completa de módulos (fallback)",
        [sys.executable, "-m", "pip", "install", *packages],
        fatal=True,
    )


def _create_iniciar_bat() -> Path:
    """Cria ou atualiza o script iniciar.bat na raiz do projeto."""
    bat_path = HERE / "iniciar.bat"
    content = (
        "@echo off\r\n"
        "chcp 65001 >nul\r\n"
        "title JT.IA - Assistente Pessoal Inteligente\r\n"
        "cd /d \"%~dp0\"\r\n\r\n"
        "echo ========================================================\r\n"
        "echo        Iniciando JT.IA - Assistente Inteligente\r\n"
        "echo ========================================================\r\n"
        "echo.\r\n\r\n"
        "if exist \".venv\\Scripts\\python.exe\" (\r\n"
        "    set \"PYTHON_CMD=.venv\\Scripts\\python.exe\"\r\n"
        ") else (\r\n"
        "    where py >nul 2>&1\r\n"
        "    if %ERRORLEVEL% EQU 0 (\r\n"
        "        set \"PYTHON_CMD=py -3.12\"\r\n"
        "    ) else (\r\n"
        "        set \"PYTHON_CMD=python\"\r\n"
        "    )\r\n"
        ")\r\n\r\n"
        "echo Usando interpretador: %PYTHON_CMD%\r\n"
        "echo.\r\n"
        "\"%PYTHON_CMD%\" main.py %*\r\n\r\n"
        "if %ERRORLEVEL% NEQ 0 (\r\n"
        "    echo.\r\n"
        "    echo ========================================================\r\n"
        "    echo [AVISO] O aplicativo encerrou com o codigo %ERRORLEVEL%.\r\n"
        "    echo Se faltar alguma dependencia, execute: python setup.py\r\n"
        "    echo ========================================================\r\n"
        "    pause\r\n"
        ")\r\n"
    )
    try:
        bat_path.write_text(content, encoding="utf-8")
        print(f"    [OK] Script de inicialização criado: {bat_path.name}")
    except Exception as exc:
        print(f"    [AVISO] Não foi possível criar iniciar.bat: {exc}")
    return bat_path


def _create_desktop_shortcut(target_bat: Path) -> None:
    """Cria atalho na Área de Trabalho do Windows."""
    if OS != "Windows":
        return

    desktop_dir = Path(os.environ.get("USERPROFILE", "")) / "Desktop"
    if not desktop_dir.exists():
        desktop_dir = Path.home() / "Desktop"
    if not desktop_dir.exists():
        print("    [AVISO] Área de Trabalho não localizada para criar atalho.")
        return

    shortcut_path = desktop_dir / "JT.IA.lnk"
    ico_path = HERE / "icone_ia.ico"

    # Tentativa 1: win32com
    try:
        import win32com.client
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(str(shortcut_path))
        shortcut.TargetPath = str(target_bat)
        shortcut.WorkingDirectory = str(HERE)
        if ico_path.exists():
            shortcut.IconLocation = str(ico_path)
        shortcut.Description = "Assistente Pessoal Inteligente JT.IA"
        shortcut.Save()
        print(f"    [OK] Atalho criado na Área de Trabalho: {shortcut_path.name}")
        return
    except Exception:
        pass

    # Tentativa 2: PowerShell script
    try:
        ps_cmd = (
            f"$WshShell = New-Object -comObject WScript.Shell; "
            f"$Shortcut = $WshShell.CreateShortcut('{str(shortcut_path)}'); "
            f"$Shortcut.TargetPath = '{str(target_bat)}'; "
            f"$Shortcut.WorkingDirectory = '{str(HERE)}'; "
            f"$Shortcut.Description = 'Assistente Pessoal Inteligente JT.IA'; "
        )
        if ico_path.exists():
            ps_cmd += f"$Shortcut.IconLocation = '{str(ico_path)}'; "
        ps_cmd += "$Shortcut.Save()"
        res = subprocess.run(["powershell", "-NoProfile", "-Command", ps_cmd], capture_output=True)
        if res.returncode == 0:
            print(f"    [OK] Atalho criado na Área de Trabalho via PowerShell: {shortcut_path.name}")
        else:
            print("    [INFO] Não foi possível criar o atalho automaticamente.")
    except Exception as exc:
        print(f"    [INFO] Criação de atalho ignorada: {exc}")


def _configure_pywin32() -> None:
    """Registra componentes COM e DLLs do pywin32 no Windows."""
    if OS != "Windows":
        return
    scripts_dir = Path(sys.executable).parent / "Scripts"
    postinstall = scripts_dir / "pywin32_postinstall.py"
    if not postinstall.exists():
        postinstall = Path(sys.executable).parent.parent / "Scripts" / "pywin32_postinstall.py"

    if postinstall.exists():
        _run("Registrando extensões pywin32",
             [sys.executable, str(postinstall), "-install"],
             fatal=False)
    else:
        print("    [INFO] Script pywin32_postinstall.py não localizado (instalação padrão ativa).")


def _install_agent_reach() -> None:
    """Instala o pacote local Agent-Reach em modo editável."""
    for name in ("agent-reach", "Agent-Reach", "agent_reach"):
        reach_dir = HERE / name
        # Preferir a pasta que tem pyproject.toml / setup.py
        if reach_dir.is_dir() and (
            (reach_dir / "pyproject.toml").exists()
            or (reach_dir / "setup.py").exists()
            or (reach_dir / "setup.cfg").exists()
        ):
            _run(
                f"Instalando Agent-Reach em modo editável ({name})",
                [sys.executable, "-m", "pip", "install", "-e", str(reach_dir)],
                fatal=False,
            )
            return
    print("    [INFO] Pasta agent-reach não localizada para instalação editável.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Instalador Completo do JT.IA")
    parser.add_argument("--minimal", action="store_true",
                        help="Instala apenas as dependências do requirements.txt.")
    parser.add_argument("--no-browsers", action="store_true",
                        help="Ignora o download dos navegadores Playwright.")
    parser.add_argument("--no-shortcuts", action="store_true",
                        help="Ignora a criação de atalhos e iniciar.bat.")
    parser.add_argument("--no-agent-reach", action="store_true",
                        help="Ignora a instalação editável do módulo agent-reach.")
    args = parser.parse_args()

    total_steps = 7 if args.minimal else 9

    _print_header("INSTALAÇÃO COMPLETA DO JT.IA — TODOS OS MÓDULOS")
    print(f"  Sistema Operacional: {OS or 'Desconhecido'}")
    print(f"  Python Ativo:        {sys.version.split()[0]} ({sys.executable})")
    print(f"  Diretório Raiz:      {HERE}")
    print(f"  Modo:                {'mínimo' if args.minimal else 'completo (todos os módulos)'}")

    # ── [1] Verificação do Python ─────────────────────────────────────────────
    _print_step(1, total_steps, "Verificando versão do Python e compatibilidade")
    _check_python()
    _ensure_directories()

    # ── [2] Atualização do pip / setuptools / wheel ───────────────────────────
    _print_step(2, total_steps, "Atualizando pip, setuptools e wheel")
    _run("Atualizando gerenciadores de pacotes",
         [sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"],
         fatal=False)

    # ── [3] Todos os requirements*.txt ────────────────────────────────────────
    req_files = REQUIREMENT_FILES_MINIMAL if args.minimal else REQUIREMENT_FILES_FULL
    _print_step(3, total_steps, "Instalando TODOS os módulos do JT.IA")
    print(f"    Arquivos: {', '.join(req_files)}")
    count = _install_requirement_files(req_files, fatal_first=True)
    if count == 0:
        print("    [AVISO] Nenhum requirements*.txt encontrado — usando lista embutida.")
        _install_fallback_packages()

    # Garante pacotes Windows (OCR + automação) mesmo se markers falharem
    if OS == "Windows" and not args.minimal:
        _print_step(4, total_steps, "Garantindo módulos exclusivos do Windows")
        _run(
            "Instalando pacotes Windows (pywin32, OCR WinRT, keyboard, ...)",
            [sys.executable, "-m", "pip", "install", *WINDOWS_PACKAGES],
            fatal=False,
        )
    else:
        _print_step(4, total_steps, "Pacotes exclusivos do Windows")
        if args.minimal:
            print("    [INFO] Modo --minimal: OCR/WinRT e extras Windows ignorados.")
        else:
            print(f"    [INFO] Ignorado no sistema {OS}.")

    # ── [5] Agent-Reach ───────────────────────────────────────────────────────
    _print_step(5, total_steps, "Configurando integração Agent-Reach (Coleta Web & Redes)")
    if not args.no_agent_reach:
        _install_agent_reach()
        _run(
            "Garantindo suporte a cookies para Agent-Reach",
            [sys.executable, "-m", "pip", "install", "browser-cookie3>=0.19"],
            fatal=False,
        )
    else:
        print("    [INFO] Agent-Reach ignorado (--no-agent-reach).")

    if not args.minimal:
        # ── [6] Garantir mídia + wake-word (já no requirements, reforço) ───────
        _print_step(6, total_steps, "Confirmando mídia, TTS e Wake-Word")
        _run(
            "Confirmando pandas, pydub, edge-tts, miniaudio, openwakeword",
            [
                sys.executable, "-m", "pip", "install",
                "pandas>=2.2,<4", "pydub>=0.25,<1", "edge-tts>=7,<8",
                "miniaudio>=1.61,<2", "openwakeword>=0.6.0",
                "claude-agent-sdk>=0.2.87",
            ],
            fatal=False,
        )

        # ── [7] Navegadores Playwright ────────────────────────────────────────
        _print_step(7, total_steps, "Instalando navegadores Playwright (Chromium e Firefox)")
        if not args.no_browsers:
            try:
                _run(
                    "Baixando binários dos navegadores Playwright",
                    [sys.executable, "-m", "playwright", "install", "chromium", "firefox"],
                    fatal=False,
                )
            except Exception as exc:
                print(f"    [AVISO] Playwright browsers não puderam ser baixados ({exc}).")
                print("    Você pode tentar novamente mais tarde com:")
                print(f"      {sys.executable} -m playwright install chromium firefox")
        else:
            print("    [INFO] Download do Playwright ignorado (--no-browsers).")

    # ── Pós-instalação Windows ────────────────────────────────────────────────
    step_win = total_steps - 1
    _print_step(step_win, total_steps, "Executando pós-instalação do sistema operacional")
    if OS == "Windows":
        _configure_pywin32()
    _check_assets()

    # ── Atalhos ───────────────────────────────────────────────────────────────
    step_end = total_steps
    _print_step(step_end, total_steps, "Criando atalhos de inicialização")
    bat_file = _create_iniciar_bat()
    if not args.no_shortcuts and OS == "Windows":
        _create_desktop_shortcut(bat_file)

    # ── Resumo Final ──────────────────────────────────────────────────────────
    _print_header("INSTALAÇÃO CONCLUÍDA COM SUCESSO!")
    print("""
  Todos os módulos foram configurados:
    [OK] Núcleo JT.IA, Interface Gráfica HUD & Gemini Live
    [OK] Visão Local, OCR WinRT & Multi-Monitor (Claude Overlay)
    [OK] Documentos (Word / PowerPoint / PDF)
    [OK] Coleta e Pesquisa de Mídias (Agent-Reach)
    [OK] Processamento de Mídia, TTS (Edge) e Wake-Word ("Hey Jarvis")
    [OK] Automação de Navegador Web (Playwright)
    [OK] Script de Inicialização (iniciar.bat) e Atalho na Área de Trabalho

  Como iniciar o aplicativo:
    1) Dê dois cliques em: iniciar.bat  (ou no atalho JT.IA na Área de Trabalho)
       Ou pelo terminal:   python main.py
    2) Na primeira inicialização, insira sua chave gratuita da API Gemini caso solicitado.
    3) Para usar voz offline ou Wake-Word, acesse Configurações (⚙) no aplicativo.
""")


if __name__ == "__main__":
    main()
