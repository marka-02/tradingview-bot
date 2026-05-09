from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("8063179662:AAFDhdokwc5Ql50rPInmvlQKR9v31xdWWu4")
CHAT_ID = os.environ.get("308957081")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if data and "message" in data:
        message = data["message"]
    else:
        message = "🚨 Алерт сработал!"
    
    requests.post(
        f"https://api.telegram.org/bot{8063179662:AAFDhdokwc5Ql50rPInmvlQKR9v31xdWWu4}/sendMessage",
        json={"chat_id": 308957081, "text": message}
    )
    return "OK", 200

@app.route("/")
def index():
    return "Bot is running!", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
