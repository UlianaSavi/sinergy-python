import sys
import random


class GenerateMatrix:
    defaultMatrixSize = 10

    def __init__(self):
        self.matrixSum = []
        self.matrixA = []
        self.matrixB = []
        print("\033[32mПривет!\n")
        self.ask()
        print("\n\033[32mРезультат: {}".format(self.matrixSum))
        print("\033[32mСпасибо за использование скрипта! Досвидания!\n")
        sys.exit()

    def ask(self):
        try:
            print("\033[32mГенерирую первую матрицу...\n")
            self.matrixA = self.generateMatrix()
            print("\033[32mРезультат: {}".format(self.matrixA))
            print("\033[32mГенерирую вторую матрицу...\n")
            self.matrixB = self.generateMatrix()
            print("\033[32mРезультат: {}".format(self.matrixB))
            print("\033[32mВыполняю сложение двух матриц...\n")
            self.matrixSum = self.getMatrixSum(self, self.matrixA, self.matrixB)
        except ValueError:
            print("\n\033[33mВы ввели неверное значение, попробуйте снова!\n")
            self.ask()
        except KeyboardInterrupt:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()
        except:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()

    def generateMatrix(self, size=defaultMatrixSize):
        return [
            [random.randint(0, size) for column in range(size)] for row in range(size)
        ]

    def getMatrixSum(self, matrixA, matrixB):
        return []


newEx = GenerateMatrix()
