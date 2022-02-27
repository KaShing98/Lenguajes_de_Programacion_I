
class Block:
    def __init__(self, size, used=False, split=False):
        self.size = size
        self.used = used
        self.split = split
        self.name = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_size(self):
        return self.size

    def get_split(self):
        return self.split

    def set_split(self, split):
        self.split = split

    def get_used(self):
        return self.used

    def set_used(self, used):
        self.used = used

class Memory:
    def __init__(self, size):
        self.left = None
        self.right = None
        self.val = Block(size)

    def split(self, size):
        actual_block_size = self.val.get_size()
        next_block_size = self.val.get_size() // 2

        if (next_block_size >= size and size < actual_block_size and not self.val.get_split()):
            self.val.set_split(True)
            # print(next_block_size)
            self.left = Memory(next_block_size)
            self.right = Memory(next_block_size)

    def allocate(self, name, size):
        if self.val.get_used():
            return False

        if (self.right is None and self.left is None and not self.val.get_used()):
            self.split(size)

        if (self.right is not None and not self.right.val.get_used()):
            status = self.right.allocate(name, size)
            if status:
                return status

        if (self.left is not None and not self.left.val.get_used()):
            status = self.left.allocate(name, size)
            if status:
                return status

        if (self.right is None and self.left is None):
            if (not self.val.get_used() and size <= self.val.get_size()):
                self.val.set_used(True)
                self.val.set_name(name)
                return True
            
        return False

    def unallocate(self, name):
        if (self.val.get_name() == name):
            self.val.set_used(False)
            self.val.set_name(None)

            if (self.left is not None and not self.left.val.get_used() and self.left.val.get_split()):
                self.left = None

            if (self.right is not None and not self.right.val.get_used() and self.right.val.get_split()):
                self.right = None

            if (self.right is None and self.left is None):
                self.val.set_split(False)

            return True
        else:
            if (self.right is not None):
                status = self.right.unallocate(name)
                if status:
                    return status

            if (self.left is not None):
                status = self.left.unallocate(name)
                if status:
                    return status

        return False

    def print(self):

        visited = {}
        queue = []
 
        queue.append(self)
        visited[self.val.get_name()] = True

        text = ""
        while queue:
            s = queue.pop(0)
            
            name = s.val.get_name()
            if name is not None:
                text += "[USED] Name: {}, Size: {}\n".format(s.val.get_name(), s.val.get_size())
            else:
                if (s.val is not None and s.left is None and s.left is None):
                    text += "[FREE] Size: {}\n".format(s.val.get_size())

                if (s.val is not None and s.right is not None and s.right.val is not None):
                    queue.append(s.right)

                if (s.val is not None  and s.left is not None and s.left.val is not None):
                    queue.append(s.left)

        return text

