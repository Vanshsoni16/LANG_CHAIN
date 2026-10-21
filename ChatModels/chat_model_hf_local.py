from langchain_huggingface import ChatHuggingFace,  HuggingFacePipeline

from dotenv import load_dotenv




llm  = HuggingFacePipeline(repo_id = "TinyLlma/TinyLlma-1.1B-Chat-v1.0" , 
                    task = "text-generation",
                     pipeline_kwargs=dict(temperature= 0.5,
                                          max_new_token= 100) )
model = ChatHuggingFace(llm= llm)


result  = model.invoke("what is the capital of india ")
print(result.content)


