import random
import math

un = 0
ra = 0
def main():
    print("HI")
    inside_square = 0
    inside_circle = 0

    _inside_square = 0
    _inside_circle = 0

    un = 0
    ra = 0

    for i in range(100001):
        x = random.uniform(1,0)
        y = random.uniform(1,0)
        _x = random.random()
        _y = random.random()
        inside_square += 1
        _inside_square += 1
        if( x * x + y * y < 1):
            inside_circle += 1
        if( _x * _x + _y * _y < 1):
            _inside_circle += 1

        pi = inside_circle / inside_square * 4
        diff = abs(pi - math.pi)
        un += diff
        _pi = _inside_circle / _inside_square * 4
        _diff = abs(_pi - math.pi)
        ra += _diff

        print(f"pi with unifor = {pi}\tdiff = {diff}\npi with random = {_pi}\tdiff = {_diff}\n\n")
        print(f"uniform = {un}\nrandom = {ra}\n")

if __name__ == "__main__":
    main()
