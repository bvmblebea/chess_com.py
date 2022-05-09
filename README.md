# chess_com.py
Web-API for chess.com that created to get player data, game data, and clubs/tournaments information

## Example
```python3
import chess_com
chess_com = chess_com.ChessCom()
player_info = chess_com.get_player_info(username="")
print(f"-- Player info::: {player_info}")
```
