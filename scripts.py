
class Letter:

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Letter):
            return  Word([self, other])

        elif isinstance(other, Word):
            w0 = []
            w0.append(self)
            for i in other.w:
                w0.append(i)

            return Word(w0)

        else:
            return "Il faut additionner une lettre avec une autre lettre ou un mot!"

    def __eq__(self, other):
        return self.name == other.name

class Word:

    def __init__(self, w: list[Letter]):
        self.w = w

    def __str__(self):
        rep = ""
        for i in self.w:
            rep += i.name
        return rep

    def __repr__(self):
        rep = ""
        for i in self.w:
            rep += i.name
        return rep

    def __add__(self, other):
        w0 = []
        for i in self.w:
            w0.append(i)

        if isinstance(other, Letter):
            w0.append(other)
            return Word(w0)

        elif isinstance(other, Word):
            for i in other.w:
                w0.append(i)
            return  Word(w0)

        else:
            return "Il faut additionner un mot avec un autre mot ou une lettre!"

    def __eq__(self, other):
        return self.w == other.w

        # Renvoie la longueur du mot
    def get_len(self):
        return len(self.w)

        # Regarde si le mot contient W
    def is_in(self, W):
        n = W.get_len()

        if n > self.get_len():
            return -1

        for i in range(self.get_len() - n + 1):
            if W.w == self.w[i:i + n]:
                return i

        return -1

        # Renvoie le mot où la section, à partir du rang n, est changée par W
    def change(self, n: int, W):
        if n + W.get_len()-1 > self.get_len():
            print("La section à changer est trop longue!")
            return self

        w0 = self.w[:]
        w0[n:n+W.get_len()] = W.w
        return Word(w0)

        # Renvoie la relation de tresse associée ex: aba -> bab (A utiliser uniquement sur des relations de tresses!)
    def slice(self):
        return Word(self.w[1:2] + self.w[:-1])

class Coxeter:

    def __init__(self, S: list[Letter], R: list[Word]):
        self.S = S

        for r in R[:]:
            R.append(r.slice())
        self.R = R

def ReflexionReduce(W: Word)->Word:
    '''
    Réduit un mot uniquement à partir des reflexions (aa=1)
    '''
    w = W.w
    w0 = w[:]
    j = True

    while(j):
        for i in range(len(w0)-1):
            if w0[i] == w0[i+1]:
                del w0[i:i+2]
                break
            if i == len(w0)-2:
                j = False

        if len(w0) == 0 or len(w0) == 1:
            break

    return Word(w0)

def BraidTrans(G: Coxeter, W: Word)->list[Word]:
    '''
    Renvoie un tableau contenant toutes les formes d'un mot à partir des relations de tresses
    Si le mot est réduit alors le résultat sera le graphe de Matsumoto du mot
    '''

    R = G.R

        # Systéme de list open/closed
    T1 = []
    T2 = [W]

    while T2 != []:
        w0 = T2[0]
        for r in R:
            n = w0.is_in(r)

                # On trouve une relation
            if n != -1:
                    # Le mot avec la relation n'a pas encore été testé
                if w0.change(n, r.slice()) not in T1 and w0.change(n, r.slice()) not in T2:
                    T2.append(w0.change(n, r.slice()))

        T2.remove(w0)
        T1.append(w0)

    return T1

def FirstReduce(G: Coxeter, W: Word)->Word:
    '''
    Renvoie la réduction d'un mot de la forme ws où w est un mot déjà réduit
    '''

        # Séparation du mot de la forme W = ws
    U = BraidTrans(G, Word(W.w[:-1]))
    s = W.w[-1]

    for u in U:
        if u.get_len() != 0:
            if u.w[-1] == s:
                return ReflexionReduce(u+s)

    return W

def Reduce(G: Coxeter, W: Word)->Word:
    '''
    Renvoie le mot réduit
    '''
    W = ReflexionReduce(W)
    w0 = Word(W.w[:2])

    for i in range(2, W.get_len()):
        s = W.w[i]
        w0 = FirstReduce(G, w0 + s)

    return w0