from requests import get


class ChessCom:
    def __init__(self):
        self.api = "https://api.chess.com"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
        }

    def get_player_info(self, username: str):
        return get(
            f"{self.api}/pub/player/{username}",
            headers=self.headers).json()

    def get_titled_players(self, title_abbrev: str):
        return get(
            f"{self.api}/pub/titled/{title_abbrev}",
            headers=self.headers).json()

    def get_player_stats(self, username: str):
    	return get(
      	  f"{self.api}/pub/player/{username}/stats",
    	    headers=self.headers).json()

    def check_player_status(self, username: str):
        return get(
            f"{self.api}/pub/player/{username}/is-online",
            headers=self.headers).json()

    def get_player_current_games(self, username: str):
        return get(
            f"{self.api}/pub/player/{username}/games",
            headers=self.headers).json()

    def get_player_turns(self, username: str):
        return get(
            f"{self.api}/pub/player/{username}/games/to-move",
            headers=self.headers).json()

    def get_player_monthly_archives(self, username: str):
        return get(
            f"{self.api}/pub/player/{username}/games/archives",
            headers=self.headers).json()

    def get_player_old_games(self, username: str, year: int, month: int):
        return get(
            f"{self.api}/pub/player/{username}/games/{year}/{month}",
            headers=self.headers).json()

    def get_player_clubs(self, username: str):
        return get(
            f"{self.api}/pub/player/{username}/clubs",
            headers=self.headers).json()

    def get_player_matches(self, username: str):
        return get(
            f"{self.api}/pub/player/{username}/matches",
            headers=self.headers).json()

    def get_player_tournaments(self, username: str):
        return get(
            f"{self.api}/pub/player/{username}/tournamens",
            headers=self.headers).json()

    def get_club_info(self, url_id: str):
        return get(
            f"{self.api}/pub/club/{url_id}",
            headers=self.headers).json()

    def get_club_members(self, url_id: str):
        return get(
            f"{self.api}/pub/club/{url_id}/members",
            headers=self.headers).json()

    def get_club_matches(self, url_id: str):
        return get(
            f"{self.api}/pub/club/{url_id}/matches",
            headers=self.headers).json()

    def get_tournament_info(self, url_id: str):
        return get(
            f"{self.api}/pub/tournament/{url_id}",
            headers=self.headers).json()

    def get_tournament_round(self, url_id: str, round: int = 1):
        return get(
            f"{self.api}/pub/tournament/{url_id}/{round}",
            headers=self.headers).json()

    def get_tournament_round_group(
            self,
            url_id: str,
            round: int = 1,
            group: int = 1):
        return get(
            f"{self.api}/pub/tournament/{url_id}/{round}/{group}",
            headers=self.headers).json()

    def get_daily_team_matches(self, id: int):
        return get(f"{self.api}/pub/match/{id}", headers=self.headers).json()

    def get_daily_team_match_board(self, id: int, board: int = 1):
        return get(
            f"{self.api}/pub/match/{id}/{board}",
            headers=self.headers).json()

    def get_live_team_matches(self, id: int):
        return get(
            f"{self.api}/pub/match/live/{id}",
            headers=self.headers).json()

    def get_live_team_match_board(self, id: int, board: int = 1):
        return get(
            f"{self.api}/pub/match/live/{id}/{board}",
            headers=self.headers).json()

    def get_country_info(self, iso: str):
        return get(
            f"{self.api}/pub/country/{iso}",
            headers=self.headers).json()

    def geT_country_players(self, iso: str):
        return get(
            f"{self.api}/pub/country/{iso}/players",
            headers=self.headers).json()

    def get_country_clubs(self, iso: str):
        return get(
            f"{self.api}/pub/country/{iso}/clubs",
            headers=self.headers).json()

    def get_daily_puzzle(self):
        return get(f"{self.api}/pub/puzzle", headers=self.headers).json()

    def get_random_daily_puzzle(self):
        return get(
            f"{self.api}/pub/puzzle/random",
            headers=self.headers).json()

    def get_streamers_info(self):
        return get(f"{self.api}/pub/streamers", headers=self.headers).json()

    def get_leaderboards(self):
        return get(f"{self.api}/pub/leaderboards", headers=self.headers).json()
