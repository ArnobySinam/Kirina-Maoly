/* Kirina Maoly Alba — Formulario de reserva: valida y abre WhatsApp con el mensaje armado. */
(function () {
  "use strict";

  var WHATSAPP = "573115551234";

  document.querySelectorAll("[data-booking]").forEach(function (form) {
    var success = form.querySelector(".form__success");
    var dateInput = form.querySelector("input[type='date']");
    if (dateInput) dateInput.min = new Date().toISOString().slice(0, 10);

    // Preselecciona el servicio si llega por URL: contacto.html?servicio=bodas
    var preset = new URLSearchParams(window.location.search).get("servicio");
    var select = form.querySelector("select[name='servicio']");
    if (preset && select) {
      Array.prototype.forEach.call(select.options, function (opt) {
        if (opt.getAttribute("data-key") === preset) opt.selected = true;
      });
    }

    function setError(field, hasError) {
      var wrap = field.closest(".field");
      if (wrap) wrap.classList.toggle("has-error", hasError);
      field.setAttribute("aria-invalid", String(hasError));
    }

    function validate(field) {
      var v = field.value.trim();
      var ok = true;
      if (field.required && !v) ok = false;
      if (ok && field.name === "telefono") ok = /^[0-9 +()-]{10,}$/.test(v) && v.replace(/\D/g, "").length >= 10;
      setError(field, !ok);
      return ok;
    }

    form.querySelectorAll("input, select, textarea").forEach(function (field) {
      field.addEventListener("blur", function () { if (field.value) validate(field); });
      field.addEventListener("input", function () {
        if (field.closest(".field.has-error")) validate(field);
      });
    });

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var fields = form.querySelectorAll("input[required], select[required], textarea[required], input[name='telefono']");
      var firstInvalid = null;
      fields.forEach(function (f) {
        if (!validate(f) && !firstInvalid) firstInvalid = f;
      });
      if (firstInvalid) {
        firstInvalid.focus();
        return;
      }

      var data = new FormData(form);
      var fecha = data.get("fecha");
      if (fecha) {
        var p = fecha.split("-");
        fecha = p[2] + "/" + p[1] + "/" + p[0];
      }
      var lines = [
        "¡Hola Kirina! Quiero agendar una cita ✨",
        "",
        "• Nombre: " + data.get("nombre"),
        "• WhatsApp: " + data.get("telefono"),
        "• Servicio: " + data.get("servicio"),
        fecha ? "• Fecha: " + fecha : null,
        data.get("lugar") ? "• Lugar: " + data.get("lugar") : null,
        data.get("personas") ? "• Personas: " + data.get("personas") : null,
        data.get("mensaje") ? "• Mensaje: " + data.get("mensaje") : null
      ].filter(function (l) { return l !== null; });

      var url = "https://wa.me/" + WHATSAPP + "?text=" + encodeURIComponent(lines.join("\n"));
      window.open(url, "_blank", "noopener");
      if (success) success.classList.add("is-visible");
    });
  });
})();
