

from langchain.vectorstores import Chroma
from langchain.schema import Document
import os
from typing import List, Dict, Any
from getpass import getpass





class Retriever:
    def __init__(self, vectorstore: Chroma, k: int = 3):
        self.retriever = vectorstore.as_retriever(
            search_type="mmr",  # Maximum Marginal Relevance
            search_kwargs={"k": k}
        )
    
    def get_relevant_documents(self, query: str) -> List[Document]:
        return self.retriever.get_relevant_documents(query)