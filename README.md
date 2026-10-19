# Kirina Maoly Alba · Makeup Artist

Sitio web de Kirina Maoly Alba, maquilladora profesional en Bucaramanga. HTML, CSS y JavaScript puros: no hace falta instalar nada.

## Ver el sitio

Abre `index.html` en el navegador, o levanta un servidor local:

```bash
python3 -m http.server 8000   # luego abre http://localhost:8000
```

## Páginas

| Archivo | Contenido |
|---|---|
| `index.html` | Inicio: hero, cifras, servicios, proceso, galería, sobre mí, precios, testimonios, temporada, FAQ y reserva |
| `servicios/index.html` | Todos los servicios |
| `servicios/eventos.html` · `grados.html` · `bodas.html` · `halloween.html` | Detalle de cada servicio |
| `galeria.html` | Portafolio con filtros, lightbox y antes/después |
| `sobre-mi.html` | Historia, trayectoria, valores y marcas |
| `precios.html` | Paquetes, extras y políticas |
| `contacto.html` | Formulario de reserva (abre WhatsApp), datos y mapa |
| `politica-de-privacidad.html` · `404.html` | Legal y página de error |

## Fotos

Mientras una foto no exista, el sitio muestra un degradado elegante con una etiqueta. Para poner las fotos reales basta con guardarlas con estos nombres (JPG, idealmente < 250 KB):

| Carpeta | Archivos | Proporción |
|---|---|---|
| `assets/img/hero/` | `hero.jpg` | horizontal, 2400 × 1350 |
| `assets/img/services/` | `eventos.jpg`, `grados.jpg`, `bodas.jpg`, `halloween.jpg` | 4:5, 800 × 1000 |
| `assets/img/gallery/` | `g01.jpg` … `g16.jpg` | 4:5, 1200 px |
| `assets/img/gallery/` | `antes-1.jpg`, `despues-1.jpg`, `antes-2.jpg`, `despues-2.jpg` | 4:5 |
| `assets/img/about/` | `kirina.jpg` | 3:4, 1200 × 1600 |
| `assets/img/testimonials/` | `t1.jpg` … `t6.jpg` | 1:1, 160 × 160 |
| `assets/img/season/` | `halloween.jpg` | 4:5 o cuadrada |
| `assets/img/` | `og-image.jpg` (para compartir en redes) | 1200 × 630 |

## Editar contenido

Header, footer, textos, precios, servicios, galería y testimonios están centralizados en `tools/build_pages.py`. Después de editarlo, regenera las páginas:

```bash
python3 tools/build_pages.py
```

Datos que hay que confirmar antes de publicar (están al inicio de ese archivo): teléfono/WhatsApp, correo, redes sociales, dominio, precios y cifras (años, clientas, novias). El número de WhatsApp del formulario está también en `assets/js/booking.js`.

## Estructura

```
assets/css/   tokens.css · base.css · components.css · sections.css
assets/js/    main.js (header, menú, animaciones) · gallery.js · booking.js
assets/img/   fotos (ver tabla)
docs/design-system/   sistema de diseño (MD + PDF)
tools/build_pages.py  generador de las páginas
```
