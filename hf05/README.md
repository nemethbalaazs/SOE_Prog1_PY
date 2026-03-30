# HF05 – Listák

## Feladatok

### 1. feladat – Lista alapműveletek

Hozz létre egy üres listát, majd:
1. Add hozzá az 1-től 10-ig terjedő számokat
2. Írd ki a listát
3. Fordítsd meg a listát (beépített `reverse()` nélkül)
4. Írd ki a megfordított listát
5. Töröld az összes páros számot
6. Írd ki a végeredményt

### 2. feladat – Szám-statisztikák

Kérj be a felhasználótól egész számokat addig, amíg 0-t nem ad meg. Tárold a számokat egy listában, majd írd ki:
- a számok darabszámát
- a pozitív és negatív számok darabszámát
- az összegüket
- az átlagukat (ha van legalább egy szám)
- a legnagyobb és legkisebb értéket

### 3. feladat – Lista rendezése

Írj egy `buborek_rendezes(lista)` függvényt, amely buborékrendezéssel rendezi a kapott számlistát növekvő sorrendbe! Beépített `sort()` és `sorted()` **nem** használható!

### 4. feladat – Mátrix

Hozz létre egy 3×3-as mátrixot (listák listájaként), amelynek elemeit a felhasználó adja meg. Majd:
1. Írd ki mátrix formában
2. Számítsd ki a főátló összegét
3. Transpozáld a mátrixot és írd ki

### 5. feladat – Halmaz-műveletek listákkal

Adott két egész számokat tartalmazó lista. Beépített `set` típus használata **nélkül** valósítsd meg:
- az unió (mindkét lista összes egyedi eleme)
- a metszet (közös elemek)
- a különbség (az első lista elemei, amelyek a másodikban nincsenek)

## Beadás

- Fájlnév: `NEPTUN_hf05.py`
- Minden feladatot külön függvénybe szervezve adj be (`feladat1()`, `feladat2()`, stb.)
- A fájl végén hívd meg az összes függvényt
