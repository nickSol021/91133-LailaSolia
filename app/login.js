function validarLogin() {
    let usuario = document.getElementById("usuario").value.trim();
    let senha = document.getElementById("senha").value.trim();

    if (usuario === "" || senha === "") {
        alert("Por favor, preencha todos os campos.");
        return false;
    }

    return true;
}