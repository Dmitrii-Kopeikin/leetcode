from typing import List
from collections import deque


# Decision taking into account votes at the end of the round.
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Here and below, "True" is a key to Radiant, "False" to Dire
        senate_dict = {True: deque(), False: deque()}
        for i, s in enumerate(senate):
            senate_dict[s == "R"].append(i)

        votes = {True: 0, False: 0}

        prev_senator = -1
        while senate_dict[True] and senate_dict[False]:
            fraction = senate_dict[False][0] > senate_dict[True][0]
            senator = senate_dict[fraction].popleft()
            # Adding len of senate needed for a check is the round was ended
            senate_dict[fraction].append(senator + len(senate))

            # This block checks is the next round started.
            if senator % len(senate) < prev_senator:
                if votes[True] != votes[False]:
                    break
                votes = {True: 0, False: 0}
            prev_senator = senator % len(senate)

            # This block decides which is better, ban or vote:
            #   - If the fraction has more than or equal to the number of votes
            #     of the opponent and there are no opponents left, then the
            #     senator votes.
            #   - Otherwise, it's best to ban one of the opponents.
            if (votes[fraction] >= votes[not fraction]
                    and len([x for x in senate_dict[not fraction] if x % len(senate) > senator % len(senate)])):
                # If chosen to ban, the next opponent is just discarded from the fraction.
                senate_dict[not fraction].popleft()
            else:
                votes[fraction] += 1

        return "Radiant" if votes[True] > votes[False] or not senate_dict[False] else "Dire"
