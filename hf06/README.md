# HF06 – Karakterláncok (stringek)

## Feladatok

### 1. feladat – String alapok

Kérj be egy mondatot a felhasználótól, majd írd ki:
- a mondat hosszát
- nagybetűsen
- kisbetűsen
- megfordítva
- szavainak számát

### 2. feladat – Szó-statisztika

Kérj be egy bekezdésnyi szöveget. Írd ki:
- az összes szó listáját (szóközök alapján darabolva)
- az egyedi szavak listáját (kis- és nagybetűt ne különböztess meg)
- a legtöbbször előforduló szót és előfordulásainak számát

### 3. feladat – Caesar-rejtjel

Valósítsd meg a Caesar-rejtjelezést!

- `titkosit(szoveg, eltolas)`: Titkosítja a szöveget az adott eltolással (csak az angol ABC betűire vonatkozzon, a többi karaktert változatlanul hagyja)
- `visszafejt(titkos, eltolas)`: Visszafejti a titkosított szöveget

**Példa (eltolás=3):**
```
Eredeti:    Hello, World!
Titkosított: Khoor, Zruog!
```

### 4. feladat – Dátumformázás

Kérj be egy dátumot `ÉÉÉÉ-HH-NN` formátumban (pl. `2025-09-01`). Ellenőrizd a formátum helyességét, majd írd ki emberi olvasásra alkalmas formában:

```
2025-09-01 → 2025. szeptember 1.
```

### 5. feladat – Szöveg igazítása

Írj egy `igazit(szoveg, szelesseg, mod)` függvényt, amely a szöveget a megadott szélességen belül igazítja. A `mod` értéke lehet `"bal"`, `"jobb"` vagy `"közép"`. Beépített `ljust()`, `rjust()`, `center()` **nem** használható!

## Beadás

- Fájlnév: `NEPTUN_hf06.py`
- Minden feladatot külön függvénybe szervezve adj be (`feladat1()`, `feladat2()`, stb.)
- A fájl végén hívd meg az összes függvényt
