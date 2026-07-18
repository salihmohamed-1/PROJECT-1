import sys
import os

# Add the cognistream folder to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..")
    )
)

from processing.polars_pipeline.flow_state_logic import calculate_flow_score


def test_flow_state_logic():

    assert calculate_flow_score(20) == "Low"
    assert calculate_flow_score(50) == "Medium"
    assert calculate_flow_score(95) == "High"

    print("✅ Flow State Logic Test Passed!")


if __name__ == "__main__":
    test_flow_state_logic()