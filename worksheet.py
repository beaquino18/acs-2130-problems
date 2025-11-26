def factorial(n):
  if n == 1 or n == 0:
    return 1
  else:
    return n * factorial(n-1)


def sum_natural_numbers(n):
  if n == 1:
    return 1
  else:
    return n + sum_natural_numbers(n - 1)
  
  
def multiple(a, b):
  if b == 0:
    return 0
  else:
    return a + multiple(a, b - 1)


def power(a, b):
  if b < 0:
    return 1 / power(a, b * -1)
  if b == 0:
    return 1
  else:
    return a * power(a, b - 1)


def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)


def reverse_words(s):
  words = s.split()
  
  if len(words) <= 1:
    return s
  else:
    last_word = words[-1] 
    remaining = " ".join(words[:-1])
    return last_word + " " + reverse_words(remaining)

