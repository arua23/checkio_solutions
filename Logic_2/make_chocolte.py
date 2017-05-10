def make_chocolate(small, big, goal):
  if goal>big*5:
    if goal-big*5<=small:
      return goal-big*5
    else:
      return -1
  elif goal%(5)==0 and goal//5<=big:
    return 0
  else:
    q=goal//5
    if goal-q*5>small:
      return -1
    else:
      return goal-q*5
    

print(make_chocolate(4, 1, 9))
print(make_chocolate(4, 1, 10))
print(make_chocolate(4,5,10))
print(make_chocolate(4, 1, 7))
print(make_chocolate(6, 2, 7))
print(make_chocolate(3, 1, 9))
print(make_chocolate(1, 2, 7))

print(make_chocolate(7, 1, 12))


##    else:
##      i=1
##      while i<=big:
##        if goal-5*i<=small:
##          return goal-5*i
##        i+=1
