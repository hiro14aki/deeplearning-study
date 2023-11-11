import numpy as np


def and_gate(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


print('-- AND Gate --')
print(and_gate(0, 0))
print(and_gate(1, 0))
print(and_gate(0, 1))
print(and_gate(1, 1))


def and_gate_with_numpy(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


print('-- AND Gate with Numpy --')
print(and_gate_with_numpy(0, 0))
print(and_gate_with_numpy(1, 0))
print(and_gate_with_numpy(0, 1))
print(and_gate_with_numpy(1, 1))


def nand_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


print('-- NAND Gate --')
print(nand_gate(0, 0))
print(nand_gate(1, 0))
print(nand_gate(0, 1))
print(nand_gate(1, 1))


def or_gate(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


print('-- OR Gate --')
print(or_gate(0, 0))
print(or_gate(1, 0))
print(or_gate(0, 1))
print(or_gate(1, 1))


def xor_gate(x1, x2):
    s1 = nand_gate(x1, x2)
    s2 = or_gate(x1, x2)
    y = and_gate(s1, s2)
    return y


print('-- XOR Gate --')
print(xor_gate(0, 0))
print(xor_gate(1, 0))
print(xor_gate(0, 1))
print(xor_gate(1, 1))
