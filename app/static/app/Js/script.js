if (!localStorage.getItem('carrito')) {
    localStorage.setItem('carrito', JSON.stringify([]));
}

// Función para verificar el contenido del carrito (opcional, solo para depuración)
function verificarCarrito() {
    let carrito = JSON.parse(localStorage.getItem('carrito'));
    console.log('Contenido del carrito:', carrito);
}

function añadirAlCarrito(comicId, comicNombre, comicPrecio, comicImagen) {
    let carrito = JSON.parse(localStorage.getItem('carrito'));

    let comicEnCarrito = carrito.find(item => item.id === comicId);

    if (comicEnCarrito) {
        comicEnCarrito.cantidad += 1;
    } else {
        carrito.push({ id: comicId, nombre: comicNombre, precio: comicPrecio, imagen: comicImagen, cantidad: 1 });
    }

    localStorage.setItem('carrito', JSON.stringify(carrito));

    alert('¡Cómic añadido al carrito exitosamente!');
    verificarCarrito(); // Llamar a la función para depurar
}

function actualizarCarrito() {
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    let listaCarrito = document.getElementById('lista-carrito');
    let totalCarrito = document.getElementById('total-carrito');

    listaCarrito.innerHTML = ''; // Limpiar la lista antes de actualizar

    let total = 0;

    carrito.forEach(item => {
        let li = document.createElement('li');
        li.classList.add('carrito-item');

        // Crear elementos para cada item
        let img = document.createElement('img');
        img.src = item.imagen;
        img.alt = item.nombre;
        img.style.width = '100px'; // Ajusta el tamaño de la imagen según sea necesario

        let nombre = document.createElement('p');
        nombre.textContent = item.nombre;

        let precio = document.createElement('p');
        precio.textContent = `Precio: ${item.precio}`;

        let cantidad = document.createElement('p');
        cantidad.textContent = `Cantidad: ${item.cantidad}`;

        // Añadir los elementos al li
        li.appendChild(img);
        li.appendChild(nombre);
        li.appendChild(precio);
        li.appendChild(cantidad);

        // Añadir el li a la lista del carrito
        listaCarrito.appendChild(li);

        // Sumar el total
        total += item.cantidad * item.precio;
    });

    totalCarrito.textContent = `Total: ${total.toFixed(2)}`;
}

// Función para vaciar el carrito
function vaciarCarrito() {
    localStorage.removeItem('carrito');
    actualizarCarrito();
}

// Añadir event listeners a los botones
document.getElementById('vaciar-carrito').addEventListener('click', vaciarCarrito);

// Mostrar el carrito al cargar la página
window.onload = actualizarCarrito;