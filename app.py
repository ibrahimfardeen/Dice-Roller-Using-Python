from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll_dice', methods=['POST'])
def roll_dice():
    num_dice = int(request.form['num_dice'])
    dice_results = []
    for _ in range(num_dice):
        dice_results.append(random.randint(1, 6))
    return render_template('result.html', dice_results=dice_results)

if __name__ == '__main__':
    app.run(debug=True)
