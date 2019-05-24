import sqlite3

conn = sqlite3.connect('escola.db')

cursor = conn.cursor()



cursor.execute("""
 CREATE TABLE tb_aluno(
   id_aluno INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT,
   nome VARCHAR(45) NOT NULL,
   matricula VARCHAR(12) NOT NULL,
   cpf VARCHAR(11)NOT NULL,
   nascimento DATE NOT NULL

 );
""")
 print ("tabela tb_aluno foi criada.")

cursor.execute("""
 CREATE TABLE tb_curso (
  id_curso INTERGER NOT NULL PRIMARY KEY  AUTOINCREMENT,
   nome VARCHAR(45) NOT NULL,
   Turno VARCHAR(1)

 );
""")
print ("tabela tb_CURSO foi criada.")

conn.close()

cursor.execute("""
 CREATE TABLE  tb_turma(
 id_turma INTERGER NOT NULL PRIMARY KEY  AUTOINCREMENT,
 curso INTEGER


 );
""")
print ("tabela tb_turma foi criada.")
