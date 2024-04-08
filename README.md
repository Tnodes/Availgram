# Availgram
![image](https://github.com/Tnodes/Availgram/assets/83104623/7be8f551-f216-4a15-bac3-62268603cba6)

Automatically check the health of avail-light nodes send the health status to the telegram bot

# Install
```
apt install screen
git clone https://github.com/Tnodes/Availgram.git
pip install python-telegram-bot
```

# Configurations
Edit telegram bot token using [Botfather](https://t.me/BotFather) & your [chatid](https://t.me/userinfobot) at line 7 & 8 https://github.com/Tnodes/Availgram/blob/e75eadf3712783a344b8ee5ae6f022cbc543beb0/check.py#L7-L8
# Usage
Create a screen for the program to run in the background
```
screen -S avcheck
```
Then run
```
python check.py
```
`CRTL + AD : close screen`

To access the screen
```
screen -r avcheck
```

# Contribution
Contributions to the Availgram are welcome. Please ensure that your code adheres to the project's standards and submit a pull request for review.
