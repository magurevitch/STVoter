import unittest
import sys
sys.path.append('../')

from src.election import Election, Ballot

class TestBallotMethods(unittest.TestCase):
    def testAddBallotNoVoter(self):
        election = Election()
        
        election.ballot([1,2])
        
        self.assertEqual(len(election.ballots), 1,"Adding a ballot works well")
        self.assertEqual(election.ballots[0].list, [1,2], "Adding a ballot works well")
        self.assertEqual(election.ballots[0].current(), 1, "Adding a ballot works well")
        
    def testAddBallotWithVoter(self):
        election = Election([])
        
        first = election.ballot([1,2])
        second = election.ballot([1,2],'A')
        third = election.ballot([1,2],'A')
        
        self.assertEqual(len(election.ballots), 1,"Adding a ballot works well")
        self.assertEqual(election.ballots[0].list, [1,2], "Adding a ballot works well")
        self.assertEqual(election.ballots[0].current(), 1, "Adding a ballot works well")
        
        self.assertEqual(first,False,"no voter not rejected")
        self.assertEqual(second,True,"new voter not accepted")
        self.assertEqual(third,False,"old voter not rejected")