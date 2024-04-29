# CECS 229 PROGRAMMING ASSIGNMENT #5
# Reyna Aguirre (030546943)
import math
# from Vec import Vec


class Vec:
    def __init__(self, contents=[]):
        """
        Constructor defaults to empty vector
        INPUT: list of elements to initialize a vector object, defaults to empty list
        """
        self.elements = contents
        return

    def __abs__(self):
        """
        Overloads the built-in function abs(v)
        returns the Euclidean norm of vector v
        """
        euclid_total = 0
        for num in self.elements:
            euclid_total += (num**2)
        euclid_total = math.sqrt(euclid_total)

        return euclid_total

    def __add__(self, other):
        """Overloads the + operator to support Vec + Vec
         raises ValueError if vectors are not same length
        """
        if len(self.elements) == len(other.elements):
            vec_add_list = []
            for i in range(len(self.elements)):
                vec_add_num = self.elements[i] + other.elements[i]
                vec_add_list.append(vec_add_num)
            return Vec(vec_add_list)
        else:
            raise ValueError()

    def __sub__(self, other):
        """
        Overloads the - operator to support Vec - Vec
        Raises a ValueError if the lengths of both Vec objects are not the same
        """
        if len(self.elements) == len(other.elements):
            vec_sub_list = []
            for i in range(len(self.elements)):
                vec_sub_num = self.elements[i] - other.elements[i]
                vec_sub_list.append(vec_sub_num)
            return Vec(vec_sub_list)
        else:
            raise ValueError()

    def __mul__(self, other):
        """Overloads the * operator to support
            - Vec * Vec (dot product) raises ValueError if vectors are not same length in the case of dot product
            - Vec * float (component-wise product)
            - Vec * int (component-wise product)
        """
        if type(other) == Vec:  # define dot product
            if len(self.elements) == len(other.elements):
                total = 0
                for i in range(len(self.elements)):
                    dot_product = self.elements[i] * other.elements[i]
                    total += dot_product
                return total
            else:
                raise ValueError()

        elif type(other) == float or type(other) == int:  # scalar-vector multiplication
            scalar_mult_num = 0.0
            scalar_mult_list = []

            for num in self.elements:
                if type(other) == int:
                    scalar_mult_num = int(other*num)
                elif type(other) == float:
                    scalar_mult_num = (other*num)
                scalar_mult_list.append(scalar_mult_num)

            return Vec(scalar_mult_list)

    def __rmul__(self, other):
        """Overloads the * operation to support
            - float * Vec
            - int * Vec
        """
        scalar_mult_num = 0
        scalar_mult_list = []
        for num in self.elements:
            scalar_mult_num = num * other
            scalar_mult_list.append(scalar_mult_num)

        return Vec(scalar_mult_list)

    def __str__(self):
        """returns string representation of this Vec object"""
        return str(self.elements)  # does NOT need further implementation

    def norm(self, p):
        if type(p) == int and p > 0:
            n = len(self.elements)
            root = p

            result_num = 0
            result_lp_norm = 0
            for i in range(n):
                temp_num = self.elements[i]

                if temp_num < 0:
                    temp_num = abs(temp_num)

                result_num = temp_num**p
                print("result num:", result_num)
                print(temp_num, "**", p, "=", temp_num**p)
                result_lp_norm += result_num

            result_lp_norm = result_lp_norm**(1/root)  # n_root of result
            # print(result_lp_norm)

            return result_lp_norm
        else:
            raise ValueError("p in not a positive int.")


