import requests

class TelegramNotificator0:
  def __init__(self, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID):
    self.TELEGRAM_BOT_TOKEN = TELEGRAM_BOT_TOKEN
    self.TELEGRAM_CHAT_ID = TELEGRAM_CHAT_ID

  def SendMessage(self, message):
    data = {
              'chat_id': self.TELEGRAM_CHAT_ID,
              'text': message,
              'parse_mode': 'HTML'
          }
    return requests.post("https://api.telegram.org/bot{token}/sendMessage".format(token=self.TELEGRAM_BOT_TOKEN), data=data).content
  
