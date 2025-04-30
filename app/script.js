// Função que valida os campos do formulário
function validarFormulario() {
    const produto = document.getElementById("produto").value;
    const tipo = document.getElementById("tipo").value;
    const quantidade = document.getElementById("quantidade").value;

    // Verifica se algum campo está vazio
    if (produto === "" || tipo === "" || quantidade === "") {
        alert("Por favor, preencha todos os campos.");
        return false; // Impede o envio do formulário
    }

    return true; // Permite o envio do formulário
}