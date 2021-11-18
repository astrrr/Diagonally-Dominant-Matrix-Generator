from random import randrange

# ex formatt = 3x3 ={{5,1,2},
#                    {1,5,2},
#                    {1,2,5},} 

#input dimension matrix
print('enter dimension of matrix')
k = int(input())
j = k

mat = []


#generate matrix

for indexj in range(j):
    mat.append([])
    for indexk in range(k):
        mat[indexj].append(randrange(1,5))

print(mat)

for indexj in range(j):
    for indexk in range(k):
        if indexj == indexk:
            mat[indexj][indexk] = sum(mat[indexj])+1

#formatting matrix
print(mat)