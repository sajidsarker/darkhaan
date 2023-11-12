#!/usr/bin/python3

from typing import List
from ui.ui import *

RESOLUTION: Tuple[int, int] = (640, 480)

class Dialogue:
    speaker: str
    prompt: str
    content: str
    choices: List

    instancer = None

    def __init__(self, speaker: str, prompt: str, content: str, choices: List[int]) -> None:
        self.speaker = speaker
        self.prompt = prompt
        self.content = content
        self.choices = choices

    def play(self) -> None:
        print('{}: {}'.format(self.speaker, self.content))

        i: int = 0
        for choice in self.choices:
            print('[{}] {}'.format(str(i + 1), self.instancer.conversations[self.instancer.conversation_id][choice].prompt))
            i += 1

    def update(self) -> None:
        if len(self.choices) > 1:
            choice: int = int(input('?'))
            choice = max(0, min(choice, len(self.choices)))
            choice -= 1
        else:
            choice: str = input('?')
            choice: int = 0

        if len(self.choices) > 0:
            self.instancer.conversations[self.instancer.conversation_id][self.choices[choice]].play()
            self.instancer.dialogue_id = self.choices[choice]
        else:
            self.instancer.conversation_id = ''

    def render(self, screen) -> None:
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

        draw_window((16.0, 144.0), (RESOLUTION[0] - 32, RESOLUTION[1] - 160), self._text, BLACK, screen)