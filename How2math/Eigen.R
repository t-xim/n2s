A = matrix(c(2, -1, 0, -1, 2, -1, 0, -1, 2), nrow=3, byrow=TRUE)

# inverse A
Ainverse = solve(A)

# Getting eigenvalues and eigenvectors of A
Aeigen = eigan(A)
Aeigen$values
#Aeigen$vectors

# Spectral decomposition
# A = PDP^-1
P = Aeigen$vectors
D = matrix(c(Aeigen$values[1],0,0,
             0,Aeigen$values[2],0,
             0,0,Aeigen$values[3]), nrow=3, byrow = TRUE)

# Checking
A == round(P %*% D %*% solve(P))
             
# Inverse D (alternative method)
Dinverse = 1/D
Dinverse[which(!is.finite(Dinverse))] <- 0

# Sqrt A
Dsqrt = sqrt(D)
Asqrt = P %*% Dsqrt %*% t(P)
