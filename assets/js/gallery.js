/* Kirina Maoly Alba — Galería: filtros, lightbox y comparador antes/después. */
(function () {
  "use strict";

  /* ── Filtros ── */
  document.querySelectorAll("[data-gallery]").forEach(function (gallery) {
    var chips = gallery.querySelectorAll("[data-filter]");
    var items = gallery.querySelectorAll(".gallery-item");
    chips.forEach(function (chip) {
      chip.addEventListener("click", function () {
        var cat = chip.getAttribute("data-filter");
        chips.forEach(function (c) { c.setAttribute("aria-pressed", String(c === chip)); });
        items.forEach(function (item) {
          item.hidden = cat !== "todos" && item.getAttribute("data-cat") !== cat;
        });
      });
    });
  });

  /* ── Lightbox ── */
  var dialog = document.getElementById("lightbox");
  if (dialog && typeof dialog.showModal === "function") {
    var stage = dialog.querySelector(".lightbox__figure .media");
    var caption = dialog.querySelector(".lightbox__figure figcaption");
    var current = [];
    var index = 0;

    function render() {
      var item = current[index];
      var src = item.getAttribute("data-full");
      var label = item.getAttribute("data-caption") || "";
      stage.innerHTML = "";
      stage.className = "media ratio-4x5";
      stage.setAttribute("data-label", label);
      var img = new Image();
      img.alt = label;
      img.onerror = function () { stage.classList.add("is-empty"); img.remove(); };
      img.src = src;
      stage.appendChild(img);
      caption.textContent = label + " · " + (index + 1) + " / " + current.length;
    }
    function step(d) {
      index = (index + d + current.length) % current.length;
      render();
    }

    document.addEventListener("click", function (e) {
      var item = e.target.closest(".gallery-item");
      if (!item) return;
      var grid = item.closest(".gallery-grid");
      current = Array.prototype.filter.call(grid.querySelectorAll(".gallery-item"), function (el) { return !el.hidden; });
      index = current.indexOf(item);
      render();
      dialog.showModal();
    });
    dialog.querySelector(".lightbox__close").addEventListener("click", function () { dialog.close(); });
    dialog.querySelector(".lightbox__prev").addEventListener("click", function () { step(-1); });
    dialog.querySelector(".lightbox__next").addEventListener("click", function () { step(1); });
    dialog.addEventListener("click", function (e) { if (e.target === dialog) dialog.close(); });
    dialog.addEventListener("keydown", function (e) {
      if (e.key === "ArrowLeft") step(-1);
      if (e.key === "ArrowRight") step(1);
    });

    var touchX = null;
    dialog.addEventListener("touchstart", function (e) { touchX = e.touches[0].clientX; }, { passive: true });
    dialog.addEventListener("touchend", function (e) {
      if (touchX === null) return;
      var dx = e.changedTouches[0].clientX - touchX;
      if (Math.abs(dx) > 50) step(dx < 0 ? 1 : -1);
      touchX = null;
    });
  }

  /* ── Antes / después ── */
  document.querySelectorAll(".compare").forEach(function (cmp) {
    var range = cmp.querySelector("input[type='range']");
    function update() { cmp.style.setProperty("--pos", range.value + "%"); }
    range.addEventListener("input", update);
    update();
  });
})();
