class User:
    """Create an instance of user with initial progress and rank"""
    def __init__(self):
        self.rank = -8
        self.progress = 0 
    
    def inc_progress(self, activity_rank):
        """Change users's progress """
        if activity_rank < -8 or activity_rank > 8 or activity_rank == 0:
            raise ValueError("Rank out of range")     
        if self.rank >= 8:
            self.progress = 0
            self.rank = 8
        else:
            # Finding the score
            rank_difference = activity_rank - self.rank

            if activity_rank > 0 and self.rank < 0:
                rank_difference -= 1
            
            if self.rank == -1 and activity_rank == 1:
                self.progress += 10
            elif self.rank == 1 and activity_rank == -1:
                self.progress += 1
            elif rank_difference == 0:
                self.progress += 3
            elif rank_difference < 0 and abs(rank_difference) == 1:
                self.progress += 1
            elif rank_difference < 0 and abs(rank_difference) >= 2:
                self.progress += 0
            elif rank_difference >= 1:
                score = self._find_score(rank_difference)
                self.progress += score

            # Checking the progress
            number_of_ranks = self.progress // 100

            if number_of_ranks >= 1:
                self.progress = self.progress % 100
                if self.rank == -1 and activity_rank == 1:
                    self.rank = 1
                else:
                    if self.rank < 0 and  (self.rank + number_of_ranks) >= 0:
                        self.rank += number_of_ranks + 1
                    else: 
                        self.rank += number_of_ranks

                    if self.rank == 0:
                        self.rank = 1
                    elif self.rank >= 8:
                        self.rank = 8
                        self.progress = 0
                
    def _find_score(self, diff):
        return 10 * (diff ** 2)
