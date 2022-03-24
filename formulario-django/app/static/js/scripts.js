function calcular() {
    var num1 = Number(document.getElementById("form.preco").value)
    var num2 = Number(document.getElementById("form.quantidade").value)
    var elemResult = document.getElementById("total")

    elemResult.textContent = " R$ " + (num1 * num2).toFixed(2)


}