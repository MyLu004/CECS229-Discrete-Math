import math

def primes(a, b):
  """
      prints all primes in the range [a, b]
      :@param a: int type; a positive integer greater than 1
      :@param b: int type; a positive integer greater than or equal to a.
      :@return: set type; a set of all primes in the range [a, b]
      :@raises ValueError if a < 1 or b < a
      """
  if a < 1 or b < a:  # handling invalid range
    raise ValueError("Invalid range given")

  if a == 1:  # handling starting point a = 1
    a = 2  # this ensures 1 is not listed as a prime

  #FIXME: initialize `stop` which is the stopping criteria for
  #        the loop in the Sieve of Eratosthenes
#   myRange = int(b) - int(a)
 
    
  stop = math.floor(math.sqrt(int(b)))

  print("my stop point: ",stop)


  # FIXME: initialize a Python set called `P` that contains
  #        all integers in the range [a, b]
  P = set(range(a,b+1))
  print("my P: ",P)

  for x in range(2, stop):

    # FIXME: use Python list comprehension to create a set
    #        of multiples of x in the range [2, b];

    # HINT: the set of multiples of x can be expressed as
    #       k * x, where k is an integer; hence the comprehension
    #       should loop over values that satisfy k * x <= b
    print("my x: ",x)
    multiples_x = set([value*x for value in range(1, (b//x)+1) if (value*x<=b)])
    print("multiples x: ",multiples_x)
    P -= multiples_x  # removing the multiples of x from the set P

  return P

if __name__ == "__main__":
  val1 = 22
  val2 = 68
  print("expected: {67, 37, 41, 43, 47, 61, 53, 23, 59, 29, 31} ")
  print("received: ",primes(val1,val2))
