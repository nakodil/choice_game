"""Главный модуль приложения."""

import pygame

import config
import content
from player import Player
from scene import Scene


class App:
    """Игра."""

    def __init__(self) -> None:
        """Конструктор класса приложения."""
        pygame.init()

        info = pygame.display.Info()
        self.display_w = info.current_w
        self.display_h = info.current_h
        self.display = pygame.display.set_mode(
            (self.display_w, self.display_h),
            pygame.FULLSCREEN,
        )
        pygame.display.set_caption(config.APP_NAME)
        self.font_size = int(min(self.display_w, self.display_h) * 0.02)

        self.is_run = False
        self.scene = None
        self.player = None

    def main_loop(self) -> None:
        """Главный цикл игры."""
        start_scene = content.start
        self.scene = Scene(self, start_scene)
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
