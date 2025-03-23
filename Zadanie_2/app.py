from datetime import datetime

def is_valid_email(email):
    if '@' not in email or email.count('@') != 1:
        return False

    local, domain = email.split('@')

    if not local or not domain:
        return False

    if '.' not in domain or domain.startswith('.') or domain.endswith('.'):
        return False

    domain_parts = domain.split('.')
    if any(not part for part in domain_parts):
        return False

    if len(domain_parts[-1]) < 2:
        return False

    return True

def calculate_rectangle_area(width, height):
    if width < 0 or height < 0:
        raise ValueError("Wymiary muszą być dodatnie")
    return width * height

def filter_even_numbers(numbers):
    return [n for n in numbers if isinstance(n, int) and n % 2 == 0]

def convert_date_format(date_str):
    try:
        date = datetime.strptime(date_str, "%d-%m-%Y")
        return date.strftime("%Y/%m/%d")
    except ValueError:
        raise ValueError("Nieprawidłowy format daty. Użyj DD-MM-YYYY")

def is_palindrome(text):
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]
