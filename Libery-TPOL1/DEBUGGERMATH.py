import sys

# Setze das maximale Limit für die Zeichenlänge der Darstellung von Ganzzahlen
sys.set_int_max_str_digits(10**6)

def calcFak(value):
    if value == 0 or value == 1:
        return 1
    else:
        result = 1
        for i in range(2, value + 1):
            result *= i
        return result

# Test Area
print(calcFak(200000))
