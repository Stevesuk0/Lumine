#gitignore

# AGENTS.md — Lumine

Windows-only thermal controller (open-source AWCC alternative) for Dell G15 / Alienware laptops.
Python >= 3.14, dependency management via [uv](https://docs.astral.sh/uv). GPL v3.
Based on AlexIII's tcc-g15; the Dell WMI protocol it talks to is documented in
[tcc-g15's WMI-AWCC-doc](https://github.com/AlexIII/tcc-g15/blob/master/WMI-AWCC-doc.md).

## Commands

```bash
uv sync                        # install deps into .venv
sudo uv run src\lumine.py      # run the app (from repo root; needs admin for the WMI thermal interface)
powershell -File pack_release.ps1   # build all 7 per-language release zips with PyInstaller
```

There is no test suite, linter, or type-checker configured. Verify changes by running the app on target hardware (or at least confirming it starts and reads the config).

## Layout

- `src/lumine.py` — the entire app: entry point, maliang UI, tray menu, hotkeys, failsafe logic, update check, startup registration. Single file by design.
- `src/Backend/AWCCWmiWrapper.py` — raw Dell AWCC WMI calls. Arguments are packed ints of the form `(id << 8) | opcode` — this is the Dell wire protocol, not dead code. Do not "simplify" it without reading the WMI-AWCC doc.
- `src/Backend/AWCCThermal.py` — fan/mode API built on the wrapper (fan index 0 = CPU, 1 = GPU). The UI layer must go through this, never call WMI directly.
- `src/Backend/DetectHardware.py` — CPU/GPU display names via WMI.
- `src/Backend/Configuration.py` — YAML config load/save; config lives in `.lumine/config.yaml` (relative to CWD, with `icons/`).
- `src/Languages/*.py` — one module per locale, each defining a `Text` Enum. `en_US.py` is the source of truth.
- `icons/` — runtime assets loaded by **relative path** (`icons/icon.png`); the app must be launched with the repo root (or dist dir) as CWD.

## Conventions & gotchas

- **All user-facing strings come from the `Text` enum.** New UI text means adding the key to `en_US.py` first, then to all 6 other locale files (`hi_IN`, `ja_JP`, `ko_KR`, `ru_RU`, `zh_CN`, `zh_TW`).
- The **example config is localized text**: `Text.example_config` inside each language file is written verbatim into `.lumine/config.yaml`. Config documentation lives there, not in Configuration.py.
- **Version bumps touch three places in lockstep**: `self.version` in `src/lumine.py`, `$VERSION` in `pack_release.ps1`, and `lumine_version:` inside `Text.example_config` in *every* language file. On mismatch, the app overwrites the user's config with `example_config` (losing their hotkeys/thresholds), so these must stay in sync.
- `pack_release.ps1` rewrites the `use_language = xx` comment block at the top of `lumine.py` (one uncommented line per build) and restores it afterward. Keep those exact lines in that exact format — the regex matches `^use_language = xx` / `^# use_language = xx` at line start.
- In `LumineApp.__init__` there are duplicate constructions; **`self.awccthermal` is the live instance** used everywhere (`self.awcc` is dead). `self.awccwrapper` is `awccthermal._awcc`.
- The UI update loop is a self-rescheduling `root.after(update_interval, ...)` in `update_info()` — keep it rescheduling on every path or the UI freezes.
- Windows-only throughout: `wmi`, `winreg` (Run-key autostart), `win32event` single-instance mutex `Global\Lumine`, `winotify` toasts, `pystray` tray, `keyboard` global hotkeys. Do not add POSIX fallbacks.
- Known hardware limitations (don't try to "fix"): switching to/from G-Mode freezes the system ~1 s (Dell limitation); BIOS can override fan speeds; GPU temp readings can be wrong on some models.
- maliang styling quirk: `maliang.configs.Env.system` is toggled between `"Windows10"`/`"Windows11"` around widget creation in `show_widgets()` to pick per-widget styling — preserve that ordering.
- Commit messages use short prefixes: `fix:`, `add:`, `chore:`.
