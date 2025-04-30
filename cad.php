<?php

// configuracao de bonco de dados

$host = "locathost";
$user = "root";
$pass = ""; //senha do MySQL
$dbname "cadastro_produtos";

//conexao com o banco
$iconn = new mysql($host,$user, $pass, $dbname);

//verifica conexao
if($iconn -> connect_error){
    die("conexao falhou!". $iconn -> connect_error;);
}

echo("conectado!");


?>



// captura e valida os dados
$produto = trim($_POST['produto']?? '');
$preco = floatval($POST]['preco'] ?? 0);
$quantidade = intval($_POSTPOST ['quantidade'] ?? 0);
$total = floatval($_POST ['total'] ?? 0);


if ($produto === || $preco <= 0 || $quantidade <= 0){
    echo ("Dados invalidos!");
    exit;
}                                                  



//prepara a insercao 

$start= $iconn -> prepare("INSERT INTO produtos, preco, qauntidade, total");
VALUES (?,?,?,?);
//executa e verifica 
if (&start )





























