[![Static Badge](https://img.shields.io/badge/Telegram-Channel-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/HowToDo3XOfficial)

[![Static Badge](https://img.shields.io/badge/Telegram-Chat-yes?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/HowToDo3XOfficialChat)

[![Static Badge](https://img.shields.io/badge/Telegram-Bot%20Link-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/PAWSOG_bot/PAWS?startapp=RrbBYTPa)

# 🐾 AUTO FARM FOR PAWS 🐾

> [!WARNING]
> As a payment for this script I take a 20 - 30% of your referrals.

> [!WARNING]
> I am not responsible for your account. Please consider the potential risks before using this bot.


## MY OTHER BOTS

### 💩 [Wcoin](https://github.com/elphador/wcoin.git)
### 🎨 [Blum](https://github.com/HowToDo3X/blum.git)

## Recommendation before use

# 🔥🔥 PYTHON version must be 3.10 🔥🔥

> 🇷 🇺 README in russian available [here](README-RU.md)

## Features  
|                      Feature                       | Supported |
|:--------------------------------------------------:|:---------:|
|                   Multithreading                   |     ✅     |
|              Proxy binding to session              |     ✅     |
|           Support for pyrogram .session            |     ✅     |
| Auto-register your account with your referral code |     ✅     |
|                     Auto tasks                     |     ✅     |


## [Settings](https://github.com/HowToDo3X/PawsBot/blob/main/.env-example/)
|                     Settings                     |                                                         Description                                                          |
|:------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------:|
|              **API_ID / API_HASH**               |                           Platform data from which to run the Telegram session (default - android)                           |
|           **USE_RANDOM_DELAY_IN_RUN**            |                                                      Name saying itself                                                      |
|             **RANDOM_DELAY_IN_RUN**              |                                      Random seconds delay for ^^^ (default is [5, 30])                                       |
|            **SLEEP_TIME_IN_MINUTES**             |                                 Random minutes delay between cycles (default is [120, 180])                                  |
|                   **USE_REF**                    |                                 Register accounts with ur referral or not (default - False)                                  |
|                    **REF_ID**                    |                           Your referral argument (comes after app/startapp? in your referral link)                           |
|             **USE_PROXY_FROM_FILE**              |                         Whether to use a proxy from the `bot/config/proxies.txt` file (True / False)                         |
|              **ENABLE_AUTO_TASKS**               |                                               Enable auto tasks (True / False)                                               |
|        **UNSAFE_ENABLE_JOIN_TG_CHANNELS**        |                                [!!UNSAFE!!] Enable auto joining to tg channels (True / False)                                |
|               **DISABLE_IN_NIGHT**               |                                          Disable script in night (default - False)                                           |
|                  **NIGHT_TIME**                  |                                          Night time [from, to] (default - [23, 6])                                           |

## Quick Start 📚

To fast install libraries and run bot - open run.bat on Windows or run.sh on Linux

## Prerequisites
Before you begin, make sure you have the following installed:
- [Python](https://www.python.org/downloads/) **version 3.10**

## Obtaining API Keys
1. Go to my.telegram.org and log in using your phone number.
2. Select "API development tools" and fill out the form to register a new application.
3. Record the API_ID and API_HASH provided after registering your application in the .env file.

## Installation
You can download the [**repository**](https://github.com/HowToDo3X/PawsBot) by cloning it to your system and installing the necessary dependencies:
```shell
git clone https://github.com/HowToDo3X/PawsBot.git
cd paws
```

Then you can do automatic installation by typing:

Windows:
```shell
run.bat
```

Linux:
```shell
run.sh
```

# Linux manual installation
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env-example .env
nano .env  # Here you must specify your API_ID and API_HASH, the rest is taken by default
python3 main.py
```

You can also use arguments for quick start, for example:
```shell
~/paws >>> python3 main.py --action (1/2)
# Or
~/paws >>> python3 main.py -a (1/2)

# 1 - Run script 🐾
# 2 - Creates a session 🐶
```

# Windows manual installation
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env-example .env
# Here you must specify your API_ID and API_HASH, the rest is taken by default
python main.py
```

You can also use arguments for quick start, for example:
```shell
~/paws >>> python main.py --action (1/2)
# Or
~/paws >>> python main.py -a (1/2)

# 1 - Run script 🐾
# 2 - Creates a session 🐶
```
