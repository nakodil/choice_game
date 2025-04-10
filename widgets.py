"""Модуль виджетов."""

import pygame

import config


class WidgetBase(pygame.sprite.Sprite):
    """Базовый текстовый виджет."""

    def __init__(
            self,
            text: str,
            coords: tuple[int, int],
            *groups: tuple[pygame.sprite.Sprite],
    ) -> None:
        """Конструктор класса базового виджета."""
        super().__init__(*groups)
        self.text = text
        self.coords = coords
        self.sprite_groups = groups
        self.font = config.BASE_FONT
        self.font_size = 20  # FIXME: передать размер шрифта из приложения
        self.color = config.BASE_FONT_COLOR
        self.image = None
        self.rect = None
        for group in self.sprite_groups:
            group.add(self)
        self.update()

    def update(self) -> None:
        """Обновление аттрибутов изображения."""
        font = pygame.font.Font(self.font, self.font_size)
        self.image = font.render(self.text, True, self.color)
        self.rect = self.image.get_rect(center=self.coords)


class WidgetCard(pygame.sprite.Sprite):
    """Карточка опции."""

    def __init__(
            self,
            text: str,
            topleft: tuple[int, int],
            *groups: tuple[pygame.sprite.Sprite],
    ) -> None:
        """Конструктор класса карточки опции."""
        super().__init__(*groups)
        self.text = text
        self.topleft = topleft
        self.sprite_groups = groups
        self.font = config.BASE_FONT
        self.font_size = 24  # или использовать размер из приложения
        self.text_color = config.CARD_TEXT_COLOR
        self.bg_color = config.CARD_BG_COLOR
        self.card_width = pygame.display.get_surface().get_width() // 3
        self.card_height = self.font_size * 4
        self.image = None
        self.rect = None
        for group in self.sprite_groups:
            group.add(self)
        self.update()

    def update(self) -> None:
        """Обновление аттрибутов изображения."""
        font = pygame.font.Font(self.font, self.font_size)
        text_surface = font.render(self.text, True, self.text_color)

        # Создаем карточку как прямоугольник с заливкой
        self.image = pygame.Surface((self.card_width, self.card_height))
        self.image.fill(self.bg_color)

        # Центрируем текст в прямоугольнике
        text_rect = text_surface.get_rect(
            center=(self.card_width // 2, self.card_height // 2),
        )

        # Заливаем прямоугольник
        self.image.blit(text_surface, text_rect)

        # Позиция карточки
        self.rect = self.image.get_rect(topleft=self.topleft)
