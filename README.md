# GFG RAG Application

![RAG App Banner](https://imgur.com/4M7IWwP.png)

A **Retrieval-Augmented Generation (RAG) Application** that allows you to query across website URLs, images, files, and YouTube videos—all in one place! Built with Flask, LangChain, and a beautiful, modern UI.

---

## 🚀 Features

- **Multi-Source Content Loading:**
  - Web pages (URLs)
  - Image files (extracts text via OCR)
  - YouTube videos (extracts transcript)
  - PDF, DOCX, TXT, CSV files
- **Unified Query Interface:**
  - Ask questions across all uploaded/linked content
- **Gorgeous, Responsive UI:**
  - Modern, mobile-friendly, and visually appealing
- **Easy to Use:**
  - Simple form-based interface

---

## 🖥️ Demo

![App Screenshot](https://imgur.com/8Q2Qw7B.png)

---

## 🛠️ Getting Started

### 1. Clone the Repository
```bash
# Using PowerShell
git clone <your-repo-url>
cd GFG_RAG
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py
```

The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📦 Project Structure

```
GFG_RAG/
│   app.py
│   requirements.txt
│   README.md
│
├── data_collection/
│     loaders.py
├── data_preprocessing/
│     preprocessor.py
├── data_transformation/
│     prompt.py
│     response_generator.py
├── embeddings_and_representation/
│     embeddings.py
│     retrival.py
├── storage_and_persistence/
│     vector_store.py
├── updating_and_refreshing/
│     RAG_pipeline.py
├── templates/
│     index.html
```

---

## ✨ Usage

1. **Enter Website URLs:** (comma separated)
2. **Upload an Image:** (optional, for OCR)
3. **Enter YouTube URL:** (optional, for transcript)
4. **Ask Your Query:**
5. **Get Instant Answers!**

---

## 🧩 Tech Stack
- **Backend:** Flask, LangChain
- **OCR:** pytesseract, Pillow
- **YouTube:** youtube_transcript_api, yt_dlp
- **File Parsing:** PyPDF2, python-docx, csv
- **Frontend:** HTML5, CSS3 (custom, responsive)

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License
This project is licensed under the MIT License.

---

## 🙏 Acknowledgements
- [LangChain](https://github.com/langchain-ai/langchain)
- [Flask](https://flask.palletsprojects.com/)
- [GFG Community](https://www.geeksforgeeks.org/)

---

> Made with ❤️ for the Generative AI community.
