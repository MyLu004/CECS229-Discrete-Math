import copy


class Vec:

  def __init__(self, contents=None):
    """
    constructor defaults to empty vector
    accepts list of elements to initialize a vector object with the
    given list
    """
    if contents is None:
      contents = []
    self.elements = contents
    return

  def __abs__(self):
    """Overloads the built-in function abs(v)
            returns the Euclidean norm of vector v
        """
    return sum([e**2 for e in self.elements])**0.5

  def __add__(self, other):
    """Overloads the + operation to support Vec + Vec
         raises ValueError if vectors are not same length
        """
    if type(other) != Vec:
      raise ValueError(f"Vec + {type(other)} is not defined.")
    if len(self.elements) == len(other.elements):
      n = len(self.elements)
      return Vec([self.elements[i] + other.elements[i] for i in range(n)])
    else:
      raise ValueError("ERROR: Vectors must be same length")

  def __mul__(self, other):
    """Overloads the * operator to support
            - Vec * Vec (dot product) raises ValueError if vectors are not same length in the case of dot product
            - Vec * float (component-wise product)
            - Vec * int (component-wise product)

        """
    if type(other) == Vec:  # define dot product
      if len(self.elements) == len(other.elements):
        n = len(self.elements)
        return sum([self.elements[i] * other.elements[i] for i in range(n)])
      else:
        raise ValueError("ERROR: Vectors must be same length")
    elif type(other) == float or type(other) == int or type(
        other) == complex:  # scalar-vector multiplication
      return Vec([x * other for x in self.elements])
    else:
      raise ValueError(f"Vec * {type(other)} is not supported.")

  def __rmul__(self, other):
    """Overloads the * operation to support
            - float * Vec
            - int * Vec
        """
    if type(other) == float or type(other) == int or type(other) == complex:
      return Vec([x * other for x in self.elements])
    else:
      raise ValueError(
          f"ERROR: {type(other)} * {type(self)} is not supported.")

  def __truediv__(self, other):
    if type(other) == complex or type(other) == int or type(other) == float:
      return Vec([x / other for x in self.elements])
    else:
      raise ValueError(f"Vec / {type(other)} is not defined.")

  def __str__(self):
    """returns string representation of this Vec object"""
    return str(self.elements)  # does NOT need further implementation

  def __sub__(self, other):
    if len(self.elements) == len(other.elements):
      n = len(self.elements)
      return Vec([self.elements[i] - other.elements[i] for i in range(n)])
    else:
      raise ValueError("ERROR: Vectors must be same length")

  def __getitem__(self, i):
    return self.elements[i]

  def __eq__(self, other):
    return self.elements == other.elements

  def norm(self, p):
    return sum([(abs(x)**p) for x in self.elements])**(1 / p)

  def dim(self):
    return len(self.elements)


