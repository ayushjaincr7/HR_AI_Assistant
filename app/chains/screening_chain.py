from langchain_core.output_parsers import StrOutputParser
from app.models.open_model import load_llm
from app.prompts.resume_prompt import resume_prompt


llm = load_llm()

chain = resume_prompt | llm | StrOutputParser()


