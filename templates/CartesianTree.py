class CartesianTree:
    def __init__(self, array):
        self.n = len(array)
        self.parent = [-1] * self.n
        self.left = [-1] * self.n
        self.right = [-1] * self.n
        self.root = self.build(array)

    def build(self, array):
        stack = []
        for i in range(self.n):
            last = -1
            while stack and array[stack[-1]] > array[i]:
                last = stack.pop()
            if stack:
                self.parent[i] = stack[-1]
                self.right[stack[-1]] = i
            if last != -1:
                self.parent[last] = i
                self.left[i] = last
            stack.append(i)
        return stack[0]