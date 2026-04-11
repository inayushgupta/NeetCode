class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.len = 0
        self.cache = {}

        # assign dummy nodes 
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        # connect the nodes
        self.tail.prev = self.head
        self.head.next = self.tail

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node):

        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            
            # remove the node
            self.remove(node)

            #insert the node
            self.insert(node)

            # return value
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        
        # check if the key exist
        if key in self.cache:
            node = self.cache[key]
            # change the value 
            node.val = value
            # remove the node
            self.remove(node)
            # insert the node
            self.insert(node)
        else:
            match self.cap == self.len:
                case True:
                    # delete the Last Recently User
                    toRemove = self.head.next
                    self.remove(toRemove)
                    del self.cache[toRemove.key]
                    
                    # create the node
                    node = Node(key, value)
                    
                    # insert the node
                    self.insert(node)

                    # update the cache
                    self.cache[key] = node
                case False:

                    # create the node
                    node = Node(key, value)
                    
                    # insert the node
                    self.insert(node)
                    
                    # update the cache
                    self.cache[key] = node
                    self.len += 1
                    
