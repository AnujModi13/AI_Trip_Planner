import requests
from langchain_tavily import TavilySearch
from typing import List

class OSMPlaceSearchTool:
    """Free place search using OpenStreetMap Nominatim API (no paid key required)."""

    def __init__(self):
        self.base_url = "https://nominatim.openstreetmap.org/search"
        self.headers = {
            "User-Agent": "ai-trip-planner/0.1 (contact: local-app)",
            "Accept": "application/json",
        }

    def _search(self, query: str, limit: int = 8) -> str:
        params = {
            "q": query,
            "format": "jsonv2",
            "addressdetails": 1,
            "limit": limit,
        }
        response = requests.get(self.base_url, params=params, headers=self.headers, timeout=20)
        response.raise_for_status()
        results = response.json()

        if not results:
            return "No results found."

        formatted_results: List[str] = []
        for idx, item in enumerate(results, start=1):
            name = item.get("display_name", "Unknown place")
            lat = item.get("lat", "N/A")
            lon = item.get("lon", "N/A")
            formatted_results.append(f"{idx}. {name} (lat: {lat}, lon: {lon})")

        return "\n".join(formatted_results)

    def osm_search_attractions(self, place: str) -> str:
        return self._search(f"top tourist attractions in {place}")

    def osm_search_restaurants(self, place: str) -> str:
        return self._search(f"best restaurants in {place}")

    def osm_search_activity(self, place: str) -> str:
        return self._search(f"things to do activities in {place}")

    def osm_search_transportation(self, place: str) -> str:
        return self._search(f"public transport metro bus train in {place}")

class TavilyPlaceSearchTool:
    def __init__(self):
        pass

    def tavily_search_attractions(self, place: str) -> dict:
        """
        Searches for attractions in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"top attractive places in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_restaurants(self, place: str) -> dict:
        """
        Searches for available restaurants in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"what are the top 10 restaurants and eateries in and around {place}."})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_activity(self, place: str) -> dict:
        """
        Searches for popular activities in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"activities in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def tavily_search_transportation(self, place: str) -> dict:
        """
        Searches for available modes of transportation in the specified place using TavilySearch.
        """
        tavily_tool = TavilySearch(topic="general", include_answer="advanced")
        result = tavily_tool.invoke({"query": f"What are the different modes of transportations available in {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    