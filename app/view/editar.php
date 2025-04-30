<?php
include 'conecta.php';

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    // Pegando o ID via GET
    if (!isset($_GET['id'])) {
        header( "Location: listar.php");
        exit;
    }

    $id = intval($_GET['id']);

    $sql = "SELECT * FROM produtos WHERE id = $id";
    $resultado = $conn->query($sql);

    if ($resultado->num_rows != 1) {
        echo "<script>alert('Produto não encontrado.'); window.location.href='listar.php';</script>";
        exit;
    }

    $produto = $resultado->fetch_assoc();
} elseif ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Atualizando o produto via POST
    $id = intval($_POST['id']);
    $nome = $_POST['produto'];
    $tipo = $_POST['tipo'];
    $quantidade = intval($_POST['quantidade']);

    if (empty($nome) || empty($tipo) || empty($quantidade)) {
        echo "<script>alert('Todos os campos são obrigatórios!'); window.history.back();</script>";
        exit;
    }

    $sql = "UPDATE produtos SET produto='$nome', tipo='$tipo', quantidade=$quantidade WHERE id=$id";

    if ($conn->query($sql) === TRUE) {
        echo "<script>alert('Produto atualizado com sucesso!'); window.location.href='listar.php';</script>";
    } else {
        echo "<script>alert('Erro ao atualizar o produto.'); window.location.href='listar.php';</script>";
    }

    $conn->close();
    exit;
}
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Controle de Estoque 1.0 - SENAI FFSA</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<h1>Controle de Estoque 1.0 - SENAI FFSA</h1>

<form method="POST" action="editar.php">
    <input type="hidden" name="id" value="<?php echo $produto['id']; ?>">

    <label for="produto">Produto:</label>
    <input type="text" id="produto" name="produto" value="<?php echo htmlspecialchars($produto['produto']); ?>" required>

    <label for="tipo">Tipo:</label>
    <select id="tipo" name="tipo" required>
        <option value="">Selecione</option>
        <option value="Eletrônico" <?php if($produto['tipo'] == 'Eletrônico') echo 'selected'; ?>>Eletrônico</option>
        <option value="Mecânico" <?php if($produto['tipo'] == 'Mecânico') echo 'selected'; ?>>Mecânico</option>
        <option value="Papelaria" <?php if($produto['tipo'] == 'Papelaria') echo 'selected'; ?>>Papelaria</option>
    </select>

    <label for="quantidade">Quantidade:</label>
    <input type="number" id="quantidade" name="quantidade" value="<?php echo $produto['quantidade']; ?>" required>

    <input type="submit" value="Atualizar">
</form>

<div class="btn-voltar">
    <a href="listar.php">
        <button>Voltar à Lista</button>
    </a>
</div>

</body>
</html>