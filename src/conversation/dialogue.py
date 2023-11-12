#!/usr/bin/python3

from typing import List
from ui.ui import *

RESOLUTION: Tuple[int, int] = (640, 480)

class Dialogue:
    speaker: str
    prompt: str
    content: str
    choices: List
    selector: int = 0

    instancer = None

    def __init__(self, speaker: str, prompt: str, content: str, choices: List[int]) -> None:
        self.speaker = speaker
        self.prompt = prompt
        self.content = content
        self.choices = choices

    def play(self) -> None:
        self.generate()

        print('{}: {}'.format(self.speaker, self.content))

        i: int = 0
        for choice in self.choices:
            print('[{}] {}'.format(str(i + 1), self.instancer.conversations[self.instancer.conversation_id][choice].prompt))
            i += 1

    def generate(self) -> None:
        self._text: List[str] = []
        self._text.append('[~] ' + self.prompt)
        self._text.append('')
        self._text.append(self.speaker + ':')
        self._text.append(self.content)
        self._text.append('')

        i: int = 0
        for choice in self.choices:
            self._text.append('[{}]: '.format(str(i + 1)) + self.instancer.conversations[self.instancer.conversation_id][choice].prompt)
            i += 1

    def update(self) -> None:
        _v: int = 0

        if self.instancer.instancer.key_pressed['k_up'] == True and self.instancer.instancer.key_pressed['k_down'] == False:
            _v = -1

        if self.instancer.instancer.key_pressed['k_up'] == False and self.instancer.instancer.key_pressed['k_down'] == True:
            _v = 1

        self.selector = max(0, min(self.selector + _v, len(self.choices) - 1))

        if self.instancer.instancer.key_pressed['k_accept'] == True:
            choice: int = self.selector
            self.selector = 0

            if len(self.choices) > 0:
                self.instancer.conversations[self.instancer.conversation_id][self.choices[choice]].play()
                self.instancer.dialogue_id = self.choices[choice]
            else:
                self.instancer.conversation_id = ''

    def render(self, screen) -> None:
        draw_text((RESOLUTION[0] - 24, 144 - 16), str(self.selector), WHITE, screen)
        draw_window((16.0, 144.0), (RESOLUTION[0] - 32, RESOLUTION[1] - 160), self._text, BLACK, screen)