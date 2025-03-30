def convert_to_int(value):
    # Konwertuje wartość na liczbę całkowitą.
    try:
        return int(value)
    except ValueError:
        return None