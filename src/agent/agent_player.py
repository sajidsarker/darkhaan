#!/usr/bin/python3

import math

from agent.agent import *

DIMENSION: float = 64.0

class AgentPlayer(Agent):
    def __init__(self, x: float, y: float, z: float = 0.0) -> None:
        super().__init__(x, y, z, '../assets/sprites/agent_player.png',
                         image_index = 0.0,
                         image_speed = 0.0,
                         image_width = DIMENSION,
                         image_height = DIMENSION)

    def interact(self) -> None:
        pass

    def update(self, delta_time: float) -> None:
        _h: int = 0
        _v: int = 0

        if self.instancer.key_pressed['k_right'] == True and self.instancer.key_pressed['k_left'] == False:
            _h = -1

        if self.instancer.key_pressed['k_right'] == False and self.instancer.key_pressed['k_left'] == True:
            _h = 1

        if self.instancer.key_down['k_down'] == True and self.instancer.key_down['k_up'] == False:
            _v = 1

        if self.instancer.key_down['k_down'] == False and self.instancer.key_down['k_up'] == True:
            _v = -1

        if self.position[0] % DIMENSION == 0 and self.position[1] % DIMENSION == 0 and self.position[2] % 90.0 == 0:
            self.set_velocity(0.0, 0.0, 0.0)

            if self.instancer.key_pressed['k_accept'] == True:
                _dx: int = int(math.cos(self.position[2] *  math.pi / 180.0))
                _dy: int = int(math.sin(self.position[2] *  math.pi / 180.0))

                _sx: int = int(self.position[0] // DIMENSION)
                _sy: int = int(self.position[1] // DIMENSION)

                print('x: {}; y: {}'.format(_sx + _dx, _sy + _dy))
                if self.instancer.map.data['agents'][_sx + _dx][_sy + _dy] != None:
                    _h = 0
                    _v = 0
                    self.instancer.map.data['agents'][_sx + _dx][_sy + _dy].interact()

            if abs(_h) > 0:
                self.set_velocity(0.0, 0.0, -_h * 5.0)
                _v = 0

            if abs(_v) > 0:
                _x: float = 8.0 * -_v * math.cos(self.position[2] *  math.pi / 180.0)
                _y: float = 8.0 * -_v * math.sin(self.position[2] *  math.pi / 180.0)

                _sx: int = int(self.position[0] // DIMENSION)
                _sy: int = int(self.position[1] // DIMENSION)

                _dx: int = int(_x / 8.0)
                _dy: int = int(_y / 8.0)

                if abs(_dx) > 0:
                    #print('X: {}->{}'.format(_sx, _dx))
                    if self.instancer.map.data['collisions'][_sy][_sx + _dx] == 0 and self.instancer.map.data['agents'][_sy][_sx + _dx] == None:
                        self.instancer.map.data['agents'][_sy][_sx] = None
                        self.instancer.map.data['agents'][_sy][_sx + _dx] = self
                        self.set_velocity(_x, 0.0, 0.0)
                        _dy = 0

                if abs(_dy) > 0:
                    #print('Y: {}->{}'.format(_sy, _dy))
                    if self.instancer.map.data['collisions'][_sy + _dy][_sx] == 0 and self.instancer.map.data['agents'][_sy + _dy][_sx] == None:
                        self.instancer.map.data['agents'][_sy][_sx] = None
                        self.instancer.map.data['agents'][_sy + _dy][_sx] = self
                        self.set_velocity(0.0, _y, 0.0)
                        _dx = 0

        for i in range(len(self.position)):
            self.position[i] += self.velocity[i]

        if self.position[2] < 0.0:
            self.position[2] += 360.0

        if self.position[2] >= 360.0:
            self.position[2] -= 360.0

        self.sprite.rect.center = (self.position[0] + self.sprite.image_width * 0.5, self.position[1] + self.sprite.image_height * 0.5)