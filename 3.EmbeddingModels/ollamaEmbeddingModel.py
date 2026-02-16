from langchain_ollama import OllamaEmbeddings

embedding_model = OllamaEmbeddings(
    model="nomic-embed-text",
    dimensions = 32
)

single_line_text = "Delhi is the capital of india"

resp1 = embedding_model.embed_query(single_line_text) 
# embed_query: used to create embeding for single sentence


documents = [
    "Delhi is the capital of India",
    "Kalkaat is the capital of west bengal",
    "Raipur is teh capital of chhattisgarh"
]
resp2 = embedding_model.embed_decuments(documents)
# embed_ducuments: used to create embeddinhg for multiple doc
#       in outoput it will return array of embedings of each line
#       output = [[embeddings...]]



print(str(resp1))