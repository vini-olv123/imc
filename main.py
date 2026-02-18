from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def calcular():
    if request.method == 'POST':
        peso = int(request.form['peso'])
        altura = int(request.form['altura'])
        altura = altura / 100
        imc = peso / altura**2
        return render_template('home.html', imc=round(imc, 2))
    
    return render_template('home.html')

@app.route('/tabela')
def mostrar_tabela():
    return render_template('tabela.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)