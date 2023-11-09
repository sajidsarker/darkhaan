#!/usr/bin/python3

from typing import Tuple, Dict
from agent.agent_manager import *
from ui.ui_helper import *

GAME = 'Darkhaan'
VERSION = '0.1.0-a1'
FRAMES_PER_SECOND: float = 60.0
RESOLUTION: Tuple[int, int] = (640, 480)

print('[!] Isfahan Engine: Launching ' + GAME + '-v' + VERSION)

import pygame

class Game:
    is_running: bool = True

    clock = None
    delta_time: float = 0.0

    key_down: Dict[str, bool]
    key_pressed: Dict[str, bool]
    key_released: Dict[str, bool]

    agent_manager: AgentManager

    screen = None

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(GAME + '-v' + VERSION)

        print('[!] Input Initialisation...')
        self.key_down = {
            'k_left': False,
            'k_right': False,
            'k_up': False,
            'k_down': False
        }
        self.key_pressed = {
            'k_left': False,
            'k_right': False,
            'k_up': False,
            'k_down': False
        }
        self.key_released = {
            'k_left': False,
            'k_right': False,
            'k_up': False,
            'k_down': False
        }

        print('[!] Renderer Initialisation...')
        self.screen = pygame.display.set_mode(RESOLUTION)

        print('[!] Clock Initialisation...')
        self.clock = pygame.time.Clock()

        print('[!] Agent Spawner Initialisation...')
        self.agent_manager = AgentManager()
        self.agent_manager.instancer = self

        print('[!] Agent Initialisation...')
        self.agent_manager.spawn(AgentPlayer, 32.0, 32.0, 180.0)

    def process_input(self) -> None:
        self.key_pressed = {
            'k_left': False,
            'k_right': False,
            'k_up': False,
            'k_down': False
        }
        self.key_released = {
            'k_left': False,
            'k_right': False,
            'k_up': False,
            'k_down': False
        }

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

            if event.type == pygame.KEYDOWN:
                self.key_pressed['k_left'] = (event.key == pygame.K_LEFT)
                self.key_pressed['k_right'] = (event.key == pygame.K_RIGHT)
                self.key_pressed['k_up'] = (event.key == pygame.K_UP)
                self.key_pressed['k_down'] = (event.key == pygame.K_DOWN)

            if event.type == pygame.KEYUP:
                self.key_released['k_left'] = (event.key == pygame.K_LEFT)
                self.key_released['k_right'] = (event.key == pygame.K_RIGHT)
                self.key_released['k_up'] = (event.key == pygame.K_UP)
                self.key_released['k_down'] = (event.key == pygame.K_DOWN)

        _key_down = pygame.key.get_pressed()
        self.key_down['k_left'] = _key_down[pygame.K_LEFT]
        self.key_down['k_right'] = _key_down[pygame.K_RIGHT]
        self.key_down['k_up'] = _key_down[pygame.K_UP]
        self.key_down['k_down'] = _key_down[pygame.K_DOWN]

    def update(self) -> None:
        for entity in self.agent_manager.entities:
            entity.update(self.delta_time)

    def render(self) -> None:
        self.screen.fill('teal')
        self.agent_manager.sprites.draw(self.screen)
        draw_text((32.0, 32.0), '{}-v{}'.format(GAME, VERSION), WHITE, self.screen)
        draw_text((32.0, 48.0), '{} ms'.format(str(self.delta_time * 1000.0)), WHITE, self.screen)
        draw_text((32.0, 64.0), str(self.agent_manager.entities[0].position), WHITE, self.screen)
        pygame.display.flip()

def main() -> None:
    game = Game()

    print('[!] Main Loop Initialisation...')
    while (game.is_running):
        game.process_input()
        game.update()
        game.render()
        game.delta_time = game.clock.tick(FRAMES_PER_SECOND) / 1000.0

    print('[!] Main Loop Ended...')
    print('[!] Exiting Game...')
    pygame.quit()

if __name__ == "__main__":
    main()