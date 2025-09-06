# Make a freaking thing that takes user input using pop ups and translates it into pig latin
import random
from traitlets import This


ay = "ay"
consonants = "B, b, C, c, D, d, F, f, G, g, H, h, J, j, K, k, L, l, M, m, N, n, P, p, Q, q, R, r, S, s, T, t, U, u, V, v, W, w, X, x, Y, y, Z, z"
vowel = "a, A, e, E, i, I, o, O, u, U"

while True :
    words = input(str("GIME UR WORD MANKE SKIBIDI RIZZ GIGAGAGAGIDIEO NO CAP FR FR"))
    if input:
        print(words)
        for word in words.split():
            if word[0] in vowel:
                print(word + "hay", end = " ")
            elif word[0] in consonants:
                print(word[1:] + word[0] + "ay", end=" ")
        print()
        
