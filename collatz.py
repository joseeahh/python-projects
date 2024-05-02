def collatz(n):
  count = 1
  while n > 1:
    if n % 2 == 1:
      n = 3 * n + 1
      count += 1
      n /= 2 # shortened version of collatz sequence, since 3n + 1 is 0 mod 2 when n is odd
      count += 1
    else:
      n /= 2
      count += 1
  if n < 1:
    return("Please enter a positive number.")
  return int(count)

def collatzNew(n, dic):
  count = 1
  original = n
  while True:
    if n < original:
      dic[original] = dic[n] + count - 1 # stores previous values, closely mimics implementation of cache
      break
    if n == 1:
      dic[original] = count # sets item in limit's index to number of iterations
      break
    if n % 2 == 0:
      n /= 2
    else:
      n = 3 * n + 1
    count += 1
  return dic
