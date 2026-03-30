"""
HF05 – Listák
Soproni Egyetem – Programozás 1 (2025/26)

Kitöltendő megoldássablon.
Cseréld ki a NEPTUN szót a saját Neptun-kódodra, és mentsd el
NEPTUN_hf05.py névvel!
"""


def feladat1():
    """1. feladat – Lista alapműveletek"""
    # IDE ÍRD A MEGOLDÁST
    pass


def feladat2():
    """2. feladat – Szám-statisztikák (bevitel 0-ig)"""
    # IDE ÍRD A MEGOLDÁST
    pass


def buborek_rendezes(lista):
    """3. feladat – Buborékrendezés (sort/sorted nélkül)"""
    # IDE ÍRD A MEGOLDÁST
    pass


def feladat4():
    """4. feladat – Mátrix"""
    # IDE ÍRD A MEGOLDÁST
    pass


def feladat5(lista1, lista2):
    """5. feladat – Halmaz-műveletek listákkal (set nélkül)
    Visszatér: (unió, metszet, különbség) tuple-lal
    """
    # IDE ÍRD A MEGOLDÁST
    pass


if __name__ == "__main__":
    print("=== 1. feladat ===")
    feladat1()

    print("\n=== 2. feladat ===")
    feladat2()

    print("\n=== 3. feladat – buborékrendezés ===")
    teszt = [64, 34, 25, 12, 22, 11, 90]
    print(f"Eredeti: {teszt}")
    rendezett = buborek_rendezes(teszt[:])
    print(f"Rendezett: {rendezett}")

    print("\n=== 4. feladat ===")
    feladat4()

    print("\n=== 5. feladat – halmaz-műveletek ===")
    a = [1, 2, 3, 4, 5]
    b = [3, 4, 5, 6, 7]
    unio, metszet, kulonbseg = feladat5(a, b)
    print(f"A: {a}")
    print(f"B: {b}")
    print(f"Unió:      {unio}")
    print(f"Metszet:   {metszet}")
    print(f"Különbség: {kulonbseg}")
