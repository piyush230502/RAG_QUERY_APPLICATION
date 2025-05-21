import os
from typing import List, Dict, Any
from data_collection.loaders import WebContentLoader
from data_preprocessing.preprocessor import DocumentChunker
from embeddings_and_representation.embeddings import HuggingFaceEmbeddings
from storage_and_persistence.vector_store import VectorStore
from data_transformation.response_generator import ResponseGenerator
from embeddings_and_representation.embeddings import Retriever
from data_transformation.prompt import PromptManager
from langchain.chains import RetrievalQA







class RAGPipeline:
    def __init__(self, urls: List[str]):
        self.loader = WebContentLoader(urls)
        self.chunker = DocumentChunker()
        self.embeddings = HuggingFaceEmbeddings()
        self.vectorstore = None
        self.retriever = None
        self.generator = None

    def build(self):
        documents = self.loader.load_all_content()
        chunks = self.chunker.create_chunks(documents)
        vector_store = VectorStore(self.embeddings.get_embeddings())
        self.vectorstore = vector_store.create_store(chunks)
        retriever_component = Retriever(self.vectorstore)
        self.retriever = retriever_component.retriever
        self.generator = ResponseGenerator()
        self.qa_chain = self.generator.create_qa_chain(self.retriever)
        
    def query(self, question: str) -> str:
        prompt = PromptManager.create_zephyr_prompt(question)
    
        response = self.qa_chain(prompt)
        return response['result']