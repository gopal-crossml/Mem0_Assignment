"""
Date Utility Tool
Calculates future dates.
"""

from datetime import datetime, timedelta

from langchain.tools import tool

#for fetching the date
@tool
def future_date(days: int) -> str:
    """
    Summary:
        Calculate a future date by adding a given number of days to today's date.

    Args:
        days (int): Number of days to add to the current date.

    Returns:
        str: The calculated future date in "YYYY-MM-DD" format,
        or an error message if the calculation fails.
    """
    try:
        target_date = datetime.today() + timedelta(days=days)
        return target_date.strftime("%Y-%m-%d")
    except Exception as e:
        return f"Error calculating date: {str(e)}"
