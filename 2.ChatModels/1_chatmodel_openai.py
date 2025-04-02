from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model= 'gpt-4' , temperature=0.9)

result = model.invoke("What is the capital of France?")

#if we use only result then it give token count and other information
print(result.content) # contenet will give us the output of the model
