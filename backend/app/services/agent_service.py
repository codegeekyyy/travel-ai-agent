from app.agents.travel_agent import TravelAgent


def run_travel_agent(user_id: int, query: str) -> str:
    agent = TravelAgent()
    return agent.run(user_id=user_id, query=query)
