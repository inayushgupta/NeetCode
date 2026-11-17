class Solution:
    def trap(self, height: List[int]) -> int:
        
        # if len of height is 1 return 0
        amount = 0
        trap = False
        stack = []
        prev = -1

        # if the previous is smaller and there is no


        for h in height:

            if not stack:
                stack.append(h)
                prev = h
                continue
            else: # here stack have some elements

                # what is possible
                if trap: # trap is set meaning there are some space between two bars
                    if prev <= h: # if the currect bar is the end bar
                        # here we will pop everything and calculate
                        while stack:
                            amount += prev - stack.pop()
                        prev, trap = h, False
                        stack.append(h)
                    else:
                        stack.append(h)
                else:

                    # here the currect bar is bigger than the previous bar
                    # if the bar is bigger then change prev
                    if h >= stack[-1]:
                        stack.pop()
                        stack.append(h)
                        prev = h
                    else:
                        trap = True
                        stack.append(h)
                    # if the bar is smaller put in the stack and set trap

        # run the code backwards

        newx = list(reversed(stack))
        stack = []
        prev, trap = -1, False
        for h in newx:

            if not stack:
                stack.append(h)
                prev = h
                continue
            else: # here stack have some elements

                # what is possible
                if trap: # trap is set meaning there are some space between two bars
                    if prev <= h: # if the currect bar is the end bar
                        # here we will pop everything and calculate
                        while stack:
                            amount += prev - stack.pop()
                        prev, trap = h, False
                        stack.append(h)
                    else:
                        stack.append(h)
                else:

                    # here the currect bar is bigger than the previous bar
                    # if the bar is bigger then change prev
                    if h >= stack[-1]:
                        stack.pop()
                        stack.append(h)
                        prev = h
                    else:
                        trap = True
                        stack.append(h)
                    # if the bar is smaller put in the stack and set trap


        return amount

