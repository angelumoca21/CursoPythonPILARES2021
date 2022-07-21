var productos = [];
function agregarItem(){
    var inputTexto = document.getElementById("cajaTexto");
    var texto = inputTexto.value;
    var textoProductos = document.getElementById("listaProductos");
    productos.push(texto);
    textoProductos.innerHTML= "";
    productos.forEach(item => textoProductos.innerHTML += `<li>${item}</li>`)
}