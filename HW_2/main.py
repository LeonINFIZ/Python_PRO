import random
import time
from flask import Flask, Response, render_template_string
import pandas as pd
import csv

from skimage.transform import resize

app = Flask(__name__)


@app.route("/generate_password")
def generate_password():
    """
    from 10 to 20 chars
    upper and lower case

    string
    ascii_lowercase
    ascii_uppercase
    int
    special symbols
    return password
    """

    def stream():
        length = random.randint(10, 20)  # from 10 to 20 chars
        password = ""
        for _ in range(length):
            choice = random.randint(0, 3)
            if choice == 0:
                password += chr(random.randint(65, 90))  # ascii_uppercase
            elif choice == 1:
                password += chr(random.randint(97, 122))  # ascii_lowercase
            elif choice == 2:
                password += chr(random.randint(33, 47))  # special symbols
            elif choice == 3:
                password += str(random.randint(0, 9))  # int

        yield (f'<div id="pass" style="font-size: 100px; font-weight: bold; height: 100%; font-family: monospace;'
               f'display: flex; justify-content: center; align-items: center; color: red">{"*" * len(password)}</div>\n')

        for i in range(1, len(password) + 1):
            yield (f'<script>'
                   f'setTimeout(() => {{'
                   f'let password = document.getElementById("pass");'
                   f'let currentText = password.textContent;'
                   f'password.textContent = currentText.substring(0, {i - 1}) + "{password[i - 1]}" + currentText.substring({i});'
                   f'}}, {i * 100});'
                   f'</script>\n')

    return Response(stream(), content_type="text/html")


@app.route("/")
def main():
    return (
        f'<div style="width: 100%; height: 100%;  position: fixed; top: 0; left: 0; flex-direction: column; display: flex; align-items: center;'
        f'align-content: center; justify-content: center;">'
        f'<a href="/calculate_average"><button style="color: WHITE; padding: 10px 50px; font-size: 20px;'
        f'background-color: BLACK; font-family: monospace;">Calculate Average</button></a><br>'
        f'<a href="/generate_password"><button style="color: WHITE; padding: 10px 50px; font-size: 20px;'
        f'background-color: BLACK; font-family: monospace;">Generate Password</button></a>'
        f'</div>\n')


@app.route("/calculate_average")
def calculate_average():
    """
    csv file with students
    1.calculate average high
    2.calculate average weight
    csv - use lib
    *pandas - use pandas for calculating
    """

    result_str = ""

    # CSV ------------------------------------------

    csv_height_list = []
    csv_weight_list = []

    with open('hw.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        skip_header = False

        for row in reader:
            if skip_header:
                csv_height_list.append(float(row[1].strip()))
                csv_weight_list.append(float(row[2].strip()))

            skip_header = True

    csv_sum_height_list = 0
    csv_sum_weight_list = 0

    for i in range(0, len(csv_height_list)):
        csv_sum_height_list += csv_height_list[i]
        csv_sum_weight_list += csv_weight_list[i]

    result_str += f"Average of Height (CSV) &nbsp;&nbsp; = {round(csv_sum_height_list / len(csv_height_list), 2)}<br>"
    result_str += f"Average of Weight (CSV) &nbsp;&nbsp; = {round(csv_sum_weight_list / len(csv_weight_list), 2)}<br><br>"

    # CSV ------------------------------------------

    # PANDAS ------------------------------------------

    df = pd.read_csv('hw.csv')

    height_list = df["Height (Inches)"].mean()
    weight_list = df["Weight (Pounds)"].mean()

    result_str += f"Average of Height (Pandas) = {round(height_list, 2)}<br>"
    result_str += f"Average of Weight (Pandas) = {round(weight_list, 2)}"

    # PANDAS ------------------------------------------

    return (f'<div id="pass" style="font-size: 40px; font-weight: bold; height: 100%; font-family: monospace;'
            f'display: flex; justify-content: center; align-items: center; color: red">{result_str}</div>\n')


if __name__ == "__main__":
    app.run(port=8000, debug=True)
