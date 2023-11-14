#!/usr/bin/python3

from typing import Tuple, Dict
from map.map import *
from camera.camera import *
from texture.texture_cache import *
from agent.agent_manager import *
from conversation.conversation_manager import *
from ui.ui import *

GAME = 'Darkhaan'
VERSION = '0.1.0-a1'
AUTHOR = '@sajidsarker'
FRAMES_PER_SECOND: float = 60.0
RESOLUTION: Tuple[int, int] = (640, 480)
DIMENSION: float = 64.0

import pygame

class Game:
    is_running: bool = True
    debug_mode: bool = True

    map: Map
    camera: Camera
    texture_cache: TextureCache
    agent_manager: AgentManager
    conversation_manager: ConversationManager

    screen = None
    clock = None

    delta_time: float = 0.0

    key_down: Dict[str, bool]
    key_pressed: Dict[str, bool]
    key_released: Dict[str, bool]

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(GAME + '-v' + VERSION)

        print('[!] Input Initialisation...')
        self.key_down = {
            'k_left': False, 'k_right': False, 'k_up': False, 'k_down': False, 'k_accept': False
        }
        self.key_pressed = {
            'k_left': False, 'k_right': False, 'k_up': False, 'k_down': False, 'k_accept': False
        }
        self.key_released = {
            'k_left': False, 'k_right': False, 'k_up': False, 'k_down': False, 'k_accept': False
        }

        print('[!] Map Initialisation...')
        self.map = Map('../assets/maps/dungeon0.map')

        print('[!] Renderer Initialisation...')
        self.screen = pygame.display.set_mode(RESOLUTION)

        print('[!] Camera Initialisation...')
        self.camera = Camera([0.0, 0.0, 0.0])
        self.camera.instancer = self

        print('[!] Clock Initialisation...')
        self.clock = pygame.time.Clock()

        print('[!] Loading Texture Cache...')
        self.texture_cache = TextureCache('../assets/textures/')

        print('[!] Agent Spawner Initialisation...')
        self.agent_manager = AgentManager()
        self.agent_manager.instancer = self

        print('[!] Agent(s) Initialisation...')
        self.agent_manager.spawn(AgentPlayer, self.map.spawn_position[0] * DIMENSION, self.map.spawn_position[1] * DIMENSION, 180.0)

        print('[!] Conversation Tree Initialisation...')
        # Consider future code modification to load conversations from a file as strings to be processed
        self.conversation_manager = ConversationManager(
            {
                'conversation_0': {
                    0: Dialogue('Narrator', 'START >>', 'Before you is a computer. What do you do?', [1, 2, 3]),
                    1: Dialogue('Narrator', 'Turn on the computer.', 'It did not respond and stays inert.', [4]),
                    2: Dialogue('Narrator', 'Check if the lid is warm.', 'It seems cold, like it has not been turned on in some time.', [4]),
                    3: Dialogue('Narrator', 'Call tech support on your phone.', 'The line is busy and the call ends.', [4]),
                    4: Dialogue('Narrator', 'CONTINUE >>', 'There is nothing to be done.', [])
                }
            }
        )
        self.conversation_manager.instancer = self

    def process_input(self) -> None:
        self.key_pressed = {
            'k_left': False, 'k_right': False, 'k_up': False, 'k_down': False, 'k_accept': False
        }
        self.key_released = {
            'k_left': False, 'k_right': False, 'k_up': False, 'k_down': False, 'k_accept': False
        }

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

            if event.type == pygame.KEYDOWN:
                self.key_pressed['k_left']   = (event.key == pygame.K_LEFT)
                self.key_pressed['k_right']  = (event.key == pygame.K_RIGHT)
                self.key_pressed['k_up']     = (event.key == pygame.K_UP)
                self.key_pressed['k_down']   = (event.key == pygame.K_DOWN)
                self.key_pressed['k_accept'] = (event.key == pygame.K_SPACE)

            if event.type == pygame.KEYUP:
                self.key_released['k_left']   = (event.key == pygame.K_LEFT)
                self.key_released['k_right']  = (event.key == pygame.K_RIGHT)
                self.key_released['k_up']     = (event.key == pygame.K_UP)
                self.key_released['k_down']   = (event.key == pygame.K_DOWN)
                self.key_released['k_accept'] = (event.key == pygame.K_SPACE)

        _key_down = pygame.key.get_pressed()
        self.key_down['k_left']   = _key_down[pygame.K_LEFT]
        self.key_down['k_right']  = _key_down[pygame.K_RIGHT]
        self.key_down['k_up']     = _key_down[pygame.K_UP]
        self.key_down['k_down']   = _key_down[pygame.K_DOWN]
        self.key_down['k_accept'] = _key_down[pygame.K_SPACE]

    def update(self) -> None:
        self.agent_manager.update(self.delta_time)
        self.camera.update(self.agent_manager.entities[0].get_position())
        self.map.update(self.agent_manager.entities[0].get_position())
        self.conversation_manager.update()

        '''
        if self.key_pressed['k_left'] == True:
            self.conversation_manager.play('conversation_0')
        '''

    def render(self) -> None:
        self.screen.fill('teal')

        # Singleton Rendering
        self.agent_manager.render(self.screen)
        self.camera.render(self.screen)
        self.map.render(self.agent_manager.entities[0].get_position(), self.screen)
        self.conversation_manager.render(self.screen)

        # Debug Information
        if self.debug_mode == True:
            draw_text((16.0, 96.0), '{}-v{}'.format(GAME, VERSION), WHITE, self.screen)
            draw_text((16.0, 112.0), '{} ms'.format(str(self.delta_time * 1000.0)), WHITE, self.screen)
            draw_text((16.0, 128.0), str(self.agent_manager.entities[0].position), WHITE, self.screen)

        pygame.display.flip()

def main() -> None:
    print('[!] Isfahan Engine: Launching {}-v{}, created by {}.'.format(GAME, VERSION, AUTHOR))
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