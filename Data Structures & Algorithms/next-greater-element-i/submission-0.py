class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st, res, out = Stack(), {}, []
        
        for i in range(len(nums2)):
            top = st.top()
            while top != -1 and nums2[top] < nums2[i]:
                poped = st.pop()
                res[nums2[poped]] = nums2[i]
                top = st.top()
            st.push(i)

        return [res.get(n, -1) for n in nums1]

    

class Stack:
    def __init__(self):
        self.data = []
    
    def top(self):
        if not self.data:
            return -1
        return self.data[-1]
    
    def pop(self):
        if not self.data:
            return -1
        return self.data.pop()
    
    def push(self, index):
        self.data.append(index)
