#!/usr/bin/env python
# *-* coding: UTF-8 *-*

"""
Organizaţia Internaţională a Aviaţiei Civile propune un alfabet în care
fiecărei litere îi este asignat un cuvânt pentru a evita problemele în
înțelegerea mesajelor critice.

Pentru a se păstra un istoric al conversațiilor s-a decis transcrierea lor
conform următoarelor reguli:
    - fiecare cuvânt este scris pe o singură linie
    - literele din alfabet sunt separate de o virgulă

Următoarea sarcină ți-a fost asignată:
    Scrie un program care să primească un fișier ce conține mesajul
    brut (scris folosind alfabetul ICAO) și generează un fișier
    numit icao_intrare ce va conține mesajul inițial.

Mai jos găsiți un dicționar ce conține o versiune a alfabetului ICAO:
"""

ICAO = {
    'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo',
    'f': 'foxtrot', 'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett',
    'k': 'kilo', 'l': 'lima', 'm': 'mike', 'n': 'november', 'o': 'oscar',
    'p': 'papa', 'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
    'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray', 'y': 'yankee',
    'z': 'zulu'
}


def din_icao(fisier_intrare):
    """Funcția va primi calea către fișierul ce conține mesajul brut și
    va genera un fișier numit icao_intrare ce va conține mesajul inițial.
    """
    fisier = open(fisier_intrare, "r")
    mesaj = fisier.read()
    fisier.close()
    l = [item for item in mesaj]
    fisier2 = open("icao_intrare", "w+")
    ok = 1
    for index in range(len(l)):
        if ok == 1:
            fisier2.write(l[index])
            ok = 0
        if l[index] == ' ':
            ok = 1
        if l[index] == '\n':
            fisier2.write(l[index])
            ok = 1
    fisier2.close()


if __name__ == "__main__":
    din_icao("mesaj.icao")
