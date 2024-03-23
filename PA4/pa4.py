import math


""" ----------------- PROBLEM 1 ----------------- """
def translate(S, z0):
  """
  translates the complex numbers of set S by z0
  :param S: set type; a set of complex numbers
  :param z0: complex type; a complex number
  :return: set type; a set consisting of points in S translated by z0
  """
  # DONE: Implement this function
  # DONE: Return correct output

  print("start working problem 1...")
  # print("z0: ",z0)
  mySet = set()

  for item in S:
      # print("my item: ",item + z0)
      mySet.add(item+z0)

  return mySet


""" ----------------- PROBLEM 2 ----------------- """
def scale(S, k):
  """
  scales the complex numbers of set S by k.
  :param S: set type; a set of complex numbers
  :param k: float type; positive real number
  :return: set type; a set consisting of points in S scaled by k
  :raise: raises ValueError if k <= 0
  """
  # FIXME: Implement this function.
  # FIXME: Return correct output
  mySet = set()
  for item in S:
      mySet.add(item*k)
  return mySet


""" ----------------- PROBLEM 3 ----------------- """
def rotate(S, tau):
    """
    rotates the complex numbers of set S by tau radians.
    :param S: set type; - set of complex numbers
    :param tau: float type; radian measure of the rotation value.
                If negative, the rotation is clockwise.
                If positive the rotation is counterclockwise.
                If zero, no rotation.
    :returns: set type; a set consisting of points in S rotated by tau radians
    """

    new_set = set()
    for item in S:

        a = item.real
        b = item.imag

        z = math.sqrt((a) ** 2 + (b) ** 2)
        theta = (math.atan2(b,a))
        new_theta = tau + theta
        trigcos = round(z*math.cos(new_theta),3)
        trigsin = round(z*math.sin(new_theta),3)

        value = complex(trigcos,trigsin)

        new_set.add(value)


    print("my set1:\n", new_set)
    return new_set


""" ----------------- PROBLEM 4 ----------------- """
class Vec:
  def __init__(self, contents = []):
      """
      Constructor defaults to empty vector
      INPUT: list of elements to initialize a vector object, defaults to empty list
      """
      self.elements = contents
      return

  def __abs__(self):
      """
      Overloads the built-in function abs(v)
      :returns: float type; the Euclidean norm of vector v
      """
      # FIXME: Implement this method
      # FIXME: Return correct output
      sum = 0
      for item in self.elements:
          sum += item**2


      return math.sqrt(sum)

  def __add__(self, other):
      """
      overloads the + operator to support Vec + Vec
      :raises: ValueError if vectors are not same length
      :returns: Vec type; a Vec object that is the sum vector of this Vec and 'other' Vec
      """

      if len(self.elements) != len(other.elements):
          raise ValueError("Vectors must be of the same length for addition")

      myResult = []
      for item in range(len(self.elements)):
          print("item: ",item)
          mySub = self.elements[item] + other.elements[item]
          myResult.append(mySub)
      return Vec(myResult)

  def __sub__(self, other):
      """
      overloads the - operator to support Vec - Vec
      :raises: ValueError if vectors are not same length
      :returns: Vec type; a Vec object that is the difference vector of this Vec and 'other' Vec
      """
      # FIXME: Finish the implementation
      # FIXME: Return correct output
      if len(self.elements) != len(other.elements):
          raise ValueError("Vectors must be of the same length for addition")

      myResult = []
      for item in range(len(self.elements)):
          mySum = self.elements[item] - other.elements[item]
          myResult.append(mySum)

      return Vec(myResult)



  def __mul__(self, other):
      """
      Overloads the * operator to support
          - Vec * Vec (dot product) raises ValueError if vectors are not
            same length in the case of dot product; returns scalar
          - Vec * float (component-wise product); returns Vec object
          - Vec * int (component-wise product); returns Vec object

      """

      if type(other) == Vec: #define dot product
          # DONE: Complete the implementation
          # DONE: Return the correct output

          if len(self.elements) != len(other.elements):
              raise ValueError("Vectors must be of the same length for dot product")

          myResult = 0
          for item in range(len(self.elements)):
              mySum = self.elements[item] * other.elements[item]
              myResult += mySum
          return myResult

      elif type(other) == float or type(other) == int: #scalar-vector multiplication
          # DONE: Complete the implementation
          # DONE: Return the correct output
          myResult = []
          for item in range(len(self.elements)):
              print("other: ",other)
              mySum = self.elements[item] * other
              myResult.append(mySum)
          return Vec(myResult)


  def __rmul__(self, other):
      """
      Overloads the * operation to support
          - float * Vec; returns Vec object
          - int * Vec; returns Vec object
      """
      # DONE: Complete the implementation
      # DONE: Return the correct output
      return self.__mul__(other)



  def __str__(self):
      """returns string representation of this Vec object"""
      return str(self.elements) # does NOT need further implementation


# if __name__ == "__main__":
#     myset = {2 + 2j, 3 + 2j, 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j,
#         3 + 1j, 3.25 + 1j}
#
#
#     myvalue =3-4j
#     theta = math.cos(math.atan2(myvalue.imag,myvalue.real))
#     a = -1
#     b = 1
#
#     print("radian value: ", math.atan2(b,a))
#     myZ = math.sqrt((myvalue.real)**2 + (myvalue.imag)**2)
#     print("myZ: ",myZ)
#     print("Theta: ",theta)
#     # print("real shit: ", myvalue.real)
#     # print("imag: ",myvalue.imag)
#
#     print(complex(myZ,theta))
    # print("testing: ",(2+2j)+(3-2j))

