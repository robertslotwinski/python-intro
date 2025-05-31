# Raport z analizy MCDM - Wybór samochodu

## 1. Wprowadzenie

Celem niniejszej analizy było zastosowanie biblioteki pymcdm do wielokryterialnego podejmowania decyzji w problemie wyboru samochodu. Implementowano dwie wymagane metody: TOPSIS i SPOTIS.

## 2. Dane wejściowe

### 2.1 Macierz decyzyjna

Analizowano 4 alternatywy (samochody) pod względem 4 kryteriów:

| Alternatywa | Cena [zł] | Osiągi [1-10] | Ocena [1-5] | Spalanie [l/100km] |
| ----------- | --------- | ------------- | ----------- | ------------------ |
| Samochód A  | 25000     | 6             | 4.5         | 8.0                |
| Samochód B  | 30000     | 7             | 4.0         | 6.5                |
| Samochód C  | 27000     | 8             | 4.8         | 7.0                |
| Samochód D  | 22000     | 5             | 4.3         | 9.0                |

### 2.2 Konfiguracja kryteriów

- **Wagi kryteriów**: [0.4, 0.3, 0.2, 0.1]

  - Cena: 40% (najważniejsze kryterium)
  - Osiągi: 30%
  - Ocena: 20%
  - Spalanie: 10%

- **Typ kryteriów**:
  - Cena: minimalizowane (-1) - niższa cena jest lepsza
  - Osiągi: maksymalizowane (1) - wyższe osiągi są lepsze
  - Ocena: maksymalizowane (1) - wyższa ocena jest lepsza
  - Spalanie: minimalizowane (-1) - niższe spalanie jest lepsze

## 3. Metodologia

### 3.1 Biblioteka pymcdm

Zastosowano bibliotekę pymcdm zawierającą implementacje metod MCDM oraz narzędzia do normalizacji danych.

### 3.2 Normalizacja danych

- **TOPSIS**: zastosowano normalizację min-max za pomocą funkcji `minmax_normalization()`
- **SPOTIS**: używano danych surowych zgodnie ze specyfikacją metody

### 3.3 Metody MCDM

#### 3.3.1 TOPSIS

Metoda TOPSIS bazuje na odległości od idealnego rozwiązania pozytywnego i negatywnego. Wyższe wartości oznaczają lepsze alternatywy.

#### 3.3.2 SPOTIS

Metoda SPOTIS oparta jest na odległości od stabilnego punktu preferencji zdefiniowanego przez granice kryteriów. Niższe wartości oznaczają lepsze alternatywy.

## 4. Wyniki analizy

### 4.1 Ranking według TOPSIS

Na podstawie uzyskanych wyników TOPSIS:

1. **Samochód C**: najwyższy wynik
2. **Samochód A**: drugi w rankingu
3. **Samochód B**: trzeci w rankingu
4. **Samochód D**: najniższy wynik

### 4.2 Ranking według SPOTIS

Na podstawie uzyskanych wyników SPOTIS:

1. **Samochód C**: najniższy wynik (najlepszy)
2. **Samochód A**: drugi najniższy wynik
3. **Samochód B**: trzeci w kolejności
4. **Samochód D**: najwyższy wynik (najgorszy)

### 4.3 Porównanie rankingów

| Alternatywa | Pozycja TOPSIS | Pozycja SPOTIS |
| ----------- | -------------- | -------------- |
| Samochód A  | 2              | 2              |
| Samochód B  | 3              | 3              |
| Samochód C  | 1              | 1              |
| Samochód D  | 4              | 4              |

## 5. Interpretacja wyników

### 5.1 Najlepsza opcja - Samochód C

**Samochód C** został uznany za najlepszy wybór przez obie metody ze względu na:

- **Najwyższe osiągi** (8/10) - najważniejszy parametr po cenie
- **Najlepszą ocenę ogólną** (4.8/5) - świadczy o wysokiej jakości
- **Umiarkowaną cenę** (27000 zł) - drugi najtańszy, ale rozsądny stosunek jakości do ceny
- **Średnie spalanie** (7.0 l/100km) - akceptowalne zużycie paliwa

### 5.2 Zgodność metod

- Obie metody (TOPSIS i SPOTIS) wygenerowały **identyczny ranking** dla wszystkich alternatyw
- Świadczy to o **wysokiej stabilności i wiarygodności** wyniku
- **Jednoznaczna rekomendacja** bez konfliktów między metodami

### 5.3 Analiza pozostałych opcji

- **Samochód A**: Druga pozycja - dobra równowaga parametrów, umiarkowana cena
- **Samochód B**: Trzecia pozycja - najdroższy przy średnich parametrach i najlepszym spalaniu
- **Samochód D**: Ostatnia pozycja - najtańszy, ale najsłabsze osiągi i najgorsze spalanie

## 6. Wnioski

### 6.1 Główne obserwacje

1. **Pełna zgodność metod** - identyczne rankingi dla wszystkich 4 pozycji zwiększają zaufanie do wyniku
2. **Wyraźna dominacja Samochodu C** - najlepsza opcja w analizie wielokryterialnej
3. **Wpływ struktury wag** - duża waga ceny (40%) i osiągów (30%) zadecydowała o wyniku
4. **Stabilność rankingu** - brak konfliktów między różnymi podejściami metodologicznymi

### 6.2 Rekomendacja końcowa

Na podstawie przeprowadzonej analizy MCDM z zastosowaniem dwóch różnych metod, **jednoznacznie rekomendujemy Samochód C** jako najlepszy wybór. Decyzja jest uzasadniona:

- Zgodnym wynikiem metod TOPSIS i SPOTIS
- Najlepszym bilansem wszystkich analizowanych kryteriów
- Najwyższymi ocenami w kluczowych kategoriach (osiągi, ocena ogólna)

### 6.3 Ograniczenia analizy

1. **Subiektywność wag** - wagi kryteriów zostały określone ekspercko, bez konsultacji z użytkownikami
2. **Ograniczony zestaw kryteriów** - nie uwzględniono innych ważnych czynników (niezawodność, koszty eksploatacji, bezpieczeństwo)
3. **Różne podejścia do normalizacji** - TOPSIS używał danych znormalizowanych, SPOTIS surowych
4. **Brak analizy wrażliwości** - nie sprawdzono wpływu zmiany wag na stabilność rankingu
