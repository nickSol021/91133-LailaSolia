<?php
// Verifica se a requisição é POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    // Redireciona para a página inicial se for acesso direto
    header("Location: http://localhost:8081/app/index.html");
    exit;
}

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