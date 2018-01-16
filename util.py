__all__ = ['xor', 'randombytes']

def xor(s, t):
  output = []
  if len(s) != len(t): raise ValueError('Cannot xor strings of unequal length')
  return bytes([x^y for (x,y) in zip(s,t)])

def randombytes(n):
  return open('/dev/urandom', 'rb').read(n)
