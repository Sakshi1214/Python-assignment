
class reverse_iter:
    def __init__(self, l):
        self.l = l[::-1]
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.l):
            i = self.i
            self.i += 1
            return self.l[i]
        else:
            raise StopIteration()
    
it = reverse_iter([1, 2, 3, 4])
next(it)
print(it)
