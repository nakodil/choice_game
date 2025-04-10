"""Конфигурация."""

from pathlib import Path

APP_NAME = "Игра"

BASE_DIR = Path(__file__).resolve().parent

ASSETS_DIR = BASE_DIR / "assets"
IMG_DIR = ASSETS_DIR / "img"
SOUND_DIR = ASSETS_DIR / "sound"
FONT_DIR = ASSETS_DIR / "font"

# Базовые цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Цвета игры
BG_COLOR = BLACK
CARD_TEXT_COLOR = BLACK
CARD_BG_COLOR = WHITE

# Шрифты игровых обхъектов
BASE_FONT = FONT_DIR / "Roboto-Regular.ttf"
BASE_FONT_COLOR = WHITE