class Matrix:

  def __init__(self, rows=[]):
    self.rows = rows
    self.cols = []
    self._set_cols()
    return

  # def dim(self):
  #   m = len(self.rows)
  #   n = len(self.cols)
  #   return (m, n)

  def _set_cols(self):
    """HELPER METHOD: Resets the column space according to the existing row space"""
    self.cols = []
    n = len(self.rows[0])
    m = len(self.rows)
    for j in range(n):
      col = []
      for i in range(m):
        col.append(self.rows[i][j])
      self.cols.append(col)
    return

  def _set_rows(self):
    """HELPER METHOD: Resets the row space according to the existing column space"""
    self.rows = []
    n = len(self.cols)
    m = len(self.cols[0])
    for i in range(m):
      row = []
      for j in range(n):
        row.append(self.cols[j][i])
      self.rows.append(row)

  def transpose(self):
    return Matrix(copy.deepcopy(self.cols))

  def __str__(self):
    """returns string representation of this Matrix object"""
    return str(self.rows)  # does NOT need further implementation

  def set_entry(self, i, j, val):
    self.rows[i - 1][j - 1] = val
    self._construct_cols()
    self._construct_rows()

  # GETTER METHOD
  def get_row(self, i):
    return self.rows[i - 1]

  def get_col(self, j):
    return self.cols[j - 1]

  def get_entry(self, i, j):
    return self.rows[i - 1][j - 1]

  def get_columns(self):
    return self.cols

  def get_rows(self):
    return self.rows

  def get_diag(self, k):
    myList = []

    num_rows = len(self.rows)
    num_cols = len(self.cols)
    if k == 0:
      for i in range(min(num_rows, num_cols)):
        # print("time running: ",len(self.rows[0]) - k)
        # print("dig0 [i]: ",i)
        # print("my dig0 value: ",self.rows[i][i])
        myList.append(self.rows[i][i])

    if k > 0:
      for i in range(min(num_rows, num_cols - k)):
        myList.append(self.rows[i][i + k])

    if k < 0:
      for i in range(min(num_rows + k, num_cols)):
        myList.append(self.rows[i - k][i])
    return myList

  def _construct_cols(self):
    """
    HELPER METHOD: Resets the columns according to the existing rows
    """
    self.cols = []
    # print("my self col: ",self.cols)
    # print("\n my len list0: ",len(self.rows[0]))
    # print("\n my len array: ",len(self.rows))

    num_Column = len(self.rows[0])

    for i in range(num_Column):
      innerList = []
      for j in self.rows:
        innerList.append(j[i])
      self.cols.append(innerList)

    # DONE: INSERT YOUR IMPLEMENTATION HERE

  def _construct_rows(self):
    """
    HELPER METHOD: Resets the rows according to the existing columns
    """
    num_Row = len(self.cols[0])
    self.rows = []
    # DONE: INSERT YOUR IMPLEMENTATION HERE

    for i in range(num_Row):
      innerList = []
      for j in self.cols:
        innerList.append(j[i])
      self.rows.append(innerList)

    print("my row1: ")
    print(self.rows)
    return

  def __add__(self, other):
    """
    overloads the + operator to support Matrix + Matrix
    :param other: the other Matrix object
    :raises: ValueError if the Matrix objects have mismatching dimensions
    :raises: TypeError if other is not of Matrix type
    :return: Matrix type; the Matrix object resulting from the Matrix + Matrix operation
    """
    # DONE: REPLACE WITH IMPLEMENTATION
    myList = []
    if len(self.rows) == len(other.rows) and len(self.cols) == len(other.cols):
      # implement the function
      for i in range(len(self.rows)):
        innerList = []
        for j in range(len(self.cols)):
          innerList.append(self.rows[i][j] + other.rows[i][j])
        myList.append(innerList)
      return Matrix(myList)
    else:
      raise ValueError

  def __sub__(self, other):
    """
    overloads the - operator to support Matrix - Matrix
    :param other:
    :raises: ValueError if the Matrix objects have mismatching dimensions
    :raises: TypeError if other is not of Matrix type
    :return: Matrix type; the Matrix object resulting from Matrix - Matrix operation
    """
    # DONE: REPLACE WITH IMPLEMENTATION

    myList = []
    if len(self.rows) == len(other.rows) and len(self.cols) == len(other.cols):
      # implement the function
      for i in range(len(self.rows)):
        innerList = []
        for j in range(len(self.cols)):
          innerList.append(self.rows[i][j] - other.rows[i][j])
        myList.append(innerList)
      return Matrix(myList)
    else:
      raise ValueError

  def __mul__(self, other):
    """
    overloads the * operator to support
        - Matrix * Matrix
        - Matrix * Vec
        - Matrix * float
        - Matrix * int
    :param other: the other Matrix object
    :raises: ValueError if the Matrix objects have mismatching dimensions
    :raises: TypeError if other is not of Matrix type
    :return: Matrix type; the Matrix object resulting from the Matrix + Matrix operation
    """

    myList = []
    if type(other) == float or type(other) == int:
      print("Insert implementation of MATRIX-SCALAR multiplication")
      print("other value scalar: ", other)
      # implement the function
      for i in range(len(self.rows)):
        innerList = []
        for j in range(len(self.cols)):
          innerList.append(self.rows[i][j] * other)
        myList.append(innerList)


    elif type(other) == Matrix:
      print("Insert implementation of MATRIX-MATRIX multiplication")

      if len(self.cols) != len(other.rows):
        raise ValueError

      for i in range(len(self.rows)):
        innerList = []
        for j in range(len(other.cols)):
          result = 0
          for k in range(len(self.cols)):
            result += self.rows[i][k] * other.rows[k][j]
          innerList.append(result)

        myList.append(innerList)

    elif type(other) == Vec:
      print("Insert implementation for MATRIX-VECTOR multiplication")
      if len(self.cols) != len(other):
        raise ValueError
      for i in range(len(self.rows)):
        result = 0
        for j in range(len(self.cols)):
          result += self.rows[i][j] * other[j]
        myList.append(result)

      return Vec(myList)

    else:
      raise TypeError(f"Matrix * {type(other)} is not supported.")

    return Matrix(myList)

  def __rmul__(self, other):
    """
    overloads the * operator to support
        - float * Matrix
        - int * Matrix
    :param other: the other Matrix object
    :raises: ValueError if the Matrix objects have mismatching dimensions
    :raises: TypeError if other is not of Matrix type
    :return: Matrix type; the Matrix object resulting from the Matrix + Matrix operation
    """
    myList = []
    if type(other) == float or type(other) == int:
      print("FIXME: Insert implementation of SCALAR-MATRIX multiplication"
            )
      for i in range(len(self.rows)):
        innerList = []
        for j in range(len(self.cols)):
          innerList.append(self.rows[i][j] * other)
        myList.append(innerList)
    else:
      raise TypeError(f"{type(other)} * Matrix is not supported.")
    return Matrix(myList)

  '''-------- ALL METHODS BELOW THIS LINE ARE FULLY IMPLEMENTED -------'''

  def dim(self):
    """
    gets the dimensions of the mxn matrix
    where m = number of rows, n = number of columns
    :return: tuple type; (m, n)
    """
    m = len(self.rows)
    n = len(self.cols)
    return (m, n)

  def __eq__(self, other):
    """
    overloads the == operator to return True if
    two Matrix objects have the same row space and column space
    """
    if type(other) != Matrix:
      return False
    this_rows = [round(x, 3) for x in self.rows]
    other_rows = [round(x, 3) for x in other.rows]
    this_cols = [round(x, 3) for x in self.cols]
    other_cols = [round(x, 3) for x in other.cols]

    return this_rows == other_rows and this_cols == other_cols

  def __req__(self, other):
    """
    overloads the == operator to return True if
    two Matrix objects have the same row space and column space
    """
    if type(other) != Matrix:
      return False
    this_rows = [round(x, 3) for x in self.rows]
    other_rows = [round(x, 3) for x in other.rows]
    this_cols = [round(x, 3) for x in self.cols]
    other_cols = [round(x, 3) for x in other.cols]

    return this_rows == other_rows and this_cols == other_cols

  #FIXME: COPY AND PASTE THE REST OF YOUR MATRIX METHODS HERE
