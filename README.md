# telegram_notificator


<div align="center">


**A tiny class to send telegram notifications or alerts from your python programs.**


<div align="left">

## Installation
  
You don't need to copy this repository into your project folder, use pip to install it instead into your [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

Once you have your virtual environment set up and activated you can install the packages thus:

```
$ pip install git+https://github.com/errais2000/telegram_notificator
```

Then, in your python script just import it and use it:

```python
import telegram_notificator
def notify = telegram_notificator(YOUR_TELEGRAM_BOT_TOKEN, YOUR_TELEGRAM_CHAT_ID)

notify.send_message('Hello world!')
```

To get your YOUR_TELEGRAM_BOT_TOKEN and YOUR_TELEGRAM_CHAT_ID details just do a search about how to create a telegram bot using [BotFather](https://t.me/botfather).