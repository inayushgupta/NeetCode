class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-1] += 1
        i = len(digits)-1
        while i+1:
            digits[i] += carry
            if digits[i] > 9:
                digits[i] = digits[i] - 10
                carry = 1
            else:
                carry = 0
                break
            i-=1
        if carry:
            return [1] + digits
        return digits
            
        