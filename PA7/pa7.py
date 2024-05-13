from helpers import gram_schmidt
from structures import Vec, Matrix
import numpy as np
import cmath


# ----------------------- PROBLEM 1 ----------------------- #
def qr_solve(A: Matrix, b: Vec):
  """
  Solves the system of equations Ax = b by using the
  QR factorization of Matrix A
  :param A: Matrix of coefficients of the system
  :param b: Vec of constants
  :return:  Vec solution to the system
  """
  # Constructing U
  # U should be the set of orthonormal vectors returned
  # by applying Gram-Schmidt Process to the columns of A
  print("Argument A: ")
  print(A)

  # converting A into an iterable list
  u_list = []
  a_list_col = []
  for i in range(len(A.rows)):
    curr_col = []

    for j in range(len(A.rows[0])):
      # print("i: ", i, "j: ", j)
      curr_col.append(A.rows[j][i])

    a_list_col.append(curr_col)
    u_list.append(Vec(curr_col))

  print("Transpose Col List:")
  str_T = "["
  for v in u_list:
    str_T += " Vec:" + str(v)
  str_T += " ]"
  print(str_T)

  print("b argument: ")
  print(b)
  print()

  # we apply Gram-Schimdt process to the columns of A to find matrix Q (u list)
  u = gram_schmidt(u_list)

  # find q transpose after gram schmidt function
  temp_q = []

  for vector in u:
    temp_vector = []
    for i in range(len(vector.elements)):
      temp_vector.append(vector.elements[i])
    temp_q.append(temp_vector)

  print()
  print("temp q: ")
  print(Matrix(temp_q))

  q_transpose = []
  len_u = len(u)

  for i in range(len(temp_q[0])):
    row_q_transpose = []
    for j in range(len(temp_q)):
      row_q_transpose.append(temp_q[j][i])
    q_transpose.append(row_q_transpose)

  print("q transpose:")
  print(Matrix(q_transpose))

  # matrix R (n x n matrix)
  n = len(q_transpose)  # FIXME: check if this is the right assignment number

  # 1. init size of matrix R
  matrix_R = []
  for i in range(n):
    temp_row = []
    for j in range(n):
      temp_row.append(0)
    matrix_R.append(temp_row)

  print("matrix R before calculation: ")
  print(Matrix(matrix_R))

  # for i > j == 0
  # for i <= j    < ui , aj >

  for i in range(len(matrix_R)):
    for j in range(len(matrix_R[i])):
      if i <= j:
        # i <= j    < ui , aj >
        # print("i index:", i, "j index:", j)
        # print("ui:", temp_q[i])
        # print("aj:", a_list_col[j])

        # inner product code
        value = inner_product(temp_q[i], a_list_col[j])
        matrix_R[i][j] = value
        # print("inner product val:", value)

      elif i > j:
        matrix_R[i][j] = 0
      # print()

  print("matrix R after calculation: ")
  print(Matrix(matrix_R))

  # Qt * b  ( REFER TO PAGE 29 EX 3 )

  # 1. make b vector iterable
  b_list = []
  for i in range(len(b.elements)):
    b_list.append(b.elements[i])

  # 2. multiply Qt and b
  Qtb = [0] * len(temp_q)
  if len(temp_q[0]) == len(b_list):
    for i in range(len(temp_q)):
      val = 0
      for j in range(len(temp_q[i])):
        print("i:", i, "j:", j)
        print("val = temp_q[j][i] * b_list[i]")
        print("val =", temp_q[j][i], "*", b_list[i])

        Qtb[j] += temp_q[j][i] * b_list[i]
        print("curr val or Qtb at", j, ":", Qtb[j])
        print()
      # Qtb.append(val)

  print("Qtb list:", Qtb)

  # Use Backward Sub to find x --> R_matrix(x) = Qtb
  ag_matrix = []
  for i in range(len(matrix_R)):
    row_list = []
    for j in range(len(matrix_R[i]) + 1):
      row_list.append(0)
    ag_matrix.append(row_list)

  for i in range(len(matrix_R)):
    for j in range(len(matrix_R[i])):
      ag_matrix[i][j] = matrix_R[i][j]

  for i in range(len(Qtb)):
    ag_matrix[i][len(ag_matrix[0]) - 1] = Qtb[i]

  print()

  # use backward sub to find values of x
  x = backward_sub(ag_matrix)

  # print("solution x:")
  # print(x)

  for i in range(len(x)):
    x[i] = round(x[i])

  return Vec(x)

def backward_sub(ag_matrix):
  print("ag matrix used for backward sub: ")
  print(Matrix(ag_matrix))

  n = len(ag_matrix[0]) - 1
  x_vec = []

  for i in range(n - 1, -1, -1):
    if i == n - 1:
      x_i = ag_matrix[i][n] / ag_matrix[i][i]
      print("x_i:", x_i)
    else:
      sum_total = 0
      for j in range(i + 1, n):
        sum_total += ag_matrix[i][j] * x_vec[n - 1 - j]
      x_i = (ag_matrix[i][n] - sum_total) / ag_matrix[i][i]
    x_vec.append(x_i)
  x_vec.reverse()
  # print("solution:", x_vec)
  return x_vec

def inner_product(ui, aj):

  if len(ui) == len(aj):
    product_list = []
    for i in range(len(ui)):
      product = ui[i] * aj[i]
      product_list.append(product)

    total = 0
    for item in product_list:
      total += item

    return total

  else:
    return None

