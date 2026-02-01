from app.rag.embeddings import fake_embedding
from app.rag.vector_store import VectorStore


# Initialize store once
vector_store = VectorStore(dimension=32)

# Seed with travel knowledge
vector_store.add(
    fake_embedding("Jaipur is known for forts, palaces, and budget travel."),
    "Jaipur is known for forts, palaces, and budget travel."
)

vector_store.add(
    fake_embedding("Goa is popular for beaches and nightlife."),
    "Goa is popular for beaches and nightlife."
)

vector_store.add(
    fake_embedding("Budget travelers prefer trains over flights."),
    "Budget travelers prefer trains over flights."
)


def retrieve_context(query: str) -> list[str]:
    query_embedding = fake_embedding(query)
    return vector_store.search(query_embedding)
