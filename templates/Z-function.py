def z_function(s):
    n = len(s)
    z = [0] * n  # Z-function array
    left = 0  # Left boundary of the current window
    right = 0  # Right boundary of the current window

    for i in range(1, n):  # Start from 1 since z[0] is always 0
        # If i is within the current window, reuse previously computed values
        if i <= right:
            z[i] = min(right - i + 1, z[i - left])
        
        # Expand the window as far as possible
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        
        # Update the window if we found a longer match
        if i + z[i] - 1 > right:
            left = i
            right = i + z[i] - 1
    
    return z