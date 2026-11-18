class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        penalty = 0
        min_pen = 0
        min_hour = 0

        for hour, arrive in enumerate(customers):

            if arrive == 'Y':
                penalty += 1
            else:
                penalty -= 1
            
            if penalty > min_pen:
                min_pen = penalty
                min_hour = hour + 1

        return min_hour