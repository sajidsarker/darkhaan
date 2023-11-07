#!/usr/bin/python3

from typing import List

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

        if len(self.choices) > 1:
            choice: int = int(input('?'))
            choice = max(0, min(choice, len(self.choices)))
            choice -= 1
        else:
            choice: str = input('?')
            choice: int = 0

        if len(self.choices) > 0:
            self.instancer.conversations[self.instancer.conversation_id][self.choices[choice]].play()
        else:
            self.instancer.conversation_id = ''
