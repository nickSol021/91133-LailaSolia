function iniciarSistema() {
    // Criar o formulário
    const form = document.createElement('form');
    const fields = ['username', 'password', 'preco', 'quantidade'];

    // Criando os campos do formulário
    fields.forEach(field => {
        const div = document.createElement('div');
        const label = document.createElement('label');
        const input = document.createElement('input');
        
        label.setAttribute('for', field);
        label.textContent = field.charAt(0).toUpperCase() + field.slice(1); // Primeira letra maiúscula
        input.setAttribute('type', field === 'preco' || field === 'quantidade' ? 'number' : 'text');
        input.setAttribute('id', field);
        if (field === 'preco') input.setAttribute('step', '0.01');
        
        div.appendChild(label);
        div.appendChild(input);
        form.appendChild(div);
    });

    // Criando o botão de submit
    const submitButton = document.createElement('button');
    submitButton.textContent = 'Adicionar Produto';
    form.appendChild(submitButton);

    // Criando a tabela
    const tabela = document.createElement('table');
    const tabelaHead = document.createElement('thead');
    const tr = document.createElement('tr');
    ['Username', 'Password', 'Preço', 'Quantidade'].forEach(text => {
        const th = document.createElement('th');
        th.textContent = text;
        tr.appendChild(th);
    });
    tabelaHead.appendChild(tr);
    tabela.appendChild(tabelaHead);
    tabela.appendChild(document.createElement('tbody'));

    // Adicionando o formulário e a tabela ao documento
    document.body.appendChild(form);
    document.body.appendChild(tabela);

    // Evento do formulário
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const data = fields.map(field => document.getElementById(field).value);
        
        const novaLinha = document.createElement('tr');
        data.forEach(d => {
            const td = document.createElement('td');
            td.textContent = d;
            novaLinha.appendChild(td);
        });

        tabela.querySelector('tbody').appendChild(novaLinha);
        form.reset();
    });
}

iniciarSistema();














//atualiza o total automaticamente
document.getElementById("preco").addEventListener("input", cacularTotal);
document.getElementById("quantidade").addEventListener("input", cacularTotal);


fuction calcularTotal(){
    const preco = parseFloat(document.getElementById("preco").value);
    const quantidade = parseInt(document.getElementById("quantidade").value);
    const totalField= document.getElementById("total");


if (!isNaN(preco) && !isNaN(quantidade)){
    totalField.value = (preco * quantidade).toFixed(2);
}else{
    totalField.value = "";

}
}





















