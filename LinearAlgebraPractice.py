import LinearAlgebraPurePython as la 
# import Short_Implementation as si


print('A matrix')
A = [[5,4,3,2,1],[4,3,2,1,5],[3,2,9,5,4],[2,1,5,4,3],[1,2,3,4,5]]
la.print_matrix(A)
print()

print('A Inverse')
# AM = la.copy_matrix(A) 
# IM = la.identity_matrix(len(A))
# Inv = si.invert_matrix(AM, IM)
Inv = la.invert_matrix(A,9)
la.print_matrix(Inv)
print()

print('Check that A * Ainv = Identity Matrix')
C = la.matrix_multiply(A, Inv)
la.print_matrix(C)
print()
