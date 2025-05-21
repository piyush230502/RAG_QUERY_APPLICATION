import os
from getpass import getpass
from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings




class HuggingFaceEmbeddings:
    def __init__(self, model_name: str = "BAAI/bge-base-en-v1.5"):
        # Get HuggingFace token if not already set
        if 'HF_TOKEN' not in os.environ:
            hf_token = getpass("Enter your HuggingFace API token: ")
            os.environ['HF_TOKEN'] = hf_token
            
        self.embeddings = HuggingFaceInferenceAPIEmbeddings(
            api_key=os.environ['HF_TOKEN'],
            model_name=model_name
        )
    
    def get_embeddings(self):
        return self.embeddings