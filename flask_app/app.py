from flask import Flask
from routes.chat_routes import chat_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(chat_bp)

if __name__ == '__main__':
    app.run(debug=True)
