class Election:
    def __init__(self, voters = False):
        self.ballots = []
        self.voters = voters
        
    def ballot(self, list, voter = False):
        self.ballots += [Ballot(list)]
        if self.voters:
            if not(voter) or voter in self.voters:
                return False
            else:
                self.voters += [voter]
        return True
        
    def runElection(self,number):
        scoreboard = {candidate:0 for ballot in self.ballots for candidate in ballot.list}
        for ballot in self.ballots:
            ballot.power = 1
            scoreboard[ballot.current()] += 1
        winners = []
        winnersLeft = number
        
        #this threshhold works in python3 but perhaps not python2, from integer division
        threshhold = len(self.ballots) / (1 + number)
        
        while len(scoreboard) > winnersLeft:
            print(scoreboard)
            roundWinners = [candidate for (candidate, votes) in scoreboard.items() if votes > threshhold]
            
            if roundWinners:
                winners += roundWinners
                winnersLeft -= len(roundWinners)
            
                for ballot in self.ballots:
                    if ballot.current() in roundWinners:
                        ballot.power *= (scoreboard[ballot.current()] - threshhold) / scoreboard[ballot.current()]
                        ballot.next()
                        if ballot.current() in scoreboard:
                            scoreboard[ballot.current()] += ballot.power
                    
                for winner in roundWinners:
                    del scoreboard[winner]
            else:
                lowestScore = min(scoreboard.values())
                roundLosers = [candidate for (candidate, votes) in scoreboard.items() if votes == lowestScore]
                
                for ballot in self.ballots:
                    if ballot.current() in roundLosers:
                        ballot.next()
                        if ballot.current() in scoreboard:
                            scoreboard[ballot.current()] += ballot.power
                    
                for loser in roundLosers:
                    del scoreboard[loser]
        winners += scoreboard.keys()
        winnersLeft -= len(scoreboard.keys())
        
        return winners
        
class Ballot:
    def __init__(self, candidates):
        self.list = candidates
        self.place = 0
        self.power = 1
        
    def current(self):
        if self.place or self.place == 0:
            return self.list[self.place]
        
    def next(self):
        if self.place < len(self.list) - 1:
            self.place += 1
        else:
            self.place = False