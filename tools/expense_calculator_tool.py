from utils.expense_calculator import Calculator
from typing import List, Optional
from langchain.tools import tool

class CalculatorTool:
    def __init__(self):
        self.calculator = Calculator()
        self.calculator_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup all tools for the calculator tool"""
        @tool
        def estimate_total_hotel_cost(price_per_night: float, total_days: float) -> float:
            """Calculate total hotel cost"""
            return self.calculator.multiply(price_per_night, total_days)
        
        @tool
        def calculate_total_expense(costs: Optional[List[float]] = None, extra_cost: Optional[float] = None) -> float:
            """Calculate total expense of the trip from a list of costs.

            Example input:
            - costs: [1200, 350, 80]
            - extra_cost: 50 (optional)
            """
            normalized_costs = costs or []
            if extra_cost is not None:
                normalized_costs.append(extra_cost)
            return self.calculator.calculate_total(*normalized_costs)
        
        @tool
        def calculate_daily_expense_budget(total_cost: float, days: int) -> float:
            """Calculate daily expense"""
            return self.calculator.calculate_daily_budget(total_cost, days)
        
        return [estimate_total_hotel_cost, calculate_total_expense, calculate_daily_expense_budget]