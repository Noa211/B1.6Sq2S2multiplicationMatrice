import os

M: int = 5
while M > 4:
    M = int(input("Entrez le nombre M (max 4) = "))

N: int = 5
while N > 4:
    N = int(input("Entrez le nombre N (max 4) = "))

P: int = 5
while P > 4:
    P = int(input("Entrez le nombre P (max 4) = "))

os.system("cls")

A = [[0] * M for _ in range(N)]
B = [[0] * N for _ in range(P)]
C = [[0] * M for _ in range(P)]

L = 6 # Largeur d'une case
H = 2 # Hauteur d'une case

# affichage de la matrice A
for x in range(0, N):
    for y in range(0, M):
        print(f"\033[{y*H+1};{x*L+1}H.")
# affichage de la matrice B
for x in range(0, P):
    for y in range(0, N):
        print(f"\033[{y*H+1};{(x+N+1)*L}H.")
# affichage signes
print(f"\033[{(M*H)//2};{N*L}Hx")
print(f"\033[{(M*H)//2};{(N+P+1)*L}H=")

# saisie des matrice A et B
for x in range(0, N):
    for y in range(0, M):
        A[x][y] = float(input(f"\033[{y*H+1};{x*L+1}H"))

for x in range(0, P):
    for y in range(0, N):
        B[x][y] = float(input(f"\033[{y*H+1};{(x+N+1)*L}H"))

# calcul de la matrice C
for x in range(0, P):
    for y in range(0, M):
        C[x][y] = 0
        for k in range(0, N):
            C[x][y] += A[k][y] * B[x][k]

# affichage de la matrice C
for x in range(0, P):
    for y in range(0, M):
        print(f"\033[{y*H+1};{(x+N+P+2)*L}H{C[x][y]}")

print("...")