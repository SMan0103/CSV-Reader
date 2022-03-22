import random
from dataclasses import dataclass

a=1
b=1
c=1

datapoints = []

@dataclass
class Datapoint:
    x: float
    y: float

# beregn y til x med globale a og b, hvis de ikke er givet i funktionskaldet
def f(x,_a=a,_b=b,_c=c):
    """funktionen til at optmiere"""
    # return _b*pow(x, _a)
    return _a*x*x+_b*x+_c

# Returner error ud fra variabelr
def e(_a,_b,_c):
    """angiv error"""

    _sum = 0
    for dp in datapoints:
        value = dp.y-f(dp.x, _a=_a, _b=_b, _c=_c)
        value *= value
        _sum += value
    return _sum

    #return sum([pow(_y-f(_x, _a=a, _b=b),2) for _x,_y in zip(x,y)])

def main():
    """main funktionen"""
    with open("data.csv", "r", encoding="utf-8") as file:
        for line in file:
            _x, _y = line.split(";")
            _x, _y = float(_x), float(_y)
            datapoints.append(Datapoint(_x, _y))

    # iteratikt prøv at forbedre erroren
    last_error = 9e9999999
    for _ in range(10240000):
        global a, b, c
        _a, _b, _c = a, b, c
        _a += random.uniform(-1, 1) * 20
        _b += random.uniform(-1, 1) * 20
        _c += random.uniform(-1, 1) * 20
        error = e(_a,_b,_c)
        if abs(error) < abs(last_error):
            a, b, c = _a, _b, _c
            last_error = error

    print(f"f(x)={a}x^2+{b}x+{c}")


if __name__ == "__main__":
    main()
