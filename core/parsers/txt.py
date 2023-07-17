from langchain.document_loaders import TextLoader
from core.models.files import File
from core.models.settings import CommonsDep

from .common import process_file


async def process_txt(commons: CommonsDep, file: File, enable_summarization, brain_id, user_openai_api_key):
    return await process_file(commons, file, TextLoader, enable_summarization, brain_id,user_openai_api_key)
