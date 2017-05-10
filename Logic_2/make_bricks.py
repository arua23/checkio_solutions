def make_bricks(small, big, goal):
  if goal//5<=big:
      if goal-(goal//5)*5<=small:
          return True
  else:
      if goal-5*big<=small:
          return True
  return False

print(make_bricks(3, 1, 8))
print(make_bricks(3, 2, 10))
print(make_bricks(3, 1, 9))
print(make_bricks(7,1,12))
print(make_bricks(7,1,13))
