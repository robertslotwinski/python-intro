# Przykład użycia biblioteki Seaborn

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Ustawienie stylu
sns.set_style("whitegrid")


def example_1_simple_plots():
    """Przykład 1: Proste i piękne wykresy"""
    print("Przykład 1: Podstawowe wykresy Seaborn")

    # Tworzenie przykładowych danych
    np.random.seed(42)
    data = pd.DataFrame(
        {
            "wiek": np.random.randint(20, 60, 100),
            "zarobki": np.random.randint(3000, 15000, 100),
            "wykształcenie": np.random.choice(["Licencjat", "Magister", "Doktor"], 100),
            "płeć": np.random.choice(["Kobieta", "Mężczyzna"], 100),
        }
    )

    # Wykres punktowy z kolorami
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x="wiek", y="zarobki", hue="wykształcenie", style="płeć")
    plt.title("Zależność między wiekiem a zarobkami")
    plt.show()


def example_2_statistical_plots():
    """Przykład 2: Wykresy statystyczne"""
    print("Przykład 2: Analiza statystyczna")

    # przykładowe dane o sprzedaży
    np.random.seed(42)
    sales_data = pd.DataFrame(
        {
            "miesiąc": ["Sty", "Lut", "Mar", "Kwi", "Maj", "Cze"] * 4,
            "produkt": [
                "A",
                "A",
                "A",
                "A",
                "A",
                "A",
                "B",
                "B",
                "B",
                "B",
                "B",
                "B",
                "C",
                "C",
                "C",
                "C",
                "C",
                "C",
                "D",
                "D",
                "D",
                "D",
                "D",
                "D",
            ],
            "sprzedaż": [
                120,
                135,
                145,
                165,
                180,
                190,
                80,
                85,
                95,
                110,
                125,
                140,
                200,
                180,
                220,
                240,
                260,
                280,
                150,
                160,
                170,
                155,
                175,
                185,
            ],
        }
    )

    # Tworzenie wykresów
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Wykres słupkowy
    sns.barplot(data=sales_data, x="miesiąc", y="sprzedaż", hue="produkt", ax=ax1)
    ax1.set_title("Sprzedaż według miesięcy")

    # Boxplot
    sns.boxplot(data=sales_data, x="produkt", y="sprzedaż", ax=ax2)
    ax2.set_title("Rozkład sprzedaży według produktów")

    plt.tight_layout()
    plt.show()


def example_3_correlation_heatmap():
    """Przykład 3: Mapa korelacji"""
    print("Przykład 3: Mapa korelacji - bardzo popularna!")

    # Dane korelacyjne
    np.random.seed(42)
    corr_data = pd.DataFrame(
        {
            "Wiek": np.random.randint(20, 65, 50),
            "Doświadczenie": np.random.randint(0, 40, 50),
            "Wykształcenie_lata": np.random.randint(12, 20, 50),
            "Zarobki": np.random.randint(3000, 20000, 50),
        }
    )

    # Obliczenie korelacji
    correlation_matrix = corr_data.corr()

    # Mapa korelacji
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        correlation_matrix,
        annot=True,  # Pokazuj wartości
        cmap="coolwarm",  # Kolorowa mapa
        center=0,  # Wyśrodkowanie na 0
        square=True,
    )  # Kwadratowe komórki

    plt.title("Mapa korelacji zmiennych")
    plt.show()


def main():
    """Funkcja główna"""
    print("=== Przykłady użycia Seaborn ===\n")

    example_1_simple_plots()
    print("\n" + "=" * 50 + "\n")

    example_2_statistical_plots()
    print("\n" + "=" * 50 + "\n")

    example_3_correlation_heatmap()

    print("\n=== Seaborn - wykresy bez wysiłku! ===")


if __name__ == "__main__":
    main()
