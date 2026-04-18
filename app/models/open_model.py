from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
def load_llm():
    model = ChatOpenAI(model='gpt-4o-mini')

    return model

