
class MyHashTable:
    def __init__(self, table_size=11):
        self.table_size = table_size
        self.hash = [[] for n in range(self.table_size)]
        self.num = 0
        self.num_collisions = 0
        self.indexkey = None

    def insert(self, key, item):
        self.num += 1
        hashindex = key % self.table_size
        # check if it is duplicate, if so replace item with new item
        if self.get_index(key):
            i = self.indexkey
            self.hash[hashindex][i] = (key, item)
            self.num -= 1
        # put in tuple key and value into hashindex
        else:
            self.hash[hashindex].append((key, item))
            if len(self.hash[hashindex]) != 1:
                self.num_collisions += 1
        # add to collision if collided

        # check if 50%, expand by 2 add 1 to size
        if self.load_factor() > 1.5:
            self.num_collisions = 0
            self.num = 0
            old_table_size = self.table_size
            self.table_size = self.table_size * 2 + 1
            temp = self.hash
            self.hash = [[] for n in range(self.table_size)]
            n = 0
            z = 0
            # rehash numbers
            while old_table_size > n:
                while len(temp[n]) > z:
                    keyy = temp[n][z][0]
                    itemy = temp[n][z][1]
                    self.insert(keyy, itemy)
                    z += 1
                z = 0
                n += 1

    def get(self, key):
        hashindex = key % self.table_size
        i = 0
        while len(self.hash[hashindex]):
            if self.hash[hashindex][i][0] == key:
                return self.hash[hashindex][i]
            i += 1
        raise LookupError

    def remove(self, key):
        hashindex = key % self.table_size
        #call self.get_index()
        if self.get_index(key):
            return self.hash[hashindex].pop(self.indexkey)
        else:
            raise LookupError

    def size(self):
        return self.num

    def load_factor(self):
        return self.num / self.table_size

    def collisions(self):
        return self.num_collisions
    def get_index(self, key):
        hashindex = key % self.table_size
        i = 0
        while len(self.hash[hashindex]) > i:
            if self.hash[hashindex][i][0] == key:
                self.indexkey = i
                return True
            else:
                i += 1
        return False


hashy = MyHashTable()
hashy.insert(7, 'nice')
