from message_media_messages.message_media_messages_client import MessageMediaMessagesClient
import json

auth_user_name = 'Hp0zfOrEImTd4sVP6KuX5oaSkDqMCwW92hFivctjnAxbNleYZR7f31yiZtXhELHOncSqprwBJRFIjd64'
auth_password = 'Fastsms@7'
use_hmac_authentication = False

client = MessageMediaMessagesClient(auth_user_name, auth_password, use_hmac_authentication)
messages_client = client.messages

body_value = {
    "messages":[
        {
            "content":"My first message",
            "destination_number":"+918688151347"
        }
    ]
}

body = json.loads(body_value)

result = messages_client.send_messages(body)

'''
Twilio SMS.
Nexmo SMS Messaging.
Telesign SMS Verify.
Nexmo Verify.
Nexmo Number Insight.
Inteltech SMS.
SMS Gateway.
ClickSend SMS.'''