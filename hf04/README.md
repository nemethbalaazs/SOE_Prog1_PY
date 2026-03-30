# HF04 – Függvények

## Feladatok

### 1. feladat – Faktoriális

Írj egy `faktorial(n)` nevű függvényt, amely visszaadja `n` faktoriálisát iteratívan (ciklussal, nem rekurzívan)! Teszteld 0-val, 1-gyel, 5-tel és 10-zel!

### 2. feladat – Maximum és minimum

Írj egy `max_min(szamok)` nevű függvényt, amely egy számlistát kap paraméterként, és visszaadja a lista legnagyobb és legkisebb elemét egy tuple-ként `(maximum, minimum)` formában. Beépített `max()` és `min()` függvény **nem** használható!

### 3. feladat – Palindróm

Írj egy `palindrom(szo)` nevű függvényt, amely megvizsgálja, hogy a kapott szó palindróm-e (visszafelé olvasva is ugyanaz-e)! A vizsgálatnál ne számítsanak a kis- és nagybetűk. Visszatérési értéke `True` vagy `False` legyen.

**Példák:**
- `"Radar"` → `True`
- `"alma"` → `False`
- `"görög"` → `True`

### 4. feladat – Alap statisztikák

Írj egy `statisztika(szamok)` nevű függvényt, amely egy számlistát kap, és visszaad egy szótárat (`dict`) az alábbi kulcsokkal:
- `"darab"`: elemek száma
- `"osszeg"`: összeg
- `"atlag"`: átlag
- `"minimum"`: legkisebb elem
- `"maximum"`: legnagyobb elem

### 5. feladat – Rekurzív összegzés

Írj egy `rekurziv_osszeg(n)` nevű rekurzív függvényt, amely visszaadja az 1-től n-ig terjedő egész számok összegét!

### 6. feladat – Egységkonverter

Írj egy általános `konvertal(ertek, egyseg_be, egyseg_ki)` függvényt, amely az alábbi hosszmértékegységek között tud váltani:
- `"m"` (méter), `"km"` (kilométer), `"cm"` (centiméter), `"mm"` (milliméter)

Ha ismeretlen egységet kap, dobjon `ValueError` kivételt!

## Beadás

- Fájlnév: `NEPTUN_hf04.py`
- Minden feladatot önálló függvényként implementálj
- A fájl végén `if __name__ == "__main__":` blokkban teszteld a függvényeket
