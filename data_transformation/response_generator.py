
from langchain.llms import HuggingFaceHub
from langchain.chains import RetrievalQA






class ResponseGenerator:
    def __init__(self, model_id: str = "HuggingFaceH4/zephyr-7b-alpha"):
        self.model = HuggingFaceHub(
            repo_id=model_id,
            model_kwargs={
                "temperature": 0.5,
                "max_new_tokens": 512,
                "max_length": 64
            }
        )
        
    def create_qa_chain(self, retriever) -> RetrievalQA:
        return RetrievalQA.from_chain_type(
            llm=self.model,
            retriever=retriever,
            chain_type="stuff"
        )