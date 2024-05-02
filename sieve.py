def sieve(limit):
  not_prime = set() # used sets to prevent overstorage
  primes = [] 
  for i in range(2, limit + 1):
    if i in not_prime: 
      continue
    for j in range(i**2, limit + 1, i): #adding up multiples of current i into not_prime
      not_prime.add(j)
    primes.append(i) # adding any left-over numbers
  return print(primes)
