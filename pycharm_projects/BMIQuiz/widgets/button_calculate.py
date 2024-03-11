import tkinter as tk

from services.bmi import BMI


class ButtonCalculate:
    def _calculate(self):
        weight = self.weight_entry.getData()
        height = self.height_entry.getData()
        if not weight == "" or not height == "":
            bmi = BMI.calculate(int(weight), int(height))
            result_string = f"Your BMI is {round(bmi, 2)} You are "
            if bmi <= 16:
                result_string += "severely thin!"
            elif 16 < bmi <= 17:
                result_string += "moderately thin!"
            elif 17 < bmi <= 18.5:
                result_string += "mild thin!"
            elif 18.5 < bmi <= 25:
                result_string += "normal weight"
            elif 25 < bmi <= 30:
                result_string += "overweight"
            elif 30 < bmi <= 35:
                result_string += "obese class 1"
            elif 35 < bmi <= 40:
                result_string += "obese class 2"
            else:
                result_string += "obese class 3"
            self.result_label.set_result(result_string)
        else:
            self.result_label.set_result("Please enter a valid data!")

    def __init__(self, root, weight_entry, height_entry, result_label):
        self.weight_entry = weight_entry
        self.height_entry = height_entry
        self.result_label = result_label
        self._button = tk.Button(root, text="Calculate", command=lambda w=weight_entry, h=height_entry: self._calculate())
        self._button.pack(padx=5, pady=5)
