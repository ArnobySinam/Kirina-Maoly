/* Kirina Maoly Alba — Comportamiento general:
   header, menú móvil, aparición al hacer scroll, imágenes de respaldo y botón de WhatsApp. */
(function () {
  "use strict";

  var root = document.documentElement;
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ── Imágenes: si una foto aún no existe, se muestra el respaldo elegante ── */
  function markEmpty(img) {
    var media = img.closest(".media");
    if (media) media.classList.add("is-empty");
    img.remove();
  }
  document.querySelectorAll(".media img").forEach(function (img) {
    if (img.complete && img.naturalWidth === 0) markEmpty(img);
    else img.addEventListener("error", function () { markEmpty(img); }, { once: true });
  });

  /* ── Header: cambia al hacer scroll ── */
  var header = document.querySelector(".site-header");
  var waFloat = document.querySelector(".wa-float");
  function onScroll() {
    var y = window.scrollY;
    if (header) header.classList.toggle("is-scrolled", y > 24);
    if (waFloat) waFloat.classList.toggle("is-visible", y > 400);
  }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* ── Menú móvil ── */
  var toggle = document.querySelector(".menu-toggle");
  var menu = document.getElementById("mobile-menu");
  function setMenu(open) {
    root.classList.toggle("menu-open", open);
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Cerrar menú" : "Abrir menú");
    menu.setAttribute("aria-hidden", String(!open));
    if ("inert" in menu) menu.inert = !open;
    if (open) {
      var first = menu.querySelector("a");
      if (first) first.focus();
    }
  }
  if (toggle && menu) {
    setMenu(false);
    toggle.addEventListener("click", function () {
      setMenu(!root.classList.contains("menu-open"));
    });
    menu.addEventListener("click", function (e) {
      if (e.target.closest("a")) setMenu(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && root.classList.contains("menu-open")) {
        setMenu(false);
        toggle.focus();
      }
    });
    window.matchMedia("(min-width: 1024px)").addEventListener("change", function (mq) {
      if (mq.matches) setMenu(false);
    });
  }

  /* ── Título del hero: entrada palabra por palabra ── */
  document.querySelectorAll("[data-split]").forEach(function (el) {
    if (reduceMotion) return;
    var i = 0;
    el.querySelectorAll("[data-line]").forEach(function (line) {
      var words = line.textContent.trim().split(/\s+/);
      line.textContent = "";
      words.forEach(function (w, idx) {
        var span = document.createElement("span");
        span.className = "word";
        span.style.setProperty("--w", i++);
        span.textContent = w;
        line.appendChild(span);
        if (idx < words.length - 1) line.appendChild(document.createTextNode(" "));
      });
    });
  });

  /* ── Aparición al hacer scroll ── */
  var revealEls = document.querySelectorAll("[data-reveal]");
  if ("IntersectionObserver" in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  }

  /* ── Año del footer ── */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
