import pandas as pd
import random
import string
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/generate")
def generate_password(min_length=10, max_length=20):
    all_characters = list(string.ascii_letters + string.digits + string.punctuation)
    length = random.randint(min_length, max_length)
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password


@app.route("/calculate")
def calculate_average():
    df = pd.read_csv('hw.csv')
    average_height = df[' Height(Inches)'].mean()
    average_weight = df[' Weight(Pounds)'].mean()
    return (f'Avarage height: {average_height:.2f} inches <br>'
            f'Avarage weight: {average_weight:.2f} pounds')




if __name__ == '__main__':
    app.run(
        port=5000
    )
