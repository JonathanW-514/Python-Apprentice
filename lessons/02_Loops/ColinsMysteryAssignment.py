# Make a freaking thing that takes user input using pop ups and translates it into pig latin

from cmath import phase
import random
from click import prompt
from traitlets import This

while True :
    ay = "ay"
    consonants = "B, b, C, c, D, d, F, f, G, g, H, h, J, j, K, k, L, l, M, m, N, n, P, p, Q, q, R, r, S, s, T, t, U, u, V, v, W, w, X, x, Y, y, Z, z"
    vowel = "a, A, e, E, i, I, o, O, u, U"
    words = input(str("GIME UR WORD MANKE SKIBIDI RIZZ GIGAGAGAGIDIEO NO CAP FR FR"))
    if input:
        for word in words.split():
            print(word[1:] + "-" + word[0] + "ay")
        