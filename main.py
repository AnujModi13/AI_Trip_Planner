from fastapi import FastAPI
from pydantic import BaseModel
from agent.agentic_workflow import GraphBuilder
import os


app =FastAPI()

class QueryRequest(BaseModel):
    query: str
    
@app.post("/query")
async def query_travel_agent(query:QueryRequest):
    try:
        print(query)
        graph = GraphBuilder(model_provider="groq")
        react_app = graph()

        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("my_graph.png", "wb") as f:
            f.write(png_graph)

        print(f"Graph saved as 'my_graph.png' in {os.getcwd()}")

        # Assuming the request is a pydantic object like : {"question" : "What is your text"}
        messages = {"message": [query.question]}
        output = react_app.invoke(messages)

        if isinstance(output, dict) and "message" in output:
            final_output = output["message"][-1].content
        else:
            final_output = str(output)

        return {"answer": final_output}
    except Exception as e:
        print(f"Error processing query: {e}")