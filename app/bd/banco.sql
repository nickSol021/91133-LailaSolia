-- Criação do banco de dados
CREATE DATABASE estoque;

-- Seleciona o banco de dados para uso
USE estoque;

-- Criação da tabela produtos
CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    quantidade INT NOT NULL
);