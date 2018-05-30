from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

app = Flask(__name__)

line_bot_api = LineBotApi('y5rsb056kL8UVgzoW7Vz8wE8dtmNPKSkXNO01/yddVDpIhmoCI9Sn53L0KZf/JdmJwFwQ5iAnhnJTAgjE6jUxwtlKjbS5FNwG0BxxBUH7FCnKa5YqDzU0nZSXd42chGB1LSZ/pm8IzABHdcv2Mv/AAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHanndler('09476e50209f395bfa593c7bd53cdef0')
 

@app.route("/")
def hello():
    return "this is chatbot sever!"

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
    

@handler.add(MessageEvent,message=TextMessage)
def handle_message(event)
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=evet.message.text))
 

if __name__ == '__main__':
    app.run(debug = True)
