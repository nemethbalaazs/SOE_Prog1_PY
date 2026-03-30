# HF07 – Fájlkezelés

## Feladatok

### 1. feladat – Szövegfájl írása és olvasása

1. Hozz létre egy `naplo.txt` fájlt, és írj bele 5 sort (pl. naplóbejegyzéseket) programból!
2. Olvasd vissza a fájlt és írd ki a tartalmát sorszámozva!
3. Fűzz hozzá egy új bejegyzést anélkül, hogy a régiek elvesznének!

### 2. feladat – Szógyakoriság elemzés

Olvass be egy szövegfájlt (`szoveg.txt`), és számolja meg minden szó előfordulásának számát! Az eredményt mentsd el egy `szavak.txt` fájlba, előfordulás szerint csökkenő sorrendben, a következő formátumban:

```
the: 42
and: 38
of: 31
...
```

Teszteléshez a `szoveg.txt` fájlban lehet tetszőleges, legalább 50 szavas szöveg.

### 3. feladat – CSV kezelés

Írj egy programot, amely:
1. Létrehoz egy `diakok.csv` fájlt az alábbi fejléccel: `nev,neptun,jegy`
2. Beolvas legalább 5 diák adatát (név, Neptun-kód, jegy) a felhasználótól, és fájlba menti
3. Visszaolvassa a fájlt, és kiírja az adatokat egy táblázatban
4. Kiszámítja és kiírja az átlagjegyet

### 4. feladat – Fájlok kezelése kivételkezeléssel

Írj egy `fajl_olvas(fajlnev)` nevű függvényt, amely:
- Megpróbálja megnyitni és visszaadni a fájl tartalmát
- Ha a fájl nem létezik (`FileNotFoundError`), írjon hibaüzenetet és `None`-t adjon vissza
- Ha olvasási hiba keletkezik (`IOError`), szintén kezelje le megfelelően

### 5. feladat – Telefonkönyv

Valósíts meg egy egyszerű szövegfájl-alapú telefonkönyvet! A program indításkor betölti az adatokat egy `telefonkonyv.txt` fájlból (ha létezik), majd menürendszeren keresztül lehetővé teszi:
1. Új bejegyzés hozzáadása (név, telefonszám)
2. Bejegyzés keresése (névtöredék alapján)
3. Bejegyzés törlése
4. Összes bejegyzés listázása
5. Kilépés (adatok mentése)

## Beadás

- Fájlnév: `NEPTUN_hf07.py`
- Minden feladatot külön függvénybe szervezve adj be
- A fájl végén `if __name__ == "__main__":` blokkban hívd meg az összes feladatot
- A fájlkezelési részeket mindig `try-except` blokkal védd!
