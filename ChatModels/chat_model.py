from langchain_openai  import ChatOpenAI
from dotenv  import load_dotenv

load_dotenv()

model = ChatOpenAI(model= "gpt-4"  ,max_completion_tokens=200)   # temperature -- 0 to 2 
result = model.invoke("what is the capital of india")
print(result.content)
