/* ============================================================
   HOOKAH69 — MAIN JS
   ============================================================ */

// ---------- Navbar scroll effect ----------
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 60) {
    navbar.style.background = 'rgba(13,13,13,0.97)';
  } else {
    navbar.style.background = 'rgba(13,13,13,0.85)';
  }
});

// ---------- Hamburger menu ----------
const hamburger = document.getElementById('hamburger');
const navLinks  = document.getElementById('navLinks');

hamburger?.addEventListener('click', () => {
  navLinks.classList.toggle('open');
  const spans = hamburger.querySelectorAll('span');
  if (navLinks.classList.contains('open')) {
    spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
    spans[1].style.opacity   = '0';
    spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
  } else {
    spans.forEach(s => { s.style.transform = ''; s.style.opacity = ''; });
  }
});

// Close nav when a link is clicked
navLinks?.querySelectorAll('.nav-link').forEach(link => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('open');
    hamburger.querySelectorAll('span').forEach(s => { s.style.transform = ''; s.style.opacity = ''; });
  });
});

// ---------- Menu tabs ----------
document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const tab = btn.dataset.tab;
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById(tab)?.classList.add('active');
  });
});

// ---------- Gallery filter ----------
document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const filter = btn.dataset.filter;
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    document.querySelectorAll('.gallery-item').forEach(item => {
      if (filter === 'all' || item.dataset.category === filter) {
        item.classList.remove('hidden');
        item.style.animation = 'fadeIn 0.4s ease';
      } else {
        item.classList.add('hidden');
      }
    });
  });
});

// ---------- Like button toggle ----------
document.querySelectorAll('.like-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const icon  = btn.querySelector('i');
    const parts = btn.textContent.trim().split(/\s+/);
    const count = parseInt(parts[parts.length - 1]) || 0;

    if (btn.dataset.liked === 'true') {
      btn.dataset.liked = 'false';
      icon.style.color  = '';
      btn.innerHTML     = `<i class="fas fa-thumbs-up"></i> ${count - 1}`;
    } else {
      btn.dataset.liked = 'true';
      icon.style.color  = 'var(--gold)';
      btn.innerHTML     = `<i class="fas fa-thumbs-up" style="color:var(--gold)"></i> ${count + 1}`;
    }
  });
});

// ---------- Auto-dismiss messages ----------
document.querySelectorAll('.alert').forEach(alert => {
  setTimeout(() => {
    alert.style.transition = 'opacity 0.5s ease';
    alert.style.opacity    = '0';
    setTimeout(() => alert.remove(), 500);
  }, 5000);
});

// ---------- Scroll reveal ----------
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('revealed');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll(
  '.feature-card, .review-card, .stat-card, .menu-card, .team-card, .value-card, .gallery-item, .info-card'
).forEach(el => {
  el.style.opacity    = '0';
  el.style.transform  = 'translateY(24px)';
  el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
  revealObserver.observe(el);
});

document.addEventListener('DOMContentLoaded', () => {
  // add revealed class styles via JS since CSS classes can't transition from JS-set initial state
  const style = document.createElement('style');
  style.textContent = `.revealed { opacity: 1 !important; transform: translateY(0) !important; }`;
  document.head.appendChild(style);
});

// ---------- Smooth active nav on scroll (homepage) ----------
const sections = document.querySelectorAll('section[id]');
if (sections.length > 0) {
  const navObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
        const match = document.querySelector(`.nav-link[href="#${entry.target.id}"]`);
        match?.classList.add('active');
      }
    });
  }, { rootMargin: '-40% 0px -55% 0px' });

  sections.forEach(s => navObserver.observe(s));
}
