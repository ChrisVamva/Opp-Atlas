import dspy

# Switch to Ollama Cloud - runs on their servers, not your laptop
lm = dspy.LM(
    model="ollama_chat/devstral-2:123b-cloud",
    api_base="http://localhost:11434",
    api_key="ollama"
)
dspy.configure(lm=lm)

qa = dspy.ChainOfThought("question -> answer")
result = qa(question="What is the capital of France?")

print("Answer:", result.answer)
dspy.inspect_history(n=1)