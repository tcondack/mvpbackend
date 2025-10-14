document.querySelectorAll('nav a').forEach(link => {
  link.addEventListener('click', function(e) {
    const destino = document.querySelector(this.getAttribute('href'));
    if (destino) {
      e.preventDefault();
      destino.scrollIntoView({ behavior: 'smooth' });
    }
  });
});

// Alternância de tema claro/escuro
const toggleBtn = document.getElementById('toggle-theme');
if (toggleBtn) {
  toggleBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    toggleBtn.textContent = document.body.classList.contains('dark-mode')
      ? 'Modo claro'
      : 'Modo escuro';
  });
}

// Saudação com base no horário
const hora = new Date().getHours();
let saudacao = "Bem-vindo";

if (hora < 12) saudacao = "Bom dia";
else if (hora < 18) saudacao = "Boa tarde";
else saudacao = "Boa noite";

const tituloSaudacao = document.querySelector('.welcome h2');
if (tituloSaudacao) {
  tituloSaudacao.textContent = '${saudacao} ao ecoturismo de Teresópolis';
}

// Filtro de trilhas por dificuldade
const filtro = document.getElementById('filtro-dificuldade');
if (filtro) {
  filtro.addEventListener('change', function () {
    const dificuldade = this.value;
    document.querySelectorAll('.trilha-card').forEach(card => {
      if (dificuldade === 'todas' || card.dataset.dificuldade === dificuldade) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  });
}