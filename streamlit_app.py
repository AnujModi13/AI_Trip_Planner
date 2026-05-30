import streamlit as st
import requests
from agent.agentic_workflow import GraphBuilder

BASE_URL = "http://localhost:8000"


def _generate_local_answer(user_input: str) -> str:
    """Fallback path: run the graph directly when FastAPI backend is unavailable."""
    graph = GraphBuilder(model_provider="groq")
    react_app = graph()
    output = react_app.invoke({"messages": [user_input]})

    if isinstance(output, dict) and "messages" in output and output["messages"]:
        return output["messages"][-1].content
    return str(output)

st.set_page_config(
    page_title="AI Trip Planner",
    page_icon="✈️",
    layout="centered",
    initial_sidebar_state="auto",
)

st.title("AI Trip Planner")

# Initilize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.header("Plan Your Perfect Journey with AI")

with st.form(key="query_form", clear_on_submit=True):
    user_input = st.text_input("User Input", placeholder="Ask me to plan your trip! e.g., 'Plan a 5-day trip to Paris in September.'")
    submit_button = st.form_submit_button(label="Submit")


if submit_button and user_input.strip():
    try:
        with st.spinner("Generating response..."):
            payload = {"question": user_input}
            response = requests.post(f"{BASE_URL}/query", json=payload, timeout=60)

        if response.status_code == 200:
            result = response.json().get("answer", "No answer found.")
            markdown_content = f"""**AI Trip Planner!**

            ````
            {result}
            ````
            """
            st.markdown(markdown_content,)
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException:
        with st.spinner("Backend unavailable. Running planner locally..."):
            try:
                result = _generate_local_answer(user_input)
                markdown_content = f"""**AI Trip Planner!**

                ````
                {result}
                ````
                """
                st.markdown(markdown_content,)
            except Exception as fallback_error:
                st.error(
                    "Could not generate a local answer. "
                    "Set GROQ_API_KEY (or run FastAPI backend at http://localhost:8000/query) "
                    "and try again."
                )
                st.caption(f"Details: {fallback_error}")
    except Exception as e:
        st.error(f"An error occurred: {e}")