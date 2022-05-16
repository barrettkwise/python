class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        key = { "2" : ["a", "b", "c"],
                "3" : ["d", "e", "f"],
                "4" : ["g", "h", "i"],
                "5" : ["j", "k", "l"],
                "6" : ["m", "n", "o"],
                "7" : ["p", "q", "r", "s"],
                "8" : ["t", "u", "v"],
                "9" : ["w", "x", "y", "z"]
              }
        
        res = []
        l = len(digits)
        if l == 0:
            return res
        
        def dfs(digits, curr):
            
            if len(curr) == l:
                return res.append(curr)
            
            left = digits[0]
            
            for i in key[left]:
                dfs(digits[1:], curr + i)
            
        dfs(digits, '')
        
        return res
            
            