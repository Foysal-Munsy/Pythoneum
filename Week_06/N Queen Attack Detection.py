#1
def drawBoard(P):
  N = len(P)
  for i in range(1,N+1):
    print("|", end="")
    for j in range(1,N+1):
      if (i,j) in P:
        ind = str(1+ P.index((i,j)))
        print(" "+ind+" |", end= "")
      else:
        print(" * |", end= "")
    print()

#2
import math
import random
def generate_positions(N):
    CL = list(range(0,N*N));
    P = []
    for i in range(N):
        p = random.choice(CL)
        CL.remove(p)
        r = math.ceil((p+1)/N)
        c = 1+p%N
        P.append((r,c))
        #print('Q{}: {},{}'.format(i+1,r,c))
    return P

generate_positions(4)


#3
N = 4
positions = generate_positions(N)
drawBoard(positions)

#4
# row attack
def rowAttack(P):
  n = len(P)
  count = 0
  for i in range(n):
    for j in range(i+1,n):
      if P[i][0] == P[j][0]:
        print('row attack:', end = " " )
        print(P[i], end = ", ")
        print(P[j])
        count = count + 1
  return count

rowAttack(positions)

#5
#column attack
def colAttack(P):
  n = len(P)
  count = 0
  for i in range(n):
    for j in range(i+1,n):
      if P[i][1] == P[j][1]:
        print('col attack:', end = " " )
        print(P[i], end = ", ")
        print(P[j])
        count = count + 1
  return count

colAttack(positions)

#6
# diagonal atack
def diaAttack(P):
  n = len(P)
  count = 0
  for i in range(n):
    for j in range(i+1,n):
      if abs(P[i][0] - P[j][0]) == abs(P[i][1] - P[j][1]):
        print('diagonal attack:', end = " " )
        print(P[i], end = ", ")
        print(P[j])
        count = count + 1
  return count

diaAttack(positions)

#7
# implement a method to print a state is valid or not

def isValid(P):
    if rowAttack(P) == 0 and colAttack(P) == 0 and diaAttack(P) == 0:
        return True
    else:
        return False

#8
# call isValid untill you get valid solution

def generate_new_state(N):
    return [(random.randint(0, N-1), col) for col in range(N)]

P = generate_new_state(N)

# Keep generating new states until a valid one is found.
while not isValid(P):
    P = generate_new_state(N)

print("Found a valid state:", P)


