import os
from PIL import Image
import math
import numpy as np
import random






def addComplexNumbers(number1, number2):
    if type(number1) != ComplexNumber or type(number2) != ComplexNumber:
        return
    return ComplexNumber(number1.real + number2.real, number1.imag + number2.imag)

def subtractComplexNumbers(number1, number2):
    if type(number1) != ComplexNumber or type(number2) != ComplexNumber:
        return
    return ComplexNumber(number1.real - number2.real, number1.imag - number2.imag)

def multiplyComplexNumbers(number1, number2):
    if type(number1) != ComplexNumber or type(number2) != ComplexNumber:
        return
    realValue = number1.real * number2.real - abs(number1.imag * number2.imag)
    imagValue = number1.real * number2.imag + number1.imag * number2.real

    return ComplexNumber(realValue, imagValue)

def divideComplexNumbers(number1, number2):
    if type(number1) != ComplexNumber or type(number2) != ComplexNumber:
        return

    modulator = ComplexNumber(number2.real, -number2.imag)
    denominator = multiplyComplexNumbers(number1, modulator)
    divider = multiplyComplexNumbers(number2, modulator)

    return ComplexNumber(denominator.real/divider.real, denominator.imag/divider.real)

def getComplexNumber(text):
    real = ""
    img = ""
    waitForImaginary = False
    text = text.replace(" ","")

    for i in text:
        if i == "i":
            break
        if i == "+" or i == "-":
            waitForImaginary = True
        if (i != "+" or i != "-") and not waitForImaginary:
            real = real+i
        elif waitForImaginary:
            img = img+i


    if real == "+" or real == "-" or real == "*" or real == "/":
        real = "0"
        img = "0"

    if ("i" in text) and img == "":
        img = str(real)
        real = "0"

    elif img == "":
        img = "0"



    return ComplexNumber(int(real), int(img))






class ComplexNumber:
    def __init__(self, real , imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real}+{self.imag}i"
        else:
            return f"{self.real}{self.imag}i"

    def __add__(self, other):
        if type(self) != ComplexNumber or type(other) != ComplexNumber:
            return
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        if type(self) != ComplexNumber or type(other) != ComplexNumber:
            return
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        if type(self) != ComplexNumber or type(other) != ComplexNumber:
            return
        realValue = self.real * other.real - abs(self.imag * other.imag)
        imagValue = self.real * other.imag + self.imag * other.real

        return ComplexNumber(realValue, imagValue)

    def __truediv__(self, other):
        if type(self) != ComplexNumber or type(other) != ComplexNumber:
            return

        modulator = ComplexNumber(other.real, -other.imag)
        denominator = multiplyComplexNumbers(self, modulator)
        divider = multiplyComplexNumbers(other, modulator)

        return ComplexNumber(denominator.real / divider.real, denominator.imag / divider.real)

def simpleCalculator():
    number = ComplexNumber(0, 0)
    sign = ""
    x = ""
    while True:
    #dodać przeładowanie operatorów
        print("Enter number or cancel(c): ")
        x = input()
        if x == "c":
            break
        complex = getComplexNumber(x)
        if sign == "":
            number = complex
        elif sign == "+":
            number +=complex
            sign = ""
        elif sign == "-":
            number -=complex
            sign = ""
        elif sign == "*":
            number *= complex

            sign = ""
        elif sign == "/":
            try:
                number /=complex
            except ZeroDivisionError:
                print("Cannot divide by 0")
                return
            sign = ""
        print("Enter operation sign:")
        sign = input()
        if sign == "=":
            break

    if x == "c":
        return

    else:
        print("Result: " + str(number))

def main():
   simpleCalculator()



if __name__ == '__main__':
    main()



