# Blog Writer Agent

A simple, professional blog writer agent built with Python, Flask, and Groq's API.
The agent generates expert-level blog posts on a topic provided by the user.

## Features

- Generate blog posts using Groq's API
- Catchy and professional frontend using Bootstrap
- In-memory storage for generated posts

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Prajjwal-Here/blog_agent.git
   ```
2. Navigate to the project folder:
   ```
   cd blog_agent
   ```
3. Create and activate a virtual environment (Windows):
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Set your Groq API key in the `.env` file:
   ```
   GROQ_API_KEY=your_actual_api_key_here
   ```
6. Run the application:
   ```
   python app.py
   ```
7. Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000)

## License

This project is licensed under the MIT License.
