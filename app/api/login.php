<?php
session_start();
include 'conexao.php';

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Recupera os dados do formulário
    $usuario = trim($_POST['usuario']);
    $senha   = trim($_POST['senha']);

    // Verifica se os campos não estão vazios
    if (empty($usuario) || empty($senha)) {
        echo "<script>
                alert('Preencha todos os campos.');
                window.location.href = 'index.html';
              </script>";
        exit;
    }

    // Prepara a consulta para buscar o usuário e validar a senha utilizando a função PASSWORD do MySQL
    $stmt = $conn->prepare("SELECT * FROM usuarios WHERE usuario = ? AND senha = PASSWORD(?)");
    $stmt->bind_param("ss", $usuario, $senha);
    $stmt->execute();
    $resultado = $stmt->get_result();

    if ($resultado->num_rows === 1) {
        // Login bem-sucedido: iniciar sessão e redirecionar
        $_SESSION['usuario'] = $usuario;
        echo "<script>
                alert('Login realizado com sucesso!');
                window.location.href = 'http://localhost:8081/app/cad.html';
              </script>";
    } else {
        // Login falhou: redireciona de volta ao login
        echo "<script>
                alert('Usuário ou senha incorretos!');
                window.location.href = 'http://localhost:8081/app/';
              </script>";
    }

    $stmt->close();
    $conn->close();
    exit;
} else {
    // Caso o acesso não seja via POST, redireciona para a página de login
    header("Location: index.html");
    exit;
}
?>