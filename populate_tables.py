import psycopg2
from faker import Faker
import random
from datetime import datetime, timedelta
 
fake = Faker()
 
# Conecte-se ao banco de dados
conn = psycopg2.connect(database="database", user="user", password="password", host="localhost", port="5432")
cur = conn.cursor()
 
# Configurar quantidade de registros para inserir
num_alunos = 100
num_funcionarios = 50
num_disciplinas = 20
num_turmas = 40
 
# Inserir alunos
for _ in range(num_alunos):
    nome = fake.name()
    data_nasc = fake.date_between(start_date='-30y', end_date='today')
    cur.execute("INSERT INTO private.aluno (nome, data_nasc) VALUES (%s, %s)", (nome, data_nasc))
 
# Inserir funcionarios
for _ in range(num_funcionarios):
    nome = fake.name()
    data_nasc = fake.date_between(start_date='-60y', end_date='-18y')
    cur.execute("INSERT INTO private.funcionario (nome, data_nasc) VALUES (%s, %s)", (nome, data_nasc))
 
conn.commit()
 
# Inserir cargos
cargos = ['Professor', 'Coordenador', 'Secretário']
salarios = [3000, 5000, 2000]
 
for i in range(1, num_funcionarios + 1):
    cargo = random.choice(cargos)
    salario = salarios[cargos.index(cargo)]
    cur.execute("INSERT INTO private.cargo (id_func, cargo, salario) VALUES (%s, %s, %s)", (i, cargo, salario))
 
# Inserir endereços de alunos
for i in range(1, num_alunos + 1 + random.randint(1, 5)):
    endereco = fake.address()
    cur.execute("INSERT INTO private.end_aluno (id_aluno, endereco) VALUES (%s, %s)", (i, endereco))
 
# Inserir endereços de funcionários
for i in range(1, num_funcionarios + 1 + random.randint(1, 5)):
    endereco = fake.address()
    cur.execute("INSERT INTO private.end_func (id_func, endereco) VALUES (%s, %s)", (i, endereco))
 
conn.commit()
 
# Inserir disciplinas
for _ in range(num_disciplinas):
    id_professor = random.randint(1, num_funcionarios)
    descricao = fake.catch_phrase()
    cur.execute("INSERT INTO private.disciplina (id_professor, descricao) VALUES (%s, %s)", (id_professor, descricao))
 
# Inserir turmas
for _ in range(num_turmas):
    id_aluno = random.randint(1, num_alunos)
    id_disciplina = random.randint(1, num_disciplinas)
    turma = fake.random_letter().upper() + str(fake.random_int(min=1, max=9))
    cur.execute("INSERT INTO private.turma (id_aluno, id_disciplina, turma) VALUES (%s, %s, %s)", (id_aluno, id_disciplina, turma))
 
conn.commit()
 
# Feche a conexão com o banco de dados
cur.close()
conn.close()
 
