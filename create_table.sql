create schema if not exists private;

create table private.aluno (
id serial primary key,
nome varchar(150) not null,
data_nasc date not null
);

create table private.funcionario (
id_func serial primary key,
nome varchar (150) not null,
data_nasc date not null
);

create table private.cargo(
id_cargo serial primary key,
id_func int not null,
cargo varchar (50) not null,
salario float not null,
FOREIGN KEY (id_func) REFERENCES private.funcionario (id_func)
);

create table private.end_aluno(
id serial primary key,
id_aluno int not null,
endereco varchar (200) not null,
FOREIGN KEY (id_aluno) REFERENCES private.aluno(id)
);

create table private.end_func(
id serial primary key,
id_func int not null,
endereco varchar (200) not null,
FOREIGN KEY (id_func) REFERENCES private.funcionario (id_func)
);

create table private.disciplina(
id_disciplina serial primary key,
id_professor int not null,
descricao varchar(100) not null,
FOREIGN KEY (id_professor) REFERENCES private.funcionario(id_func)
);

create table private.turma(
id serial primary key,
id_aluno int not null,
id_disciplina int not null,
turma varchar(100) not null,
FOREIGN KEY (id_aluno) REFERENCES private.aluno(id),
FOREIGN KEY (id_disciplina) REFERENCES private.disciplina(id_disciplina)
);