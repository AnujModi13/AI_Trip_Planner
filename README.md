# ✈️ AI Trip Planner

An intelligent trip planning application powered by AI agents that helps you create personalized travel itineraries. This project leverages advanced language models, LangChain, LangGraph, and agentic workflows to deliver smart travel recommendations.

## 🌟 Features

- **AI-Powered Trip Planning**: Generate comprehensive travel itineraries based on your preferences
- **Multi-Provider Support**: Works with multiple LLM providers (Groq, OpenAI)
- **Dual Interface**: Access via FastAPI backend or Streamlit web interface
- **Agentic Workflow**: Implements ReAct (Reasoning + Acting) pattern using LangGraph
- **Web Search Integration**: Tavily integration for real-time travel information
- **Graceful Fallback**: Streamlit app can run independently without backend if needed
- **CORS Enabled**: RESTful API with cross-origin resource sharing support

## 📋 Prerequisites

- Python 3.10+ (as specified in `.python-version`)
- API Keys:
  - `GROQ_API_KEY` - For Groq LLM provider
  - `OPENAI_API_KEY` (optional) - For OpenAI integration
  - `TAVILY_API_KEY` - For web search capabilities

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AnujModi13/AI_Trip_Planner.git
cd AI_Trip_Planner
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Using pip:
```bash
pip install -r requirements.txt
```

Or using UV (faster package installer):
```bash
uv sync
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
OPENAI_API_KEY=your_openai_api_key_here  # Optional
```

## 📦 Dependencies

- **LangChain Stack**: `langchain`, `langchain-community`, `langchain-experimental`
- **LLM Providers**: `langchain_groq`, `langchain_openai`
- **Agentic Framework**: `langgraph`
- **Web Framework**: `fastapi`, `uvicorn`
- **Frontend**: `streamlit`
- **Utilities**: `python-dotenv`, `pydantic`, `httpx`, `requests`

## 🏃 Running the Application

### Option 1: Streamlit Web Interface (Recommended for Users)

```bash
streamlit run streamlit_app.py
```

The app will open at `http://localhost:8501`

**Features:**
- Clean, user-friendly interface
- Real-time response generation
- Automatic fallback to local processing if backend is unavailable

### Option 2: FastAPI Backend Only (for Developers/API Usage)

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

**Endpoints:**
- `POST /query` - Submit a travel planning query
  - Request body: `{"question": "your trip planning question"}`
  - Response: `{"answer": "detailed travel itinerary"}`

**Interactive API Documentation:**
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Option 3: Both Backend + Frontend

Terminal 1:
```bash
uvicorn main:app --reload
```

Terminal 2:
```bash
streamlit run streamlit_app.py
```

### Option 4: Direct Python Execution

```bash
python main.py
```

This will automatically detect if running via Streamlit and route accordingly.

## 📁 Project Structure

```
AI_Trip_Planner/
├── agent/                          # Core agentic workflow
│   └── agentic_workflow.py         # GraphBuilder and ReAct agent
├── tools/                          # Tool definitions for agents
├── prompt_library/                 # Prompt templates and engineering
├── utils/                          # Utility functions
│   └── save_to_document.py        # Document export functionality
├── config/                         # Configuration management
├── exception/                      # Custom exception classes
├── logger/                         # Logging utilities
├── main.py                        # FastAPI application
├── streamlit_app.py               # Streamlit web interface
├── setup.py                       # Package configuration
├── requirements.txt               # Python dependencies
├── pyproject.toml                 # Project metadata
└── README.md                      # This file
```

## 🔄 How It Works

### Agentic Workflow (ReAct Pattern)

1. **User Query**: Submit a travel planning request
2. **Agent Reasoning**: AI analyzes the query and plans approach
3. **Tool Usage**: Agent uses available tools to gather information
4. **Action**: Execute search, filter, or process information
5. **Observation**: Integrate results and refine plan
6. **Iteration**: Repeat steps 2-5 until comprehensive itinerary is ready
7. **Response**: Return structured travel plan to user

### Architecture

```
User Input
    ↓
Streamlit UI / FastAPI Endpoint
    ↓
GraphBuilder (LangGraph)
    ↓
ReAct Agent (Groq/OpenAI LLM)
    ↓
Tools (Web Search, etc.)
    ↓
Final Itinerary
    ↓
User Output
```

## 💡 Example Queries

- "Plan a 5-day trip to Paris in September"
- "Create a budget-friendly itinerary for Tokyo with 10 days"
- "Design a romantic weekend getaway to Barcelona"
- "Plan a family trip to New York City for spring break"
- "Create a backpacking route through Southeast Asia for 3 weeks"

## 🛠️ Configuration

### Model Provider

Change the LLM provider in `main.py` and `streamlit_app.py`:

```python
graph = GraphBuilder(model_provider="groq")  # or "openai"
```

### API Configuration

Edit `main.py` to customize:
- CORS settings (line 19-25)
- Model provider (line 33)
- Response handling (lines 44-50)

## 📝 Example API Request

```bash
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"question": "Plan a 3-day trip to Rome"}'
```

## 🐛 Troubleshooting

### Issue: `GROQ_API_KEY not found`
**Solution**: Ensure `.env` file exists with valid API key

### Issue: Backend unavailable error in Streamlit
**Solution**: The app will automatically run locally. Ensure `GROQ_API_KEY` is set

### Issue: ModuleNotFoundError
**Solution**: Reinstall dependencies:
```bash
pip install -r requirements.txt
```

### Issue: Port already in use
**Solution**: 
- For Streamlit: `streamlit run streamlit_app.py --server.port 8502`
- For FastAPI: `uvicorn main:app --port 8001`

## 🚀 Deployment

### Streamlit Cloud

1. Push repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Set environment variables in Settings
5. Deploy

### Docker

Create `Dockerfile`:
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "streamlit_app.py"]
```

Build and run:
```bash
docker build -t ai-trip-planner .
docker run -p 8501:8501 -e GROQ_API_KEY=your_key ai-trip-planner
```

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Anuj Modi**
- GitHub: [@AnujModi13](https://github.com/AnujModi13)
- Email: modianuj7613@gmail.com

## 🙏 Acknowledgments

- [LangChain](https://www.langchain.com/) - LLM framework
- [LangGraph](https://www.langchain.com/langgraph) - Agentic workflows
- [Streamlit](https://streamlit.io/) - Web interface
- [FastAPI](https://fastapi.tiangolo.com/) - API framework
- [Groq](https://groq.com/) - LLM provider
- [Tavily](https://tavily.com/) - Web search API

## 📞 Support

For issues, questions, or suggestions, please open an [issue](https://github.com/AnujModi13/AI_Trip_Planner/issues) on GitHub.

---

**Happy Traveling! 🌍✈️🏖️**
