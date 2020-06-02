#!/usr/bin/python

from cmath import phase

if __name__ == "__main__":
    z = complex(input())
    # A complex number (a + bi) is composed of two things:
    # 1. Modulus: In this example, a is a modulus. This can be computed using abs(complex(a + bi))
    # 2. Phase: In this example, b is a phase. This can be computed using cmath.phase() like phase(complex(a+bi))
    print(abs(z))
    print(phase(z))