class Matrix:

    def __init__(self, rowsp):
        self.rowsp = rowsp
        self.colsp = self._construct_cols(rowsp)

    def _construct_cols(self, rowsp):
        colsp = []

        num_rows = len(rowsp)
        num_cols = 0
        for row in rowsp:
            num_cols = len(row)

        temp_col_list = []
        for i in range(num_cols):
            for j in range(num_rows):
                temp_col_list_item = rowsp[j][i]
                temp_col_list.append(temp_col_list_item)
            colsp.append(temp_col_list)
            temp_col_list = []

        return colsp

    def __add__(self, other):
        if len(self.rowsp) == len(other.rowsp) and len(self.colsp) == len(other.colsp) and type(other) == Matrix:
            new_addition_matrix = []

            # initialize size of new matrix
            for i in range(len(self.rowsp)):
                new_list_item = []
                for j in range(len(self.colsp)):
                    new_list_item.append(0)

                new_addition_matrix.append(new_list_item)

            for i in range(len(self.rowsp)):
                for j in range(len(self.colsp)):
                    addition_var = (self.rowsp[i][j]) + other.rowsp[i][j]
                    new_addition_matrix[i][j] = addition_var

            return Matrix(new_addition_matrix)

        else:
            raise ValueError("Error. Matrix dimensions don't match.")

    def __sub__(self, other):
        if len(self.rowsp) == len(other.rowsp) and len(self.colsp) == len(other.colsp) and type(other) == Matrix:
            new_sub_matrix = []

            # initialize size of new matrix
            for i in range(len(self.rowsp)):
                new_list_item = []
                for j in range(len(self.colsp)):
                    new_list_item.append(0)

                new_sub_matrix.append(new_list_item)

            for i in range(len(self.rowsp)):
                for j in range(len(self.colsp)):
                    sub_var = (self.rowsp[i][j]) - other.rowsp[i][j]
                    new_sub_matrix[i][j] = sub_var

            return Matrix(new_sub_matrix)

        else:
            raise ValueError("Error. Matrix dimensions don't match.")

    def __mul__(self, other):
        if type(other) == float or type(other) == int:
            scalar_mult_matrix = []
            for i in range(len(self.rowsp)):
                scalar_mult_item = []
                for j in range(len(self.colsp)):
                    scalar_mult_var = self.rowsp[i][j] * other
                    scalar_mult_item.append(scalar_mult_var)
                scalar_mult_matrix.append(scalar_mult_item)
            return Matrix(scalar_mult_matrix)

        elif type(other) == Matrix:
            # new matrix dimensions : (self num rows) x (other num cols)
            if len(self.colsp) == len(other.rowsp):
                result_matrix = []
                for i in range(len(self.rowsp)):
                    temp = []
                    for j in range(len(other.colsp)):
                        temp.append(0)
                    result_matrix.append(temp)

                counter = 0
                while counter < len(other.colsp):
                    for i in range(len(self.rowsp)):
                        result = 0
                        for j in range(len(self.colsp)):
                            result += (other.rowsp[j][counter] * self.rowsp[i][j])
                            # print("other=", other.rowsp[j][counter], " self=", self.rowsp[i][j], end= " ")
                            # print(" counter:", counter, " i:", i, " j:", j, end=" ")
                        # print(result)
                        result_matrix[i][counter] = result
                    counter += 1

                return Matrix(result_matrix)
            else:
                raise ValueError("Error. Matrix dimensions don't match.")

        elif type(other) == Vec:
            # (m x n)(n x 1) = (m x 1)

            n = len(other.elements)

            # print("len of other:", n, end=" ")
            # print("len of self:", len(self.col_space()))

            if len(self.col_space()) == n:
                result_vec_list = []
                for i in range(len(self.rowsp)):
                    result_vec_list.append(0)
                # print(result_vec_list)
                counter = 0
                while counter < n:
                    for i in range(len(self.rowsp)):
                        result = 0
                        for j in range(len(self.colsp)):
                            if counter == j:
                                # print("counter=", counter, "i=", i, "j=", j, "matrix num=", self.rowsp[i][j])
                                # print(other.elements[counter], "*", self.rowsp[i][j], end=" ")
                                result += (other.elements[counter] * self.rowsp[i][j])
                        result_vec_list[i] += result
                    counter += 1
                return Vec(result_vec_list)

            else:
                print("incompatible dimensions")
                # raise ValueError("incompatible dimensions")

        else:
            raise ValueError("ERROR: Unsupported Type.")

    def __rmul__(self, other):
        if type(other) == float or type(other) == int:
            scalar_mult_matrix = []
            for i in range(len(self.rowsp)):
                scalar_mult_item = []
                for j in range(len(self.colsp)):
                    scalar_mult_var = self.rowsp[i][j] * other
                    scalar_mult_item.append(scalar_mult_var)
                scalar_mult_matrix.append(scalar_mult_item)
            return Matrix(scalar_mult_matrix)
        else:
            print("ERROR: Unsupported Type.")
        return

    def __str__(self):
        """prints the rows and columns in matrix form """
        mat_str = ""
        for row in self.rowsp:
            mat_str += str(row) + "\n"
        return mat_str

    def __eq__(self, other):
        """overloads the == operator to return True if
        two Matrix objects have the same row space and column space"""
        return self.row_space() == other.row_space() and self.col_space() == other.col_space()

    def __req__(self, other):
        """overloads the == operator to return True if
        two Matrix objects have the same row space and column space"""
        return self.row_space() == other.row_space() and self.col_space() == other.col_space()

    def row_space(self):
        return self.rowsp

    def col_space(self):
        return self.colsp

    def set_row(self, i, v):

        if len(v) == len(self.rowsp[0]):
            self.rowsp[i - 1] = v

            # reconstruct cols of matrix
            self.colsp = self._construct_cols(self.rowsp)
        else:
            raise ValueError("Incompatible row length.")

    def get_row(self, i):
        getter_row = self.rowsp[i]
        return getter_row

    def set_col(self, j, u):
        if len(u) == len(self.colsp[0]):
            self.colsp[j - 1] = u

            # reconstruct rows of matrix
            index = 0
            for row in self.rowsp:
                row[j - 1] = u[index]
                index += 1

        else:
            raise ValueError("Incompatible column length.")

    def get_col(self, j):
        getter_col = self.colsp[j - 1]
        return getter_col

    def set_entry(self, i, j, x):
        self.rowsp[i - 1][j - 1] = x
        self.colsp[j - 1][i - 1] = x

    def get_entry(self, i, j):
        return self.rowsp[i - 1][j - 1]

    def get_diag(self, k):
        num_rows = len(self.rowsp)
        num_cols = len(self.colsp)
        store_diagonal = []

        if k == 0:
            i = 0
            j = 0
            while i < num_rows and j < num_cols:
                store_diagonal.append(self.rowsp[i][j])
                i += 1
                j += 1

        elif k > 0:
            i = 0
            j = k

            for row in self.rowsp:
                if j > len(row) - 1:
                    break
                else:
                    store_diagonal.append(self.rowsp[i][j])
                    i += 1
                    j += 1

        elif k < 0:
            i = abs(k)
            j = 0

            for row in self.rowsp:
                if i > len(self.rowsp) - 1:
                    break
                else:
                    store_diagonal.append(self.rowsp[i][j])
                    i += 1
                    j += 1

        return store_diagonal

    def ref(self):
        """ returns ref of matrix using gaussian elimination. """

        # initialize NEW matrix with self contents
        ref_matrix = []
        for i in range(len(self.rowsp)):
            temp_row_list = []
            for j in range(len(self.colsp)):
                temp_row_list.append(self.rowsp[i][j])
            ref_matrix.append(temp_row_list)

        # print(Matrix(ref_matrix))

        for i in range(len(self.rowsp) - 1):
            prev_row = Matrix(ref_matrix).get_row(i)
            # print("prev row", prev_row, "i index:", i)

            # check if swapping is necessary (if pivot is zero)
            if i >= len(self.colsp) - 1:
                break

            if prev_row[i] == 0:
                for k in range(i+1, len(self.rowsp)):
                    if ref_matrix[k][i] != 0:
                        ref_matrix[i], ref_matrix[k] = ref_matrix[k], ref_matrix[i]
                        break
                prev_row = ref_matrix[i]

            for j in range(i+1, len(self.rowsp)):
                curr_row = Matrix(ref_matrix).get_row(j)

                if prev_row[i] == 0:
                    if i < len(self.rowsp) - 1:
                        for temp_i in range(i, len(prev_row)):
                            if prev_row[temp_i] != 0:  # special case matrix e
                                factor = curr_row[temp_i] / prev_row[temp_i]
                                # print("i:", i, "temp i:", temp_i, "element:", prev_row[temp_i], "&", curr_row[temp_i])
                                break

                    # continue
                else:
                    factor = curr_row[i] / prev_row[i]

                # print("i index:", i, "j index:", j)
                # print("factor=", factor, "(", curr_row[i], "/", prev_row[i], ")")
                # print("prev row:", prev_row, " curr row:", curr_row)
                # print()

                for k in range(len(ref_matrix[0])):
                    # print()
                    # print("k:", k)
                    # print("curr_row[k] = curr_row[k] - (factor*prev_row[k])")
                    # print("curr_row[k] =", curr_row[k], "- ", factor, "*", prev_row[k])
                    curr_row[k] = curr_row[k] - (factor*prev_row[k])
                    # print("answer:", curr_row[k])

                ref_matrix[j] = curr_row
                # print("updated row=", curr_row)
                # print()

        return Matrix(ref_matrix)

    def rank(self):
        # number of non-zero rows in ref(matrix)
        temp_matrix = self.ref()

        """ converting matrix object back to a 2d list to make it iterable """
        ref_matrix = []
        row_num = 0
        num_rows = len(self.rowsp)

        while row_num < num_rows:
            curr_row = temp_matrix.get_row(row_num)
            ref_list = []

            for j in range(len(curr_row)):
                ref_list.append(curr_row[j])

            row_num += 1
            ref_matrix.append(ref_list)

        for i in range(len(ref_matrix)):
            for j in range(len(ref_matrix[i])):
               ref_matrix[i][j] = round(ref_matrix[i][j], 2)

        # print("rank matrix in rank function:")
        # print(Matrix(ref_matrix))
