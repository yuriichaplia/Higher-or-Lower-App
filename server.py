import random
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home_page():
    return ('<h1>Guess a number between 0 and 9</h1> '
            '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjd1ODZoOWV3ZnUyd2s2OXh4c3poYWsyeWh5MjRnazBwbXhkdnhiNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Sy1m3x6DiJzOzeTDan/giphy.gif" width="450" height="350" />')

number = random.randint(0, 9)
@app.route('/<int:digit>')
def random_number(digit):
    if digit < number:
        return (f'<h1 style="color:red">Too low, try again!</h1> '
                f'<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
    elif digit > number:
        return (f'<h1 style="color:purple">Too high, try again!</h1> '
                f'<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
    else:
        return (f'<h1 style="color:green">You found me!</h1> '
                f'<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')


if __name__ == '__main__':
    app.run(debug=True)