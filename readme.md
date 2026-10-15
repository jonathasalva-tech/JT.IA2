# ⚙️ MARK LV (55)
### The Ultimate Cross-Platform Personal AI Assistant — By FatihMakes

> 📺 **[Watch the full setup video on YouTube](https://www.youtube.com/@FatihMakes)**

A real-time voice AI that can hear, see, speak, and control your computer — on any OS. Supports Windows, macOS, and Linux. Built on the Gemini Live API for native audio streaming, delivering zero subscriptions and total digital autonomy.

---

## ✨ Overview

Mark LIV gave the assistant a face. **Mark LV gives it a screen — and the stamina to keep working when a model goes down.**

Say "play the new Dune trailer" and the video appears **where the avatar was**, in the HUD itself, muted until you ask for sound. A YouTube link, a local file, a direct URL or just a description to search for: they all land in the same place, and JARVIS tells you it is coming *before* the picture arrives instead of going quiet for five seconds.

Underneath, every Gemini call in the app now goes through **one ladder of nine models**, ordered by measured response time rather than guesswork. When a model hits its quota, times out or disappears, the next rung takes the call and the dead one is put on a cooldown so nobody pays for it twice. Before this release, sixteen files named their own model, twenty-six times, with **no timeout at all** — one unwell alias could hang a request forever.

The release also draws a line through the bundled skill list. **Everything JARVIS ships with now drives the computer** — applications, files, the browser, the desktop, the screen. Five skills that served one hobby or one trade left the list, which is a thousand tokens the model no longer reads on every connection, and five fewer wrong tools for it to reach for.

It's not just an assistant — it's an extension of your digital life.

---

## 🚀 Capabilities

### JT.IA: programmer execution and diagnostic evidence

Project tests are verified only when the fixed Python unittest command exits
with zero, reports a nonempty run, and ends with `OK`, with at least one test
not skipped. Empty discovery, missing evidence, timeout and cancellation are
not successful validation. Test runners use temporary isolated bytecode caches
so rapid same-size source edits cannot reuse stale `.pyc` files. These caches
are removed after each run; existing project caches are not deleted.

The Windows test runner drains stdout/stderr while waiting, avoiding pipe
deadlocks with verbose tests. Reports preserve the final output; orchestration
keeps validation evidence even when the displayed log is shortened. Cancelled
programmer test requests do not launch a process.

Explicit file-controller failures and incomplete programming tasks returned as
text now reach the existing persistent diagnostic queue, without replacing the
original tool result. Recording an error does not authorize a repair: application
self-repair remains disabled, and external project corrections still require
the existing workspace, tool, profile and approval checks.

Ollama availability is not proof of a usable code proposal. Invalid Python from
the model is rejected before editing. A rejected proposal requires review/retry;
the application does not bypass syntax checks, download another model or weaken
permissions to make it appear successful.

See [the repair verification report](docs/relatorio-reparacao-programador.md)
for measured results and remaining limitations.

### JT.IA: GitHub module central in Programmer mode

The existing **AUTONOMOUS PROGRAMMER** panel includes a **GitHub Module Central**
area (also reachable via **OPEN MODULE CENTRAL** in Programmer Mode):

- paste a public GitHub URL;
- run repository analysis (purpose, languages, dependencies, compatibility,
  risks and integration strategy);
- review conflicting dependency declarations and the exact commit SHA used;
- install into managed storage with a durable restore snapshot;
- keep a local module library with state (`installed`, `active`, `disabled`,
  `error`), dependencies and operation history;
- run static Python syntax and entrypoint checks before activation;
- activate/deactivate/update/remove/restore managed modules with confirmations.

Security controls include granular permissions for:
code analysis, GitHub downloads, module creation/editing, module tests,
bridge-code / main-code changes, and module update/removal. High-risk operations
require explicit confirmation and authorization.

Installed apps are stored under `modo_programador/aplicativos_github/`. Activate an
app to register an AI tool bridge; JT.IA reloads plugins so voice/chat can run it
(e.g. “abrir Sample”). Use **REMOVE MODULE** or **UNINSTALL ALL APPS** to uninstall.

**JT.IA self-edit (2B):** with the Settings capability `main_code_changes` enabled
and the Workspace Programmer checkbox **Allow JT.IA self-edit**, you may authorize
the JT.IA installation folder itself. Apply still creates recovery points; assisted
mode still requires approval. Only programmer/test tools may use that workspace.

Repository commands are not executed automatically. Activation only creates a
bridge for repositories where a compatible JT.IA entry point was detected, and
only after critical static tests pass. Downloaded archives are pinned to the
analyzed commit SHA. Tests do not execute module handlers, install dependencies,
or build/test JavaScript projects. A module is not considered validated merely
because it was downloaded or installed. Restore returns managed sources to the
saved snapshot and leaves the module inactive.

### JT.IA: interface language

Choose **Português (Brasil)**, **Español**, or **English** in Settings. The
selection is saved and updates open interface widgets as well as panels opened
afterward. The shared interface catalog is `translations/ui.json`; each source
message must have entries in all three languages and preserve its named
placeholders. Buttons, group titles, menus, tooltips, placeholders, dialog
messages, tabs, table headers and spin-box units use the language manager.

Model identifiers, commands, paths, editable user text and document contents
are not translated. Messages returned verbatim by external programs and the
interfaces of separately installed third-party tools may retain their original
language; changing the JT.IA interface does not translate those applications.

Localization regression checks:
`python -m unittest tests.test_i18n tests.test_programmer_ui tests.test_local_vision_ui`.

### JT.IA: reusable Ollama model and persistent project memory

The existing **Settings -> AI Library** checks Ollama's installed model list.
**Use model** persists the exact selected tag without replacing other settings.
An omitted tag means `latest`, not any model of the same family. Startup never
pulls a model; even an explicitly requested download returns immediately if
that exact model is already present. Models remain in Ollama's own store
(`OLLAMA_MODELS` when configured, otherwise `~/.ollama/models`); JT.IA does not
copy model files.

See [the local-model guide](docs/modelos-locais.md) for the existing workflow,
privacy boundaries, and the distinction between running local models and
altering their safeguards.

Downloads require the existing confirmation. Missing catalog models are checked
against free disk space, conservative RAM estimates and registry availability.
Only one download runs per application process, with connection/read timeouts
and a one-hour progress deadline. A completed download must report success,
appear in the inventory and pass a short local generation check. Failures
require an explicit retry; no automatic model substitution or download loop.
An authorized local chat/download can start the existing Ollama executable;
ordinary health checks do not start it. OpenAI-compatible providers remain
separate and require the user's server to be running.
Offline-only requests reject models marked `cloud` before sending text, in
addition to requiring a loopback endpoint and bypassing proxy environment settings.

**Programmer -> USE AND SAVE PROJECT MEMORY** is off by default. When enabled,
it recalls only summaries for the selected project/file, verifies that the
file still exists and compares its current SHA-256 with the stored hash.
Changed code marks previous evidence stale. Summaries are untrusted model
context, not instructions. An approved edit records pending behavior tests and
the syntax check, never an automatically proven fix.

The existing `memory/long_term.json` remains the only general/technical fact
store; Ollama is not required to load it. Existing personal categories and
session summaries are preserved; technical categories are tasks, decisions,
solutions and test results. No full source/conversation is stored by this
programmer integration. The existing memory panel now supports **ADD MEMORY**,
**EDIT** and deletion. Editing technical evidence revokes its verified flag.
`record_project_fact(..., category="solutions", verified=True, evidence=...)`
requires evidence supplied by a caller that actually ran verification; this
memory API does not itself run tests or certify arbitrary claims.

Memory and local-model setting writes use same-directory atomic replacement;
read-modify-write operations are protected against concurrent threads.
Corruption, denied access or capacity exhaustion are reported instead of
overwriting data or discarding old entries. Memory is capped at 200,000
serialized characters; ordinary manual facts are limited to 380 characters
and technical summaries/evidence to 2,000 each. Credential-pattern detection
rejects common secrets, but is not a complete DLP detector or encryption:
never enter credentials in normal memory. Multiple simultaneous application
processes are not transactionally coordinated by this JSON store.

Regression tests use temporary stores, mocked download failures and Qt controls:
`python -m unittest tests.test_local_models tests.test_memory_manager tests.test_programmer tests.test_programmer_ui`.
Real local-only model acceptance and remaining operational limits are recorded
in `engineering-audit.md`. Computer reboot, disconnecting the machine's network
and restarting a shared Ollama service are not performed by these tests.

### JT.IA: hybrid connectivity and web research

The existing **AI MODE** preference remains persistent: **Automatic** uses the
configured Gemini Live session with local Ollama fallback for text when the
online session is unavailable; **Online only** does not fall back to Ollama;
**Offline only** uses local chat and does not invoke web tools. The header reports
general internet reachability separately from the current assistant connection
and selected mode. Reachability is probed in a background thread about once per
minute and is not an Ollama or Gemini health check.

Online web research reuses the existing `web_search` action and DuckDuckGo's
public search results (the `ddgs` dependency already in `requirements.txt`).
It adds URL reading for public HTTP(S) HTML pages, a five-redirect limit,
response-size and time limits, and blocks loopback/private-network destinations.
No new search API key or paid search API is required; search queries and URLs
are sent to DuckDuckGo or to the explicitly requested public site, subject to
their policies. Online chat still uses the existing configured Gemini service.
No local project files are included in a web request. Page text is marked as
untrusted source material and is never executed as a command. Press Escape to
interrupt the current assistant turn; page fetches stop at the next cancellation
check or bounded network timeout. A failed search reports failure rather than
presenting model knowledge as a search result.

### JT.IA: authorized local vision, OCR and image analysis

Use the sidebar **LOCAL VISION** panel to select **DISABLED**, **MANUAL**, or
**ASSISTED**. The selected mode and 5-60 second interval are saved in the
existing local configuration. Capture permission is never restored at launch:
ASSISTED mode still needs an explicit activation confirmation each time.
Window monitoring captures only a visible, selected Windows window; there is no
fallback to full-screen capture. **CAPTURE PRIMARY SCREEN LOCALLY** is a separate
manual MSS capture with its own explicit confirmation. Close confidential
content first. Both paths run in a bounded child process and keep images in memory.

Manual capture requires confirmation for each image. Assisted mode performs
local change detection and optionally Windows OCR at the chosen interval, with
a hard limit of 120 frames per activation. **ENABLE LOCAL OCR** is off by
default. Captures produce a temporary JPEG preview limited to 1280x720 and 1 MB.
Images are kept in memory only and cleared on pause, disable, cancel, panel
close, or use of **CLEAR VISUAL DATA**. Capture/OCR text is also removed from
labeled credential lines and common token formats, but this heuristic cannot
reliably recognize every secret; password fields are not visually masked.
Do not select confidential windows.

To request semantic interpretation, explicitly press **ANALYZE WITH LOCAL
OLLAMA** and confirm. The app checks the selected, already-installed Ollama
model's `/api/show` `capabilities` for `vision`, then uses only a validated
loopback endpoint. Analysis streams locally and **CANCEL TASK** closes the
active response; capture and analysis run off the UI thread. It never downloads
a model or uses the cloud as fallback.
When local vision is unsupported or unavailable, the UI reports that failure
and offers a clearly labeled OCR/keyword-only summary instead. Text found in an
image is untrusted evidence, not an instruction. Interpretations and
recommendations are suggestions, not verified facts or automatic edits.
User-selected image files are processed through the same size and local-only
limits. **SEND ERROR TO PROGRAMMER** transfers bounded OCR as untrusted context;
the existing workspace, review, authorization and test gates still apply.

Summaries are not saved by default. **SAVE SUMMARY TO MEMORY** requires separate
confirmation and stores only a short text summary, never an image or OCR text.
**CLEAR VISUAL DATA** also removes this feature's saved summary. Capture and
OCR stay local. The separate, pre-existing manual screen-to-Gemini feature is
not part of this local-only workflow and retains its own behavior.

Optional OCR bindings: `python -m pip install -r requirements-vision.txt`.
Use the project's `.venv\Scripts\python.exe`, not the global Python installation.
This integration uses the installed Windows OCR engine (WinRT), not Tesseract:
there is no OCR executable path to configure. Dependency checks run outside the
Qt UI thread. The panel lists available Windows OCR languages and independently
reports Ollama image capability. A text-only model does not disable capture/OCR.
Manual results and errors remain visible instead of being overwritten by the
periodic monitor's empty snapshot. **CANCEL TASK** discards late worker results.
At least one Windows OCR language pack must already be installed; there is no
cloud OCR fallback. OCR has a 4,000-character limit, reuses only an identical
frame's result, and is cleared on stop/failure. The isolated capture child has a
three-second deadline for hashes (eight seconds with OCR or preview; ten
seconds with both), one in-flight frame and no frame queue. Inputs are limited
to eight million pixels for a window and sixteen million for the primary screen;
this is not a hard process-memory or CPU quota.
Protected/GPU-rendered windows may refuse capture or return blank frames.
Packaged executables do not yet support this backend.

Regression tests: `python -m unittest tests.test_visual_monitor tests.test_visual_ocr tests.test_visual_analysis tests.test_programmer_ui`.
The explicit native acceptance test, `python -m unittest tests.visual_capture_acceptance`,
uses only its synthetic window and is not run by default discovery.

### Core Features
| Feature | Description |
|---|---|
| 🧑‍🎤 Holographic Avatar | An animated human head in the HUD — real facial geometry, lit and drawn in software, no GPU or extra packages |
| 👄 Real Lip-Sync | ~50 mouth shapes a second from the audio's formants **and** the transcript — closures, spreads and rounds, not a volume meter |
| 🌍 Language-Free Mouth | Articulation is derived by Unicode reduction, so Latin, Cyrillic and Greek scripts all work from one rule set — and scripts that hide pronunciation fall back cleanly |
| 🙂 Facial Acting | Brows track the phrase, gaze saccades between fixations, natural blinking, a small nod on stressed syllables |
| 😐 Face as Status | Looks away while thinking, meets your eyes while listening, lids fall while asleep, glances down at new content |
| 🎚️ Push-to-Talk | Hold **Ctrl+Space** and the mic opens — closed the rest of the time. Truly global on Windows, window-scoped elsewhere |
| 🔇 Self-Echo Guard | Never answers its own last sentence: the tail of its own voice is recognised and dropped without muting you |
| 🪪 Runtime Self-Knowledge | Name, OS, abilities **and limits** are generated from the live system each session — rename it or add a plugin and it knows |
| 🎙️ Wake Word | Local **"Hey Jarvis"** detection — sleeps until called, auto-sleeps after 2 min of silence, and never streams audio while asleep |
| ⚡ Instant Acknowledgment | Speaks a short, context-aware reply in **your language** the instant a longer task starts — no more silent waiting |
| 🚀 Faster Live Engine | Runs on **Gemini 3.1 Flash Live** — roughly 2× faster time-to-first-word than the previous model |
| 🧩 Self-Describing Skills | Every bundled skill declares its own `TOOL` dict + handler and is auto-discovered at launch — adding one is a single file |
| 🧠 Recallable Memory | Local persistent facts with a 200,000-character guard; no silent eviction — bounded prompt context and selective recall |
| 👁️ Memory Panel | Inspect, add, edit and delete stored facts; technical verification is revoked when its text is edited |
| ↩️ Undo | Take back what the assistant did — files it moved, renamed, created or wrote, and settings it changed |
| ⚠️ Real Confirmation | Shutdown, restart and WiFi wait for a button **you** press — the model cannot confirm its own irreversible actions |
| 🎧 Audio Device Picker | Choose the microphone and speakers by name, filtered to the short list your OS shows — and measured, so every entry actually works |
| 🔗 Session Continuity | A dropped connection, a voice change or a device change no longer wipes the conversation |
| 🧩 Plugin System | Drop a single `.py` file into `plugins/` — JARVIS learns a new skill on next launch |
| 📺 Video on the HUD | Plays YouTube, a local file or any video URL **where the avatar sits** — starts muted, sound on request |
| 🪜 Model Ladder | Nine Gemini models in one measured order — a quota, a timeout or an outage steps to the next rung instead of failing |
| 🎙️ Real-time Voice | Ultra-low latency conversation in any language via Gemini Live API |
| 🎨 Live Theming | Recolour the entire HUD from a hue wheel or hex — the avatar retints with it |
| 〰️ Reactive HUD | Waveform pulses to real audio — your mic while listening, JARVIS while speaking |
| 🎙️ Voice Picker | Choose from 5 native Gemini voices and switch live from the UI — no restart |
| ♾️ Unlimited Sessions | Sliding-window context compression — one conversation can last for hours |
| 🖥️ System Control | Launch apps, adjust volume/brightness, WiFi, shortcuts, power — all by voice |
| 🧩 Autonomous Tasks | High-level planning for complex multi-step goals via agent mode |
| 🧾 Diagnostic Programmer | Open a read-only analysis of JT.IA's recorded runtime errors from Settings; no files are modified |
| 🛠 Programmer Mode | Preview local Ollama fixes for one selected Python project file, then explicitly approve applying them with an original backup |
| 🧑‍💻 Workspace Programmer | Inspect and search an authorized project, preview bounded local-model changes, run tests asynchronously and report modified files |
| 🔬 REA Reverse Engineering | Run the pinned REA CLI and its full command catalog from the authorized workspace programmer, with per-command confirmation and no shell |
| 👁️ Visual Awareness | Screen capture and webcam vision piped into your main Gemini session, labelled by source |
| 🧠 Persistent Memory | Deeply remembers projects, preferences, and personal context across sessions |
| ⌨️ Hybrid Input | Seamlessly switch between keyboard typing and voice commands |
| 🌅 Morning Briefing | On first boot: greets you, reads the time, recaps yesterday, and fetches live news |
| 🔔 Proactive 2.0 | Time-aware, context-aware check-ins — knows the time of day, your projects, and what you've been discussing |
| 🗓️ Session Memory | Summarises each conversation and mentions it naturally next morning — consumed after use, never repeats |
| 👁️‍🗨️ Background Monitoring | User-configured topic watching — checks for new headlines once a day and alerts naturally |
| 📊 Hardware Monitoring | Continuous CPU, RAM, GPU and temperature telemetry with localized voice alerts |
| 🌤️ Weather Report | Live weather data for your city, personalized from memory |
| 🗺️ Dynamic Content Panel | Scrollable display layer beneath the HUD that renders web results, news, and search data |
| 🔍 Multi-Mode Web Search | `news` / `research` / `price` / `compare` / `search` — Gemini Grounded first, DDG fallback |
| ⏰ Smart Reminders | OS-native scheduled notifications (Windows Task Scheduler / macOS LaunchAgent / Linux systemd) |
| 📂 File Processor | Read, summarize, and answer questions about local files |
| 🌐 Browser Control | Open URLs, navigate tabs, and interact with the browser by voice |
| 📨 Send Message | Compose and send messages through WhatsApp, Telegram, and more |
| 🖱️ Desktop Control | Taskbar, window management, and desktop-level operations |
| 🧑‍💻 Silent Language Memory | Detects spoken language on first use — all future sessions adapt automatically |
| 📱 Remote Dashboard | Control the assistant from your phone via QR code pairing |
| ⚡ Auto-Start on Boot | Registers with the OS startup system (registry / LaunchAgent / .desktop) |
| 📋 Clipboard Intelligence | Copy any text → floating panel with Translate / Summarise / Explain / Fix |
| 🪪 Assistant Customization | Change the assistant name, your name, voice, and colour from the UI — takes effect immediately |

---

## 🆕 What's New in Mark LV

One new dependency for the whole release — `yt-dlp`, and only to turn a YouTube page into something Qt can play.

### The display

#### 📺 Video where the face is
The HUD already had a surface that takes the centre of the screen and gives it back: the camera. Video shares that same stack, so the avatar, the live camera and a video can never be on screen at once — and a video always lands exactly where you are already looking.

It accepts **a local file, a direct media URL, a YouTube link, or just a description** ("play the new Dune trailer") and searches for it. It **starts muted every time**, because a soundtrack talking over the assistant is the one way this feature could make JARVIS worse rather than better. You turn the sound on by asking, or from the button in the video header.

**It answers before it opens.** Resolving what to play takes seconds nothing can remove — measured at 2.0s for a link and 3.3s for a spoken phrase, plus buffering. Restricting yt-dlp to a lighter client was tried and made it worse: the fast clients came back with zero usable formats. So the seconds stay, and what changed is where you spend them — listening to JARVIS say it is coming, instead of watching nothing happen. Say "stop" during those seconds and the video is cancelled before it ever reaches the screen.

#### 🔀 Two streams, one picture
The first version asked YouTube for a format carrying both picture and sound and got *"Requested format is not available"*. That was not a bad selector; it was a wrong assumption. Checked against three videos — including the oldest upload on the site — **every one offered zero combined formats.** Picture and sound are separate streams now.

So there are two players running together, with a timer that corrects any drift over 300 ms. And the audio track is chosen on **language first, bitrate second** — because YouTube auto-dubs a great many videos and ships every dub at the *same* bitrate as the original: measured on one video, English at 129.483 and Arabic, Bangla, German, Spanish, French, Hindi and Indonesian all at 129.482. Sorting on bitrate alone came down to a thousandth of a kilobit, so the same video would play in Arabic one time and English the next for no reason you could see. It now reads YouTube's own original-track marker first.

#### 🔇 It stopped hearing the film
The microphone is open while a video plays, so the moment you turn the sound on, JARVIS starts answering the film. The mic now mutes itself when the video's sound goes on and unmutes when it goes off — and it says so in the activity log rather than going deaf silently.

#### 🎛 Two drawers instead of one
⚙ **SETUP** holds the things you set once — remote control, desktop shortcut, auto-start and customisation. 🎛 **CONTROLS** holds the switches you flick daily — fullscreen, morning brief, wake word, sleep, push-to-talk, HUD style. Only one is open at a time, and each sits under its own header button.

The panel used to stutter when it opened, and the obvious explanation — too many buttons — was wrong. Measured, the **first** wake-word state check took **2.104 seconds**, because it imported `openwakeword` on the UI thread the moment the drawer was built. That import now happens off-thread at boot, and the drawer opens instantly whether it has six buttons or sixteen.

> The drawer also used to vanish *behind* the video. `QVideoWidget` creates a native child window, and no Qt overlay can be drawn on top of one. The video is now a `QGraphicsVideoItem` inside a graphics view — same picture, and the interface stays where it belongs.

### Staying up

#### 🪜 Every Gemini model, in one ladder
Every one-shot Gemini call in the app now goes through `core/gemini.py`. Before this, **sixteen files named their own model — twenty-six times — and not one of them set a timeout.** When a single alias went unwell, the call did not fail; it hung.

The ladder is nine models deep, ordered by **measurement rather than guesswork**:

| Model | Measured | Model | Measured |
|---|---|---|---|
| `gemini-3.5-flash-lite` | 0.56s | `gemini-2.5-flash` | 0.67s |
| `gemini-3.1-flash-lite` | 0.60s | `gemini-2.5-flash-lite` | 0.74s |
| `gemini-flash-lite-latest` | 0.60s | `gemini-3.5-flash` | 1.13s |
| `gemini-3-flash-preview` | 504 after 14.7s | `gemini-3.6-flash` | 504 after 12.0s |
| `gemini-flash-latest` | 503 UNAVAILABLE | | |

The three that fail were **not deleted** — a model that is unwell today is a real rung tomorrow. They sit at the bottom, and a **cooldown** decides how long a failure is believed:

| What happened | Rested for | Why |
|---|---|---|
| Quota exhausted (429) | 5 minutes | Quotas refill |
| No answer (503 / 504 / DEADLINE_EXCEEDED) | 30 minutes | An outage outlasts a retry |
| Not found, or no access (404) | 6 hours | Your key does not have it, and won't in a minute |

That middle row is where the time was going. Only quota and 404 used to be cooled, so the 14-second wait on a dead model was paid **on every single call**. Measured after the fix: first call 13.15s, second 1.98s, third 1.16s — **11.2 seconds saved on every call from then on.**

**The Live model is deliberately not on this ladder.** Live models are not drop-in replacements for one another; they accept different config fields, and the same API key also exposes transcribe-live, live-translate and robotics-streaming models that will happily connect and then not behave like an assistant. So Live has exactly **two** rungs — the current model, and the one this project used before it — and it steps only on quota or loss of access. Never on a network blip or a bad key, which would otherwise walk the whole list into the same wall.

### The shape

#### 🧩 Everything bundled drives the computer
The bundled skill list had grown to seventeen, and some of it was nobody's business but its author's. **Not everyone updates games; everyone opens applications.**

Mark LV trims it to **twelve**, and every one of them does the same kind of thing: drive this machine. Applications, the browser, files, the desktop, the screen, the clock, the weather, the display. The rule is written into the project tree, so the next skill lands in the right folder without anyone having to ask.

This is not only tidiness. Every bundled skill is declared to the model on **every** connection, whether you ever use it or not. The declarations sent at startup dropped from **16,827 characters to 12,907** — roughly a thousand tokens off every session, and five fewer wrong tools for the model to reach for.

### 🩹 Fixes
* An unanswering model was retried on **every call**, at 12–15 seconds a time, because only quota and 404 failures were ever cooled down. 503/504 now rest for 30 minutes — **11.2 seconds saved per call**.
* One-shot Gemini calls had **no timeout anywhere**, in any of the sixteen files that made them. Every call now carries a deadline of at least 10 seconds.
* YouTube playback failed outright with *"Requested format is not available"* — it was asking for a combined stream that no longer exists.
* Videos played in a **random language**, because YouTube's auto-dubs carry the same bitrate as the original track.
* The settings drawer **stuttered on first open** — a 2.1-second `openwakeword` import on the UI thread, not the button count it looked like.
* The settings drawer opened **underneath the video**, because `QVideoWidget` creates a native window.
* JARVIS **answered the video's soundtrack.** The microphone now follows the video's sound.
* Qt's multimedia backend printed an ffmpeg banner to the console on every play, containing the **signed streaming URL with the viewer's IP address in it**. Silenced at startup.
* **Every launch paid 201 ms for a plugin nobody had asked to use.** Discovery executes every file in `plugins/`, and `youtube_video` imported `requests` and `youtube_transcript_api` at module scope. Deferring one of them would have saved nothing — the transcript library imports `requests` itself. Both are now checked with `find_spec`, which answers "is it installed?" without executing anything, and loaded on first use: **plugin discovery 211 ms → 39 ms**.
* A plugin that needed a file from a **newer Mark** was rejected with *"pip install core"*. The loader could not tell this project's own packages from a third-party one, so it told people to install a same-named stranger from an index — wrong, and a supply-chain hazard dressed up as a fix. First-party names now say the app is behind the plugin and that there is nothing to install.

> Built on the Mark LI–LIV foundation: the **🧑‍🎤 Holographic Avatar**, **👄 Lip-Sync**, **🎚️ Push-to-Talk**, **🔇 Self-Echo Guard**, **🧩 Plugin System**, **♾️ Unlimited Sessions**, **🎨 Live Theming** and **🎙️ Wake Word** are all still here.

---

## 🔄 The Foundation Update — in every Mark from LII

These four landed across **Mark LII, LIII, LIV and LV at the same time**, after each of those releases had already shipped. They are not what any one of those versions originally introduced; they are the floor all of them now stand on, so moving up a Mark never costs you something the one below it had.

No new dependencies. No bundled asset files. No hardcoded language, and nothing that assumes one operating system.

### 🧠 A memory that actually remembers

The store was capped at **2,200 characters — the whole memory, not per entry** — because all of it was pasted into the system prompt on every connect, so growing the memory grew every request. When it filled, the oldest entries were deleted and one line was printed to a console nobody reads. An assistant advertised as remembering "projects, preferences and personal context" was in practice a two-page notepad that quietly forgot your sister's name after a few weeks.

Storage and prompt budget are now separate problems:

* **Nothing is deleted.** The cap is a runaway guard normal use never approaches, and if it is ever hit it says so in the activity log instead of on stdout.
* **The prompt carries a core, not a dump.** Identity in full, then the most recently updated facts, budgeted — measured at **971 characters on a memory holding 62 stored facts.** That is *smaller* than the old whole-store cap, so sessions now connect with fewer tokens than before.
* **The rest is fetched on demand.** A `recall_memory` tool searches the full store locally — no network, no second model, well under a millisecond.

The part that is easy to get wrong: **a model cannot look something up if it doesn't know the thing exists.** So the prompt also carries an **index of the keys** it had no room for. Without it, "who is Ayşe?" gets "I don't know" while `ayse_sister` sits on disk unread. That index interleaves categories rather than sorting by recency — sorted like the core, a memory with forty preferences pushed the one entry the index existed for off the end.

⚙ → **🧠 MEMORY** shows every stored fact, when it was learned, and a ✕ to forget it. Everything stays in `memory/long_term.json` on your machine.

### ↩️ Undo — it can take back what it did

JARVIS moves files, renames them, writes to them and changes your settings. None of that had a way back; if it misheard you, the only remedy was to fix it by hand.

Say **"undo"** — in any language — and it reverses its own last action:

| | |
|---|---|
| **Files** | move · rename · create · copy · write · delete · organize desktop |
| **Settings** | volume · brightness · dark mode |

Three things it deliberately does *not* do:

* **It does not guess.** Settings undo reads the current value *before* changing it. Where a platform won't report that value, nothing is registered — an undo that restores a guess is worse than no undo.
* **It does not hoard.** Undoing a write means keeping the old contents in memory, so files over 1 MB are excluded and it says so rather than holding a 200 MB log for the session.
* **It does not delete your files to undo a copy.** The reverse of a copy is removing the copy; the reverse of "create a folder" is removing it *only while it's still empty*.

`organize_desktop` gets special treatment — one command that moves dozens of files, which made it the least reversible thing the assistant could do. It journals every move and puts all of them back in one go, cleaning up the folders it created if they're still empty.

**Undo costs nothing at runtime.** It appends a closure to a list; nothing in it runs unless you ask.

### ⚠️ A confirmation the model can't forge

The old gate read like this:

```python
if action in _DANGEROUS_ACTIONS:            # {"restart", "shutdown"}
    confirmed = str(params.get("confirmed", "")).lower()
```

`confirmed` is a **tool parameter, which means the model fills it in.** Nothing stopped it sending `confirmed=yes` on the first call and nothing checked that a human was ever involved. It was a convention, not a gate. And its coverage was two actions — so `toggle_wifi`, which cuts the assistant's own connection to the Live API and therefore *cannot be asked to undo itself*, went through with no gate at all.

The token is now issued by the interface. Shutdown, restart and WiFi put a banner on the HUD and **return immediately**; the action runs only if you press CONFIRM. Nothing blocks — JARVIS keeps talking while the banner is up — so this is **cheaper than the old gate**, which burned two tool round trips on every power command.

> The split between the two mechanisms is about reversibility, not about how alarming a word sounds. Anything undoable is done at once; only the genuinely irreversible asks. An assistant that checks with you before turning the volume down is one you stop talking to.

### 🎧 It finally asks which microphone

Both audio streams opened with no device argument at all, so they always took whatever the OS called "default" — and on Windows that *moves on its own* the moment you plug a headset in. "JARVIS can't hear me" almost always meant "JARVIS is listening to the webcam".

⚙ → **🎧 AUDIO DEVICES** lets you pick the microphone and the speakers by name. Two things matter more than the dropdown:

**The list is short.** `query_devices()` returns one entry per *device × host API*, not per device — measured on an ordinary Windows machine, **41 entries for what the sound settings show as 4 microphones and 4 speakers.** The same microphone appears four times, under MME, DirectSound, WASAPI and WDM-KS, with nothing to say which is which. That is not a choice, it's a quiz. The picker takes one host API per direction, drops the "Sound Mapper" and "Primary Sound Driver" pseudo-devices that just mean "default", and deduplicates. **41 → 8.**

**Every entry has been measured, not assumed.** The obvious approach is to pick the host API with the nicest names — WASAPI on Windows, which in shared mode **doesn't resample**, so with 16 kHz in and 24 kHz out against 48 kHz hardware every open failed. Adding a rate check and moving to DirectSound passes that test on both sides, and PortAudio's DirectSound **output is a silent sink**: the stream opens, every write returns success in ~0 ms, and not one sample reaches the speakers.

| | write(2.0 s) took | |
|---|---|---|
| MME | **2.02 s** | consumed in real time |
| DirectSound | **0.00 s** | swallowed instantly |

No capability flag reports that. So the app measures it — once per host API per direction, on a background thread at startup, using silence. Two consequences worth stating plainly:

* **Each direction picks its own host API.** On Windows this lands on DirectSound for the microphone and MME for the speakers — a split no amount of reasoning would have produced.
* **The probe runs in the mode the app actually ships.** DirectSound input passes a callback stream and fails a blocking read; probing the wrong mode rejected a microphone that works perfectly.

Your choice is stored **by name, not by index** — indices shift whenever something is plugged in. If the saved device is gone, it falls back to the system default and says so in the log rather than failing to start.

### 🔗 It stops forgetting the conversation when the connection drops

`session_resumption` was switched on in the config and the handle the server sent back was **never read** — so every reconnect started an empty session. A dropped packet, or simply changing the voice, wiped the conversation. "Unlimited sessions" leaked through exactly this hole.

The handle is captured and replayed now. A network blip, or switching your microphone, keeps the conversation intact.

It is held in memory only, deliberately: writing it to disk would make a fresh launch continue yesterday's chat, which sounds appealing but breaks the session-summary flow — a conversation that never ends never produces a summary, and the "yesterday we talked about…" line in the morning briefing silently disappears. Changing the **voice** also starts clean on purpose, since resuming restores the server's session state and would likely bring the old voice back with it.

### 🩹 Fixes that came with it

* **The assistant could die on a log line.** Status lines carry emoji and arrows (`📤 file_controller → Moved: a.txt → Documents/`). On a non-UTF-8 console — cp1254 on a Turkish Windows, cp1251 on a Russian one, cp932 on a Japanese one — printing one raises `UnicodeEncodeError`, and because that print sits *after* the tool's own `try/except`, it escaped into the receive loop and took the session down.
* **Every computer command paid for two model round trips.** `computer_settings` made an *entire second Gemini call, inside the tool*, purely to translate the request into one of its own action names — because the declaration only said "The action to perform", so the model rarely filled it in. When that second call failed, the fallback was `description.lower().replace(" ", "_")`, which turns the Turkish for "turn it down" into `sesi_kis` and straight into "Unknown action". The declaration now names all 56 actions and the rest is spelling tolerance handled locally by `difflib` in microseconds. When nothing matches it suggests real action names instead of dead-ending.
* An unresolvable saved audio device, or one the driver refuses to open, falls back to the system default and says so — on both the microphone and the speakers.
* A rejected session-resumption handle is dropped after one attempt, so an expired handle can never be replayed on every retry and prevent the reconnect it exists to protect.



---

## 🗺️ Mark Roadmap

| Mark | Focus |
|---|---|
| **XLIX** | Auto-start · clipboard intelligence · assistant customization |
| **L** | Session memory · background monitoring · proactive 2.0 · instant vision |
| **LI** | Plugin system · affective dialog · proactive audio · unlimited sessions |
| **LII** | Voice picker · live theming · reactive HUD · recallable memory · undo · real confirmation · audio device picker · session continuity |
| **LIII** | Wake word · Gemini 3.1 Flash Live · instant acknowledgment · self-describing action/plugin architecture |
| **LIV** | Holographic avatar · viseme lip-sync · facial acting · face-as-status · push-to-talk · self-echo guard · runtime self-knowledge & limits |
| **LV** | Video on the HUD · model ladder with measured fallback · split settings drawers · trimmed bundled skill list |
| *shared* | The last five above also shipped to LIII, LIV and LV at the same time — moving up a Mark never loses them |
| **LVI+** | Interrupt by voice · conversation history · Telegram remote · full file access · security camera · Obsidian |

---

## ⚡ Quick Start

### Windows installer

Run [dist/JT.IA-Setup.exe](dist/JT.IA-Setup.exe) to install JT.IA with its custom installer artwork and icon. Python 3.11–3.13 and an internet connection are required to install the app's dependencies; API keys and personal configuration are not bundled.

### Run from source

```bash
git clone https://github.com/FatihMakes/Mark-LV.git
cd Mark-LV
python setup.py        # installs deps for YOUR OS + the browser automation engine
python main.py
```

`setup.py` only ever installs what your operating system needs — the Windows-only libraries are skipped automatically on macOS and Linux, and vice-versa. It also checks your Python version up front, so a wrong interpreter fails with a sentence instead of a wall of pip output. Prefer to do it by hand? `pip install -r requirements.txt` works too.

On first launch, JT.IA guides you through choosing Automatic (Gemini Live with local fallback) or Offline mode and confirms the detected operating system. Enter your own Gemini API key in the app; it is not bundled with the installer. Ollama, the local Qwen model, and offline speech are managed from **Settings**.

> ⚠️ **Installation Note:** If you hit a `ModuleNotFoundError` for an OS-specific package, install it with `pip install <module_name>`. The optional **wake word** engine is *not* installed here — grab it in one click from **⚙ → WAKE WORD** inside the app.

## 🔌 Online and offline chat

### Remote dashboard ports

The dashboard prefers port 8000 and its HTTPS alias prefers port 8001. If another
instance occupies either port, JT.IA reserves an available port without closing
the other instance. **Remote Control** displays the selected address and QR code;
use these rather than assuming a fixed port. If the alias is unavailable, manual
entry uses the primary address. Startup failures remain visible in the logs.

### Diagnostic and Programmer shortcuts

Use the always-visible **DIAGNOSTICS** and **PROGRAMMER** buttons at the top of
the main window's left panel, without opening Settings. The Settings shortcuts
remain available as well.

Open **DIAGNOSTICS** (or **Settings → Diagnostic Programmer**) to inspect each recorded error name,
component, classification and summary. **COPY ERROR REPORT** copies the event
details; **OPEN IN PROGRAMMER MODE** transfers that report to the coding panel.
Older events may lack an exception name. Reports are sanitized summaries, not
full tracebacks; heuristic confidence is not proof of the underlying cause.
New grouped exceptions include their internal exception names and messages in
the sanitized summary (limited to 500 characters); older records are not rewritten.

**Settings → Programmer Mode** also opens the coding panel directly. Select a
project folder and one existing Python file (maximum 64 KB), describe the bug,
then choose **GENERATE PREVIEW**. Only that file and the supplied description
are sent to the configured loopback HTTP Ollama service, without proxies,
redirects, cloud fallback, model downloads or executing generated code.
JT.IA's own files and dependency/environment files cannot be edited in this mode.
An environment cannot be authorized by selecting its root (`pyvenv.cfg`) or
its `site-packages`/`dist-packages` directory. If a newly selected file is
outside scope, the previous target is cleared rather than silently retained.

Review the explanation and diff before **APPROVE AND APPLY**. Approval requires
another confirmation; a changed source file invalidates the proposal. Syntax is
checked before saving, and an original `.bak` file is retained next to the source.
No project tests are executed automatically: run them to verify behavior. The
application's diagnostic queue still never applies repairs automatically.

The Programmer panel now shows both **OPEN WORKSPACE AGENT** and
**OPEN REA REVERSE-ENGINEERING TOOLS**. The REA button opens the authorized
workspace and then the REA command panel directly; select a project folder
first if none has been authorized. The **OPEN WORKSPACE AGENT** button opens
the project workflow. Select an existing project folder, choose one of four persistent
autonomy modes, and describe the task:

* **Assisted** previews changes and waits for explicit approval before writing.
* **Controlled autonomous** applies a bounded proposal and runs Python
  `unittest` discovery; after a failing test it permits one correction attempt
  and one verification run.
* **Analysis only** reads and reports without applying changes.
* **Maximum within authorized scope** performs routine authorized edits and tests
  without repeated approval. It does not enable disabled tools or expand the
  workspace. Critical actions still require the human confirmation banner.

The workspace index inventories common source/configuration files and indexes
Python symbols and imports without executing source. Dependency folders, hidden
folders, caches, generated output, symlinks, and credential-like files are
excluded. Proposals are limited to eight text files, checked for workspace
containment and Python syntax, and retain non-overwritten `.jtia.bak` backups.
Each successful edit adds a credential-redacted change record to
`.jtia-changes.jsonl` inside the authorized project. The JT.IA installation
itself cannot be selected as a workspace. Model requests use only the existing
loopback Ollama service; no model is downloaded, and unavailable models are
reported without discarding project files.

**READ FROG**, available in **Settings -> Modules** and **Programmer Mode**,
opens the official [Read Frog](https://github.com/mengxi-ream/read-frog)
extension in a separate, persistent Chromium profile. The pinned source,
lockfile and GPLv3 license are preserved in
`integrations/read-frog/read-frog-1.51.0`; the extension build is
`.output/chrome-mv3` inside that directory. This is the upstream extension,
not a replacement translator or a claim that JT.IA understands every desktop
application. Its official UI provides bilingual reading, translation,
selection tools, custom AI actions/writing/dictionaries, supported video
subtitles, Edge TTS, glossary, input translation, batching, shortcuts,
provider settings and Notebase/flashcard study.

The conversation tool `read_frog` supports `status`, `guide`, `settings`,
`open`, `read_page`, `translate_page`, `show_original`,
`translate_selection` and `speak_selection`. `settings` opens the selected
official feature screen; it does not execute every feature automatically.
Selection operations require text manually selected in the dedicated browser.
Enable the **browser** application in Windows control and the existing
**internet_access** capability. Browser operations require explicit on-screen
confirmation, including in Maximum autonomy; local-model tool use additionally
requires Maximum autonomy. Permissions are checked again after confirmation.
Restart JT.IA after adding the action so discovery refreshes its tool catalog.

Example: “Use read_frog com action status e explique o que está disponível.”
Then: “Abra as configurações de provedores do Read Frog.” Confirm on the HUD.
Configure providers/accounts manually in that browser; JT.IA does not copy its
API keys. Some services require credentials, payment or supported media.
The build omits production Google OAuth and analytics credentials, so hosted
sign-in and account-dependent features are not certified. Installing the
extension alone does not activate or verify those services.

**Language-learning keyword:** say or type **“aprender idiomar agora”**.
The spoken variants “aprender idioma agora” and “aprender idiomas agora” are
also recognized. Online voice/text and local prompts instruct the assistant
to begin a lesson, verify Read Frog using `status`/`guide`, ask the target
language when unknown, and choose relevant resources for reading, listening,
pronunciation, vocabulary, writing and review. Follow-up lessons remain in
conversation context; this is not a separately persisted global mode.
Ask to stop or change subject to end the lesson. The keyword does not execute
all tools at once or bypass confirmation, permissions or provider setup.
Local conversations without tool access offer text-only teaching and explain
the missing Read Frog access instead of claiming it was activated.

Page translation and speech may send content to external providers. Use only
public, non-sensitive content. Conversational URLs reject non-HTTP(S),
embedded credentials, obvious local hostnames and non-public literal IPs.
These checks are not DNS/network isolation and do not control manual browser
navigation. The dedicated profile does not expose personal browser tabs.
Returned text is bounded/redacted untrusted evidence, not authorization or
instructions. Translation/audio acknowledgements are not proof of completion;
provider errors remain visible in the extension. Confirmed results are
returned to the active conversation without replaying cancelled operations.

For a fresh build, obtain the official `v1.51.0` source archive from GitHub,
preserving its license and sources, and extract it to the directory above.
From the JT.IA root (npm must be available), use the upstream lockfile and
pnpm-managed Node runtime; this release requires Node `^26.11.1`:

```powershell
npm.cmd exec --yes --package=pnpm@12.10.1 -- pnpm --dir '.\integrations\read-frog\read-frog-1.51.0' install --frozen-lockfile
$env:WXT_SKIP_ENV_VALIDATION='true'
npm.cmd exec --yes --package=pnpm@12.10.1 -- pnpm --dir '.\integrations\read-frog\read-frog-1.51.0' build
```

`WXT_SKIP_ENV_VALIDATION` permits a local build without production OAuth and
analytics credentials; it does not grant access to hosted services.
The JT.IA Python environment also needs Playwright's Chromium
(`python -m playwright install chromium` if missing).
Focused regressions:
`python -m unittest tests.test_read_frog tests.test_programmer_ui tests.test_rea_reverse_engineer tests.test_assistant_shutdown`.
Set `JTIA_TEST_READ_FROG=1` to include the headful browser test, which uses an
isolated temporary profile and local fixture. It verifies official screens,
real extension messaging, original-page state and reopening after closure,
without claiming provider-backed translation, speech or account features.

**OPEN REA REVERSE-ENGINEERING TOOLS** exposes the upstream REA 6.4.0 CLI from
the same workspace panel. Install the pinned runtime once from the JT.IA folder
with Node.js 22.19+, 24.11+, or 26+ and npm:

```powershell
npm.cmd install --prefix integrations\rea
```

Enter any command shown by `--help` and put each argument on its own line;
arguments (including Windows paths and search text with spaces) are passed
literally without a shell. Every operation shows its exact command and requires
confirmation, runs as the current Windows user, and is recorded in the security
audit. **STOP REA COMMAND** requests cancellation. REA adds workflows for
native binaries, Go/Rust/WASM/EVM, .NET, Android/APKs, JavaScript/Electron,
SQLite, websites, saved network and packet captures, firmware, providers, and
other targets supported by its CLI.

The assistant can also invoke a bounded, read-only subset of REA during a
conversation. Ask it to inspect or decompile a file in the authorized project,
search for a string/function, or inspect a saved HAR/mitmproxy capture. Enable
**workspace_programmer** in Windows control settings and select an existing
project folder first. REA reuses this permission; there is no separate
`rea_reverse_engineer` checkbox. Each conversational REA operation displays its target and
command for confirmation before it runs. Local-model conversations additionally
require Maximum autonomy; online conversations use the currently selected
assistant mode and the same project/confirmation checks. This conversational
tool does not expose REA's editing, install, device-control, or other
side-effecting CLI commands; use the REA command panel to access the broader
upstream catalog.
After confirmation, REA's returned evidence is sent back to the connected online
assistant for explanation (or to the waiting local model). If the conversation
is cancelled or disconnected, the operation is not replayed automatically.

Closing the assistant through conversation also requires on-screen confirmation.
A tool failure or an instruction to stop an individual task does not authorize
closing JT.IA.

The pinned CLI does not install REA's optional analysis engines or external
tools. Available targets and operations depend on the host and caller-installed
providers (for example Ghidra/Hopper/IDA, JADX/JDK, ADB, WABT, Binwalk, or
TShark); inspect REA's `doctor`, `providers`, and `capabilities` output for
readiness. Some workflows can execute or interact with a target, device, or
external provider, so review the command and target before confirming. See the
[REA project documentation](https://github.com/morluto/rea) for current
platform and provider limits.

Project analysis/model work and test execution run off the UI thread. **STOP
TASK** cancels indexing/tests and prevents a returned proposal from being
applied; an active Ollama request may take up to its bounded request timeout to
return. Test execution is limited to the project's Python `unittest` discovery
command (no shell or model-supplied command is executed), with a 120-second
timeout. Passing tests describe that invocation only; they do not prove the
entire project is correct.

The workspace panel also offers **Generate a React app from a user story**.
This uses the configured local Ollama model to propose a React composition,
component configurations, reusable components, a composed page and a demo or
entry point, following the target project's existing conventions. It does not
bundle the upstream Node/OpenAI service or require an OpenAI key. React
generation is limited to **Assisted** (explicit preview and approval) and
**Analysis only**; it does not run Node, install packages, or claim a build or
test succeeded. Review and validate the proposed React files using the target
project's own tooling.

The legacy `code_helper` and `dev_agent` execution paths share a shell-free
command runner. Reports include the exit code, stdout, stderr and elapsed time.
Only exit code zero counts as successful execution; a timeout or launch failure
stops the build validation instead of assuming a server or GUI is working.
Successful execution is not proof of functional correctness or passing tests.
Command arguments retain quoted spaces; Python subprocess output uses UTF-8.
Failed file saves are reported rather than claimed as completed changes.
This runner is not a sandbox: existing action permissions still apply, output
is captured in memory, and timeout termination does not guarantee cleanup of
all descendant processes. Persistent cancellation/process-tree limits remain
future work.

The **WINDOWS CONTROL** sidebar panel configures explicit permissions for one
existing project folder, individual built-in tools, a small set of applications,
and the fixed Python `unittest` discovery command. Permissions are persisted in
the existing local settings file and checked again for each action. JT.IA's own
installation, Python environments, hidden files, dependency folders, caches,
generated output, credential-like files, symlinks and paths outside the selected
project are excluded. Project reads and searches are bounded; file/folder
creation refuses to overwrite existing content.

The actions can open allowlisted applications or project items, search/read
project files, create a folder or new UTF-8 file, and open Windows Terminal in
the selected folder. The pre-existing Windows application launcher now routes
through the same app allowlist and confirmation gate; it no longer builds shell
commands or types arbitrary names into the Start menu. Assisted autonomy asks
through the existing human-operated confirmation banner before actions with
side effects; controlled autonomy cannot run model-provided shell commands.
Test execution is a fixed
`sys.executable -m unittest discover -v` process, only after enabling the
matching command and tool; it runs asynchronously with a three-minute limit,
redacted in-memory output, a task ID, status lookup and cancellation. Project
tests are code and can themselves have side effects, so review the selected
project before enabling test execution. Analysis mode does not execute actions.
The process list contains only direct processes started and tracked by JT.IA;
stopping one requires the existing confirmation UI, and unrelated system
processes are never enumerated or terminated. Task and process records are
session-local and are not persisted across application restarts.

The legacy Windows file controller now also requires its permission toggle
and confines paths to the selected project; mutations use the same human
confirmation banner. Low-level computer input has a separate permission toggle
and requires confirmation for desktop interactions. The legacy desktop action
no longer executes model-generated Python on Windows; its file-changing
operations are limited to the authorized Desktop and confirmed before running.

The **TASK ORCHESTRATOR** sidebar panel shows the active request, the actual
tool calls selected by the online assistant, their order/dependencies, current
state, returned output, confirmation status and final report. It does not
pretend to have a model-generated plan before the model has selected tools.
Simple offline Ollama chat outside the Maximum profile remains text-only and reports that no actions were
run; it does not get a second tool executor. Memory recall, project memory,
vision, voice, web research and Windows actions continue through their existing
owners. Task records are redacted and kept in memory for this application
session only. The panel's cancel action prevents queued work and, when the
Windows cancellation permission is enabled, attempts to stop a tracked JT.IA
test process; an already-running synchronous tool may finish before it stops.
Repeated identical tool calls are capped, and task plans/results are bounded.

Operations that contact another person (for example `send_message`) now show
an explicit human confirmation containing the recipient and a redacted message
preview. Confirmation completion or decline is reflected in the task report.
The legacy `dev_agent` generator is intentionally blocked from orchestration:
it currently accepts model-produced output paths and can install dependencies
without the selected-workspace/per-operation review required here. Use
**PROGRAMMER** or the explicitly authorized **WINDOWS CONTROL** project tools
instead. This restriction is not evidence that the legacy generator was fixed.

**⚙ → Settings → SECURITY AND PERMISSIONS** contains the security controls in
the existing settings view. The **WINDOWS CONTROL** sidebar shortcut opens this
same section; it is not a separate security window. Select the authorized
project there, then enable only the required applications, commands and tools.
Permissions are read again when actions run, so disabling one takes effect
without restarting JT.IA. The section also controls project edits, web research,
local screen capture, whether screen images may be sent to online AI, microphone
input, saved-memory context, audit-log viewing and model/dependency downloads.
External screen sharing and downloads default off. Web research permission
controls web tools; it does not disable the configured Gemini connection or
other provider traffic. Critical confirmations and recovery-before-edit are
fixed on and cannot be switched off by the model. The user may require or waive
confirmation for safe project file/folder creation in controlled mode; test runs
and legacy file-controller mutations continue to require human confirmation.
Offline voice-model installation is subject to the same dependency-installation
permission. The security section also provides a separately confirmed action to
clear the persistent memory store; this replaces its contents with the empty
schema and does not delete other application settings.

Before the local Programmer or Windows file controller changes project files,
JT.IA stores a verified recovery point outside the workspace under
`%LOCALAPPDATA%\JT.IA\security\recovery` on Windows (or the platform's local
application-data directory). Files over 10 MB or points over 50 MB are refused;
if a recovery point cannot be created, the edit does not proceed. Restore is
available in the same Settings section, only for files within the currently
authorized Windows project, after a separate confirmation. When replacing a
file, the current version is backed up before restoring. Existing `.jtia.bak`
copies are retained for compatibility with the Programmer workflow.

The redacted, bounded audit history is stored locally at
`%LOCALAPPDATA%\JT.IA\security\audit.jsonl`; it records tool activity, file
changes, test output summaries and recovery identifiers, not full source
contents. The Settings section can show recent entries, cancel the active
orchestrated task, revoke all Windows workspace/application/command/tool
permissions, or delete recovery copies and audit data after confirmation.
Credential filters cover common key names and token formats but are heuristic:
they are not complete secret detection, encryption or a guarantee that every
private value is hidden. Do not put credentials in project prompts, code
proposals or normal memory. No Git repository was present, so this change did
not initialize or modify version control.

The default **Automatic** mode preserves Gemini Live as the online voice experience. When a network failure disconnects Gemini Live, the app can listen and answer locally until it retries the online session. **Online only** never uses the local model. **Offline only** does not create a Gemini session. With the Maximum autonomy profile, local voice/text can use the declared tools through the same permission checks, auditing and cancellation as online commands. The model runs locally; authorized web tools still require a network connection and share the requested queries/form values with the selected website.

Open **⚙ → Settings → AI Library — Ollama** to inspect the suggested Qwen 2.5 models. A model is never downloaded automatically: choose **DOWNLOAD** and confirm the displayed approximate size first. The download requires the Ollama application and an internet connection; the app uses Ollama's local service and checks that the model appears installed before reporting it ready. The smaller `qwen2.5:3b` option is the recommended starting point for computers with about 16 GB RAM; actual speed and quality vary by hardware.

For offline voice, choose **DOWNLOAD OFFLINE VOICE MODEL** in the same Settings panel and confirm the one-time Portuguese speech-model download (about 31 MB). Speech recognition runs locally with Vosk, and spoken replies use an installed Windows SAPI voice; Portuguese (Brazil) is preferred when available. The model must be downloaded before disconnecting from the internet. Audio and local-model requests are not uploaded to Gemini; explicitly requested network tool operations remain subject to their own permissions.

The **TRANSCRIBE** button beside the chat input captures one short utterance locally (Vosk, Portuguese Brazil). In Offline mode with Maximum autonomy, the recognized instruction goes directly through the text-command dispatcher. Other profiles put the transcript in the editable chat field for review; Automatic/Online mode retains the consent step before sending it to Gemini. **CANCEL** or **INTERRUPT** stops capture. No audio recording is saved. Speech replies can be disabled with **Speak replies**; that setting also suppresses Gemini Live audio while preserving its text response. The manual profile selector and **PROFILES** button are directly below **Speak replies**, with explicit dark-theme text and menu colors. On Windows, use **PROFILES → Local voice settings** to select an installed SAPI voice and adjust speed/volume.

Voice profiles are optional, manual local preferences for allowing voice chat and spoken replies. Creating one requires confirmation; no voice sample is collected and profiles do not identify or authenticate a person. Voice commands use the same autonomy and confirmation rules as typed commands. Existing **Hey Jarvis** wake-word detection is an optional, continuously listening local feature when enabled; it is separate from the one-shot Transcribe button and can be switched off in Controls.

Outside Maximum autonomy, offline chat remains text-only. Local-model tool conversations are bounded to 12 rounds with at most eight calls per round, and recheck permissions before execution. Browser operations are exposed to small local models as compact `browser_*` adapters, all routed to the existing `browser_control` handler, not a second browser implementation. A protected action pauses the local task and resumes it after accepted confirmation without replaying the submission. Conversation and continuation state are session-local; restarting the application does not automatically replay interrupted tasks.

### Authorized browser form automation

Enable the browser application in Windows permissions. In Security settings,
list the exact HTTP(S) origins permitted for field editing. An origin includes
scheme, hostname and port; authorizing navigation alone does not authorize edits.
The browser uses a dedicated persistent JT.IA profile: sign in manually, including
MFA or CAPTCHA when required. Existing normal-browser cookies are not copied.

Form fields, selections and checkbox states are checked against the actual DOM.
The `fill_form` tool schema accepts a list of `selector`/`text` entries; internal
dictionary calls remain compatible. Saving requires an expected visible result.
Only explicitly configured origin/selector pairs for reversible save buttons can
skip confirmation in Maximum mode. Purchases, publications and other consequential
actions must not be listed as reversible save targets. Uncertain submissions are
not clicked again; verify the page or ask for intervention instead.

The local screen tool returns capture/OCR evidence without uploading images.
A text-only Ollama model cannot interpret images; it reports this limitation.
An optional `local_vision_model` setting selects a separate installed local
Ollama model for the visual panel and screen-analysis tool, without changing
`llm_model` used by chat/programming. If absent, the existing chat-model choice
is checked for visual capability. The installed `moondream:latest` model uses
a short image caption instead of structured JSON diagnostics. Captions may
contain incorrect interpretations and are explicitly labeled as unverified;
OCR remains a separate source of text evidence. Cloud models are not accepted
for this visual setting. Incomplete/error responses are reported, not accepted
as completed analysis.
Running approved project tests executes project code under the current Windows
account, not an operating-system sandbox.

### JT.IA: manual diagnostics and test reports

Open **⚙ → Settings → SYSTEM DIAGNOSTICS** and choose **RUN DIAGNOSTIC**.
Checks run on a worker thread and can be cancelled. They inspect the application
entry/UI files, declared Python dependencies and version ranges, persistent
memory readability, programming/search/voice/vision module availability,
configured Ollama/model availability, local file-system permissions, the
read-only diagnostic database, current task/process state when available, and
a non-blocking CPU/RAM sample. The check does not start Ollama, send a web
request, write probe files, or modify project data.

**Run full unittest suite (optional)** explicitly enables the existing local
`unittest` discovery command. The timeout and number of test attempts are
bounded in the same section. Test discovery is not run at application startup.
Reports include check timings, results, available error summaries and test
status; credential-like strings are redacted heuristically. History is kept in
`%LOCALAPPDATA%\JT.IA\diagnostics\history.jsonl` on Windows (or the platform
application-data directory), with a bounded 20-report history. The report can
be reviewed in the existing Programmer, whose edit permissions, previews and
confirmation rules remain in force.

System diagnostics are read-only and do not apply automatic code corrections.
No performance change is made based on synthetic indicators; investigate
measured issues first. A missing optional package/model is reported as
unavailable rather than as a failure of a feature that is not installed.

---

## 📋 Requirements

Spreadsheet analysis, pydub audio processing and the alternate Edge TTS engine
can be installed together with `python -m pip install -r requirements-media.txt`,
using the same interpreter that starts JT.IA. Most pydub formats also require
FFmpeg and FFprobe on PATH; installing pydub alone does not install those tools.
Edge TTS requires internet to synthesize speech. Whisper, Kokoro and wake-word
engines remain separate opt-in extras; this media bundle does not download
speech models or change the selected voice engine.

| Requirement | Details |
| --- | --- |
| **OS** | Windows 10/11, macOS, or Linux |
| **Python** | 3.11, 3.12 or 3.13 |
| **Microphone** | Required for voice interaction (and for the "Hey Jarvis" wake word) |
| **Speakers** | Required for voice replies |
| **API Key** | Free Gemini API key for online Gemini Live mode; offline-only setup does not require one |
| **Local AI** *(optional)* | Ollama and a model downloaded from ⚙ → Settings → AI Library; downloads require internet and explicit confirmation |
| **Offline voice** *(optional)* | Vosk and its Portuguese model downloaded from ⚙ → Settings; Windows SAPI supplies local speech output |
| **GPU** | **Not required.** The avatar is rendered in software, and so is HUD video |
| **YouTube on the HUD** | `yt-dlp`, installed by `setup.py`. Without it, local files and direct URLs still play and YouTube links open in the browser with an explanation |
| **Wake word** *(optional)* | One-click download from ⚙ → WAKE WORD (`openwakeword`, a few MB, fully local) |

---

## 🗂️ Project Structure

```
Mark LV/
├── main.py                   # Core loop — Gemini Live session, audio I/O, viseme extraction, tool dispatch
├── ui.py                     # PyQt6 HUD — avatar canvas, waveform, log panel, settings drawer, camera feed
├── setup.py                  # OS-aware installer (skips wrong-OS dependencies, checks your Python)
├── .gitignore                # Keeps your API key, TLS key and memories out of the repository
├── plugins/
│   └── _template.py          # Copy this to write a new skill — one file, drop in, done
├── actions/                  # Bundled skills — each self-describes via a TOOL dict + handler
│                             #   Everything here drives the COMPUTER, which is what decides
│                             #   whether a new skill belongs in this folder at all.
│   ├── web_search.py         # Gemini + DDG parallel search (news, research, price, compare)
│   ├── screen_processor.py   # Screen & webcam capture for vision
│   ├── background_monitor.py # User-configured topic watching — daily DDG check
│   ├── proactive.py          # Proactive 2.0 — time/context/rotation-aware check-ins
│   ├── reminder.py           # OS-native scheduled notifications
│   ├── system_monitor.py     # CPU / RAM / GPU / temperature telemetry
│   ├── computer_settings.py  # Volume, brightness, WiFi, power (per-OS)
│   ├── computer_control.py   # Keyboard shortcuts, mouse, window management
│   ├── windows_control.py    # Allowlisted Windows and authorized-project actions
│   ├── open_app.py           # Application launcher (per-OS name map)
│   ├── browser_control.py    # Web browser control
│   ├── file_controller.py    # File system operations
│   ├── file_processor.py     # Document reading and summarization
│   ├── send_message.py       # Messaging integration
│   ├── weather_report.py     # Live weather data
│   ├── video_player.py       # Plays video on the HUD, where the avatar normally is
│   └── desktop.py            # Desktop and taskbar control
├── memory/
│   ├── memory_manager.py     # Load/save long_term.json — sessions, monitors, identity
│   ├── config_manager.py     # api_keys.json access — key, OS, name, voice, colour, toggles
│   └── long_term.json        # Persistent store — created on first run
├── core/
│   ├── gemini.py             # One place for every one-shot Gemini call — model ladder, timeouts, cooldowns
│   ├── prompt.txt            # All prompt wording — {tokens} are filled from the live system at startup
│   ├── avatar.py             # Avatar renderer — lighting, pose, expression, mouth (QPainter)
│   ├── avatar_mesh.py        # Head geometry — loads the face, generates skull/neck/rigs
│   ├── face_model.obj        # The face itself (MediaPipe canonical model, Apache-2.0, 25 KB)
│   ├── viseme.py             # Transcript → mouth shapes, fused with the audio's timing
│   ├── echo.py               # Tells your voice from the assistant's own echo; self-calibrating
│   ├── hotkey.py             # Push-to-talk chord — global on Windows, windowed fallback elsewhere
│   ├── undo.py               # One shared undo stack — actions register how to reverse themselves
│   ├── confirm.py            # Irreversible-action gate — the token is issued by the UI, not the model
│   ├── windows_control.py    # Per-action Windows permissions, project boundaries and cancellable tests
│   ├── audio_devices.py      # Microphone / speaker list — filtered, measured, resolved by name
│   ├── voice_input.py        # One-shot local microphone capture and Vosk transcription
│   ├── voice_profiles.py     # Local manual voice preferences — no biometric templates
│   ├── plugin_loader.py      # Plugin engine — discovery, validation, crash isolation
│   ├── action_loader.py      # Bundled-action engine — the built-in twin of plugin_loader
│   └── wake_word.py          # Local "Hey Jarvis" detector — own thread, offline, opt-in
└── config/
    ├── api_keys.json         # Credentials, voice preferences/profiles and toggles (git-ignored)
    └── certs/                # Self-signed TLS pair for the phone dashboard — generated locally (git-ignored)
```

---

## 🙏 Third-Party Assets

| Asset | Source | Licence |
| --- | --- | --- |
| `core/face_model.obj` | [MediaPipe](https://github.com/google-ai-edge/mediapipe) canonical face model — 468 vertices of measured human face geometry | Apache License 2.0 |

---

## 🔒 Your Data

Everything stays on your machine. There is no MARK server, no telemetry and no account.

| What | Where | Notes |
|---|---|---|
| Gemini API key, plugin credentials | `config/api_keys.json` | **Plaintext.** Anyone with your user account can read it. Treat it like a password file. |
| Dashboard TLS certificate + private key | `config/certs/` | Generated locally, self-signed, never leaves the machine. |
| What the assistant remembers about you | `memory/long_term.json` | Delete the file to make it forget everything. |

All three are listed in `.gitignore`, so a fork or a pull request cannot leak them by accident. **If you have already committed `config/api_keys.json` anywhere public, revoke that key** at [aistudio.google.com](https://aistudio.google.com/app/apikey) and generate a new one — removing the file in a later commit does not remove it from the history.

Your voice is streamed to Google's Gemini Live API while a session is open; that is the one thing that leaves your computer, and it stops when you mute or close the app.

---

## ⚠️ License

Personal and non-commercial use only.
Licensed under **[Creative Commons BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)**.

---

## 👤 Connect with the Creator

Engineered by a developer building a real-world JARVIS-style assistant.
⭐ **Star the repository to support the journey to Mark 100.**

| Platform | Link |
| --- | --- |
| YouTube | [@FatihMakes](https://www.youtube.com/@FatihMakes) |
| Instagram | [@fatihmakes](https://www.instagram.com/fatihmakes) |
