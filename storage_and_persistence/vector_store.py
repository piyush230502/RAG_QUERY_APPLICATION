
from langchain_community.vectorstores import Chroma
from typing import List, Dict, Any
from langchain.schema import Document






class VectorStore:
    def __init__(self, embeddings):
        self.embeddings = embeddings
        self.vectorstore = None
    
    def create_store(self, documents: List[Document]) -> Chroma:
        self.vectorstore = Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings
        )
        return self.vectorstore