def bezout_coeffs(a, b):
  """
      computes the Bezout coefficients of two given positive integers
      :param a: int type; positive integer
      :param b: int type; positive integer
      :returns: dict type; a dictionary with parameters a and b as keys,
                and their corresponding Bezout coefficients as values.
      :raises: ValueError if a < 0 or b < 0
      """
  if a < 0 or b < 0:
    raise ValueError(
      f"bezout_coeffs(a, b) does not support negative arguments.")
  s0 = 1
  t0 = 0
  s1 = -1 * (b // a)
  t1 = 1

  temp = b #21
  bk = a #13
  ak = temp % a #8 -> remainder

  print(f"s1: {s1} | t1: {t1} | temp: {temp} | bk: {bk} | ak: {ak}")
  i = 0
  while ak != 0:
    temp_s = s1 #s_k-1
    temp_t = t1 #t_k-1

    # FIXME: Update s1 according to the formula for sk
    s1 = s0-s1*(bk // ak) #s_k-2

    # FIXME: Update t1 according to the formula for tk
    t1 = t0-t1*(bk//ak)

    s0 = temp_s
    t0 = temp_t
    temp = bk

    # FIXME: Update bk and ak
    bk = ak
    ak = temp % bk

    print(f"{i} -> ak: {ak} | bk: {bk}")
    i += 1

  # FIXME: Replace each string with the correct coefficients of a and b
  return {a: s0, b: t0}

if __name__ == "__main__":
  val_a = 3
  val_b = 28
  print((val_a,val_b))
  print("expected: 414: 8, 662 : 5")