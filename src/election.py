class Election:
    def __init__(self, voters = False):
        self.ballots = []
        self.voters = voters
        
    def ballot(self, list, voter = False):
        if self.voters or self.voters == []:
            if not(voter) or voter in self.voters:
                return False
            self.voters += [voter]
        self.ballots += [Ballot(list)]
        return True

    def runElection(self,number):
        scoreboard = self.makeScoreboard()
        winners = []
        winnersLeft = number
        
        #this threshhold works in python3 but perhaps not python2, from integer division
        threshhold = len(self.ballots) / (1 + number)
        
        while len(scoreboard) > winnersLeft:
            roundWinners = self.runRound(scoreboard, threshhold, len)
            winners += roundWinners
            winnersLeft -= len(roundWinners)
                
        winners += scoreboard.keys()
        winnersLeft -= len(scoreboard.keys())
        
        if winnersLeft > 0:
            return False
        
        return winners

    def makeScoreboard(self):
        scoreboard = {candidate:0 for ballot in self.ballots for candidate in ballot.list}
        for ballot in self.ballots:
            ballot.power = 1
            scoreboard[ballot.current()] += 1
        return scoreboard

    def allocate(self,scoreboard,threshhold,candidatesEliminated,winner = False):
        for ballot in self.ballots:
            if ballot.current() in candidatesEliminated:
                if winner:
                    ballot.power *= candidatesEliminated[ballot.current()]
                ballot.next()
                while ballot.current() and ballot.current() not in scoreboard and ballot.current() not in candidatesEliminated:
                    ballot.next()
                if ballot.current():
                    scoreboard[ballot.current()] += ballot.power
        for eliminated in candidatesEliminated:
            del scoreboard[eliminated]

    def runRound(self, scoreboard, threshhold, len):
        roundWinners = {candidate:(votes - threshhold)/votes for candidate, votes in scoreboard.items() if votes > threshhold}
        if roundWinners:
            self.allocate(scoreboard,threshhold,roundWinners, True)
            return roundWinners
        lowestScore = min(scoreboard.values())
        roundLosers = [candidate for candidate, votes in scoreboard.items() if votes == lowestScore]
        self.allocate(scoreboard,threshhold,roundLosers,False)
        return []
        
class Ballot:
    def __init__(self, candidates):
        self.list = candidates
        self.place = 0
        self.power = 1
        
    def current(self):
        if self.place < len(self.list):
            return self.list[self.place]
        return False
        
    def next(self):
        self.place += 1