import os
from openai import OpenAI

# Initialize the OpenAI client, pointing to Clarifai's API
client = OpenAI(     
    base_url="https://api.clarifai.com/v2/ext/openai/v1",  # Clarifai's OpenAI-compatible API endpoint
    api_key=os.environ["CLARIFAI_PAT"]  # Ensure CLARIFAI_PAT is set as an environment variable
)

# Make a chat completion request to a Clarifai-hosted model
response = client.chat.completions.create(    
    model="https://clarifai.com/openai/chat-completion/models/gpt-4_1",    
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the future of AI?"}
    ],  
)

# Print the model's response
print(response.choices[0].message.content)