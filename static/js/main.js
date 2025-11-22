// main.js - theme + sidebar + helpers
(function(){
  const html = document.documentElement;
  const btnTheme = document.getElementById('btnTheme');
  const btnToggleSidebar = document.getElementById('btnToggleSidebar');
  const sidebar = document.getElementById('sidebar');

  // Theme toggle (persist in localStorage)
  function setTheme(t){
    html.setAttribute('data-bs-theme', t);
    localStorage.setItem('theme', t);
    if(btnTheme) btnTheme.innerHTML = t === 'dark' ? '<i class="bi bi-sun"></i>' : '<i class="bi bi-moon-stars"></i>';
  }
  const saved = localStorage.getItem('theme') || 'light';
  setTheme(saved);
  if(btnTheme) btnTheme.addEventListener('click', ()=> setTheme(html.getAttribute('data-bs-theme') === 'light' ? 'dark' : 'light'));

  // Sidebar toggle for small devices
  if(btnToggleSidebar){
    btnToggleSidebar.addEventListener('click', ()=> sidebar.classList.toggle('open'));
  }

  // Close sidebar when clicking outside (mobile)
  document.addEventListener('click', (e)=>{
    if(window.innerWidth < 768 && sidebar.classList.contains('open')){
      if(!sidebar.contains(e.target) && !document.getElementById('btnToggleSidebar').contains(e.target)){
        sidebar.classList.remove('open');
      }
    }
  });
})();
