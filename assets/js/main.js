// ===================== Theme Toggle =====================
(function () {
  const root = document.documentElement;
  const saved = localStorage.getItem('ahs-theme');
  if (saved) root.setAttribute('data-theme', saved);
  document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('themeToggle');
    if (!btn) return;
    const setIcon = () => { btn.textContent = root.getAttribute('data-theme') === 'light' ? '🌙' : '☀️'; };
    setIcon();
    btn.addEventListener('click', () => {
      const current = root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
      if (current === 'dark') { root.removeAttribute('data-theme'); } else { root.setAttribute('data-theme', 'light'); }
      localStorage.setItem('ahs-theme', current === 'dark' ? '' : 'light');
      setIcon();
    });

    // Mobile nav
    const burger = document.getElementById('navBurger');
    const links = document.getElementById('navLinks');
    if (burger && links) {
      burger.addEventListener('click', () => links.classList.toggle('open'));
      links.querySelectorAll('a').forEach(a => a.addEventListener('click', () => links.classList.remove('open')));
    }

    // Animated counters
    document.querySelectorAll('[data-counter]').forEach(el => {
      const target = parseInt(el.getAttribute('data-counter'), 10);
      let cur = 0;
      const step = Math.max(1, Math.ceil(target / 40));
      const tick = () => {
        cur += step;
        if (cur >= target) { el.textContent = target; return; }
        el.textContent = cur;
        requestAnimationFrame(tick);
      };
      tick();
    });
  });
})();

// ===================== Project Filtering (Projects Overview Page) =====================
function initProjectFilters(projects) {
  const grid = document.getElementById('projectGrid');
  const searchInput = document.getElementById('projectSearch');
  const categoryChips = document.querySelectorAll('[data-category-filter]');
  const statusSelect = document.getElementById('statusFilter');
  const techSelect = document.getElementById('techFilter');

  let activeCategory = 'all';

  function render() {
    const q = (searchInput?.value || '').toLowerCase().trim();
    const status = statusSelect?.value || 'all';
    const tech = techSelect?.value || 'all';

    const filtered = projects.filter(p => {
      if (activeCategory !== 'all' && p.categorySlug !== activeCategory) return false;
      if (status !== 'all' && p.status !== status) return false;
      if (tech !== 'all' && !p.tech.includes(tech)) return false;
      if (q && !(p.title.toLowerCase().includes(q) || p.short.toLowerCase().includes(q) || p.tech.join(' ').toLowerCase().includes(q))) return false;
      return true;
    });

    grid.innerHTML = filtered.map(p => projectCardHTML(p)).join('') ||
      '<p class="text-muted">No projects match the current filters.</p>';
  }

  function projectCardHTML(p) {
    return `
    <a href="projects/${p.slug}.html" class="card project-card">
      <span class="pnum">PROJECT ${String(p.id).padStart(2, '0')}</span>
      <h3>${p.title}</h3>
      <div class="cat">${p.category}</div>
      <p class="desc">${p.short}</p>
      <div>${p.tech.slice(0, 4).map(t => `<span class="tag">${t}</span>`).join('')}</div>
      <div class="meta-row">
        <span class="badge-status ${p.statusClass}"><span class="dot"></span>${p.status}</span>
        <span class="view-link">View Details &rarr;</span>
      </div>
    </a>`;
  }

  categoryChips.forEach(chip => {
    chip.addEventListener('click', () => {
      categoryChips.forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      activeCategory = chip.getAttribute('data-category-filter');
      render();
    });
  });
  searchInput?.addEventListener('input', render);
  statusSelect?.addEventListener('change', render);
  techSelect?.addEventListener('change', render);

  render();
}
