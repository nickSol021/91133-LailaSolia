<?php

// Verifica se a requisição é POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    // Redireciona para a página inicial se for acesso direto
    header("Location: http://localhost:8081/app/index.html");
    exit;
}

// Recebe os dados do formulário
$produto = $_POST['produto'];
$tipo = $_POST['tipo'];
$quantidade = $_POST['quantidade'];

// Prepara a query SQL
$sql = "INSERT INTO produtos (produto, tipo, quantidade) VALUES (?, ?, ?)";

// Prepara o statement
$stmt = $conn->prepare($sql);
$stmt->bind_param("ssi", $produto, $tipo, $quantidade);

// Executa o insert
$stmt->execute();
$stmt->close();
?>