`

        rank_counter = 0

        for i in range(len(ref_matrix)):
            non_zero_counter = 0
            for j in range(len(ref_matrix[0])):

                if j == len(ref_matrix[0]) - 1:  # check if last index is 0
                    # print("last index:", ref_matrix[i][j])
                    if ref_matrix[i][j] == 0 and non_zero_counter <= 1:
                        # print("this is not counted in rank")
                        non_zero_counter = 0  # set variable back to 0 to mark as linearly dependent
                    elif ref_matrix[i][j] != 0:
                        non_zero_counter += 1

                elif ref_matrix[i][j] != 0:
                    non_zero_counter += 1

            if non_zero_counter > 0:
                rank_counter += 1

        return rank_counter


# Problem 2:
def gauss_solve(A, b):
    # Ax = b

    # (m x n)(n x 1) = (m x 1)
    len_matrix = len(A.rowsp)  # n variable
    len_vec = len(b.elements)  # m variable

    # print("check:", end=" ")
    # print("length of matrix:", len_matrix, " len of vec:", len_vec)

    if len_matrix != len_vec:
        raise ValueError("dimensions do not match")
    else:
        # obtain rank of ref of matrix and ag matrix

        # rank of ref matrix
        rank_ref_a = A.rank()
        # print("rank A:", rank_ref_a)

        # rank ag matrix
        # init matrix size of ag and append all 0's
        ag_matrix = []
        for i in range(len_matrix):
            row_list = []
            for j in range(len(A.colsp) + 1):
                row_list.append(0)
            ag_matrix.append(row_list)
        # print(Matrix(ag_matrix))


        # converting matrix object back to a 2d list to make it iterable
        # converting vec object back to a list to make it iterable
        temp_matrix = []
        for i in range(len(A.rowsp)):
            row_list = []
            for j in range(len(A.colsp)):
                row_list.append(A.rowsp[i][j])
            temp_matrix.append(row_list)

        vec_list = []
        for num in b.elements:
            vec_list.append(num)
        # print("vec list:", vec_list)


        # fill ag matrix with contents of ref matrix
        for i in range(len_matrix):
            for j in range(len(A.colsp)):
                ag_matrix[i][j] = temp_matrix[i][j]

        for i in range(len(vec_list)):
            # print("[", i, "]", "[", len(ag_matrix[0]) - 1, "]")
            ag_matrix[i][len(ag_matrix[0]) - 1] = vec_list[i]

        ref_ag = Matrix(ag_matrix).ref()
        rank_ag = ref_ag.rank()
        # print("matrix after storing vec list")
        # print(Matrix(ag_matrix))
        # print()
        #
        # print("matrix after rank function ")
        # print(ref_ag)
        # print("rank AG:", rank_ag)
        # print("rank A:", rank_ref_a)


        """" Number of Solutions Find """

        # 1. if rank(ref(A)) < rank(Ag) --> no solution
        if rank_ref_a < rank_ag:
            # print("NO SOLUTION")
            return None

        elif rank_ref_a == rank_ag:  # FIXME: update later

            num_variables = len(temp_matrix[0])  # counting the amount of columns in matrix
            # print("rank_ref_a == rank_ag", "   num variables:", num_variables)

            # check if all of last column is 0.
            # 2. if rank(ref(A)) = rank(Ag) < n --> inf many solutions
            if rank_ag < num_variables:

                # k (free variables) = num  variables - rank(A)
                k = num_variables - rank_ref_a
                # print("INF MANY SOLUTIONS")
                return k

            # 2. if rank(ref(A)) = rank(Ag) = n --> one solution
            elif rank_ag == num_variables:
                # print("ONE SOLUTION")
                # print(ref_ag)

                # solve for transpose vector solution with backward sub

                solution = []
                for i in range(num_variables - 1, -1, -1):
                    if i == num_variables - 1:
                        x_i = ref_ag.rowsp[i][num_variables] / ref_ag.rowsp[i][i]
                    else:
                        sum_total = 0
                        for j in range(i + 1, num_variables):
                            sum_total += ref_ag.rowsp[i][j] * solution[num_variables - 1 - j]
                        x_i = (ref_ag.rowsp[i][num_variables] - sum_total) / ref_ag.rowsp[i][i]
                    solution.append(x_i)

                solution.reverse()
                # print("solution check:", solution)
                flag = 0
                for item in solution:
                    if abs(item) != 0.0:
                        flag += 1

                if flag != 0:
                    return Vec(solution)
                else:
                    return None

        # for is_independent funct
        # print("for is_independent funct....")
        """ example:    S1 = [Vec([1, 2]), Vec([2, 3]), Vec([3, 4])]
                        sol1 = is_independent(S1)
                        print("S1 is Independent:", sol1)
                        print("Expected: False")
        """
        free_variables_counter_list = []
        for i in range(len(ref_ag.rowsp)):
            free_variables_counter = 0
            for j in range(len(ref_ag.colsp) - 1):
                if ref_ag.rowsp[i][j] != 0:  # count non zeros
                    free_variables_counter += 1
            free_variables_counter_list.append(free_variables_counter)
        # print(free_variables_counter_list)

        # FIXME: unsure if right algorithm

        for item in free_variables_counter_list:
            if item == 0:  # means linearly dependent
                pass

        unique_counter = 0
        for leading_i in range(len(ref_ag.colsp) - 1, -1, -1):
            non_zero_counter = 0
            for leading_j in range(len(ref_ag.rowsp) - 1, -1, -1):
                # print(ref_ag.rowsp[leading_j][leading_i], end=" ")
                if ref_ag.rowsp[leading_j][leading_i] != 0:
                    non_zero_counter += 1
            # print()
            if non_zero_counter != 0:
                unique_counter += 1
        # print("unique_counter:", unique_counter, "  ==  ", len(ref_ag.rowsp) - 1)
        if unique_counter == len(ref_ag.rowsp) - 1 or unique_counter < len(ref_ag.rowsp) - 1 :
            # print("unique solution, each variable has a coefficent in one of the columns")


            # perform backward sub
            # solve for transpose vector solution with backward sub

            variables_counter = len(ref_ag.rowsp[0]) - 1
            # print("variables counter:", variables_counter)
            unique_solution = []

            for temp_i in range(variables_counter -1, -1, -1):
                if temp_i == variables_counter - 1:
                    x = ref_ag.rowsp[temp_i][variables_counter] / ref_ag.rowsp[temp_i][temp_i]
                else:
                    sum_total = 0
                    for j in range(temp_i + 1, variables_counter):
                        sum_total += ref_ag.rowsp[temp_i][j] * unique_solution[variables_counter - 1 - j]
                    x = (ref_ag.rowsp[temp_i][variables_counter] - sum_total) / ref_ag.rowsp[temp_i][temp_i]
                unique_solution.append(x)

            unique_solution.reverse()

            # print("solution:", unique_solution)

            return Vec(unique_solution)
        return None


# Problem 3:
def is_independent(S):
    # Input will be a list of Vec objects instead of a set

    # make list of vectors into matrix
    temp_matrix = []
    for vector in S:
        row_list = []
        for i in range(len(vector.elements)):
            row_list.append(vector.elements[i])
        temp_matrix.append(row_list)

    # make a vec object to pass into gauss_solve function
    num_rows = len(temp_matrix)
    vec_list = []
    for i in range(num_rows):
        vec_list.append(0)
    # print("vec matrix:")
    # print(Matrix(temp_matrix))
    # print("vec list:", vec_list)

    sol = gauss_solve(Matrix(temp_matrix), Vec(vec_list))

    if sol == None:
        # print("linearly INDEPENDENT")
        # print()
        return True
    else:
        print("linearly dependent")
        return False


# Problem 4:
def gram_schmidt(S):
    # Input and output will be lists of Vec objects instead of sets

    # Input: List of linearly independent vectors

    result = is_independent(S)
    if result is False:
        raise ValueError



    # make list of vectors into iterable lists of lists
    temp_vec_list = []
    for vector in S:
        temp_vec = []
        for i in range(len(vector.elements)):
            temp_vec.append(vector.elements[i])
        temp_vec_list.append(temp_vec)

    # print("initialization of vec list:", temp_vec_list)
    # print()

    for i in range(len(temp_vec_list)):
        for j in range(i):
            # print("i:", i, "j:", j)
            # print("before proj:", temp_vec_list)
            proj = projection(temp_vec_list[j], temp_vec_list[i])
            temp_vec_list[i] = proj

        #     print("updated ", temp_vec_list)
        #
        #     print()
        # print()

    # u = ( 1 / || w || )* w
    u_list = [0]*len(temp_vec_list)
    for k in range(len(temp_vec_list)):
        denominator = 0
        for j in range(len(temp_vec_list[0])):
            denominator += temp_vec_list[k][j]*temp_vec_list[k][j]
        denominator = denominator**0.5  # square root

        if denominator == 0:
            factor = 0
        else:
            factor = 1/denominator

        for m in range(len(temp_vec_list[0])):
            # print("temp_vec_list[k][m] BEFORE:", temp_vec_list[k][m], "   k:", k, "m:", m)
            temp_vec_list[k][m] = temp_vec_list[k][m]*factor
            # print("temp_vec_list[k][m]:", temp_vec_list[k][m])

        # print()


    # convert back to list of Vec objects
    orthogonal_list = []
    for i in range(len(temp_vec_list)):
        orthogonal_list.append(Vec(temp_vec_list[i]))

    # print("returning orthogonal list from gram schmidt funct")

    return orthogonal_list


def projection(w_vector, x_vector):
    # print("~")
    # print("x vector:", x_vector, "w vector:", w_vector)
    len_vector = len(w_vector)

    numerator = 0  # < x2, w1 >
    denominator = 0  # < w1, w1 >

    for i in range(len_vector):
        numerator += (w_vector[i]*x_vector[i])
        denominator += (w_vector[i]**2)

    if denominator == 0:
        factor = 0
    else:
        factor = numerator/denominator

    # temp_w_vector = factor * w_vector
    temp_w_vector = [0]*len_vector
    for i in range(len_vector):
        temp_w_vector[i] = w_vector[i]*factor

    # w_vector = x_vector - w_vector
    temp_vector = [0]*len_vector

    for i in range(len_vector):
        temp_vector[i] = x_vector[i] - (temp_w_vector[i])

    # print("factor:", numerator, "/", denominator, "=", factor)
    # print(x_vector, "-", temp_w_vector, "=", temp_vector)
    # print("~")

    return temp_vector



# def main():
#
#     # A = Matrix([[-13, -13, -17,  -8,   5,  -1, -13,  19],[-19, -11,  17,  -9,   4,  -7,  -8,   2],[-18,  -6, -19,  -2,  -7, -10,  19, -15],[-26, -26, -34, -16,  10,  -2, -26,  38],[ 15, -10,  -5,  45,  75, -55, -50, -65],[  3,  -2,  -1,   9,  15, -11, -10, -13],[  9,  13,  10, -19,  -5, 1,   4, -17]])
#     # B = Matrix([[11, 9, -20, 10, 9, -1, -10, -15], [9, 7, -17, 14, 17, -9, -16, -15], [6, -7, -7, 1, -15, -16, -16, -1], [53, -87, -88, -9, -145, -162, -146, -4], [20, 10, -20, -20, -1, 2, 17, 1], [10, -4, 3, -12, 0, 14, -18, 10], [-7, -17, -18, -19, 5, -2, 14, 6], [4, 11, 7, 1, -7, 15, -16, 13]])
#     #
#     # temp3 = Matrix([[20,  -7,   0,  11,  -7,   7],
#     #                 [6,  11, -10,  -5, -20,  16],
#     #                 [-14,  12,   6, -15, -13,   1]])
#     #
#     # temp4 = Matrix([[ -16,    9,   -7,   11,    9,  -12,   -7,   -1],
#     #                [ 0,    2,    1,  -10,  -17,   19,    3,  -15],
#     #                [ 0,   15,   -1,    1,   -4,   8,   -1,   18],
#     #                [ -34,   98,   43, -137, -118,  109, -14, -114],
#     #                [-14,   26,   15,  -73, -142,  161,   34, -122],
#     #                [ 0,   33,    8,  -89, -157,  179,   26, -117],
#     #                [ -14,   10,    7,    7,   -6,    9,  10,   -2],
#     #                [5,  -18,   -7,   16,   -6,   13,   12,   -2]])
#     #
#     # temp5 = Matrix([[167,    13,   167,  -161],
#     #                 [ -3,     3,    17,    19],
#     #                 [-4,    20,    -7,     0],
#     #                 [16,    11,    10,   -11],
#     #                 [-1336,  -104, -1336,  1288],
#     #                 [17,     1,    15,   -18]])
#     #
#     # temp3sol = temp3.rank()
#     # print(temp3sol)
#     #
#     # temp = Matrix([[16, -18, 18, 7, 19, -10],
#     #                [6, 16, -20, -19, 8, -9],
#     #                [-3, -5, 12, 20, -11, -8],
#     #                [1, -4, -16, -12, 11, -20],
#     #                [-5, -3, -12, -2, -3, -5],
#     #                [-15, -3, 5, 11, -11, -7],
#     #                [19, -3, -20, 3, -6, -2],
#     #                [9, 0, 20, 18, -17, -7],
#     #                [-14, 5, 3, -5, 7, 14]])
#     # temp_vec = Vec([-162, 390, -162, 377, 142, 15, -56, -375, 92])
#     # temp_sol = gauss_solve(temp, temp_vec)
#     # print(temp_sol)
#     # print("Expected: [-9.000000000000016, 7.000000000000008, -9.000000000000018, 2.977755167447311e-14, 10.00000000000003, -7.999999999999991]")
#     # print()
#
#     # temp1 = Matrix([[8, 7, -5, 15, 6],
#     #                [-5, 7, -2, -20, 12],
#     #                [-7, -7, -9, -8, 19],
#     #                [-1, 6, 18, -14, 9],
#     #                [-5, -1, -1, -4, -10]])
#     # temp_vec1 = Vec([-112, 299, 188, 252, -29])
#     # temp_sol1 = gauss_solve(temp1, temp_vec1)
#     # print(temp_sol1)
#     # print("Expected: [-0.9999999999998792, 1.9999999999999503, 1.999999999999986, -10.000000000000046, 7.0]")
#
#
#     # # S = [Vec([-6, -10, 2, -5]), Vec([-7, -5, 10, 9]), Vec([-10, 8, -4, -1]), Vec([-6, -7, 9, -5])]
#     # # T = gram_schmidt(S)
#     # # str_T = "["
#     # for v in T:
#     #     str_T += str(v) + 'T '
#     # str_T += "]"
#     # print(str_T)
#     #
#     # print()
#
#     # """TESTER CELL #2 FOR GRAM SCHMIDT"""
#     # S = [Vec([20, 32, -12]), Vec([10, 16, -6]), Vec([5, 8, -3])]
#     # try:
#     #     T = gram_schmidt(S)
#     #     print("INCORRECT: ValueError was not raised.")
#     # except ValueError:
#     #     print("CORRECT: ValueError was raised.")
#
#     """ Determining Dependency """
#
#     # S = [Vec([16, 12, -14, 10, -8, -11]), Vec([-8, 5, 6, 3, 18, -1]), Vec([9, 16, -5, -19, 9, 10]), Vec([11, -4, -3, -14, 9, 11]), Vec([-2, -18, -15, 9, -18, -18]), Vec([-4, -5, 10, -15, 17, 13])]
#     S = [Vec([-7, -6, 14, 14, 5, 20]), Vec([-5, 19, -9, 13, -3, -14]), Vec([50, 40, -60, -90, -70, -100]),
#          Vec([10, 8, -12, -18, -14, -20]), Vec([14, 12, -28, -28, -10, -40]), Vec([-11, 6, 6, -7, -12, -2])]
#     # S_sol = is_independent(S)
#     # print(S_sol)
#
#
# main()