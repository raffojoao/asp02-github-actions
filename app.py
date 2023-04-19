from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        return f"A soma de {num1} e {num2} é {num1 + num2}"
    return '''
        <form method="post">
            <p>Primeiro número: <input type="text" placeholder="Número 1" name="num1"></p>
            <p>Segundo número: <input type="text" placeholder="Número 2" name="num2"></p>
            <p><input type="submit" value="Somar"></p>
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0')
