
def lcm(a, b):
  """compute Least Common Multiple between two integers."""
  return abs(a*b) // math.gcd(a, b)
  pass