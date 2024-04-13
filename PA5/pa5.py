from Vec import Vec

"""-------------------- PROBLEM 1 --------------------"""
class Matrix:

    def __init__(self, rows):
        """
        initializes a Matrix with given rows
        :param rows: the list of rows that this Matrix object has
        """
        self.rows = rows
        self.cols = []
        self._construct_cols()
        # self._construct_rows()
        return

    """
  INSERT MISSING SETTERS AND GETTERS HERE
  """

    #SETTER METHOD
    def set_row(self,i, new_row):
        pass


    def set_col(self,j,new_col):
        pass

    def set_entry(self,i,j,val):
        pass

    #GET METHOD
    def get_row(self,i):
        return self.rows[i-1]

    def get_col(self,j):
        return self.cols[j-1]

    def get_entry(self,i,j):
        return self.rows[i][j]

    def get_colums(self):
        return self.rows

    def get_rows(self):
        return self.cols


    def get_diag(self,k):


    def _construct_cols(self):
        """
        HELPER METHOD: Resets the columns according to the existing rows
        """
        self.cols = []
        # print("my self col: ",self.cols)
        # print("\n my len list0: ",len(self.rows[0]))
        # print("\n my len array: ",len(self.rows))

        num_Column = len(self.rows[0])
        num_Row = len(self.rows)

        for i in range(num_Column):
            innerList = []
            for j in range(num_Row):
                innerList.append(self.rows[j][i])
            self.cols.append(innerList)

        # DONE: INSERT YOUR IMPLEMENTATION HERE

        #return self._cols

    def _construct_rows(self):
        """
        HELPER METHOD: Resets the rows according to the existing columns
        """
        num_Column = len(self.cols[0])
        num_Row = len(self.rows)
        self.rows = []
        # FIXME: INSERT YOUR IMPLEMENTATION HERE

        for i in range(num_Row):
            innerList = []
            for j in range(num_Column):
                innerList.append(self.cols[j][i])
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
        pass  # FIXME: REPLACE WITH IMPLEMENTATION

    def __sub__(self, other):
        """
        overloads the - operator to support Matrix - Matrix
        :param other:
        :raises: ValueError if the Matrix objects have mismatching dimensions
        :raises: TypeError if other is not of Matrix type
        :return: Matrix type; the Matrix object resulting from Matrix - Matrix operation
        """
        pass  # FIXME: REPLACE WITH IMPLEMENTATION

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
        if type(other) == float or type(other) == int:
            print("FIXME: Insert implementation of MATRIX-SCALAR multiplication"
                  )  # FIXME: REPLACE WITH IMPLEMENTATION
        elif type(other) == Matrix:
            print("FIXME: Insert implementation of MATRIX-MATRIX multiplication"
                  )  # FIXME: REPLACE WITH IMPLEMENTATION
        elif type(other) == Vec:
            print("FIXME: Insert implementation for MATRIX-VECTOR multiplication"
                  )  # FIXME: REPLACE WITH IMPLEMENTATION
        else:
            raise TypeError(f"Matrix * {type(other)} is not supported.")
        return

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
        if type(other) == float or type(other) == int:
            print("FIXME: Insert implementation of SCALAR-MATRIX multiplication"
                  )  # FIXME: REPLACE WITH IMPLEMENTATION
        else:
            raise TypeError(f"{type(other)} * Matrix is not supported.")
        return

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

    def __str__(self):
        """prints the rows and columns in matrix form """
        mat_str = ""
        for row in self.rows:
            mat_str += str(row) + "\n"
        return mat_str

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


"""-------------------- PROBLEM 2 --------------------"""


def rotate_2Dvec(v: Vec, tau: float):
    """
    computes the 2D-vector that results from rotating the given vector
    by the given number of radians
    :param v: Vec type; the vector to rotate
    :param tau: float type; the radians to rotate by
    :return: Vec type; the rotated vector
    """
    pass  # FIXME: REPLACE WITH IMPLEMENTATION
