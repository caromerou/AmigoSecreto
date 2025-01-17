// Array para guardar los nombres de los amigos
let nombres = [];

// Función para agregar un amigo al array
function agregarAmigo() {
    const inputAmigo = document.getElementById("amigo");
    const listaAmigos = document.getElementById("listaAmigos");
    const nombre = inputAmigo.value.trim();

    if (nombre) {
        // Verificar si el nombre ya existe
        if (nombres.includes(nombre)) {
            alert("Este nombre ya está en la lista.");
        } else {
            nombres.push(nombre);
            const li = document.createElement("li");
            li.textContent = nombre;

            const botonEditar = document.createElement("button");
            botonEditar.textContent = "Editar";
            botonEditar.onclick = () => actualizarAmigo(nombre, li);

            const botonEliminar = document.createElement("button");
            botonEliminar.textContent = "Eliminar";
            botonEliminar.onclick = () => eliminarAmigo(nombre, li);

            li.appendChild(botonEditar);
            li.appendChild(botonEliminar);
            listaAmigos.appendChild(li);

            inputAmigo.value = "";
            inputAmigo.focus();
        }
    } else {
        alert("Por favor, escribe un nombre válido.");
    }
}

// Función para actualizar un amigo
function actualizarAmigo(nombre, li) {
    const nuevoNombre = prompt("Ingresa el nuevo nombre:", nombre);
    if (nuevoNombre && nuevoNombre.trim() !== "" && !nombres.includes(nuevoNombre.trim())) {
        const index = nombres.indexOf(nombre);
        nombres[index] = nuevoNombre.trim();

        li.firstChild.textContent = nuevoNombre;

        li.querySelector("button:nth-child(1)").onclick = () => actualizarAmigo(nuevoNombre, li);
        li.querySelector("button:nth-child(2)").onclick = () => eliminarAmigo(nuevoNombre, li);
    } else {
        alert("El nombre no es válido o ya existe en la lista.");
    }
}

// Función para eliminar un amigo
function eliminarAmigo(nombre, li) {
    if (confirm(`¿Estás seguro de que deseas eliminar a ${nombre}?`)) {
        nombres = nombres.filter((n) => n !== nombre);
        li.remove();
    }
}

// Función para sortear un amigo secreto
function sortearAmigo() {
    const resultado = document.getElementById("resultado");
    resultado.innerHTML = "";

    if (nombres.length < 2) {
        alert("Debes agregar al menos 2 nombres para realizar el sorteo.");
        return;
    }

    const nombresCopia = [...nombres];
    const sorteos = [];

    nombres.forEach((nombre) => {
        let posibleAmigo;
        do {
            const indice = Math.floor(Math.random() * nombresCopia.length);
            posibleAmigo = nombresCopia[indice];
        } while (posibleAmigo === nombre);

        sorteos.push(`${nombre} → ${posibleAmigo}`);
        nombresCopia.splice(nombresCopia.indexOf(posibleAmigo), 1);
    });

    sorteos.forEach((sorteo) => {
        const li = document.createElement("li");
        li.textContent = sorteo;
        resultado.appendChild(li);
    });
}
