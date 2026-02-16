from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-previewo")

res = model.invoke("what is 2*4")

print(res.content)