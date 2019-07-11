from flask import Flask, request
import sqlite3
from flask import jsonify

app = Flask(__name__)

@app.route("/escolas", methods=['GET'])
def getEscolas():
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM tb_escola;
    """)
    escolas = list()
    for linha in cursor.fetchall():
        escolas = {
            "id_escolas": linha[0],
            "nome": linha[1],
            "logradouro": linha[2],
            "cidade": linha[3]
        }
        escolas.append(escolas)
    conn.close()
    return jsonify(escolas)

    return ("Listagem com sucesso", 200)

@app.route("/escolas/<int:id>", methods=['GET'])
def getEscolasByID(id):
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_escola
        WHERE id_escola = ?;
    """, (id, ))

        linha = cursor.fetchone()
        escolas = {
            "id_escolas": linha[0],
            "nome": linha[1],
            "logradouro": linha[2],
            "cidade": linha[3]
        }
    conn.close()
    return jsonify(linha)
    return("Executado!", 200)

@app.route("/escola", methods=['POST'])
def setEscola():
    print('Cadastrando a escola')
    nome = request.form["nome"]
    print(nome)
    logradouro = request.form["logradouro"]
    print(logradouro)
    cidade = request.form["cidade"]
    print(cidade)

    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tb_escola(nome, logradouro, cidade)
        VALUES(?, ?, ?);
    """, (nome, logradouro, cidade))

    conn.commit()
    conn.close()

    return("Inserido com sucesso!", 200)

@app.route("/alunos", methods=['GET'])
def getAlunos():
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_aluno;
    """)
    alunos = list()
    for linha in cursor.fetchall():
        alunos = {
            "id_aluno": linha [0],
            "nome": linha [1],
            "matricula": linha [2],
            "cpf": linha [3],
            "nascimento": linha [4]
        }
        alunos.append(alunos)
    conn.close()
    return jsonify(alunos)
    return("Executado!", 200)

@app.route("/alunos/<int:id>", methods=['GET'])
def getAlunosByID(id):
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_aluno
        WHERE id_aluno = ?;
    """,(id, ))

    linha = cursor.fetchone()
    aluno = {
        "id_aluno": linha[0],
        "nome": linha[1],
        "matricula": linha[2],
        "cpf": linha[3],
        "nascimento": linha[4]
    }
    conn.close()
    return jsonify(linha)
    return("Executado!", 200)

@app.route("/aluno", methods=['POST'])
def setAluno():
    print('Cadastrando o aluno')
    nome = request.form["nome"]
    print(nome)
    matricula = request.form["matricula"]
    print(matricula)
    cpf = request.form["cpf"]
    print(cpf)
    nascimento = request.form["nascimento"]
    print(nascimento)

    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tb_aluno(nome, matricula, cpf, nascimento)
        VALUES(?, ?, ?, ?);
    """, (nome, matricula, cpf, nascimento))

    conn.commit()
    conn.close()

    return("Executado!", 200)

@app.route("/cursos", methods=['GET'])
def getCursos():
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_curso;
    """)

    cursos = list()
    for linha in cursor.fetchall():
        cursos= {
            "id_curso": linha[0],
            "nome": linha[1],
            "turno": linha[2]
        }
        cursos.append(cursos)
    conn.close()
    return jsonify(cursos)
    return("Executado!", 200)

@app.route("/cursos/<int:id>", methods=['GET'])
def getCursosByID(id):
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_curso
        WHERE id_curso = ?;
    """, (id, ))

    linha = cursor.fetchone():
        cursos = {
            "id_curso": linha[0],
            "nome": linha[1],
            "turno": linha[2]
    }

    conn.close()
    return jsonify(linha)
    return("Executado!", 200)

@app.route("/curso", methods=['POST'])
def setCurso():
    print('Cadastrando o curso')
    nome = request.form["nome"]
    print(nome)
    turno = request.form["turno"]
    print(turno)

    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tb_curso(nome, turno)
        VALUES(?, ?);
    """, (nome, turno))

    conn.commit()
    conn.close()

    return("Executado!", 200)

@app.route("/turmas", methods=['GET'])
def getTurmas():
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_turma;
    """)

    turmas = list()
    for linha in cursor.fetchall():
        turmas= {
            "id_turma": linha [0],
            "nome": linha [1],
            "curso": linha [2]
        }
        turmas.append(turmas)
    conn.close()
    return jsonify(turmas)
    return("Executado!", 200)

@app.route("/turmas/<int:id>", methods=['GET'])
def getTurmasByID(id):
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_turma
        WHERE id_turma = ?
    """, (id, ))

    linha = cursor.fetchone()
        turmas= {
            "id_turma": linha [0],
            "nome": linha [1],
            "curso": linha [2]
        }


    conn.close()
    return jsonify(linha)
    return("Executado!", 200)

@app.route("/turma", methods=['POST'])
def setTurma():
    print('Cadastrando a turma')
    nome = request.form["nome"]
    print(nome)
    curso = request.form["curso"]
    print(curso)

    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tb_turma(nome, curso)
        VALUES(?, ?);
    """, (nome, curso))

    conn.commit()
    conn.close()

    return("Executado!", 200)

@app.route("/disciplinas", methods=['GET'])
def getDisciplinas():
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_disciplina;
    """)

    disciplinas = list()
    for linha in cursor.fetchall():
        disciplinas= {
            "id_disciplinas": linha [0],
            "nome": linha [1]
        }
    disciplinas.append(disciplinas)
    conn.close()
    return jsonify(disciplinas)
    return("Executado!", 200)

@app.route("/disciplinas/<int:id>", methods=['GET'])
def getDisciplinasByID(id):
    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tb_disciplina
        WHERE id_disciplina = ?
    """, (id, ))

    linha = cursor.fetchall()
        disciplinas= {
            "id_disciplinas": linha [0],
            "nome": linha [1]
        }

    conn.close()
    return jsonify(linha)
    return("Executado!", 200)

@app.route("/disciplina", methods=['POST'])
def setDisciplina():
    print('Cadastrando a disciplina')
    nome = request.form["nome"]
    print(nome)

    conn = sqlite3.connect('IFPB.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tb_disciplina(nome)
        VALUES(?);
    """, (nome, ))

    conn.commit()
    conn.close()

    return("Executado!", 200)

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
