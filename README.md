# telegram_notificator


<div align="center">


**A tiny class to send telegram notifications or alerts from your python programs.**


<div align="left">

## Installation
  
Install the libriry requests as follow:

```
pip install requests
```

Then copy the telegram_notificator file to your project folder and us it as the following example:

```python
from telegram_notificator import telegram_notificator as tn

def telegram = tn(YOUR_TELEGRAM_BOT_TOKEN, YOUR_TELEGRAM_CHAT_ID)

telegram.send_message('Hello world!')
```

To get your `YOUR_TELEGRAM_BOT_TOKEN` and `YOUR_TELEGRAM_CHAT_ID` details just do a search about how to create a telegram bot using [BotFather](https://t.me/botfather).