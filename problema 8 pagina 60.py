A=set(input('Dati numere intregi care vor fi elemnetele multimii A:'))
B=set(input('Dati numere intregi care vor fi elemnetele multimii B:'))
print(A)
print(B)
print('Reuniunea multimilor A si B ->',A.union(B))
print('Intersectia multimilor A si B ->',A.intersection(B))
print('Diferenta multimilor A si B ->',A.difference(B))
print('Diferenta multimilor B si A ->',B.difference(A))