def extend_euclid(a: int, b: int) -> list[int]:
	if not b:
		return [1, 0]
	p = extend_euclid(b, a % b)
	return [p[1], p[0] - (a // b) * p[1]]