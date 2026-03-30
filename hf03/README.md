# HF03 – Ciklusok: `for`, `while`

## Feladatok

### 1. feladat – Szorzótábla

Kérj be egy egész számot (1–10), és írd ki a szorzótábláját 1-től 10-ig!

**Elvárt kimenet (példa, n=3):**
```
3 * 1 = 3
3 * 2 = 6
...
3 * 10 = 30
```

### 2. feladat – Összegzés

Kérj be egy pozitív egész számot `n`-t, majd számítsd ki és írd ki az 1-től n-ig terjedő egész számok összegét! Ezt követően ellenőrizd az eredményt a Gauss-képlettel: `n*(n+1)//2`.

### 3. feladat – Prímszám ellenőrzés

Kérj be egy pozitív egész számot, és döntsd el, hogy prímszám-e! Írd ki az összes osztóját is.

### 4. feladat – Fibonacci-sorozat

Kérj be egy `n` értéket, és írd ki a Fibonacci-sorozat első `n` tagját!

**Elvárt kimenet (n=8):**
```
0 1 1 2 3 5 8 13
```

### 5. feladat – Számkitaláló játék

Generálj egy véletlenszerű egész számot 1 és 100 között (`random.randint`), majd kérd meg a felhasználót, hogy találja ki! Minden tipp után írd ki, hogy a keresett szám kisebb vagy nagyobb-e. Az ismétlések számát is tartsd nyilván és írd ki a végén!

### 6. feladat – FizzBuzz

Írd ki az 1-től 100-ig terjedő számokat az alábbi szabályok szerint:
- Ha a szám osztható 3-mal, írd ki: `Fizz`
- Ha osztható 5-tel, írd ki: `Buzz`
- Ha mindkettővel, írd ki: `FizzBuzz`
- Egyébként a számot magát írd ki

## Beadás

- Fájlnév: `NEPTUN_hf03.py`
- Minden feladatot külön függvénybe szervezve adj be (`feladat1()`, `feladat2()`, stb.)
- A fájl végén hívd meg az összes függvényt
