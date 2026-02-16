from langchain_ollama import ChatOllama

model = ChatOllama(
    model="llama3",
    temperature=0.3
)

response = model.invoke("who are you")
print(response)