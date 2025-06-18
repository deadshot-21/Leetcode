class RandomizedSet:

    def __init__(self):
        self.list = []
        self.hashmap = {}

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.hashmap[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        index_to_remove = self.hashmap[val]
        self.list[-1], self.list[index_to_remove] = self.list[index_to_remove], self.list[-1]
        self.hashmap[self.list[index_to_remove]] = index_to_remove
        self.list.pop()
        del self.hashmap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()