from pathlib import Path

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


BASE_DIR = Path(__file__).resolve().parent.parent
BOT_DB_PATH = BASE_DIR / "chatbot_app.sqlite3"

TRAINING_DATA = [
    ["hi", "hello"],
    ["hello", "hi there"],
    ["good morning", "good morning, how can I help you today?"],
    ["how are you", "I am doing well, thank you for asking."],
    ["what is your name", "I am a Django chatbot built with ChatterBot."],
    ["bye", "goodbye, have a nice day."],
]


def build_bot() -> ChatBot:
    return ChatBot(
        "DjangoChatBot",
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        database_uri=f"sqlite:///{BOT_DB_PATH}",
        logic_adapters=[
            "chatterbot.logic.BestMatch",
            "chatterbot.logic.TimeLogicAdapter",
        ],
        read_only=False,
    )


def train_bot(bot: ChatBot) -> None:
    trainer = ListTrainer(bot)
    for conversation in TRAINING_DATA:
        trainer.train(conversation)
