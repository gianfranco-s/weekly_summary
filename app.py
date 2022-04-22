import os

from dotenv import load_dotenv
from flask import Flask
from slack import WebClient


app = Flask(__name__)

load_dotenv()
TOKEN = os.environ.get("SLACK_BOT_TOKEN")

gdocs_link = 'https://docs.google.com/document/d/1VJUXKDc1WfmXYjRYZLHIFU_ZlCkQHdgzN7h6TFXF93o/edit?usp=sharing'

MESSAGE_BLOCK = {
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": "",
    }
}

@app.route('/')
def weekly_summary_to_slack():
    # Create document in google docs
    # Send message to #webdev

    current_channel = '#tests'
    message = f"Weekly summary time! \
            {gdocs_link} \
            Add your changes and report when you finish please :+1:"

    MESSAGE_BLOCK["text"]["text"] = message
    MESSAGE_BLOCK["text"]["text"] = 'hola'
    
    print("="*80)
    print(MESSAGE_BLOCK)
    print("="*80)    

    slack_client = WebClient(TOKEN)

    slack_client.chat_postMessage(
        channel=current_channel,
        blocks=MESSAGE_BLOCK
    )

    print("="*80)
    print("Enviado!")
    print("="*80)

    return "Hola!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)