#!/usr/bin/python3

from typing import Dict
from conversation.dialogue import *

class ConversationManager:
    conversations: Dict[str, Dict[int, Dialogue]]
    conversation_id: str
    dialogue_id: int

    def __init__(self, conversations: Dict[str, Dict[int, Dialogue]]) -> None:
        self.conversations = conversations
        self.conversation_id = ''
        self.dialogue_id = 0

        for conversation in self.conversations:
            for dialogue in self.conversations[conversation]:
                self.conversations[conversation][dialogue].instancer = self

    def play(self, conversation: str) -> None:
        self.conversation_id = conversation
        self.dialogue_id = 0
        self.conversations[self.conversation_id][0].play()

    def update(self) -> None:
        pass

    def render(self, screen) -> None:
        if self.conversation_id != '':
            self.conversations[self.conversation_id][self.dialogue_id].render(screen)