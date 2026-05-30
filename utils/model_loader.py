import os
from dotenv import load_dotenv
from typing import Any, Literal, Optional
from pydantic import Field , BaseModel
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from utils.config_loader import load_config


class ConfigLoader():
    def __init__(self):
        print(f"Loading config........")
        self.config = load_config()

    def __getitem__(self, key):
        return self.config[key]

class ModelLoader(BaseModel):
    model_provider: Literal["openai", "groq"] = "groq"
    config: Optional[ConfigLoader] = Field(default=None, exclude=True)

    def model_post_init(self, __context: Any) -> None:
        self.config = ConfigLoader()

    class Config:
        arbitrary_types_allowed = True

    def load_llm(self):
        """
        Load and return the LLM Model.
        """
        load_dotenv()
        print("LLM Loading...")
        print(f"Loading model from provider: {self.model_provider}")
        if self.model_provider == "groq":
            print("Loading llm from Groq........")
            groq_api_key = os.getenv("GROQ_API_KEY")
            if not groq_api_key:
                raise ValueError("Missing GROQ_API_KEY. Set it in your environment or .env file.")
            model_name = os.getenv("GROQ_MODEL") or self.config['llm']['groq']['model_name']
            llm=ChatGroq(model=model_name, api_key=groq_api_key)
        elif self.model_provider == "openai":
            print("Loading llm from OpenAI........")    
            openai_api_key = os.getenv("OPENAI_API_KEY")
            if not openai_api_key:
                raise ValueError("Missing OPENAI_API_KEY. Set it in your environment or .env file.")
            model_name = os.getenv("OPENAI_MODEL") or self.config['llm']['openai']['model_name']
            llm = ChatOpenAI(model_name=model_name,api_key=openai_api_key)

        return llm  