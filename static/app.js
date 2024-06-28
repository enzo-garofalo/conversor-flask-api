function atualizarResultado() {
    // Obtendo o valor da conversão por unidade
    const valor = parseFloat(document.getElementById('valor').innerText);
    // Obtendo o valor de entrada do usuário
    const entrada = parseFloat(document.getElementById('entrada').value);
    // Calculando o resultado
    const resultado = valor * entrada;
    // Atualizando o campo de resultado
    document.getElementById('resultado').innerText = isNaN(resultado) ? 0 : resultado.toFixed(2);
}