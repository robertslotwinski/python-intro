# Przykład użycia biblioteki Matplotlib

import matplotlib.pyplot as plt
import numpy as np


def example_1_basic_plot():
    """Przykład 1: Podstawowy wykres liniowy"""
    print("Przykład 1: Wykres funkcji matematycznych")

    # Generowanie danych
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    # Tworzenie wykresu
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, "r-", label="sin(x)", linewidth=2)
    plt.plot(x, y2, "b--", label="cos(x)", linewidth=2)

    plt.title("Funkcje trygonometryczne")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)
    plt.show()


def example_2_different_charts():
    """Przykład 2: Różne typy wykresów"""
    print("Przykład 2: Różne typy wykresów")

    # Dane do wykresów
    categories = ["A", "B", "C", "D", "E"]
    values = [23, 45, 56, 78, 32]
    colors = ["red", "blue", "green", "orange", "purple"]

    # Tworzenie 4 wykresów w jednym oknie
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))

    # Wykres słupkowy
    ax1.bar(categories, values, color=colors)
    ax1.set_title("Wykres słupkowy")
    ax1.set_ylabel("Wartości")

    # Wykres kołowy
    ax2.pie(values, labels=categories, colors=colors, autopct="%1.1f%%")
    ax2.set_title("Wykres kołowy")

    # Histogram
    data = np.random.normal(50, 15, 1000)
    ax3.hist(data, bins=30, color="skyblue", alpha=0.7)
    ax3.set_title("Histogram")
    ax3.set_xlabel("Wartości")
    ax3.set_ylabel("Częstotliwość")

    # Wykres punktowy
    x = np.random.randn(50)
    y = np.random.randn(50)
    ax4.scatter(x, y, c=colors[: len(x) % 5], alpha=0.6)
    ax4.set_title("Wykres punktowy")
    ax4.set_xlabel("X")
    ax4.set_ylabel("Y")

    plt.tight_layout()
    plt.show()


def main():
    """Funkcja główna"""
    print("=== Przykłady użycia Matplotlib ===\n")

    example_1_basic_plot()
    print("\n" + "=" * 50 + "\n")

    example_2_different_charts()

    print("\n=== Matplotlib - łatwe i przyjemne! ===")


if __name__ == "__main__":
    main()
