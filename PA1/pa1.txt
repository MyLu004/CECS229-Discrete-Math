""" ---------------- PROBLEM 1 ----------------"""
def equiv_to(a, m, low, high):
    k_low = (low - a)//m
    k_high = (high - a)//m
    k_vals = list(range(k_low, k_high + 1))
    x_vals = []
    for i in k_vals:
        if low <= (m*i+a) <= high:
            x_vals.append(m*i+a)
    return x_vals

""" ---------------- PROBLEM 2 ----------------"""
def b_rep(n, b):
    print("it went here")
    digits = [] # stores the digits of the b-representation of n
    q = n
    k = 0
    while q != 0:
        digit = q - ((q // b)*b)
        if b == 16 and digit > 9:
            hex_dict = {10: 'A', 11 : 'B', 12: 'C', 13: 'D', 14: 'E', 15 : 'F'}
            if digit in hex_dict:
                digit = hex_dict[digit]

        digits.append(digit)
        q = q // b
        k += 1
    myStr = map(str, digits[::-1])
    result = ''.join(myStr)
    # print("my result: ",result)
    return  result

""" ---------------- PROBLEM 3 ----------------"""
def binary_add(a, b):
    # removing all whitespace from the strings
    a = a.replace(' ', '')
    b = b.replace(' ', '')

    myList = ""
    # padding the strings with 0's so they are the same length
    if len(a) < len(b):
        diff = len(b) - len(a)
        a = "0" * diff + a
    elif len(a) > len(b):
        diff = len(a) - len(b)
        b = "0" * diff + b

    # addition algorithm
    result = ""
    carry = 0
    for i in reversed(range(len(a))):
        a_i = int(a[i])
        b_i = int(b[i])
        result = (a_i+b_i+carry) %2
        carry = (a_i+b_i+carry) //2
        # print('my carry: ',carry)

        # myList.append(result)
        myList += str(result)
    if carry == 1:
        # FIXME: remove
        # print('carry: ', carry)
        myList += str(carry)
        # myList.append(carry)

    return myList[::-1]
    # return  # FIXME return the appropriate string

""" ---------------- PROBLEM 4 ----------------"""
def binary_mul(a, b):

    # removing all whitespace from the strings
    a = a.replace(' ', '')
    b = b.replace(' ', '')

    # multiplication algorithm
    partial_products = []
    i = 0  # index of the current bit of string 'a' beginning at 0, right-to-left
    for bit in reversed(a):
        # print("bit: ",bit)
        # print("my i: ",i)
        if bit == '1':
            # print("my_bit: ",bit)
            my_val = b + "0"*i
            partial_products.append(my_val)
        i += 1
    # print("my partial product: ",partial_products)
    # print("my len partial product: ",len(partial_products))
    result = '0'

    #adding number
    while len(partial_products) > 0:
        result = binary_add(result,partial_products[0])
        print("my result: ",result)
        del partial_products[0]
    return  result


# if __name__ == "__main__":
#     va1 = 491
#     base  = 16
#     b_rep(va1,base)