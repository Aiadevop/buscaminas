function showVictoryMessage(message) {
    const victoryMessage = document.createElement('div');
    victoryMessage.classList.add('victory-message');
    
    // Texto con animación
    victoryMessage.innerHTML = `<span class="animation">${message}</span>`;
    
    // Añadir el mensaje a la página
    document.body.appendChild(victoryMessage);
    
    // Mostrar el mensaje con la animación
    victoryMessage.style.display = 'block';
    
    // Eliminar el mensaje después de unos segundos
    setTimeout(() => {
        victoryMessage.style.display = 'none';
        document.body.removeChild(victoryMessage);
    }, 5000); // 5 segundos
}

function addEvents() {
    const cells = document.querySelectorAll('.cell');
    const formPlay = document.getElementById('form-play');
    const icons = document.querySelectorAll('.icon');

    cells.forEach(cell => {
        cell.addEventListener('click', function () {
            const row = this.getAttribute('data-row');
            const col = this.getAttribute('data-col');
            state = formPlay.getAttribute('data-play');
            const icon = "img_" + row + col;
            const iconDiv = document.querySelector(`[data-img='${icon}']`);
            if(iconDiv.style.display =='block'){
                return;
            }
            if (iconDiv) {
                iconDiv.style.display = 'block';  // Mostrar el icon relacionado con esa cell
            }
            // Enviar la jugada al servidor
            document.getElementById('row').value = row;
            document.getElementById('col').value = col;
            if (state == 'play') {
                // Hacer la solicitud POST al servidor
                fetch('/play', {
                    method: 'POST',
                    body: new FormData(document.getElementById('form-play'))
                })
                    .then(response => response.json())
                    .then(data => {
                        if (data.status == 0) {
                            // alert(data.msg); // Mensaje: Sigue jugando!
                        } else if (data.status == 1) {
                            // alert(data.msg); // Mensaje: Game Over
                            formPlay.setAttribute('data-play', 'block');
                            icons.forEach(icon => {
                                icon.style.display = 'block';
                            });
                        } else if (data.status == 2) {
                            showVictoryMessage("¡Has salvado el mundo! 🌍✨");// Ganaste¡¡
                            formPlay.setAttribute('data-play', 'block');
                            icons.forEach(icon => {
                                icon.style.display = 'block';
                            });
                        }
                    });
            }
        });
    });

};
addEvents();

function restartGame() {
    fetch(window.location.href, {
        method: 'GET',
    })
        .then(response => response.text())
        .then(html => {
            document.body.innerHTML = html;
            addEvents();
        });
}

document.getElementById('config-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Previene el envío tradicional del formulario

    const formData = new FormData(document.getElementById('config-form'));
    // for (let [key, value] of formData.entries()) {
    //     console.log(`${key}: ${value}`);
    // }

    // Comprobar los valores de rows, cols y bombs
    // let rows = formData.get('rows');
    // let cols = formData.get('cols');
    // let bombs = formData.get('bombs');
    // Convertir los valores a enteros

    // Enviar los datos del formulario mediante fetch
    fetch(window.location.href, {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())  // Obtener la respuesta como texto
    .then(html => {
        // Reemplazar el cuerpo de la página con el HTML actualizado
        document.body.innerHTML = html;
        addEvents(); 
    })
    .catch(error => {
        console.error('Error al enviar los datos:', error);
    });
});
