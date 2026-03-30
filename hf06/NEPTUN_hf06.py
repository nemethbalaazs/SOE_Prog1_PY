"""
HF06 – Karakterláncok (stringek)
Soproni Egyetem – Programozás 1 (2025/26)

Kitöltendő megoldássablon.
Cseréld ki a NEPTUN szót a saját Neptun-kódodra, és mentsd el
NEPTUN_hf06.py névvel!
"""


def feladat1():
    """1. feladat – String alapok"""
    # IDE ÍRD A MEGOLDÁST
    pass


def feladat2():
    """2. feladat – Szó-statisztika"""
    # IDE ÍRD A MEGOLDÁST
    pass


def titkosit(szoveg, eltolas):
    """3. feladat – Caesar-titkosítás"""
    # IDE ÍRD A MEGOLDÁST
    pass


def visszafejt(titkos, eltolas):
    """3. feladat – Caesar-visszafejtés"""
    # IDE ÍRD A MEGOLDÁST
    pass


def feladat4():
    """4. feladat – Dátumformázás"""
    # IDE ÍRD A MEGOLDÁST
    pass


def igazit(szoveg, szelesseg, mod):
    """5. feladat – Szöveg igazítása (ljust/rjust/center nélkül)
    mod: 'bal', 'jobb' vagy 'közép'
    """
    # IDE ÍRD A MEGOLDÁST
    pass


if __name__ == "__main__":
    print("=== 1. feladat ===")
    feladat1()

    print("\n=== 2. feladat ===")
    feladat2()

    print("\n=== 3. feladat – Caesar-rejtjel ===")
    eredeti = "Hello, World!"
    eltolas = 3
    titkos = titkosit(eredeti, eltolas)
    vissza = visszafejt(titkos, eltolas)
    print(f"Eredeti:     {eredeti}")
    print(f"Titkosított: {titkos}")
    print(f"Visszafejtve: {vissza}")

    print("\n=== 4. feladat ===")
    feladat4()

    print("\n=== 5. feladat – igazítás ===")
    szoveg = "alma"
    for mod in ["bal", "jobb", "közép"]:
        eredmeny = igazit(szoveg, 10, mod)
        print(f"|{eredmeny}|  ({mod})")
