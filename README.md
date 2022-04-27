# MemoBot
***A simple telegram bot, that can send mems to users.***

At the request of the user, the bot sends a random meme from folder [memchiki](https://github.com/shlom41k/MemoBot/tree/main/src/files).<br>
Statistics on the number of requests is stored [Statistic.json](https://github.com/shlom41k/MemoBot/tree/main/src/files).
<hr>

## Bot Commands
- ```/start``` - start chat;
- ```/test``` - check connection;
- ```/getmem``` - get mem;

## Main tools:
```
- Python 3.10.2
- PyTelegramBotAPI 4.2.2
- JSON
```

## Projects setup
Insert your bot token into ```shlom41k_bot_token = ""``` field in [TeleBot.py](https://github.com/shlom41k/MemoBot/tree/main/src/files) file (line 15).

### Running application:
- ```pip install -r requirements.txt```
- ```python .\TeleBot.py ```
<hr>

## Some screenshots:
<p align="center">
  <img src="https://github.com/shlom41k/MemoBot/blob/main/src/img/start.jpg" width="30%">
  <img src="https://github.com/shlom41k/MemoBot/blob/main/src/img/test.jpg" width="30%">
  <img src="https://github.com/shlom41k/MemoBot/blob/main/src/img/getmem_1.jpg" width="30%">
  <img src="https://github.com/shlom41k/MemoBot/blob/main/src/img/getmem_2.jpg" width="30%">
  <img src="https://github.com/shlom41k/MemoBot/blob/main/src/img/getmem_3.jpg" width="30%">
</p>
