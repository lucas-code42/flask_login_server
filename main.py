from flask import *
import mysql.connector
from acess import MysqlAcess
from autenticar_login import autenticar_mysql
from cadastro_login import cadastrar_mysql


app = Flask(__name__)
app.secret_key = 'secret'


global user_acess
user_acess = MysqlAcess.user_acess()

global password_acess
password_acess = MysqlAcess.password_acess()



@app.route('/')
def index():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')
    else:
        return render_template('index.html')


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/autenticar', methods=['POST',])
def autenticar():
    session['usuario_logado'] = request.form['usuario']
    user = request.form['usuario']
    password = request.form['senha']
    verificar_user_pass = autenticar_mysql(user, password)
    if verificar_user_pass == False:
        flash('Usuário ou senha não encontrados')
        return redirect('/cadastro')
    if verificar_user_pass != False:
        lista = verificar_user_pass[:]
        user = lista[0]
        password = lista[1]
        if user == request.form['usuario']:
            if password == request.form['senha']:
                flash(user + ' logado com sucesso!')
                return redirect('/')


@app.route('/cadastro')
def criar_novo_cadastro():
    return render_template('cadastro.html')


@app.route('/enviar_cadastro', methods=['POST',])
def enviar_dados():
    nome = request.form['nome']
    email = request.form['email']
    celular = request.form['celular']
    senha = request.form['senha']
    enviar = cadastrar_mysql(nome, email, celular, senha)
    if enviar == True:
        flash('Cadastro realizado com sucesso!')
        return redirect('/')
    elif enviar == False:
        flash('Algo deu errado! Tente novamente.')
        return redirect('/cadastro')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect('/login')


app.run(debug=True, host='0.0.0.0', port=8080)