def cache_fib(function):
  cache = {}
  
  def d_func(*args):
    if args in cache: # check if already there
      return cache[args]
    else: # add and return same value
      cache[args] = function(*args)
      return function(*args)
  return d_func


@cache_fib
def fibonacci(n):
  # recursive function to get the nth fib number.
  if n <= 1:
    return n
  else:
    return(fibonacci(n-1)+fibonacci(n-2))
  
print(fibonacci(100))
