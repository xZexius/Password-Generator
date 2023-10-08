from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_password():
    length = int(request.form.get('length', 12))
    include_letters = 'letters' in request.form
    include_numbers = 'numbers' in request.form
    include_symbols = 'symbols' in request.form

    characters = string.ascii_letters if include_letters else ''
    characters += string.digits if include_numbers else ''
    characters += string.punctuation if include_symbols else ''

    if not characters:
        return "Debes seleccionar al menos un tipo de carácter."

    password = ''.join(random.choice(characters) for _ in range(length))
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
