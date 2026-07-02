print("Step 1")

from src.rag.llm import generate_answer

print("Step 2")

answer = generate_answer(
    question="What is artificial intelligence?",
    context="Artificial intelligence enables computers to perform tasks that usually require human intelligence."
)

print("Step 3")
print(answer)