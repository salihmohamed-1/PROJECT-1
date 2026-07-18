"""
flow_state_logic.py

Calculates the productivity (flow state) of a developer.
"""


def calculate_flow_score(duration_minutes):
    """
    Calculate developer productivity level based on coding duration.
    """

    if duration_minutes < 0:
        return "Invalid"

    if duration_minutes >= 90:
        return "High"

    elif duration_minutes >= 45:
        return "Medium"

    return "Low"


if __name__ == "__main__":

    test_values = [-5, 20, 50, 95]

    for value in test_values:
        print(
            f"Duration: {value} minutes -> Flow Score: {calculate_flow_score(value)}"
        )