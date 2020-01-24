from linearAlgebra import Matrix


A = Matrix(dims=(3,3), fill=1.0)
B = Matrix(dims=(3,3), fill=2.0)


# Test 01
C = A + B
print('Left add (Matrix-Matrix):')
print(C)


# Test 02
C = A + 10.0
print('Left add (Matrix-Scalar):')
print(C)

# Test 03
C = 20.0 + A
print('Right add:')
print(C)


# Test 04
C = A @ B
print('Standard multiplication (Matrix-Matrix):')
print(C)

# Test 05
C = A * B
print('point-wise multiplication (Matrix-Matrix):')
print(C)

# Test 06
C =  A * 0.5
print('Left point-wise multiplication (Matrix-scalar):')
print(C)

# Test 07
C =   0.5 * A
print('Right point-wise multiplication (Matrix-scalar):')
print(C)

# Test 08
print('Element access (Matrix-scalar):')
print(A[0,0])


# Test 09
print('Element update (Matrix-scalar):')
print(A)
A[0,0] = -10.0
print(A)