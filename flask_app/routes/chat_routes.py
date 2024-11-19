# from flask import Blueprint, render_template, request, Response
# import ollama
# from nemoguardrails import LLMRails, RailsConfig

# # Blueprint setup
# chat_bp = Blueprint('chat', __name__)

# # Load Nemoguardrails configuration
# config = RailsConfig.from_path("/home/offsec/llm/launchathon/team15/config")  # Update with the actual config path
# rails = LLMRails(config)

# # Home route
# @chat_bp.route('/')
# def index():
#     return render_template('index.html')

# # Chat route
# @chat_bp.route('/chat', methods=['POST'])
# def chat():
#     user_message = request.form.get("message")

#     # Process the message through Guardrails
#     guarded_response = rails.generate(messages=[{"role": "user", "content": user_message}])

#     # Convert the Guardrails response to a format Ollama expects
#     ollama_messages = [{"role": "user", "content": user_message}]

#     # Stream the response from Ollama
#     def generate_stream():
#         stream = ollama.chat(
#             model="llama3.1",
#             messages=ollama_messages,
#             stream=True,
#         )
#         for chunk in stream:
#             if "message" in chunk and "content" in chunk["message"]:
#                 yield chunk["message"]["content"]

#     return Response(generate_stream(), content_type="text/plain")

from flask import Blueprint, render_template, request, Response, redirect, url_for
import ollama
from nemoguardrails import LLMRails, RailsConfig

# Blueprint setup
chat_bp = Blueprint('chat', __name__)

# Load Nemoguardrails configuration
config = RailsConfig.from_path("/home/offsec/llm/launchathon/team15/config")  # Update with the actual config path
rails = LLMRails(config)

# Home route
@chat_bp.route('/')
def index():
    return render_template('chat.html')

@chat_bp.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'GET':
        return redirect(url_for('chat.index'))  # Redirect GET requests to the homepage

    user_message = request.form.get("message")

    # Process the message through Guardrails
    guarded_response = rails.generate(messages=[{"role": "user", "content": user_message}])

    # Convert the Guardrails response to a format Ollama expects
    ollama_messages = [{"role": "user", "content": user_message}]

    # Stream the response from Ollama and combine it into a single response
    response_text = ""
    stream = ollama.chat(
        model="llama3.1",
        messages=ollama_messages,
        stream=True,
    )
    for chunk in stream:
        if "message" in chunk and "content" in chunk["message"]:
            response_text += chunk["message"]["content"]

    return {"response": response_text}, 200  # Return the full response as JSON


    # return Response(generate_stream(), content_type="text/plain")
