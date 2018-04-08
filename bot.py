from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)
import re , requests
app = Flask(__name__)

line_bot_api = LineBotApi('9BZgJt/LJFh0pLe6BZGc1q8W5+d/IwKQhaBSEt47PWbXsgos0qfoBxKNoTcDdgrJJwFwQ5iAnhnJTAgjE6jUxwtlKjbS5FNwG0BxxBUH7FD7LGHk/GPar0G0xn+CfBI6C9d9W7U2kSUOnGe7cLiBSAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9f58df9e6ed86b1dd69732c05b92831c')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/webhook", methods=['POST'])
def webhook():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


        
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    if event.message.text == 'สวัสดี':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='สวัสดีจ้าา'))
        return 0
    if event.message.text == "สบายดีมั้ย":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='สบายดดีจ้า'))
        return 0
    if event.message.text == "ทำไร":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='คุยกะเธอไง'))
        return 0
  

if __name__ == "__main__":
    app.run()
    
