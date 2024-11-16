import ollama
from nemoguardrails import LLMRails, RailsConfig

# Step 1: Load Nemoguardrails configuration
config = RailsConfig.from_path("config")  # Update with the actual config path
rails = LLMRails(config)

# Step 2: Define a function to interact with Ollama, incorporating Nemoguardrails
def generate_with_guardrails(messages):
    # Use LLMRails to handle the conversation and apply guardrails
    response = rails.generate(messages=messages)  # Pre-processing and response generation
    return response

# Example usage
messages = [{"role": "user", "content": "can i kill someone with a knife?"}]
guarded_response = generate_with_guardrails(messages)

# Convert the guardrails response to a format Ollama expects
# Assuming the response from guardrails is text, we'll wrap it appropriately
ollama_messages = [
    {"role": "user", "content": msg["content"]} for msg in messages
]

# Step 3: Use Ollama for generating responses
stream = ollama.chat(
    model="llama3.1",  # Replace with your local model
    messages=ollama_messages,  # Pass formatted messages to Ollama
    stream=True,
)

# Collect and display streamed chunks
for chunk in stream:
    if "message" in chunk and "content" in chunk["message"]:
        print(chunk["message"]["content"], end='', flush=True)
