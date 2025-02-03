from math import ceil, log2, gcd, lcm
from functools import reduce

class segment_tree:
    def __init__(self, array, operation="sum"):
        self.n = len(array)
        self.array = array
        self.operation = operation

        # Define merge, basef, basev, lazy_merge, lazy_apply, and lazy_base based on the operation
        if operation == "sum":
            self.merge = lambda x, y: x + y
            self.basef = lambda x: x
            self.basev = 0
            self.lazy_merge = lambda x, y: x + y
            self.lazy_apply = lambda a, b, ln, rn: a + b * (rn - ln + 1)
            self.lazy_base = 0
        elif operation == "max":
            self.merge = max
            self.basef = lambda x: x
            self.basev = -float('inf')
            self.lazy_merge = lambda x, y: y
            self.lazy_apply = lambda a, b, ln, rn: b
            self.lazy_base = None
        elif operation == "min":
            self.merge = min
            self.basef = lambda x: x
            self.basev = float('inf')
            self.lazy_merge = lambda x, y: y
            self.lazy_apply = lambda a, b, ln, rn: b
            self.lazy_base = None
        elif operation == "xor":
            self.merge = lambda x, y: x ^ y
            self.basef = lambda x: x
            self.basev = 0
            self.lazy_merge = lambda x, y: x ^ y
            self.lazy_apply = lambda a, b, ln, rn: a ^ b if (rn - ln + 1) % 2 else a
            self.lazy_base = 0
        elif operation == "product":
            self.merge = lambda x, y: x * y
            self.basef = lambda x: x
            self.basev = 1
            self.lazy_merge = lambda x, y: x * y
            self.lazy_apply = lambda a, b, ln, rn: a * (b ** (rn - ln + 1))
            self.lazy_base = 1
        elif operation == "gcd":
            self.merge = lambda x, y: gcd(x, y)
            self.basef = lambda x: x
            self.basev = 0
            self.lazy_merge = None  # Lazy propagation not typically used for GCD
            self.lazy_apply = None
            self.lazy_base = None
        elif operation == "lcm":
            self.merge = lambda x, y: lcm(x, y)
            self.basef = lambda x: x
            self.basev = 1
            self.lazy_merge = None  # Lazy propagation not typically used for LCM
            self.lazy_apply = None
            self.lazy_base = None
        elif operation == "and":
            self.merge = lambda x, y: x & y
            self.basef = lambda x: x
            self.basev = ~0  # Identity for AND (all bits set to 1)
            self.lazy_merge = lambda x, y: x & y
            self.lazy_apply = lambda a, b, ln, rn: a & b
            self.lazy_base = ~0
        elif operation == "or":
            self.merge = lambda x, y: x | y
            self.basef = lambda x: x
            self.basev = 0  # Identity for OR
            self.lazy_merge = lambda x, y: x | y
            self.lazy_apply = lambda a, b, ln, rn: a | b
            self.lazy_base = 0
        else:
            raise ValueError("Unsupported operation. Choose from 'sum', 'max', 'min', 'xor', 'product', 'gcd', 'lcm', 'and', 'or'.")

        # Initialize the segment tree and lazy arrays
        self.size = 1 << (self.n - 1).bit_length()
        self.tree = [self.basev] * (2 * self.size)
        self.lazy = [self.lazy_base] * (2 * self.size)
        self.build(array)

    def __str__(self):
        return ' '.join([str(x) for x in self.tree])

    def _build_util(self, l, r, i, a):
        if l == r:
            self.tree[i] = self.basef(a[l])
            return self.tree[i]
        mid = (l + r) // 2
        self.tree[i] = self.merge(
            self._build_util(l, mid, 2 * i + 1, a),
            self._build_util(mid + 1, r, 2 * i + 2, a)
        )
        return self.tree[i]

    def build(self, a):
        self._build_util(0, len(a) - 1, 0, a)

    def _push_down(self, i, ln, rn):
        if self.lazy[i] != self.lazy_base:
            # Apply the lazy update to the current node
            self.tree[i] = self.lazy_apply(self.tree[i], self.lazy[i], ln, rn)
            if ln != rn:
                # Propagate the lazy update to the children
                self.lazy[2 * i + 1] = self.lazy_merge(self.lazy[2 * i + 1], self.lazy[i])
                self.lazy[2 * i + 2] = self.lazy_merge(self.lazy[2 * i + 2], self.lazy[i])
            # Clear the lazy update for the current node
            self.lazy[i] = self.lazy_base

    def _query_util(self, i, ln, rn, l, r):
        self._push_down(i, ln, rn)
        if ln >= l and rn <= r:
            return self.tree[i]
        if ln > r or rn < l:
            return self.basev
        mid = (ln + rn) // 2
        return self.merge(
            self._query_util(2 * i + 1, ln, mid, l, r),
            self._query_util(2 * i + 2, mid + 1, rn, l, r)
        )

    def query(self, l, r):
        return self._query_util(0, 0, self.n - 1, l, r)

    def _update_util(self, i, ln, rn, l, r, val):
        self._push_down(i, ln, rn)
        if ln > r or rn < l:
            return
        if ln >= l and rn <= r:
            # Apply the lazy update to the current node
            self.lazy[i] = self.lazy_merge(self.lazy[i], val)
            self._push_down(i, ln, rn)
            return
        mid = (ln + rn) // 2
        self._update_util(2 * i + 1, ln, mid, l, r, val)
        self._update_util(2 * i + 2, mid + 1, rn, l, r, val)
        self.tree[i] = self.merge(self.tree[2 * i + 1], self.tree[2 * i + 2])

    def update(self, l, r, val):
        self._update_util(0, 0, self.n - 1, l, r, val)

    def point_update(self, x, val):
        self._update_util(0, 0, self.n - 1, x, x, val)
        self.array[x] = val
        
