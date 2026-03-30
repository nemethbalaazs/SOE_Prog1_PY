"""
HF07 – Fájlkezelés
Soproni Egyetem – Programozás 1 (2025/26)

Kitöltendő megoldássablon.
Cseréld ki a NEPTUN szót a saját Neptun-kódodra, és mentsd el
NEPTUN_hf07.py névvel!
"""


def feladat1():
    """1. feladat – Szövegfájl írása és olvasása"""
    # IDE ÍRD A MEGOLDÁST
    pass


def feladat2(bemeneti_fajl="szoveg.txt", kimeneti_fajl="szavak.txt"):
    """2. feladat – Szógyakoriság elemzés"""
    # IDE ÍRD A MEGOLDÁST
    pass


def feladat3():
    """3. feladat – CSV kezelés"""
    # IDE ÍRD A MEGOLDÁST
    pass


def fajl_olvas(fajlnev):
    """4. feladat – Fájl olvasása kivételkezeléssel.
    Visszatér a fájl tartalmával (str), vagy None-nal hiba esetén.
    """
    # IDE ÍRD A MEGOLDÁST
    pass


def feladat5():
    """5. feladat – Telefonkönyv"""
    # IDE ÍRD A MEGOLDÁST
    pass


if __name__ == "__main__":
    print("=== 1. feladat ===")
    feladat1()

    print("\n=== 2. feladat ===")
    feladat2()

    print("\n=== 3. feladat ===")
    feladat3()

    print("\n=== 4. feladat – fájl_olvas ===")
    tartalom = fajl_olvas("naplo.txt")
    if tartalom is not None:
        print("Fájl tartalma:")
        print(tartalom)
    tartalom_nem_letezo = fajl_olvas("nem_letezik.txt")
    print(f"Nem létező fájl visszatérési értéke: {tartalom_nem_letezo}")

    print("\n=== 5. feladat ===")
    feladat5()
