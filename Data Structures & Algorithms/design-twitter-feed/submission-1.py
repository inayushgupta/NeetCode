class Twitter:

    def __init__(self):
        self.userFollows = defaultdict(set)
        self.userTweets = defaultdict(list)
        self.timer = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userFollows[userId].add(userId)
        self.userTweets[userId].append((self.timer, tweetId))
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        
        # here is the list of all the followers of userId
        allFollowers = self.userFollows[userId]
        heap = []
        res =  []

        for follow in allFollowers:

            tweets = self.userTweets[follow]
            if tweets:
                time, tid = tweets[-1]
                idx = len(tweets) - 1
                heapq.heappush_max(heap, (time, tid, follow, idx))
        
        # now we will expand
        while heap and len(res) < 10:
            time, tid, follow, idx = heapq.heappop_max(heap)
            res.append(tid)
            if idx > 0:
                time, tid = self.userTweets[follow][idx - 1]
                heapq.heappush_max(heap, (time, tid, follow, idx - 1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollows[followerId].add(followerId)
        self.userFollows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.userFollows[followerId].discard(followeeId)
            
