# https://docs.python.org/3/library/functions.html#zip
# 1. zip() - iteruje po wieloktortnych sekwencjach danych, zwracając tuple, przy tym  przydzielając n-ty tuple do n-tego elementu z każdej iterowanej sekwencji. Domyślnie zip() kończy działanie, gdy najkrótsza z sekwencji się skończy. 

# Przykład  - zip() iteruje po dwóch listach id i name, zwracając tuple i, gdzie pierwszy element tuple to id, a drugi to name.
id = [1, 2, 3, 4, 5]
name = ['Marek', 'Tomek', 'Robert', 'Bob', 'JonasBrothers']
for i in zip(id, name):
    print(i)
  
print('-----------------------')
  
# https://docs.python.org/3/library/random.html#module-random
# 2. random() - moduł, który implementuje generator liczb pseudolosowych. Aby móc korzystać z funkcji modułu random, trzeba go zaimportować przy pomocy "import random".Dzięki modułowi można używać funkcji, które generują liczby losowe, np. randint(a, b) - zwraca losową liczbę całkowitą z przedziału [a, b]. random() - zwraca losową liczbę z przedziału [0.0, 1.0] oraz wiele innych, o których można poczytać więcej w dokumentacji :).


# Przykład 
import random as r
print(f'Liczba z przedziału (1,20): {r .randint(1,20)}')
print(f'Liczba z przedziału (0,1): {r.random()}')

print('-----------------------')

# https://docs.python.org/pl/3.13/reference/compound_stmts.html#except
# 3. try-except - pozwala na obsługę wyjątków w Pythonie. W bloku try umieszczamy kod, który chcemy wykonać, a w bloku except obsługę wyjątków. Jeśli w bloku try wystąpi wyjątek, program przechodzi do bloku except, gdzie obsługujemy wyjątek jak w podanych przykładach poniżej.

# Przykład 1 - x nie jest zdefiniowane, więc program przechodzi do bloku except, gdzie wypisuje "An exception occurred"
try:
  print(x)
except:
  print("An exception occurred")
  
# Przykład 2 - x jest zdefiniowane, więc program wypisuje "Hello World" i blok except nie jest wykonywany

x = "Hello World"
try:
  print(x)
except:
  print("An exception occurred")