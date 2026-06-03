import os
import shutil
from pathlib import Path


FRONTEND_DIR = Path(__file__).resolve().parent
REPO_ROOT = FRONTEND_DIR.parent
BACKEND_DIR = REPO_ROOT / "Project Backend"


def load_dotenv_if_present():
    """Load simple KEY=VALUE pairs from .env without adding a new dependency."""
    for env_path in (REPO_ROOT / ".env", FRONTEND_DIR / ".env"):
        if not env_path.exists():
            continue

        for raw_line in env_path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue

            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and key not in os.environ:
                os.environ[key] = value


def get_config_value(name, default=None):
    load_dotenv_if_present()
    return os.environ.get(name, default)


def resolve_optional_path(value):
    if not value:
        return None

    path = Path(value).expanduser()
    if path.is_absolute():
        return path

    repo_path = REPO_ROOT / path
    if repo_path.exists():
        return repo_path

    frontend_path = FRONTEND_DIR / path
    if frontend_path.exists():
        return frontend_path

    return path


def configure_tesseract(pytesseract_module):
    tesseract_cmd = get_config_value("TESSERACT_CMD")
    resolved_cmd = resolve_optional_path(tesseract_cmd)

    if resolved_cmd and Path(resolved_cmd).exists():
        pytesseract_module.pytesseract.tesseract_cmd = str(resolved_cmd)
        return None

    detected_cmd = shutil.which("tesseract")
    if detected_cmd:
        pytesseract_module.pytesseract.tesseract_cmd = detected_cmd
        return None

    return (
        "Tesseract OCR not found. Install Tesseract OCR and configure "
        "TESSERACT_CMD in .env if it is not available on PATH."
    )


def configure_google_credentials():
    credentials = get_config_value("GOOGLE_APPLICATION_CREDENTIALS")
    resolved_credentials = resolve_optional_path(credentials)

    if not resolved_credentials:
        return (
            "Google Cloud credentials not configured. Set "
            "GOOGLE_APPLICATION_CREDENTIALS in .env."
        )

    if not Path(resolved_credentials).exists():
        return (
            "Google Cloud credentials file not found. Check "
            "GOOGLE_APPLICATION_CREDENTIALS in .env."
        )

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(resolved_credentials)
    return None


def get_youtube_api_key():
    api_key = get_config_value("YOUTUBE_API_KEY", "")
    return api_key.strip()
