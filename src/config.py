"""Central paths and constants (dataset filenames, RANDOM_STATE, TOP_N)."""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA = BASE_DIR / "data" / "raw"

PROCESSED_DATA = BASE_DIR / "data" / "processed"

MODEL_PATH = BASE_DIR / "models"

ASSET_PATH = BASE_DIR / "app" / "assets"