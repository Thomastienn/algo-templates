class SparseTable:
    def __init__(self, array, func=min):
        self.n = len(array)
        self.func = func
        self.k = self.n.bit_length()
        self.st = [[0] * self.n for _ in range(self.k)]
        self.st[0] = array.copy()
        for i in range(1, self.k):
            j = 0
            while j + (1 << i) <= self.n:
                self.st[i][j] = self.func(self.st[i - 1][j], self.st[i - 1][j + (1 << (i - 1))])
                j += 1

    def query(self, l, r):
        i = (r - l + 1).bit_length() - 1
        return self.func(self.st[i][l], self.st[i][r - (1 << i) + 1])