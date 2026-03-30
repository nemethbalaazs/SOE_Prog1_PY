"""
HF04 – Függvények
Soproni Egyetem – Programozás 1 (2025/26)

Kitöltendő megoldássablon.
Cseréld ki a NEPTUN szót a saját Neptun-kódodra, és mentsd el
NEPTUN_hf04.py névvel!
"""


def faktorial(n):
    """1. feladat – Faktoriális (iteratív)"""
    # IDE ÍRD A MEGOLDÁST
    pass


def max_min(szamok):
    """2. feladat – Maximum és minimum (beépített max/min nélkül)"""
    # IDE ÍRD A MEGOLDÁST
    pass


def palindrom(szo):
    """3. feladat – Palindróm ellenőrzés"""
    # IDE ÍRD A MEGOLDÁST
    pass


def statisztika(szamok):
    """4. feladat – Alap statisztikák"""
    # IDE ÍRD A MEGOLDÁST
    pass


def rekurziv_osszeg(n):
    """5. feladat – Rekurzív összegzés"""
    # IDE ÍRD A MEGOLDÁST
    pass


def konvertal(ertek, egyseg_be, egyseg_ki):
    """6. feladat – Egységkonverter (m, km, cm, mm)"""
    # IDE ÍRD A MEGOLDÁST
    pass


if __name__ == "__main__":
    print("=== 1. feladat – faktoriális ===")
    for szam in [0, 1, 5, 10]:
        print(f"{szam}! = {faktorial(szam)}")

    print("\n=== 2. feladat – max/min ===")
    lista = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Lista: {lista}")
    print(f"Maximum, minimum: {max_min(lista)}")

    print("\n=== 3. feladat – palindróm ===")
    for szo in ["Radar", "alma", "Görög", "Python"]:
        print(f'"{szo}" palindróm: {palindrom(szo)}')

    print("\n=== 4. feladat – statisztika ===")
    adatok = [4, 7, 2, 9, 1, 5]
    print(f"Adatok: {adatok}")
    print(f"Statisztika: {statisztika(adatok)}")

    print("\n=== 5. feladat – rekurzív összeg ===")
    for n in [1, 5, 10, 100]:
        print(f"1..{n} összege: {rekurziv_osszeg(n)}")

    print("\n=== 6. feladat – egységkonverter ===")
    print(f"1 km = {konvertal(1, 'km', 'm')} m")
    print(f"100 cm = {konvertal(100, 'cm', 'm')} m")
    print(f"5000 mm = {konvertal(5000, 'mm', 'km')} km")
