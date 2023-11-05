#!/usr/bin/python3

from agent.agent import *

class AgentPlayer(Agent):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, '../assets/sprites/agent_player.png',
                         image_index=0.0,
                         image_speed=0.0,
                         image_width = 32.0,
                         image_height = 32.0)

    def update(self, delta_time: float) -> None:
        _h: int = 0
        _v: int = 0

        if self.instancer.input[pygame.K_RIGHT] == True and self.instancer.input[pygame.K_LEFT] == False:
            _h = 1

        if self.instancer.input[pygame.K_RIGHT] == False and self.instancer.input[pygame.K_LEFT] == True:
            _h = -1

        if self.instancer.input[pygame.K_DOWN] == True and self.instancer.input[pygame.K_UP] == False:
            _v = 1

        if self.instancer.input[pygame.K_DOWN] == False and self.instancer.input[pygame.K_UP] == True:
            _v = -1

        self.set_velocity(_h * 3.0, _v * 3.0)
        super().update()