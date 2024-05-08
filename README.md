# lichess-bot

Built using the [Lichess Bot API](https://lichess.org/api#tag/Bot).


## Running locally 
```
source ./venv/bin/activate
python3 -m pip install -r requirements.txt
python3 lichess-bot.py
```

## Testing
```
python3 -m unittest discover engines/minimax_bot/test
```

## License
lichess-bot is licensed under the AGPLv3 (or any later version at your option). Check out the [LICENSE file](https://github.com/lichess-bot-devs/lichess-bot/blob/master/LICENSE) for the full text.
