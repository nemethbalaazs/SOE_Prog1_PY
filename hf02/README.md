# HF02 – Elágazások: `if`, `elif`, `else`

## Feladatok

### 1. feladat – Páros vagy páratlan

Kérj be egy egész számot, és döntsd el, hogy páros-e vagy páratlan!

**Elvárt kimenet (példa):**
```
Adj meg egy egész számot: 7
7 páratlan szám.
```

### 2. feladat – Osztályozás

Kérj be egy pontszámot (0–100), és írd ki a megfelelő osztályzatot az alábbi skála szerint:
- 0–49 → elégtelen (1)
- 50–61 → elégséges (2)
- 62–74 → közepes (3)
- 75–87 → jó (4)
- 88–100 → jeles (5)

### 3. feladat – Háromszög típusa

Kérj be három oldalhosszt, és döntsd el, hogy az azokból alkotott háromszög:
- egyenlő oldalú
- egyenlő szárú
- általános (különböző oldalú)

Ha a három szám nem alkothat háromszöget, ezt is jelezd! (Háromszög-egyenlőtlenség: minden oldal kisebb a másik kettő összegénél.)

### 4. feladat – Szökőév

Kérj be egy évszámot, és döntsd el, hogy szökőév-e!

**Szökőév feltétele:** Osztható 4-gyel, DE ha 100-zal is osztható, akkor csak akkor szökőév, ha 400-zal is osztható.

### 5. feladat – BMI kalkulátor

Kérj be egy személy testtömegét (kg) és magasságát (m), számítsd ki a BMI értékét, és írd ki a kategóriát:
- BMI < 18.5 → Alulsúlyos
- 18.5 ≤ BMI < 25 → Normál
- 25 ≤ BMI < 30 → Túlsúlyos
- BMI ≥ 30 → Elhízott

**Képlet:** `BMI = testtömeg / magasság²`

## Beadás

- Fájlnév: `NEPTUN_hf02.py`
- Minden feladatot külön függvénybe szervezve adj be (`feladat1()`, `feladat2()`, stb.)
- A fájl végén hívd meg az összes függvényt
