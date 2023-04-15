# telegram_notificator


<div align="center">


**Send telegram notifications or alerts from your python programs.**


<div align="left">

## Installation
  
Install the library TelegramNotificator as follow:

```
pip install TelegramNotificator
```

Then simply use it like this:

```python
from telegram_notificator import TelegramNotificator as tn

telegram = tn(YOUR_TELEGRAM_BOT_TOKEN, YOUR_TELEGRAM_CHAT_ID)

telegram.SendMessage('Hello world!')
```

To get your `YOUR_TELEGRAM_BOT_TOKEN` and `YOUR_TELEGRAM_CHAT_ID` details just do a search about how to create a telegram bot using [BotFather](https://t.me/botfather).