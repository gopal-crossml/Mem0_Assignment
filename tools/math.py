from langchain.tools import tool

@tool
def math_calculator(expression: str) -> str:
    """
    Summary:
        This function takes a string containing a valid Python
        arithmetic expression and evaluates it to produce a result.
  

    Args:
        expression (str): A mathematical expression to evaluate.
        Example: "(234 * 12) + 98"

    Returns:
        str: A string containing either:
           - The calculated result in the format "Result: <value>", or
           - An error message in the format "Error evaluating expression: <error>"

    Evaluates a simple mathematical expression.

    Input:
        expression (str): Example -> "(234 * 12) + 98"

    Output:
        str: Result of calculation
    """
    try:
        # Evaluate the expression
        result = eval(expression)

        return f"Result: {result}"

    except Exception as error:
        return f"Error evaluating expression: {error}"


