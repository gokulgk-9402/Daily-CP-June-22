# problem link -> https://leetcode.com/problems/bulls-and-cows/


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cows = 0
        bulls = 0

        secret_dict = {str(i):0 for i in range(10)}
        guess_dict = {str(i):0 for i in range(10)}

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_dict[secret[i]] += 1
                guess_dict[guess[i]] += 1

        for i in secret_dict.keys():
            if secret_dict[i]== guess_dict[i]:
                cows += secret_dict[i]

            elif secret_dict[i] < guess_dict[i]:
                if secret_dict[i]:
                    cows += secret_dict[i]

            else:
                cows += guess_dict[i]

        return f'{bulls}A{cows}B'