/*
  Sidebar + Footer injector
  Requires: <div id="navbar"></div> and <div id="footer"></div> in each template.
  Active link is highlighted based on the current URL path.
*/

(function () {
    const path = window.location.pathname;

    const navLinks = [
        { href: '/home/',         icon: '🏠', label: 'Dashboard' },
        { href: '/transactions/', icon: '💳', label: 'Transactions' },
        { href: '/create-budget/',icon: '📊', label: 'Budgets' },
        { href: '/goals/',        icon: '🎯', label: 'Goals' },
        { href: '/viewreport/',   icon: '📈', label: 'Reports' },
    ];

    const linksHTML = navLinks.map(link => {
        const isActive = path.startsWith(link.href) ? ' active' : '';
        return `<a href="${link.href}" class="${isActive}">
                    <span class="nav-icon">${link.icon}</span>
                    ${link.label}
                </a>`;
    }).join('');

    const navbarEl = document.getElementById('navbar');
    if (navbarEl) {
        navbarEl.innerHTML = `
            <div class="sidebar-brand">
                <div class="sidebar-brand-icon">💰</div>
                <div>
                    <div class="sidebar-brand-text">Budgeter</div>
                    <div class="sidebar-brand-sub">Personal Finance</div>
                </div>
            </div>
            <div class="sidebar-section-label">Navigation</div>
            <nav class="sidebar-nav">
                ${linksHTML}
            </nav>
            <div class="sidebar-footer">
                <form method="post" action="/logout/" id="sidebar-logout-form">
                    <input type="hidden" name="csrfmiddlewaretoken" value="${getCookie('csrftoken')}">
                    <button type="submit">
                        <span>🚪</span> Sign Out
                    </button>
                </form>
            </div>
        `;
    }

    const footerEl = document.getElementById('footer');
    if (footerEl) {
        footerEl.innerHTML = `
            <footer class="footer">
                <p>&copy; 2026 Personal Budgeter. All rights reserved.</p>
                <ul class="footer-links">
                    <li><a href="/home/">Home</a></li>
                    <li><a href="#">About</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
            </footer>
        `;
    }

    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
        return '';
    }
})();
