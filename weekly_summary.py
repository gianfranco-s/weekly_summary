import os

from dotenv import load_dotenv
from slack import WebClient



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


def connect_to_gdrive():
    pass

def create_doc():
    # Get date
    # Copy-paste 
    pass

def weekly_summary_to_slack():

    current_channel = '#tests'
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
    weekly_summary_to_slack()


if __name__ == "__main__":
    weekly_summary()