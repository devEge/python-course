class BMI:

    @staticmethod
    def calculate(weight: int, height: int):
        return float(weight) / ((float(height) / 100) ** 2)

