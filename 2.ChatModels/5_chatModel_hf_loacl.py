from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ['HF_HOME'] = 'D:/HuggingFace_cache'  # Set the cache directory for Hugging Face models

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    model_kwargs={"temperature": 0.9, "max_length": 512},
    pipeline_kwargs={"max_length": 512}
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("what is the captial of france?")
print(result.content)  # Print the model's response