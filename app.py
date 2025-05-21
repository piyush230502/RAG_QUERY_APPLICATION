from flask import Flask, render_template, request
import os
from data_collection.loaders import WebContentLoader

def get_answer_from_content(content, query):
    # Return all processed content for the query
    if not content:
        return "No content found."
    return content

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        website_url = request.form.get('website_url', '')
        youtube_url = request.form.get('youtube_url', '')
        query = request.form.get('query', '')
        image_file = request.files.get('image_file')
        image_path = None
        if image_file and image_file.filename:
            image_path = os.path.join('uploads', image_file.filename)
            os.makedirs('uploads', exist_ok=True)
            image_file.save(image_path)
        urls = [u.strip() for u in website_url.split(',') if u.strip()]
        loader = WebContentLoader(urls)
        # Set image_path if provided
        if image_path:
            loader.image_path = image_path
        # Load all content
        try:
            content = ''
            if urls:
                content += ' '.join([doc.page_content if hasattr(doc, 'page_content') else str(doc) for doc in loader.load_content()])
            if image_path:
                img_text = loader.extract_image_text()
                if img_text:
                    content += ' ' + img_text
            if youtube_url:
                content += ' ' + loader.load_yt_text(youtube_url)
        except Exception as e:
            content = f"Error loading content: {e}"
        result = get_answer_from_content(content, query)
        # Clean up uploaded image
        if image_path and os.path.exists(image_path):
            os.remove(image_path)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
