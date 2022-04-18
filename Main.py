
import Scripts as sc

# Groupe S4
a = sc.Letter("a")
b = sc.Letter("b")
c = sc.Letter("c")

r1 = sc.Word([a, c])
r2 = sc.Word([a, b, a])
r3 = sc.Word([b, c, b])

G = sc.Coxeter([a, b, c], [r1, r2, r3])


W1 = a+b+a+b+c+b+a
print(f"Mot à réduire: {W1}")

W1r = sc.Reduce(G, W1)
print(f"Mot réduit: {W1r}")

print(f"Mot(s) réduit(s) similaire(s): {sc.BraidTrans(G, W1r)} \n")


W2 = a+b+c+a+b+c+a+b+c+a+b
print(f"Mot à réduire: {W2}")

W2r = sc.Reduce(G, W2)
print(f"Mot réduit: {W2r}")

print(f"Mot(s) réduit(s) similaire(s): {sc.BraidTrans(G, W2r)}")
