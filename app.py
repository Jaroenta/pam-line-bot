from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)

app = Flask(__name__)

line_bot_api = LineBotApi('y5rsb056kL8UVgzoW7Vz8wE8dtmNPKSkXNO01/yddVDpIhmoCI9Sn53L0KZf/JdmJwFwQ5iAnhnJTAgjE6jUxwtlKjbS5FNwG0BxxBUH7FCnKa5YqDzU0nZSXd42chGB1LSZ/pm8IzABHdcv2Mv/AAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('09476e50209f395bfa593c7bd53cdef0')


@app.route("/")
def hello():
    return 'chatbot sever!!!'

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
            TextSendMessage(text='สวัสดีค่า'))
        return 0
    if event.message.text == "หวัดดี":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='หวัดดีค่ะ'))
        return 0
    if event.message.text == "สบายดีมั้ย":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='สบายดีค่า'))
        return 0
    if event.message.text == "หิวอะ":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='หิวก็หาอะไรกินสิ'))
        return 0
    if event.message.text == "เหงา":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='เหงาก็คุยกับเราก่อน'))
        return 0
    if event.message.text == "ทำไรอยู่":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='คุยกะเธอไง'))
        return 0
    if event.message.text == "แชทบอทคืออะไร":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='แชทบอทก็คือ โปรแกรมที่ตอบกลับข้อความกลับอัตโนมัติยังไงหล่ะ'))
        return 0
    if event.message.text == 'ชื่ออะไร':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='ชื่อแพมค่ะ'))
        return 0
    


if __name__ == "__main__":
    app.run()