"""Главный модуль приложения."""

import pygame

from player import Player
from scene import Scene


class App:
    """Игра."""

    def __init__(self) -> None:
        """Конструктор класса."""
        pygame.init()

        info = pygame.display.Info()
        self.display_w = info.current_w
        self.display_h = info.current_h
        self.display = pygame.display.set_mode(
            (self.display_w, self.display_h),
            pygame.FULLSCREEN,
        )

        self.is_run = False
        self.player = None

    def main_loop(self) -> None:
        """Главный цикл игры."""
        self.scene = Scene(self)
        self.player = Player()
        self.is_run = True
        while self.is_run:
            self.scene.handle_events()
            self.scene.update()
            self.scene.render()
        pygame.quit()


if __name__ == "__main__":
    app = App()
    app.main_loop()
