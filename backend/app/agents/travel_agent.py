from app.agents.base import BaseAgent
from app.rag.retriever import retrieve_context
from app.services.preference_service import get_user_preferences
from app.db.session import SessionLocal


class TravelAgent(BaseAgent):

    def run(self, user_id: int, query: str) -> str:
        db = SessionLocal()

        try:
            preferences = get_user_preferences(db, user_id)
            context_docs = retrieve_context(query)

            preference_text = ""
            if preferences:
                preference_text = (
                    f"User prefers {preferences.travel_style} travel, "
                    f"uses {preferences.transport_mode}, "
                    f"budget range is {preferences.budget_range}."
                )

            context_text = " ".join(context_docs)

            response = (
                f"{preference_text}\n"
                f"Relevant travel info: {context_text}\n"
                f"User query: {query}"
            )

            return response  #after replace with llm response

        finally:
            db.close()
