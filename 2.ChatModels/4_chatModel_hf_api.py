# from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
# from dotenv import load_dotenv
# load_dotenv()


# llm = HuggingFaceEndpoint(
#     repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task = "text-generation",
# )  
    
# model = ChatHuggingFace(llm=llm)

# result = model.invoke("What is the capital of France?")
# print(result.content) # contenet will give us the output of the model



from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch API token
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Ensure the token is loaded correctly
if not hf_token:
    raise ValueError("Hugging Face API token is missing. Set it in a .env file or use 'setx' command.")

# Initialize the model with the token
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=hf_token,
    max_length=512,
    # max_tokens=20
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("hello how are you?")
print(result.content)


