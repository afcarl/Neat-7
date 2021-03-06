import numpy


alpha = 1.6732
beta = 1.0507


def identity(a: float) -> float:
    return a


def sigmoid(a: float) -> float:
    return 1 / (1 + numpy.exp(-5 * a))


def relu(a: float) -> float:
    return 0 if a < 0 else a


def sine(a: float) -> float:
    return numpy.sin(a * numpy.pi)


def binary(a: float) -> float:
    return 0 if a < 0 else 1


def gaussian(a: float) -> float:
    return numpy.exp(-(a**2))


def selu(a: float) -> float:
    return beta * (a if a > 0 else alpha * numpy.exp(a) - alpha)
