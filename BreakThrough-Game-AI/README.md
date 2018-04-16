# Python-Projects


## Goal 
For this lab we have implemented a Python code to play the game of Break-Through usingdifferent functions that we have designed. In our implementation, player ?O? gets the firstmove by default.

###Utility Functions:##Evasive AI
 - The evasive AI does not actively go after the other player?s pieces unless thatis the only option. It will try to maximize its number of pieces therefore in each level itmight choose to eat the opponent?s piece if that is the only way to keep its piece. It usuallyspreads out its pieces and moves most of the pieces forward as opposed to forwardingonly a single piece forward as was seen in the case of the Conqueror AI.
##Conqueror AI 
- The Conqueror AI moves its pieces with the goal of capturing the otherplayer?s pawns. This AI often moves the same piece multiple times to get closer to and eatanother player?s piece. This AI often will move only one piece at a time as required tocapture other pieces leaving the rest of the pieces behind.

##Collective_utility
-This heuristic takes into account several things to calculate the utilityof the board state. If the board is winning state, the utility is infinite. If the board state isalmost about to win with the piece about to reach the end state not being attacked, it adds50 to the utility. Similarly, it adds utility of 1 for every piece that is protected and subtract1 for every piece that is being attacked. Further, this heuristic calculates the threat of eachopponent piece and adds negative utility. The opponent pieces that are almost about towin (i.e. far ahead in the board) are marked as more dangerous than the ones that arebehind.


##Avg_dist_utility:
-This is the heuristic we designed. This calculates the averageprogression between how far our pieces have gotten and looks at the same distancebetween the opponents and maximizes the utility value. This heuristic decides to eat aplayer?s piece if taking out the opponent?s piece reduces their score and increases ours (ifour piece gets closer). Further, this heuristic calculates the threat of each opponent pieceand adds negative utility. The opponent piece that are almost about to win (i.e. far aheadin the board) are marked as more dangerous than the ones that are behind. Similarly, itadds utility of 1 for every piece that is protected and subtracts 1 for every piece that isbeing attacked.Each of our functions took roughly 1.5 seconds to calculate the optimal move during eachstate.
