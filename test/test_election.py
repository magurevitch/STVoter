import unittest
import sys
sys.path.append('../')

from src.election import Election, Ballot

class TestElectionMethods(unittest.TestCase):
    def testAddBallot(self):
        election = Election()
        
        election.ballot([1,2])
        
        self.assertEqual(len(election.ballots), 1,"Adding a ballot works well")
        self.assertEqual(election.ballots[0].list, [1,2], "Adding a ballot works well")
        self.assertEqual(election.ballots[0].current(), 1, "Adding a ballot works well")

    def testOneMajority(self):
        election = Election()
        
        election.ballot([1,2,3])
        election.ballot([1,3,2])
        election.ballot([2,3,1])
    
        winners = election.runElection(1)
    
        self.assertEqual(winners,[1],"cannot find winner with majority")
        
    def testOneNoMajority(self):
        election = Election()
        
        election.ballot([1,2,3])
        election.ballot([1,3,2])
        election.ballot([2,1,3])
        election.ballot([2,3,1])
        election.ballot([3,1,2])

        winners = election.runElection(1)
    
        self.assertEqual(winners,[1],"cannot find winner without majority")
        
    #def testOneTooManyTies(self):
    #
    #    election = Election()
    #    election.ballot([1,2])
    #    election.ballot([2,1])
    
    #    winners = election.runElection(1)
        
    def testTwoJustEnoughCandidates(self):
        election = Election()
        
        election.ballot([1,2])
        election.ballot([1])
        election.ballot([1])
        
        winners = election.runElection(2)
        
        self.assertEqual(winners, [1,2], "won't choose all available candidates")
        
    #def testTwoNotEnoughCandidates(self):
    #
    #    election = Election()
    #    election.ballot([1])
    
    #    winners = election.runElection(2)
        
    def testTwoBothAtThreshhold(self):
        election = Election()
        
        election.ballot([1,2,3])
        election.ballot([1,3,2])
        election.ballot([2,1,3])
        election.ballot([2,3,1])
        election.ballot([3,1,2])

        winners = election.runElection(2)
    
        self.assertEqual(winners,[1,2],"cannot find two winners with enough votes")
        
    def testTwoOneAtThreshholdAllSame(self):
        election = Election()
        
        election.ballot([1,2])
        election.ballot([1,2])
        election.ballot([1,2])
        election.ballot([2])
        election.ballot([3])

        winners = election.runElection(2)
    
        self.assertEqual(winners,[1,2],"cannot find winner with only one at threshhold")
        
    def testTwoOneAtThreshholdAllDifferent(self):
        election = Election()
        
        election.ballot([1,2])
        election.ballot([1,2])
        election.ballot([1,3])
        election.ballot([2])
        election.ballot([3])

        winners = election.runElection(2)
    
        self.assertEqual(winners,[1,2],"cannot find winner with only one at threshhold")