class GameEntry:
    """Represents one entry of a list of high scores"""

    def __init__(self, name: str, score: int):
        self._name = name
        self._score = score
    
    def __repr__(self):
        return f"GameEntry({self._name}, {self._score})"

    def __str__(self):
        return f"({self._name}, {self._score})"
    
    def get_name(self):
        """Return name of the person earning the score"""
        return self._name

    def get_score(self):
        """Return the score"""
        return self._score


class ScoreBoard:
    """Fixed-length sequence of high scores in nondescending order."""

    def __init__(self, capacity: int =0):
        """Initialized scoreboard with given maximum capacity

        All entries are initiall None
        """
        self._board: list[GameEntry] = [None] * capacity
        self._n: int = 0

    def __getitem__(self, k: int):
        """Return entry at index k"""
        return self._board[k]
    
    def __str__(self):
        """Return string representation of the high score list"""

    def add(self, entry: GameEntry):
        """Consider adding entry to high scores"""
        score = entry.get_score()

        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1
            
            j = self._n - 1

            while j > 0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry