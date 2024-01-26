import requests
import sys

bot_token = "6485519390:AAFfNaoczrJ1iogn0b_8P62KZ6fCbuOs20E"
chat_id = "6833892136"

# Check if a message was passed as a command line argument
if len(sys.argv) > 1:
    message_text = sys.argv[1]
else:
    message_text = "Hello, this is a message from your Telegram bot!"

send_message_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
params = {"chat_id": chat_id, "text": message_text}

response = requests.get(send_message_url, params=params)

if response.status_code == 200:
    print("Message sent successfully!")
else:
    print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")