# ----------------------- PROBLEM 2 ----------------------- #
def _submatrix(A: Matrix, i: int, j: int):
  """
  constructs the sub-matrix of an mxn Matrix A that
  results from omitting the i-th row and j-th column;
  i and j satisfy that 0 <= i <= m, and 0 <= j <= n
  :param A: Matrix object
  :param i: int index of row to omit
  :param j: int index of column to omit
  :return: Matrix object representing the sub-matrix
  """
  m, n = A.dim()
  if not (1 <= i <= m and 1 <= j <= n):
    raise ValueError("Invalid row or column index")

  submatrix = []
  for row_idx in range(m):
    if row_idx != (i - 1):
      subrow = []
      for col_idx in range(n):
        if col_idx != (j - 1):
          subrow.append(A.get_entry(row_idx + 1, col_idx + 1))
      if len(subrow) > 0:
        submatrix.append(subrow)

  return Matrix(submatrix)


# ----------------------- PROBLEM 3 ----------------------- #
def determinant(A: Matrix):
  """
  computes the determinant of square Matrix A;
  Raises ValueError if A is not a square matrix.
  :param A: Matrix object
  :return: float value of determinant
  """
  m, n = A.dim()
  if m != n:
    raise ValueError(
      f"Determinant is not defined for Matrix with dimension {m}x{n}.  Matrix must be square."
    )
  if n == 1:
    return A.get_entry(1, 1)
  elif n == 2:
    # For a 2x2 matrix [[a, b], [c, d]], the determinant is ad - bc
    return A.get_entry(1, 1) * A.get_entry(2, 2) - A.get_entry(1, 2) * A.get_entry(2, 1)
  else:
    d = 0
    for j in range(1, n + 1):
      # Calculate the determinant recursively using Laplace expansion
      d += ((-1) ** (1 + j)) * A.get_entry(1, j) * determinant(_submatrix(A, 1, j))
    return d


# ----------------------- PROBLEM 4 ----------------------- #
def eigen_wrapper(A: Matrix):
  """
  uses numpy.linalg.eig() to create a dictionary with
  eigenvalues of Matrix A as keys, and their corresponding
  list of eigenvectors as values.
  :param A: Matrix object
  :return: Python dictionary
  """
  # Get the dimensions of the matrix
  m, n = A.dim()

  # Convert the Matrix object to a numpy array
  A_array = np.array([[elem for elem in row] for row in A.rows])

  if m != n:
    raise ValueError("Input matrix must be square")

  if m < 1:
    raise ValueError("Input matrix must have at least one row and column")

  eigenvalues, eigenvectors = np.linalg.eig(A_array)

  # Convert the eigenvalues to a list
  eigenvalues_list = eigenvalues.tolist()

  # Convert the eigenvectors to Matrix objects
  eigenvectors = [Matrix([list(vec)]) for vec in eigenvectors.T]

  # Create a dictionary with eigenvalues as keys and corresponding eigenvectors as values
  eigen_dict = {}
  for i, val in enumerate(eigenvalues_list):
    eigen_dict[val] = eigenvectors[i]

  return eigen_dict



# ----------------------- PROBLEM 5 ----------------------- #
def svd(A: Matrix):
  """
  computes the singular value decomposition of Matrix A;
  returns Matrix objects U, Sigma, and V such that:
  1. V is the Matrix whose columns are eigenvectors of
     A.transpose() * A
  2. Sigma is a diagonal Matrix of singular values of
     A.transpose() * A appearing in descending order along
     the main diagonal
  3. U is the Matrix whose j-th column uj satisfies
     A * vj = sigma_j * uj where sigma_j is the j-th singular
     value in decreasing order and vj is the j-th column vector of V
  4. A = U * Sigma * V.transpose()
  :param A: Matrix object
  :return: tuple with Matrix objects; (U, Sigma, V)
  """
  m, n = A.dim()
  aTa = A.transpose() * A
  eigen = eigen_wrapper(aTa)
  eigenvalues = np.sort_complex(list(eigen.keys())).tolist()[::-1]

  # Constructing V
  # V should be the mxm matrix whose columns
  # are the eigenvectors of matrix A.transpose() * A
  #V = Matrix([[None for j in range(n)] for i in range(n)])

  V = Matrix([[eigen[v][j] for j in range(n)] for v in eigen])

  # for j in range(1, n + 1):
  #   pass  # FIXME: Replace this with the lines that will
  #   #        correctly build the entries of V

  # Constructing Sigma
  # Sigma should be the mxn matrix of singular values.
  singular_values = [np.sqrt(val) for val in eigenvalues]
  #        holds a list of singular values of A
  #        in decreasing order
  Sigma = Matrix([[0 for j in range(n)] for i in range(m)])
  for i in range(1, m + 1):
    Sigma.set_entry(i + 1, i + 1, singular_values[i])


  # Constructing U
  # U should be the matrix whose j-th column is given by
  # A * vj / sj where vj is the j-th eigenvector of A.transpose() * A
  # and sj is the corresponding j-th singular value
  U = Matrix([[None for j in range(m)] for i in range(m)])
  for j in range(1, m + 1):
    v_j = V.get_col(j + 1)
    u_j = (1 / singular_values[j]) * (A * Vec(v_j))
    for i in range(m):
      U.set_entry(i + 1, j + 1, u_j[i])

  return (U, Sigma, V)