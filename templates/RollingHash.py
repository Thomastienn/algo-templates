class RollingHash:
    def __init__(self, s, base=911382629, mod=10**18 + 3):
        """
        Initialize the rolling hash for the string `s`.
        :param s: The input string.
        :param base: Base for the rolling hash (should be a large prime).
        :param mod: Modulus for the rolling hash (should be a large prime).
        """
        self.s = s
        self.n = len(s)
        self.base = base
        self.mod = mod
        self.powers = [1] * (self.n + 1)  # Precompute powers of the base
        self.prefix_hashes = [0] * (self.n + 1)  # Precompute prefix hashes

        # Precompute powers of the base
        for i in range(1, self.n + 1):
            self.powers[i] = (self.powers[i - 1] * self.base) % self.mod

        # Precompute prefix hashes
        for i in range(1, self.n + 1):
            self.prefix_hashes[i] = (self.prefix_hashes[i - 1] * self.base + ord(s[i - 1])) % self.mod

    def get_hash(self, l, r):
        """
        Get the hash of the substring s[l:r].
        :param l: Left index (inclusive).
        :param r: Right index (exclusive).
        :return: The hash of the substring s[l:r].
        """
        return (self.prefix_hashes[r] - self.prefix_hashes[l] * self.powers[r - l]) % self.mod


# REDUCE THE PROBABILITY OF COLLISION
class DoubleRollingHash:
    def __init__(self, s, base1=911382629, mod1=10**18 + 3, base2=357168791, mod2=10**18 + 9):
        """
        Initialize the double rolling hash for the string `s`.
        :param s: The input string.
        :param base1: Base for the first rolling hash (should be a large prime).
        :param mod1: Modulus for the first rolling hash (should be a large prime).
        :param base2: Base for the second rolling hash (should be a large prime).
        :param mod2: Modulus for the second rolling hash (should be a large prime).
        """
        self.s = s
        self.n = len(s)
        self.base1 = base1
        self.mod1 = mod1
        self.base2 = base2
        self.mod2 = mod2
        self.powers1 = [1] * (self.n + 1)  # Precompute powers of the first base
        self.powers2 = [1] * (self.n + 1)  # Precompute powers of the second base
        self.prefix_hashes1 = [0] * (self.n + 1)  # Precompute prefix hashes for the first hash
        self.prefix_hashes2 = [0] * (self.n + 1)  # Precompute prefix hashes for the second hash

        # Precompute powers of the bases
        for i in range(1, self.n + 1):
            self.powers1[i] = (self.powers1[i - 1] * self.base1) % self.mod1
            self.powers2[i] = (self.powers2[i - 1] * self.base2) % self.mod2

        # Precompute prefix hashes
        for i in range(1, self.n + 1):
            self.prefix_hashes1[i] = (self.prefix_hashes1[i - 1] * self.base1 + ord(s[i - 1])) % self.mod1
            self.prefix_hashes2[i] = (self.prefix_hashes2[i - 1] * self.base2 + ord(s[i - 1])) % self.mod2

    def get_hash(self, l, r):
        """
        Get the double hash of the substring s[l:r].
        :param l: Left index (inclusive).
        :param r: Right index (exclusive).
        :return: A tuple (hash1, hash2) representing the double hash of the substring s[l:r].
        """
        hash1 = (self.prefix_hashes1[r] - self.prefix_hashes1[l] * self.powers1[r - l]) % self.mod1
        hash2 = (self.prefix_hashes2[r] - self.prefix_hashes2[l] * self.powers2[r - l]) % self.mod2
        return (hash1, hash2)
        
def is_palindrome(s, rh, l, r):
    """
    Check if the substring s[l:r] is a palindrome.
    :param s: The input string.
    :param rh: A RollingHash or DoubleRollingHash object.
    :param l: Left index (inclusive).
    :param r: Right index (exclusive).
    :return: True if the substring is a palindrome, False otherwise.
    """
    return rh.get_hash(l, r) == rh.get_hash(len(s) - r, len(s) - l)


def count_distinct_substrings(s, rh):
    """
    Count the number of distinct substrings in the string `s`.
    :param s: The input string.
    :param rh: A RollingHash or DoubleRollingHash object.
    :return: The number of distinct substrings.
    """
    n = len(s)
    distinct_hashes = set()
    for l in range(n):
        for r in range(l + 1, n + 1):
            distinct_hashes.add(rh.get_hash(l, r))
    return len(distinct_hashes)
    
s = "abacaba"
rh = RollingHash(s)

# Get hash of substring s[1:4] ("bac")
hash_val = rh.get_hash(1, 4)
print(hash_val)  # Output: Some numeric hash value

# Checking hash first "ba" vs the end "ba"
print(rh.get_hash(1,3), rh.get_hash(5,7))