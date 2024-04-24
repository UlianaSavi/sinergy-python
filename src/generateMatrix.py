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
        print("\n\033[32mРезультат сложения матриц A и B: {}".format(self.matrixSum))
        print("\033[32mСпасибо за использование скрипта! Досвидания!\n")
        sys.exit()

    def ask(self):
        try:
            columnSize = int(input("\033[35mВведите размер матриц по колонкам: "))
            rowSize = int(input("\033[35mВведите размер матриц по строкам:  "))
            if bool(columnSize) and bool(rowSize):
                self.matrixA = self.generateMatrix(columnSize, rowSize)
                self.matrixB = self.generateMatrix(columnSize, rowSize)
            else:
                self.matrixA = self.generateMatrix()
                self.matrixB = self.generateMatrix()
            print("\033[32mГенерирую первую матрицу...")
            print("\033[32mРезультат: {}\n".format(self.matrixA))
            print("\033[32mГенерирую вторую матрицу...")
            print("\033[32mРезультат: {}\n".format(self.matrixB))
            print("\033[32mВыполняю сложение двух матриц...")

            self.getMatrixSum(self.matrixA, self.matrixB)

        except ValueError:
            print("\n\033[33mВы ввели неверное значение, попробуйте снова!\n")
            self.ask()
        except KeyboardInterrupt:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()
        except:
            print("\n\033[33mВы вышли из скрипта. Досвидания!\n")
            sys.exit()

    def generateMatrix(self, columnSize=defaultMatrixSize, rowSize=defaultMatrixSize):
        return [
            [random.randint(0, rowSize) for column in range(rowSize)]
            for row in range(columnSize)
        ]

    def getMatrixSum(self, matrixA, matrixB):
        result = [
            [matrixA[i][j] + matrixB[i][j] for j in range(len(matrixA[0]))]
            for i in range(len(matrixA))
        ]
        for r in result:
            self.matrixSum.append(r)


newEx = GenerateMatrix()
