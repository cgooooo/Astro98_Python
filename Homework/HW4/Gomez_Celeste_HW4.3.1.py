#3.1

matrix = [[0 for x in range(5)] for x in range(5)]

num = 1
for i in range(5):
    for j in range(5):
        matrix[i][j] = num
        num += 1


for row in matrix:
    print(row)

#Errors
            
# 1) line 8
#    biglist(i,j) = num
#SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
    ### changed (i,j) to (i)(j)
            
# 2) biglist(i)(j)) = num
#SyntaxError: unmatched ')'
    ### got rid of extra parentheses
    
#3) File "<stdin>", line 1
#SyntaxError: invalid syntax
    ###