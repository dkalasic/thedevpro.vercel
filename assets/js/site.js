// TheDevPro — small progressive enhancements. All content is in the HTML.
(function () {
  document.documentElement.classList.remove('no-js');

  // Mobile menu
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Reveal on scroll
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  // Hours calculator (/ai/)
  var calc = document.querySelector('[data-calc]');
  if (calc) {
    var pos = calc.querySelector('[name=pos]');
    var min = calc.querySelector('[name=min]');
    var render = function () {
      var p = Number(pos.value), m = Number(min.value);
      var saved = Math.max(0, p * (m - 5) / 60);
      calc.querySelector('[data-pos]').textContent = p;
      calc.querySelector('[data-min]').textContent = m;
      calc.querySelector('[data-weekly]').textContent = saved.toFixed(1);
      calc.querySelector('[data-yearly]').textContent = Math.round(saved * 50);
    };
    pos.addEventListener('input', render);
    min.addEventListener('input', render);
    render();
  }

  // Contact form -> opens a pre-written email (nothing is stored on this site)
  var form = document.querySelector('[data-mailto]');
  if (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var f = new FormData(form);
      var subject = 'New project — ' + (f.get('company') || f.get('name') || 'website');
      var body = [
        'Name: ' + (f.get('name') || ''),
        'Company: ' + (f.get('company') || ''),
        'Phone: ' + (f.get('phone') || ''),
        'Interested in: ' + (f.get('service') || ''),
        '',
        (f.get('message') || '')
      ].join('\n');
      window.location.href = 'mailto:hello@thedevpro.io?cc=dkalasic@gmail.com&subject=' +
        encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    });
  }
})();
