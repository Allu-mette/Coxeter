# Réduction de mots dans un groupe de Coxeter

## 📖 Présentation du projet

Ce projet a été réalisé dans le cadre de mon mémoire de fin de Master sur les groupes de Coxeter. Il implémente un algorithme Python permettant de réduire un mot donné dans un groupe de Coxeter et de générer son graphe de Matsumoto. L'objectif final est de résoudre le problème des mots pour ce type particulier de groupe.

## 📌 Description 

Ce projet permet de manipuler :

- des générateurs (classe `Letter`),

- des mots (classe `Word`),

- un groupe de Coxeter (classe `Coxeter`),

et d’appliquer les opérations suivantes :

- réduction par réflexions (ex: `aa = 1`),

- réduction par tresses (ex : `aba = bab`),

- génération du graphe de Matsumoto d’un mot réduit.

## ⚙️ Installation

Aucune dépendance externe.  
Python ≥ 3.8 est recommandé.

Cloner le dépôt :
```bash
git clone https://github.com/Allu-mette/Coxeter.git
cd Coxeter
```

## 🚀 Exemple d’utilisation

Dans `main.py` vous pouvez modifier le nombre de générateurs et les relations de tresses du groupe de Coxeter : 
```python
# Définition des générateurs
a = sc.Letter("a")
b = sc.Letter("b")

# Relation(s) de tresse(s) (ici : ab = ba)
r1 = sc.Word([a, b])

# Groupe de Coxeter correspondant
G = sc.Coxeter([a, b], [r1])
```

Définir le mot à réduire :
```python
# Mot à réduire
W1 = a+b+a+b+b+a+b+a+a
```

Puis exécuter :
```bash
python main.py
```

Sortie : 
```
Mot à réduire: ababbabaa
Mot réduit: a
Longueur de l'élément: 1
Mot(s) réduit(s) similaire(s): [a]
```