arr = [1, 2, 3, 4, 5, 6, 7, 8]
st_sum = segment_tree(arr, operation="sum")
st_max = segment_tree(arr, operation="max")
st_min = segment_tree(arr, operation="min")
st_xor = segment_tree(arr, operation="xor")
st_product = segment_tree(arr, operation="product")
st_gcd = segment_tree(arr, operation="gcd")
st_lcm = segment_tree(arr, operation="lcm")
st_and = segment_tree(arr, operation="and")
st_or = segment_tree(arr, operation="or")

print("TEST")
print(st_sum.query(1, 3))  # Output: 9 (2 + 3 + 4)
print(st_max.query(1, 3))  # Output: 4 (max(2, 3, 4))
print(st_min.query(1, 3))  # Output: 2 (min(2, 3, 4))
print(st_xor.query(1, 3))  # Output: 5 (2 ^ 3 ^ 4)
print(st_product.query(1, 3))  # Output: 24 (2 * 3 * 4)
print(st_gcd.query(1, 3))  # Output: 1 (gcd(2, 3, 4))
print(st_lcm.query(1, 3))  # Output: 12 (lcm(2, 3, 4))
print(st_and.query(1, 3))  # Output: 0 (2 & 3 & 4)
print(st_or.query(1, 3))   # Output: 7 (2 | 3 | 4)

st_sum.update(1, 3, 2)  # Add 2 to elements in range [1, 3]
st_max.update(1, 3, 10)  # Assign 10 to elements in range [1, 3]
st_min.update(1, 3, 0)   # Assign 0 to elements in range [1, 3]
st_xor.update(1, 3, 2)   # XOR 2 to elements in range [1, 3]
st_product.update(1, 3, 2)  # Multiply by 2 to elements in range [1, 3]
st_and.update(1, 3, 3)   # AND 3 to elements in range [1, 3]
st_or.update(1, 3, 3)    # OR 3 to elements in range [1, 3]

print()
print("UPDATED")
print(st_sum.query(1, 3))  # Output: 15 (4 + 5 + 6)
print(st_max.query(1, 3))  # Output: 10 (max(10, 10, 10))
print(st_min.query(1, 3))  # Output: 2 (min(2, 3, 4))
print(st_xor.query(1, 3))  # Output: 5 (2 ^ 3 ^ 4)
print(st_product.query(1, 3))  # Output: 24 (2 * 3 * 4)
print(st_gcd.query(1, 3))  # Output: 1 (gcd(2, 3, 4))
print(st_lcm.query(1, 3))  # Output: 12 (lcm(2, 3, 4))
print(st_and.query(1, 3))  # Output: 0 (2 & 3 & 4)
print(st_or.query(1, 3))   # Output: 7 (2 | 3 | 4)