from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB('caminhos.json')

@app.route('/')
def index():
    caminhos = db.all()
    return render_template('index.html', caminhos=caminhos)

@app.route('/novo', methods=['GET', 'POST'])
def novo():
    if request.method == 'POST':
        nome = request.form['nome']
        pontos = {
            'x': request.form['x'],
            'y': request.form['y'],
            'z': request.form['z'],
            'r': request.form['r']
        }
        db.insert({'nome': nome, 'pontos': pontos})
        return redirect(url_for('index'))
    return render_template('novo.html')

@app.route('/pegar_caminho/<int:id>')
def pegar_caminho(id):
    caminho = db.get(doc_id=id)
    return render_template('pegar_caminho.html', caminho=caminho)

@app.route('/listas_caminhos')
def listas_caminhos():
    caminhos = db.all()
    return render_template('listas_caminhos.html', caminhos=caminhos)

@app.route('/atualizar/<int:id>', methods=['GET', 'POST'])
def atualizar(id):
    caminho = db.get(doc_id=id)
    
    if request.method == 'POST':
        nome = request.form['nome']
        pontos = {
            'x': request.form['x'],
            'y': request.form['y'],
            'z': request.form['z'],
            'r': request.form['r']
        }
        db.update({'nome': nome, 'pontos': pontos}, doc_ids=[id])
        return redirect(url_for('listas_caminhos'))
    
    return render_template('atualizar.html', caminho=caminho)

@app.route('/deletar/<int:id>')
def deletar(id):
    db.remove(doc_ids=[id])
    return redirect(url_for('listas_caminhos'))

if __name__ == '__main__':
    app.run(debug=True)
