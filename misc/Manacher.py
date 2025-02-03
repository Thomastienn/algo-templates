# EASIER VERSION
def longest_palindrome(s):
    n = len(s)
    if n == 0:
        return ""
    
    start, end = 0, 0
    
    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # Return the length of the palindrome
    
    for i in range(n):
        # Odd-length palindrome
        l1 = expand_around_center(s, i, i)
        # Even-length palindrome
        l2 = expand_around_center(s, i, i + 1)
        length = max(l1, l2)
        
        if length > (end - start):
            start = i - (length - 1) // 2
            end = i + length // 2
            print(f"Length: {length}, Center: {i}, Substring: {s[start:end+1]}, Start: {start}, End: {end}")
    
    return s[start:end + 1]

# Example Usage
print(longest_palindrome("babad"))  # Output: "bab" or "aba"



def shortestPalindrome(self, s: str) -> str:
    if s == "": return ""
    string = ""

    # convert odd / even strings to odd
    for i in range(len(s) - 1):
        string += s[i] + "#"
    string += s[len(s) - 1]

    # initialize variables
    pLengths = [0] * len(string)
    c = 0
    R = 0

    for i in range(len(string)):
        # mirror the palindromic length
        if i < R:
            mirror = 2 * c - i
            pLengths[i] = min(R - i, pLengths[mirror])

        # explore beyond bounds
        while (
            i - pLengths[i] - 1 >= 0
            and i + pLengths[i] + 1 < len(string)
            and string[i + pLengths[i] + 1] == string[i - pLengths[i] - 1]
        ):
            pLengths[i] += 1

        # update center and bound
        if pLengths[i] + i > R:
            c = i
            R = i + pLengths[i]

    # fix: some indices having extra pLength
    for i in range(int(len(pLengths) / 2)):
        if pLengths[2 * i] % 2:
            pLengths[2 * i] -= 1
        if pLengths[2 * i + 1] != 0 and not pLengths[2 * i + 1] % 2:
            pLengths[2 * i + 1] -= 1

    # if pL == i, at any point perform an expansion.
    for i in range(int(len(pLengths) / 2), -1, -1):
        if pLengths[i] == i:
            expand_index = i
            break

    # slice the part to be appended
    prefix_reversed = string[expand_index + pLengths[i] + 1 : len(string)]
    prefix = "".join(reversed(prefix_reversed))
    string = prefix + string
    return string.replace("#", "")

def longestPalindrome(s: str) -> str:
    if s == "": 
        return ""
    string = ""

    # convert odd/even strings to odd
    for i in range(len(s) - 1):
        string += s[i] + "#"
    string += s[len(s) - 1]
    
    # initialize variables
    pLengths = [0] * len(string)
    c = 0
    R = 0

    for i in range(len(string)):
        # mirror the palindromic length
        if i < R:
            mirror = 2 * c - i
            pLengths[i] = min(R - i, pLengths[mirror])

        # explore beyond bounds
        while (
            i - pLengths[i] - 1 >= 0
            and i + pLengths[i] + 1 < len(string)
            and string[i + pLengths[i] + 1] == string[i - pLengths[i] - 1]
        ):
            pLengths[i] += 1

        # update center and bound
        if pLengths[i] + i > R:
            c = i
            R = i + pLengths[i]

    # fix: some indices having extra pLength
    for i in range(int(len(pLengths) / 2)):
        if pLengths[2 * i] % 2:
            pLengths[2 * i] -= 1
        if pLengths[2 * i + 1] != 0 and not pLengths[2 * i + 1] % 2:
            pLengths[2 * i + 1] -= 1
    
    # return the longest substring
    mxpLengths = max(pLengths)
    longest_pL = pLengths.index(mxpLengths)
    start = longest_pL - mxpLengths
    end = longest_pL + mxpLengths
    return string[start : end + 1].replace("#", "")
    
    
print(longestPalindrome("abcdbdc"))