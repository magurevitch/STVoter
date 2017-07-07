# STVoter
Single Transferable Voting is a system for allowing districts that can choose multiple representatives. STV gives each voter the option to rank candidates from favorite to least favorite. It claims to elimate certain pitfalls of plurality voting (the most votes chose one representative, even if they do not have the majority of votes), such as allowing minorities groups to also be represented and not forcing voters to strategically choose the candidates that would win rather than the ones they like the best.

## Methods
A new Election object is a blank object that stores what ballots have been cast, and optionally who has cast ballots.
It has two main methods.
* The ballot method takes a list of candidates, ranked by most liked candidate first, and optionally the voter who is casting it, and adds it to the election.
* The runElection method takes the number of representatives to choose, and gives back a list of who those representatives are. It specifically gives them ordered by which round the candidates were chosen in it.

## Counting up votes
STV uses the following methodology to find winners:
* choose a threshhold for how many votes a candidate needs to get chosen
* go through the following process until you get enough winners
*  if there any candidates over the threshhold, chose them, and if they have more votes than are necessary, their extra votes are reällocated to their voter's next most favorite candidate.
*  if no candidates are good enough, the least voted for candidate is eliminated, and their voters are reällocated to their next favorite candidates.

There are two main methods for setting the threshhold.
* The Hare method splits it up equally, so in a round for four representatives, winners need a quarter of the votes.
* The Droop method splits it up so that you need a slightly lower amount, specifically, a little more than if you split among one more than the number of winners. So, a round for four representatives, a winner needs just over one fifth of the votes.
This STVoter uses the Droop method, because while it is harder to explain, usually gives better outcomes.

There are many methods to allocate the excess votes of winners. This STVoter uses the Gregory method, which gives a fraction of each vote to a winner, just enough so that everyone puts in enough for the winner to reach the threshhold, and then allocates the remaining fractions to the next candidates. This method is hard to do by hand, as you need to keep track of many fractions of votes, but it presents no problems to a computer.
Other methods to reällocate a winner's votes could be random.
