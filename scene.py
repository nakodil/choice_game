"""Модуль сцены."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from main import App


class Scene:
    """Игровая сцена."""

    def __init__(self, app: App) -> None:
        """Конструктор класса."""
        self.app = app

    def handle_events(self) -> None:
        """Сбор событий, клавиши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.is_run = False
            if event.type == pygame.KEYDOWN and pygame.K_ESCAPE:
                    self.app.is_run = False

    def update(self) -> None:
        """Обновление."""

    def render(self) -> None:
        """Отрисовка игровых объектов на дисплее."""
        self.app.display.fill((255, 0, 0))
        pygame.display.flip()
