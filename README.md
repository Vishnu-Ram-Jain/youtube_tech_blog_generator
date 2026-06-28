# 🎥 YouTube Blog Generator using CrewAI

An AI-powered multi-agent application that transforms YouTube videos from a specific channel into well-structured, SEO-friendly blog articles using **CrewAI** and **Groq LLM**.

Instead of manually watching long videos and writing blogs, this application automates the complete workflow using specialized AI agents.

---

## 🚀 Features

* 🔍 Search videos from a specific YouTube channel
* 🎯 Find the most relevant video based on the user's topic
* 📝 Extract and analyze video transcript
* 🤖 Multi-Agent workflow using CrewAI
* ✍️ Generate detailed, human-readable blog articles
* ⚡ Powered by Groq LLM for ultra-fast inference
* 📄 Save generated blog automatically as a Markdown file

---

## 🏗️ Architecture

```
                    User Input
          (Topic + YouTube Channel)
                      │
                      ▼
          ┌────────────────────────┐
          │   Research Agent       │
          │------------------------│
          │ • Search YouTube       │
          │ • Find Best Video      │
          │ • Read Transcript      │
          │ • Extract Insights     │
          └──────────┬─────────────┘
                     │
                     ▼
          ┌────────────────────────┐
          │   Blog Writer Agent    │
          │------------------------│
          │ • Organize Research    │
          │ • Generate Blog        │
          │ • Improve Readability  │
          │ • Format Markdown      │
          └──────────┬─────────────┘
                     │
                     ▼
             output/blog.md
```

---

## 🧠 Agents

### 🔎 Research Agent

Responsible for:

* Searching the requested YouTube channel
* Identifying the most relevant video
* Reading and analyzing transcript
* Collecting key insights

---

### ✍️ Blog Writer Agent

Responsible for:

* Understanding research results
* Writing a structured blog
* Improving readability
* Formatting the final output in Markdown

---

## 📋 Tasks

### Task 1

Research the requested topic from the specified YouTube channel.

### Task 2

Generate a complete SEO-friendly blog article from the collected research.

---

## 🛠️ Tech Stack

### AI Framework

* CrewAI

### LLM

* Groq

### Language

* Python 3.11+

### APIs

* YouTube Data API
* YouTube Transcript API

### Libraries

* crewai
* crewai-tools
* langchain
* langchain-groq
* python-dotenv
* pydantic

---

## 📁 Project Structure

```text
youtube-blog-agent/
│
├── models/
│
├── output/
│   └── blog.md
│
├── tools/
│   ├── transcript.py
│   └── youtube_search.py
│
├── utils/
│
├── agents.py
├── tasks.py
├── crew.py
├── app.py
├── config.py
│
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/youtube-blog-agent.git
```

Move into the project directory

```bash
cd youtube-blog-agent
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
YOUTUBE_API_KEY=your_youtube_api_key
```

---

## ▶️ Run the Application

```bash
python app.py
```

Enter:

```
Topic:
YouTube Channel:
```

The generated blog will be saved inside:

```
output/blog.md
```

---

## 📌 Example Workflow

```
User Input
     │
     ▼
Topic:
"Agentic AI"

Channel:
"IBM Technology"

     │
     ▼

Research Agent
     │
     ▼

Transcript Analysis
     │
     ▼

Blog Writer Agent
     │
     ▼

SEO-Friendly Blog Generated
```

---

## 📦 Output

The generated blog includes:

* Engaging title
* Introduction
* Main concepts
* Detailed explanation
* Key takeaways
* Conclusion
* Proper Markdown formatting

---

## 💡 Why CrewAI?

CrewAI makes it easy to build AI systems using specialized agents that collaborate on a shared goal. Each agent has a well-defined role, enabling cleaner workflows, better maintainability, and easier scalability compared to putting all logic into a single prompt.

For this project:

* One agent focuses entirely on research.
* Another agent specializes in writing.
* Tasks are modular and reusable.
* The workflow can easily be extended with additional agents for SEO optimization, fact-checking, or publishing.

---

## 🔮 Future Improvements

* Support multiple YouTube channels
* Add RAG with vector database
* Generate blog images using AI
* Export to PDF and DOCX
* Publish directly to Medium or WordPress
* SEO scoring
* Citation and reference generation
* Multi-language blog generation

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Vishnu Jain**

If you found this project useful, consider giving it a ⭐ on GitHub!
