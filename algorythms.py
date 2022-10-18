import os
from PIL import Image
import math
import numpy as np
import random


def roots(a, b, c):
    delta = pow(b, 2) - 4 * a * c
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / 2 * a
        x2 = (-b + math.sqrt(delta)) / 2 * a
        return x1, x2
    else:
        print("no roots")
    return


def sort(number):
    change = False
    n = len(number)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if number[j] > number[j + 1]:
                change = True
                number[j], number[j + 1] = number[j + 1], number[j]
        if not change:
            return
    return number


def countScalar(vector1, vector2):
    n = len(vector1)
    result = 0
    for i in range(0, n):
        result = result + vector1[i] * vector2[i]

    return result

def sumMatrix(matrix1,matrix2):
    print(matrix1)
    print()
    print(matrix2)
    print()
    sum = np.empty((len(matrix1), len(matrix1)))
    for i in range(0, len(matrix1)):
        for j in range(0, len(matrix1)):
            sum[i][j] = matrix1[i][j] + matrix2[i][j]
    print(sum)
    return sum
def multiplyMatrix(matrix1,matrix2):
    print(matrix1)
    print()
    print(matrix2)
    print()
    multiply = np.empty((len(matrix1), len(matrix1)))
    for i in range(0, len(matrix1)):
        for j in range(0, len(matrix1)):
            multiply[i][j] = matrix1[i][j] * matrix2[i][j]
    print(multiply)
    return multiply

def calculateDet(matrix):
    return np.linalg.det(matrix)

def main():


    print(roots(1, 1, -2))

    randomNumbers = []

    for i in range(0, 50):
        num = random.randint(1, 30)
        randomNumbers.append(num)
    print(randomNumbers)
    print(sort(randomNumbers))
    print(countScalar([1, 2, 12, 4], [2, 4, 2, 8]))
    print(np.dot([1, 2, 12, 4], [2, 4, 2, 8]))
    matrix1 = np.random.randint(10, size=(128, 128))
    matrix2 = np.random.randint(10, size=(128, 128))

    print("Summing matrix:\n")
    sum = sumMatrix(matrix1, matrix2)
    matrix3 = matrix1 + matrix2
    print(matrix3)
    print(np.array_equal(matrix3,sum))
    print("\nMultiplying matrix:\n")
    multi = multiplyMatrix(matrix1, matrix2)
    matrix3 = (matrix1 * matrix2)
    print(matrix3)
    print(np.array_equal(matrix3, multi))
    matrix = np.random.randint(10, size=(3, 3))
    print(matrix)
    print(calculateDet(matrix))


if __name__ == '__main__':
    main()