def basic():
  for i in range(151):
    print(i)

def mults_of_5():
  for i in range(5, 1001, 5):
    print(i)

def counting_dojo_way():
  for i in range(1, 101):
    if i % 10 == 0:
      print("Coding Dojo")
    elif i % 5 == 0:
      print("Coding")
    else:
      print(i)

def woah_that_suckers_huge():
  sum = 0
  for i in range(1, 500001, 2):
    sum += i
  print(sum)

def countdown_by_4s():
  for i in range(2018, 0, -4):
    print(i)

def flexible_counter(lowNum, highNum, mult):
  for i in range(lowNum, highNum + 1, mult):
    print(i)

basic()
mults_of_5()
counting_dojo_way()
woah_that_suckers_huge()
countdown_by_4s()
flexible_counter(2,10,2)