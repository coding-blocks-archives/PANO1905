def gen_dec(char):
  def dec(fn):
    def wrapper(*args, **kwargs):
      print(char * 10)
      fn(*args, **kwargs)
      print(char * 10)
    return wrapper
  return dec

@gen_dec("#")
def add(a, b):
  print(a+b)

add(1, 2)