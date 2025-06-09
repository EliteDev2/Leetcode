class Solution:
    def reformat(self, s: str) -> str:
        alphabets = [alpha for alpha in s if alpha.isalpha()]
        digits = [digit for digit in s if digit.isdigit()]
        if abs(len(alphabets) - len(digits)) > 1:
            return ""
        
        res = []
        flag = len(alphabets) > len(digits)
        while alphabets or digits :
            res.append( alphabets.pop() if flag else digits.pop() )
            flag = not flag # turns true , false every loop
        return ''.join(res)
