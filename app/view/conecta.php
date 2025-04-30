<?php

$host = "localhost";
$usuario = "root";
$senha = "";
$banco = "estoque";

// Cria a conexão
$conn = new mysqli($host, $usuario, $senha, $banco);

// Verifica se ocorreu erro
if ($conn->connect_error) {
    die("Erro na conexão: " . $conn->connect_error);
}
?>