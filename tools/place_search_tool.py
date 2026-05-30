import os
from utils.place_info_search import OSMPlaceSearchTool, TavilyPlaceSearchTool
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv

class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.osm_search = OSMPlaceSearchTool()
        self.tavily_search = TavilyPlaceSearchTool()
        self.tavily_enabled = bool(os.environ.get("TAVILY_API_KEY"))
        self.place_search_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup all tools for the place search tool"""
        @tool
        def search_attractions(place:str) -> str:
            """Search attractions of a place"""
            try:
                attraction_result = self.osm_search.osm_search_attractions(place)
                if attraction_result:
                    return f"Following are free OpenStreetMap-based attractions for {place}: {attraction_result}"
            except Exception as e:
                if self.tavily_enabled:
                    tavily_result = self.tavily_search.tavily_search_attractions(place)
                    return f"OSM search failed due to {e}. \nFollowing are attractions of {place} (Tavily fallback): {tavily_result}"
                return f"OSM search failed due to {e}. Please try another place name."
            return f"No attraction results found for {place}."
        
        @tool
        def search_restaurants(place:str) -> str:
            """Search restaurants of a place"""
            try:
                restaurants_result = self.osm_search.osm_search_restaurants(place)
                if restaurants_result:
                    return f"Following are free OpenStreetMap-based restaurants for {place}: {restaurants_result}"
            except Exception as e:
                if self.tavily_enabled:
                    tavily_result = self.tavily_search.tavily_search_restaurants(place)
                    return f"OSM search failed due to {e}. \nFollowing are restaurants of {place} (Tavily fallback): {tavily_result}"
                return f"OSM search failed due to {e}. Please try another place name."
            return f"No restaurant results found for {place}."
        
        @tool
        def search_activities(place:str) -> str:
            """Search activities of a place"""
            try:
                activities_result = self.osm_search.osm_search_activity(place)
                if activities_result:
                    return f"Following are free OpenStreetMap-based activities for {place}: {activities_result}"
            except Exception as e:
                if self.tavily_enabled:
                    tavily_result = self.tavily_search.tavily_search_activity(place)
                    return f"OSM search failed due to {e}. \nFollowing are activities of {place} (Tavily fallback): {tavily_result}"
                return f"OSM search failed due to {e}. Please try another place name."
            return f"No activity results found for {place}."
        
        @tool
        def search_transportation(place:str) -> str:
            """Search transportation of a place"""
            try:
                transportation_result = self.osm_search.osm_search_transportation(place)
                if transportation_result:
                    return f"Following are free OpenStreetMap-based transport options for {place}: {transportation_result}"
            except Exception as e:
                if self.tavily_enabled:
                    tavily_result = self.tavily_search.tavily_search_transportation(place)
                    return f"OSM search failed due to {e}. \nFollowing are transport options for {place} (Tavily fallback): {tavily_result}"
                return f"OSM search failed due to {e}. Please try another place name."
            return f"No transportation results found for {place}."
        
        return [search_attractions, search_restaurants, search_activities, search_transportation]