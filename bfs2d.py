a = "\n".join([
 ".W.",
 ".W.",
 "..."
])

a = a.split('/n')
def make_2d (str):
  a = str.split('/n')
  new_a = []
  for x in a:
    new_a.append(list(x))
  return new_a
