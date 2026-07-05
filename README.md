# 🔍 Multi Research Agent

An AI-powered Multi-Agent Research System built using **LangChain**, **Google Gemini**, **Tavily Search**, and **BeautifulSoup**. The system automates the research workflow by assigning specialized AI agents to different tasks such as searching, reading, writing, and critically evaluating information from the web.

---

## 🚀 Features

- 🔎 **Search Agent**
  - Searches the web for recent and reliable information using Tavily Search.

- 📖 **Reader Agent**
  - Reads and extracts the most relevant information from the collected search results.

- ✍️ **Writer Agent**
  - Generates a structured research report based on the extracted information.

- 🧠 **Critic Agent**
  - Reviews the generated report, identifies weaknesses, and provides suggestions for improvement.

- 🌐 **Web Search Integration**
  - Uses Tavily API for accurate and up-to-date web search.

- 📄 **Web Scraping**
  - Uses BeautifulSoup to scrape and process webpage content.

- 🔄 **Automated Research Pipeline**
  - Connects all agents into a sequential workflow from search to final report generation.

---

## 🛠️ Tech Stack

- Python
- LangChain
- Google Gemini API
- Tavily API
- BeautifulSoup (bs4)
- Requests
- Python Dotenv

---

## 📂 Project Structure

```
Multi_research_agent/
│
├── agents.py           # Multi-agent definitions
├── pipeline.py         # Research pipeline
├── tools.py            # Search & scraping tools
├── requirements.txt    # Project dependencies
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/DebasundarNayak/Multi_research_agent.git
```

Move into the project directory:

```bash
cd Multi_research_agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your API keys:

```env
TAVILY_API_KEY=your_tavily_api_key
GOOGLE_API_KEY=your_google_api_key
MODEL_NAME=gemini-2.5-flash
```

---

## ▶️ Usage

Run the research pipeline:

```bash
python pipeline.py
```

The system will:

1. Search the web
2. Read the collected information
3. Generate a research report
4. Critically evaluate the report
5. Produce the final output

---

## 🎯 Future Improvements

- Support parallel execution of agents
- Add memory for long-term context
- Generate reports in PDF and Markdown formats
- Add citation verification
- Build a Streamlit/React user interface
- Integrate LangGraph for advanced agent orchestration

---

## 👨‍💻 Author

**Debasundar Nayak**

GitHub: https://github.com/DebasundarNayak

---

## ⭐ If you found this project useful, consider giving it a Star on GitHub!