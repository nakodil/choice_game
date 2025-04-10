"""Модуль сцены."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pygame

import config
from widgets import WidgetBase, WidgetCard

if TYPE_CHECKING:
    from main import App


class Scene:
    """Игровая сцена."""

    def __init__(
            self,
            app: App,
            content: dict,
    ) -> None:
        """Конструктор класса игровой сцены."""
        self.sprites = pygame.sprite.Group()
        self.app = app
        self.display = app.display
        self.width = self.app.display_w
        self.height = self.app.display_h

        # Загрузка контента
        image_name = content["bg"]
        title = content["title"]
        description = content["description"]
        options = content["options"]

        self.bg_image = self.get_scaled_image(image_name)
        self.title_text = title
        self.description_text = description
        self.options = options

        self.make_widgets()

    def handle_events(self) -> None:
        """Сбор событий, клавиши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.is_run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.app.is_run = False

    def update(self) -> None:
        """Логика."""
        self.sprites.update()

    def render(self) -> None:
        """Отрисовка игровых объектов на дисплее."""
        self.display.fill(config.BG_COLOR)
        self.display.blit(self.bg_image, (0, 0))
        self.sprites.draw(self.display)
        pygame.display.flip()

    def get_scaled_image(self, name: str) -> pygame.Surface:
        """Возвращает масштабированное на весь экран изображение.

        Загружает изображение, масштабирует, обрезает при необходимости
        и возвращает его поверхность.
        """
        image = pygame.image.load(config.IMG_DIR / name).convert()
        original_width, original_height = image.get_size()

        # Вычисляем пропорцию изображения и его размеры
        scale_factor = max(self.width / original_width, self.height / original_height)
        scaled_width = int(original_width * scale_factor)
        scaled_height = int(original_height * scale_factor)

        # Масштабируем изображение
        scaled_image = pygame.transform.smoothscale(image, (scaled_width, scaled_height))

        # Вычисляем координаты верхнего левого угла под обрез
        x = (scaled_width - self.width) // 2
        y = (scaled_height - self.height) // 2

        return scaled_image.subsurface((x, y, self.width, self.height)).copy()

    def make_widgets(self) -> None:
        """Создает все виджеты сцены."""
        margin_y = self.app.font_size * 2
        x = self.width // 2
        y = self.height // 10

        # Заголовок
        WidgetBase(self.title_text, (x, y), self.sprites)
        y += margin_y

        # Описание
        WidgetBase(self.description_text, (x, y), self.sprites)
        y += margin_y

        # Карточки опций
        card_width = self.width // 3
        card_height = self.app.font_size * 4  # должно совпадать с высотой в WidgetCard
        num_cards = len(self.options)
        total_width = num_cards * card_width
        total_padding = self.width - total_width
        padding = total_padding // (num_cards + 1)

        # Центрируем карточки по горизонтали
        current_x = padding

        # Центрируем карточки по вертикали
        y = (self.height - card_height) // 2

        for option in self.options:
            WidgetCard(option, (current_x, y), self.sprites)
            current_x += card_width + padding
