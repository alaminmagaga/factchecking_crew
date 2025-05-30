
# src/factchecking_crew/main.py

import os
from factchecking_crew.crew import FactcheckingCrew

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

def run():
    """
    Run the factchecking crew.
    """
    inputs = {
        'user_input': 'Barack Obama was born in Kenya.'
    }

    # Create and run the crew
    result = FactcheckingCrew().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== FACT-CHECK RESULT ===\n\n")
    print(result.raw)

if __name__ == "__main__":
    run()
