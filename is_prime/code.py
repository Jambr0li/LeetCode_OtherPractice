

def is_prime(n):
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return False
	return True

def list_primes(limit):
	if limit < 2:
		print("no primes")
	for i in range(2, limit):
		if is_prime(i):
			print(i)

list_primes(1000)

