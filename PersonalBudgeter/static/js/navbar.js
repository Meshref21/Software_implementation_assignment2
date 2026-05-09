// Highlights nav links client-side (adds active class when server-side missing)
document.addEventListener('DOMContentLoaded', function () {
  const links = document.querySelectorAll('#navbar .sidebar-nav a');
  const path = location.pathname.replace(/\/+$|\/$/, '') || '/';
  links.forEach(a => {
    try {
      const href = new URL(a.href, location.origin).pathname.replace(/\/+$|\/$/, '') || '/';
      if (href === path) a.classList.add('active');
    } catch (e) { /* ignore malformed */ }
  });
});
