class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        #totals
        Y = 0
        for customer in customers:
            if customer == 'Y':
                Y += 1
        
        min_pen = Y
        min_hour = 0

        y, n = 0, 0
        for hour in range(len(customers)):
            arrive = customers[hour]
            
            if arrive == 'Y':
                y += 1
            else:
                n += 1

            if n + (Y-y) < min_pen:
                min_pen = n + (Y-y)
                min_hour = hour+1

        return min_hour