
function bloquear_caracteres_especiais(input) {
    var regex = /[!@#$%^&*()_+{}\[\]:;<>,.?~\/\\=-]/g;
    input.value = input.value.replace(regex, '');
}
function bloquear_numeros(input) {
    var regex = /[0-9]/g;
    input.value = input.value.replace(regex, '');
}
function receber_apenas_letras(input) {
    var regex = /[^a-zA-Z ]/g;
    input.value = input.value.replace(regex, '');
}
