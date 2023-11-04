#!/usr/bin/python3

from typing import Tuple
from agent.agent_spawner import *

GAME = 'Darkhaan'
VERSION = '1.0.0'
FRAMES_PER_SECOND: float = 60.0
RESOLUTION: Tuple[int, int] = (640, 480)

print('[Info] Launching ' + GAME + '-v' + VERSION)

import pygame

class Game:
    is_running: bool = True
    delta_time: float = 0.0

    agent_spawner: AgentSpawner

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(GAME + '-v' + VERSION)

        print('[Info] Renderer Initialisation...')
        self.screen = pygame.display.set_mode(RESOLUTION)

        print('[Info] Clock Initialisation...')
        self.clock = pygame.time.Clock()

        print('[Info] Agent Spawner Initialisation...')
        self.agent_spawner = AgentSpawner()
        self.agent_spawner.instancer = self

        print('[Info] Agent Initialisation...')
        self.agent_spawner.spawn(AgentPlayer, 64.0, RESOLUTION[1] * 0.5)
        #self.agent_spawner.spawn(AgentEnemyA, 128.0, 32.0)
        #self.agent_spawner.spawn(AgentEnemyB, 128.0, 64.0)

    def process_input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

        self.input = pygame.key.get_pressed()

    def update(self) -> None:
        for entity in self.agent_spawner.entities:
            entity.update(self.delta_time)

    def render(self) -> None:
        self.screen.fill('teal')
        self.agent_spawner.sprites.draw(self.screen)
        pygame.display.flip()

def main():
    game = Game()

    print('[Info] Main Loop Initialisation...')
    while (game.is_running):
        game.process_input()
        game.update()
        game.render()
        game.delta_time = game.clock.tick(FRAMES_PER_SECOND) / 1000.0

    print('[Info] Main Loop Ended...')
    print('[Info] Exiting Game...')
    pygame.quit()

if __name__ == "__main__":
    main()