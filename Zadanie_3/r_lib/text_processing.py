def reverse_text(text):
    # Odwraca podany ciąg znaków.
    return text[::-1]

def count_vowels(text):
    # Zlicza liczbę samogłosek w tekście.
    return sum(1 for char in text.lower() if char in "aeiouy")