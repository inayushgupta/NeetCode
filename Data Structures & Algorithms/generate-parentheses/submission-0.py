class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def generate(para, openp, closep):

            if openp == n and closep == n: 
                ans.append(para)
                return
            
            if openp < n:
                generate(para + '(', openp + 1, closep)
            
            if closep < openp:
                generate(para + ')', openp, closep + 1)
            
            return None
            
        generate("", 0, 0)
        
        return ans