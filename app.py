from flask import Flask, render_template, request, redirect, url_for
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

app = Flask(__name__)

# In-memory storage for blog posts
blog_posts = []

def generate_blog_content(topic):
    prompt = (
        f"Write a catchy, engaging and professional blog post on '{topic}'. "
        "Provide expert-level insights, structure the content with clear paragraphs "
        "and include real-world examples."
    )
    client = Groq(api_key=GROQ_API_KEY)
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    content = ""
    for chunk in completion:
        content += chunk.choices[0].delta.content or ""
    return content

@app.route('/')
def index():
    return render_template('index.html', posts=blog_posts)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        topic = request.form.get('topic')
        content = generate_blog_content(topic)
        blog_posts.append({'topic': topic, 'content': content})
        return redirect(url_for('index'))
    return render_template('new_post.html')

if __name__ == '__main__':
    app.run(debug=True)