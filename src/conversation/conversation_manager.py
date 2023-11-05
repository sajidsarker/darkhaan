#!/usr/bin/python3

from typing import Dict
from dialogue import *

class ConversationManager:
    conversations: Dict[str, Dict[int, Dialogue]]
    conversation_id: str

    def __init__(self, conversations: Dict[str, Dict[int, Dialogue]]) -> None:
        self.conversations = conversations
        for conversation in self.conversations:
            for dialogue in self.conversations[conversation]:
                self.conversations[conversation][dialogue].instancer = self

    def play(self, conversation: str) -> None:
        self.conversation_id = conversation
        self.conversations[self.conversation_id][0].play()