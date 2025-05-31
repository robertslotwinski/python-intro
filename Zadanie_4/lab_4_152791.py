import numpy as np
import pandas as pd
from pymcdm.methods import TOPSIS, SPOTIS
from pymcdm.normalizations import minmax_normalization

print("------------------- WYBÓR SAMOCHODU - ANALIZA MCDM -------------------\n")

# 1. Dane wejściowe
decision_matrix = np.array(
    [
        [25000, 6, 4.5, 8.0],  # Samochód A
        [30000, 7, 4.0, 6.5],  # Samochód B
        [27000, 8, 4.8, 7.0],  # Samochód C
        [22000, 5, 4.3, 9.0],  # Samochód D
    ]
)

alternatives = ["Samochód A", "Samochód B", "Samochód C", "Samochód D"]
criteria = ["Cena", "Osiągi", "Ocena", "Spalanie"]

# Wyświetl dane
df = pd.DataFrame(decision_matrix, index=alternatives, columns=criteria)
print("DANE WEJŚCIOWE:")
print(df)
print()

# 2. Konfiguracja
weights = np.array([0.4, 0.3, 0.2, 0.1])
types = np.array([-1, 1, 1, -1])

print(f"Wagi: {weights}")
print(f"Typy: {['min' if t == -1 else 'max' for t in types]}")
print()

# 3. TOPSIS
normalized_matrix = minmax_normalization(decision_matrix)
topsis = TOPSIS()
topsis_scores = topsis(normalized_matrix, weights, types)
topsis_ranking = np.argsort(topsis_scores)[::-1] + 1

print("=== TOPSIS ===")
for i, (alt, score, rank) in enumerate(
    zip(alternatives, topsis_scores, topsis_ranking)
):
    print(f"{rank}. {alt}: {score:.3f}")
print()

# 4. SPOTIS
bounds = np.array(
    [
        [decision_matrix[:, i].min(), decision_matrix[:, i].max()]
        for i in range(decision_matrix.shape[1])
    ]
)

spotis = SPOTIS(bounds)
spotis_scores = spotis(decision_matrix, weights, types)
spotis_ranking = np.argsort(spotis_scores) + 1

print("=== SPOTIS ===")
spotis_sorted = sorted(
    zip(alternatives, spotis_scores, spotis_ranking), key=lambda x: x[1]
)
for i, (alt, score, rank) in enumerate(spotis_sorted):
    print(f"{i+1}. {alt}: {score:.3f}")
print()

# 5. Porównanie
results = pd.DataFrame(
    {
        "Alternatywa": alternatives,
        "TOPSIS": topsis_ranking,
        "SPOTIS": spotis_ranking,
    }
)

print("=== PORÓWNANIE RANKINGÓW ===")
print(results)
print()

# 6. Najlepszy wybór
best_topsis = alternatives[np.argmax(topsis_scores)]
best_spotis = alternatives[np.argmin(spotis_scores)]

print("=== WNIOSKI ===")
print(f"Najlepszy według TOPSIS: {best_topsis}")
print(f"Najlepszy według SPOTIS: {best_spotis}")

if best_topsis == best_spotis:
    print(f"Rekomendacja: {best_topsis}")
else:
    print("Metody wskazują różne opcje - wymaga analizy")
