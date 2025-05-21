import os
from typing import List, Dict, Any
from getpass import getpass
import pytesseract
from PIL import Image
import requests
from bs4 import BeautifulSoup
import PyPDF2
import docx
import csv
import re

from langchain_community.document_loaders import WebBaseLoader
import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.vectorstores import Chroma
from langchain.schema import Document

## Page Summary : ability to load websites,images,files like pdf,docx,csv,loads youtube videos



class WebContentLoader:
    def __init__(self, urls: List[str]):
        self.urls = urls
        
    # function loads the documents input by users    
    def load_content(self) -> List[Document]:
        loader = WebBaseLoader(self.urls)
        try:
            documents = loader.load()
            print(f"Successfully loaded content from {len(self.urls)} URLs")
            return documents
        except Exception as e:
            print(f"Error loading content: {str(e)}")
            return []
        
     # loads image   
    def load_image(self):
        try:
            image = Image.open(self.image_path)
            return image
        except Exception as e:
            print(f"Error loading image: {e}")
            return None
     #extract texts from images
    def extract_image_text(self):
        image = self.load_image()
        if image:
            text = pytesseract.image_to_string(image)
            return text
        return None
    
    # loads files like .pdf,.docx,.csv
    def load_file(self, file_path: str) -> str:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        
        file_extension = os.path.splitext(file_path)[1].lower()
        
        if file_extension == '.pdf':
            text = ""
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    text += page.extract_text() + "\n"
            return text
        elif file_extension in ['.doc', '.docx']:
            text = ""
            doc = docx.Document(file_path)
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            return text
        elif file_extension == '.txt':
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        elif file_extension == '.csv':
            text = ""
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    text += ','.join(row) + "\n"
            return text
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")
        
      
    def extract_video_id(self, url):
        # Extracts the video ID from a YouTube URL
        import re
        match = re.search(r"(?:v=|youtu.be/)([\w-]+)", url)
        return match.group(1) if match else None

    def extract_transcript(self, video_id):
        try:
            return YouTubeTranscriptApi.get_transcript(video_id)
        except Exception:
            return None
        
    # extracts from youtube videos
    def load_yt_text(self, youtube_url):
        video_id = self.extract_video_id(youtube_url)
        transcript = self.extract_transcript(video_id)
        if not transcript:
            return ""
        else:
            text = " ".join([seg['text'] for seg in transcript])
            return text
        
    def load_all_content(self,file_path,youtube_url):
        Document_text = self.load_content()+self.extract_image_text() + self.load_file(file_path) + self.load_yt_text(youtube_url)
        return Document_text