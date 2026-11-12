// Personal-link alerts for private proposals.
// Only runs when the link has ?p=<name> (e.g. /thermal/?p=aron).
// Sends: one "open" ping, then one "leave" ping with time on page and the furthest section seen.
(function () {
  var HOOK = 'https://n8n.srv773540.hstgr.cloud/webhook/thedevpro-page-view';
  var params = new URLSearchParams(location.search);
  var person = (params.get('p') || '').trim().slice(0, 40);
  if (!person) return;

  var started = Date.now();
  var furthest = '';
  var furthestIndex = -1;
  var sent = false;
  var device = window.matchMedia('(max-width: 760px)').matches ? 'mobile' : 'desktop';

  function ping(event) {
    var q = new URLSearchParams({
      p: person,
      e: event,
      path: location.pathname,
      s: String(Math.round((Date.now() - started) / 1000)),
      sec: furthest,
      d: device
    });
    try { fetch(HOOK + '?' + q.toString(), { method: 'GET', mode: 'no-cors', keepalive: true }); } catch (e) {}
  }

  // Track the furthest section reached
  var sections = Array.prototype.slice.call(document.querySelectorAll('section[id]'));
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var i = sections.indexOf(en.target);
        if (i > furthestIndex) {
          furthestIndex = i;
          var h = en.target.querySelector('h2, h1');
          furthest = (h ? h.textContent : en.target.id).trim().slice(0, 80);
        }
      });
    }, { threshold: 0.3 });
    sections.forEach(function (s) { io.observe(s); });
  }

  ping('open');

  function leave() {
    if (sent) return;
    sent = true;
    ping('leave');
  }
  document.addEventListener('visibilitychange', function () {
    if (document.visibilityState === 'hidden') leave();
  });
  window.addEventListener('pagehide', leave);
})();
