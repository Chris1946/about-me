# Chris Jobi | Digital Ecosystem & Portfolio

Welcome to the repository for my interactive, AI-powered portfolio! 

Instead of a traditional static website, I built a **dynamic terminal interface** where you can interact directly with an AI proxy trained on my background, skills, and projects.

## 🌟 Features
* **AI Terminal Interface**: Type commands like `skills` or `projects`, or simply chat with the AI!
* **Groq API Integration**: Powered by Llama-3.3-70b-versatile for lightning-fast, intelligent responses.
* **Secure Backend proxy**: Uses a Flask backend to proxy chat requests safely without exposing API keys.
* **Cursor Reveal Engine**: Custom interactive mouse-tracking visual effects.

## 💻 Tech Stack
* **Frontend**: HTML5, CSS3, Vanilla JavaScript
* **Backend**: Python 3, Flask, flask-cors
* **AI Provider**: Groq API (Llama-3 models)

## 🚀 How to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Chris1946/about-me.git
   cd about-me
   ```

2. **Set up the virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure your API Key**:
   * Create a file named `.env` in the root directory.
   * Add your Groq API key:
     ```env
     GROQ_API_KEY="your_api_key_here"
     ```

4. **Start the Flask Backend**:
   ```bash
   python app.py
   ```

5. **Open the Frontend**:
   Simply open `index.html` in your web browser!

---
*Built by [Chris Jobi](https://github.com/Chris1946) — Computer Science & AI Engineering*
