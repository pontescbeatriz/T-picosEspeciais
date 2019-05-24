from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello_word():
    return ("Olá mundo! Estou aprendendo Flask" , 2008)

@app.route("/alunos", methods=['GET'])
def getAlunos():
    conn = sqlite3.connect('escola2.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_aluno;
    """)

    for linha in cursor.fetchall():
        print(linha)
        conn.close()

    return ("Executado", 200)


@app.route("/alunos/<id>", methods = ['GET'])
def getAlunosByID(id):
    pass

@app.route("/aluno", methods = ['POST'])
def setAluno():
    print('Cadastrando o aluno')
    return ('Cadastrado com sucesso', 200)

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
