# Font Conversion (TTF / OTF to WOFF2)

A lightweight Python utility to batch convert `.ttf` and `.otf` font files into modern, web-optimized `.woff2` files using [fonttools](https://github.com/fonttools/fonttools) and [brotli](https://github.com/google/brotli). Managed with [uv](https://github.com/astral-sh/uv).

---

## Directory Structure

```text
Font_Conversion_TTF_2_WOFF/
├── import/          # Place input font files (.ttf, .otf) here
├── export/          # Converted .woff2 fonts are saved here
├── main.py          # Batch conversion script
├── pyproject.toml   # Project dependencies and configuration
└── uv.lock          # Locked dependencies
```

---

## Prerequisites

Make sure you have `uv` installed. If you do not have it yet, install it via:

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

## Setup (New Clone / Machine)

When cloning the repository to a new directory or machine, set up the project environment with `uv`:

```bash
# 1. Navigate to the project directory
cd Font_Conversion_TTF_2_WOFF

# 2. Sync and install dependencies
uv sync
```

> [!NOTE]
> `uv sync` will automatically create a local virtual environment (`.venv`) and install all required dependencies specified in `pyproject.toml` (`fonttools` and `brotli`).

---

## How to Use

1. **Add font files**: Place any `.ttf` or `.otf` files you wish to convert into the `import/` directory.
2. **Run the conversion**:
   ```bash
   uv run python main.py
   ```
3. **Collect your fonts**: Find your converted `.woff2` font files in the `export/` directory.

---

## Notes

* **Formats Supported**: Input supports `.ttf` and `.otf`. Output is `.woff2`.
* **Legacy WOFF**: Output for `.woff` is commented out by default in `main.py`. If legacy `.woff` support is ever required, uncomment the respective lines in `main.py`.
