from logger import get_logger
from models.chats import ChatMessage
from models.settings import common_dependencies

logger = get_logger(__name__)


def get_chat_name_from_first_question(chat_message: ChatMessage):
    chat_name = " ".join(chat_message.question.split()[:3])
    return chat_name