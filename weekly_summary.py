import os

from dotenv import load_dotenv
from slack import WebClient

load_dotenv()
TOKEN = os.environ.get("SLACK_BOT_TOKEN")
DEBUG = True

MESSAGE_BLOCK = {
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": "",
    }
}


def connect_to_gdrive():
    pass


def create_doc():
    # Get date
    # Copy-paste 
    pass

def slack_weekly_summary():
    """Get weekly summary updates from developers in Slack
    
    Keyword arguments:
    Send text to developers asking for latest updates

    Return: JSON with updates
    updates = {
        "dev": "devname",
        "functional": "...",
        "visual": "...",
        "internal": "...",
    }
    """
    
    if DEBUG:
        current_channel = '#tests'
    else:
        current_channel = '#webdev'

    message = f"Weekly summary time! \
            {gdocs_link} \
            Add your changes and report when you finish please :+1:"

    MESSAGE_BLOCK["text"]["text"] = message
    
    slack_client = WebClient(TOKEN)
    
    slack_client.chat_postMessage(
        channel=current_channel,
        blocks=[MESSAGE_BLOCK]
    )

def weekly_summary():
    create_doc()
    

if __name__ == "__main__":
    slack_weekly_summary()
