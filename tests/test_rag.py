from src.rag.rag_pipeline import rag_answer

print("=" * 60)
print("Testing Complete RAG Pipeline")
print("=" * 60)

question = "Should I invest in Alphabet?"

print(f"\nQuestion: {question}\n")

answer = rag_answer(question)

print("=" * 60)
print("AI Answer")
print("=" * 60)

print(answer)