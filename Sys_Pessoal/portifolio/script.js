// Capturando os elementos de navegação
const navLinks = document.querySelectorAll('nav a');

// Adicionando um ouvinte de eventos para cada link de navegação
navLinks.forEach(link => {
    link.addEventListener('mouseenter', () => {
        link.style.color = '#ff00ff'; // Altera a cor ao passar o mouse
    });

    link.addEventListener('mouseleave', () => {
        link.style.color = '#fff'; // Restaura a cor ao remover o mouse
    });
});
