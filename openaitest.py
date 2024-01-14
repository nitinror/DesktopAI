import os
import openai
from config import apikey  # Make sure apikey is correctly imported from your config module

# Set your OpenAI API key
openai.api_key = apikey

# Request completion from OpenAI
response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Write an email to my boss for resignation?",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# Print the response from OpenAI
print(response)

# The 'response' variable now contains the generated text, which you can access using response['choices'][0]['text']
