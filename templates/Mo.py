def mo_algorithm(array, queries):
    block_size = int(len(array) ** 0.5) + 1
    sorted_queries = sorted(enumerate(queries), key=lambda x: (x[1][0] // block_size, x[1][1]))
    result = [0] * len(queries)
    current_l, current_r, current_sum = 0, -1, 0

    for idx, (l, r) in sorted_queries:
        while current_r < r:
            current_r += 1
            current_sum += array[current_r]
        while current_r > r:
            current_sum -= array[current_r]
            current_r -= 1
        while current_l < l:
            current_sum -= array[current_l]
            current_l += 1
        while current_l > l:
            current_l -= 1
            current_sum += array[current_l]
        result[idx] = current_sum

    return result