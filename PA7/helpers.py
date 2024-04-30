import copy
from structures import Matrix, Vec


def norm(v: Vec, p: int):
  """
  returns the p-norm of Vec v
  INPUT:
      p - an integer determining the norm to be calculated
      v - the Vec object for which the norm will be applied
  OUTPUT:
      the norm as a float
  """
  return sum(abs(v.elements[i])**p for i in range(len(v.elements)))**(1 / p)


def is_independent(S):
  rows = [vec.elements for vec in S]
  A = Matrix(rows)
  return rank(A) == len(S)


def gram_schmidt(S):
  if not is_independent(S):
    raise ValueError("The vectors are not linearly independent")
  pass  # FIXME: COPY-PASTE YOUR IMPLEMENTATION FROM PA #6


def _ref(A: Matrix):
  pass  # FIXME: COPY-PASTE YOUR IMPLEMENTATION FROM PA #6


def rank(A: Matrix):
  pass  # FIXME: COPY-PASTE YOUR IMPLEMENTATION FROM PA #6


def frobenius_norm(A: Matrix):
  f = 0
  m, n = A.dim()
  for i in range(m):
    for j in range(n):
      f += abs(A.get_entry(i + 1, j + 1))**2
  return f**0.5


count = {
    1: 'First',
    2: 'Second',
    3: 'Third',
    4: 'Fourth',
    5: 'Fifth',
    6: 'Sixth',
    7: 'Seventh',
    8: 'Eighth',
    9: 'Ninth',
    10: 'Tenth'
}

def _pivot_idx(i: int, j: int, A: Matrix):
  """
  finds the row index >= i of the first non-zero entry
  in column j of the given Matrix.  If no non-zero entry
  exists in column j at or after row i, then None is returned.
  :param i: int type; the row index of where to begin search
  :param j: int type; the column index of where to begin search
  :param A: Matrix type; the matrix of interest
  :return: int type or None type; if int, the row index of the
           first non-zero entry in column j.
  """
  column = A.get_col(j)
  for k in range(i - 1, len(column)):
      if abs(column[k]) > 1E-6:
          return k + 1
      else:
          A.set_entry(k, j, 0)
  return None
