// Array para almacenar los nombres de los amigos
let nombres = [];

// Función para agregar un amigo al array
function agregarAmigo() {
  const inputAmigo = document.getElementById("amigo");
  const listaAmigos = document.getElementById("listaAmigos");
  const nombre = inputAmigo.value.trim();

  if (nombre) {
    // Agregar nombre al array
    nombres.push(nombre);

    // Crear un nuevo elemento de lista
    const li = document.createElement("li");
    li.textContent = nombre;
    listaAmigos.appendChild(li);

    // Limpiar el campo de entrada
    inputAmigo.value = "";
    inputAmigo.focus();
  } else {
    alert("Por favor, escribe un nombre válido.");
  }
}

// Función para sortear un amigo secreto
function sortearAmigo() {
  const resultado = document.getElementById("resultado");

  // Limpiar resultados previos
  resultado.innerHTML = "";

  if (nombres.length < 2) {
    alert("Debes agregar al menos 2 nombres para realizar el sorteo.");
    return;
  }

  // Crear una copia del array para evitar modificaciones
  const nombresCopia = [...nombres];
  const sorteos = [];

  // Realizar el sorteo asegurando que nadie se asigne a sí mismo
  nombres.forEach((nombre) => {
    let posibleAmigo;
    do {
      const indice = Math.floor(Math.random() * nombresCopia.length);
      posibleAmigo = nombresCopia[indice];
    } while (posibleAmigo === nombre);

    // Asignar y eliminar el nombre sorteado
    sorteos.push(`${nombre} → ${posibleAmigo}`);
    nombresCopia.splice(nombresCopia.indexOf(posibleAmigo), 1);
  });

  // Mostrar los resultados en la lista
  sorteos.forEach((sorteo) => {
    const li = document.createElement("li");
    li.textContent = sorteo;
    resultado.appendChild(li);
  });
}
