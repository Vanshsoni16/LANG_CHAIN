from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()
documents = ["Delhi is the capital of india", "Kolkata is the capital of west Bengal "]

model = OpenAIEmbeddings(model= "text-embeddings-3-large", dimensions= 32)
result  = model.embed_documents(documents)


print(str(result))
# model
