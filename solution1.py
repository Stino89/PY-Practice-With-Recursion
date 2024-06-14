def recursive_count_down(n):
	if n == 0:
		print(n)
		return

	else:
		print(n)
		return recursive_count_down(n-1)

recursive_count_down(7)