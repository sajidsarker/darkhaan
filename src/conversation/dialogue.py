#!/usr/bin/python3

from typing import List

class Dialogue:
    prompt: str
    content: str
    choices: List

    instancer = None

    def __init__(self, prompt: str, content: str, choices: List[int]) -> None:
        self.prompt = prompt
        self.content = content
        self.choices = choices

    def play(self) -> None:
        print(self.content)

        i: int = 0
        for choice in self.choices:
            print(str(i + 1) + ': ' + self.instancer.conversations[self.instancer.conversation_id][choice].prompt)
            i += 1

        if len(self.choices) > 1:
            choice: int = int(input('?'))
            choice -= 1
        else:
            choice: int = 0

        if len(self.choices) > 0:
            self.instancer.conversations[self.instancer.conversation_id][self.choices[choice]].update()
        else:
            self.instancer.conversation_id = ''
