import os

from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter

app = Flask(__name__)

DEBUG = True
# DEBUG = current_app.config['DEBUG']
if DEBUG:
    from dotenv import load_dotenv
    load_dotenv()
    SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
    SLACK_EVENTS_TOKEN = os.environ.get("SLACK_EVENTS_TOKEN")
# else:
#     SLACK_BOT_TOKEN = current_app.config['SLACK_BOT_TOKEN']
#     SLACK_EVENTS_TOKEN = current_app.config['SLACK_EVENTS_TOKEN']
    
slack_client = WebClient(SLACK_BOT_TOKEN)
# slack_events_adapter = SlackEventAdapter(SLACK_EVENTS_TOKEN,'/slack/events',current_app)
slack_events_adapter = SlackEventAdapter(SLACK_EVENTS_TOKEN,'/slack/events',app)
    
def __connect_to_gdrive():
    pass


def __create_doc(updates):
    # Get date
    # Copy-paste gdoc from template
    # paste updates into gdoc
    pass

def slack_weekly_summary(payload):
    """Get weekly summary updates from developers in Slack
    
    Keyword arguments:
    Send text to developers asking for latest updates

    Return: JSON with updates
    """

    __send_request_for_summary()
    current_channel = '#tests' if DEBUG else '#webdev'
    event = payload.get('event', {})
    update_text = payload.get('text')
    
    # process update_text
    developer = 0
    functional = 0
    visual = 0
    internal = 0


    updates = {
        "developer": developer,
        "functional": functional,
        "visual": visual,
        "internal": internal,
    }

    return updates


def __send_request_for_summary():
    current_channel = '#tests' if DEBUG else '#webdev'
    bot_message = f"Weekly summary time! \
                    Add your changes and report when you finish please :+1: \
                    Please define if changes ar in category **functional** | **visual** | **internal**"
        
    block = __slack_message(bot_message)
    
    slack_client.chat_postMessage(
        channel=current_channel,
        blocks=block
        )

def __slack_message(message):
    block = [{
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": message,
        }
    }]
    return block

@slack_events_adapter.on('message')
def weekly_summary():
    updates = slack_weekly_summary()
    __create_doc(updates)
    

if __name__ == "__main__":
    app.run('0.0.0.0',port=8080)
