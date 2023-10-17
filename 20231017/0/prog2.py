import string
import timeit
s = input()

def vow_cons(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = set(string.ascii_lowercase) - vowels

    set_s = set(s)
    occur_vowels = set_s & vowels
    occur_cons = set_s & consonants

    return len(occur_vowels), len(occur_cons)

cyc, tim = (timeit.Timer('vow_cons(s)', globals=globals()).autorange())
print(cyc * 1 / tim)
