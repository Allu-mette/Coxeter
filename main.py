import scripts as sc

# Groupe S4 (ou pas)

# Définition des générateurs
a = sc.Letter("a")
b = sc.Letter("b")
c = sc.Letter("c")
d = sc.Letter("d")

# Relations de tresses (ex: [a, c, a] correspond à la relation de tresse : aca=cac)
r1 = sc.Word([a, b])
r2 = sc.Word([a, c, a])
r3 = sc.Word([b, c, b, c])
r4 = sc.Word([b, c, b, c, b])
r5 = sc.Word([b, d])
r6 = sc.Word([d, c, d, c, d])

# Creattion du groupe de Coxeter
G = sc.Coxeter([a, b, c], [r1, r2, r3])

# Mot à réduire
W1 = c+c+a+b+a+c+b+a+a+c+b
print(f"Mot à réduire: {W1}")

# Mot réduit
W1r = sc.Reduce(G, W1)
print(f"Mot réduit: {W1r}")
print(f"Longueur de l'élément: {W1r.get_len()}")

# Graphe de Matsumoto du mot
print(f"Mot(s) réduit(s) similaire(s): {sc.BraidTrans(G, W1r)} \n")


W2 = a+b+c+a+b+c+a+b+c+a+b
print(f"Mot à réduire: {W2}")

W2r = sc.Reduce(G, W2)
print(f"Mot réduit: {W2r}")
print(f"Longueur de l'élément: {W2r.get_len()}")

print(f"Mot(s) réduit(s) similaire(s): {sc.BraidTrans(G, W2r)}")
