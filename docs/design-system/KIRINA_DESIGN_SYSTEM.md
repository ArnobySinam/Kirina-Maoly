# Kirina Maoly Alba · Makeup Artist
## Sistema de diseño y estructura del sitio web — v1.0

> Documento base del proyecto. Define la identidad visual (color, tipografía, espaciado, componentes) y la arquitectura del sitio, a partir de la maqueta de referencia y con las mejoras propuestas para hacerla más atractiva, profesional y orientada a conseguir reservas.

| Dato | Valor |
|---|---|
| Cliente | Kirina Maoly Alba — Maquilladora profesional |
| Ubicación | Bucaramanga, Colombia |
| Idioma | Español (Colombia), tuteo |
| Objetivo principal | Convertir visitas en citas (WhatsApp / formulario) |
| Versión | 1.0 · Octubre 2026 |

---

## Índice

1. [Concepto de marca](#1-concepto-de-marca)
2. [Mejoras frente a la maqueta](#2-mejoras-frente-a-la-maqueta)
3. [Paleta de colores](#3-paleta-de-colores)
4. [Tipografía](#4-tipografía)
5. [Espaciado, grid y breakpoints](#5-espaciado-grid-y-breakpoints)
6. [Bordes, sombras y degradados](#6-bordes-sombras-y-degradados)
7. [Iconografía e imágenes](#7-iconografía-e-imágenes)
8. [Componentes](#8-componentes)
9. [Movimiento e interacción](#9-movimiento-e-interacción)
10. [Arquitectura del sitio](#10-arquitectura-del-sitio)
11. [Voz y tono](#11-voz-y-tono)
12. [Accesibilidad, SEO y rendimiento](#12-accesibilidad-seo-y-rendimiento)
13. [Tokens CSS](#13-tokens-css)
14. [Estructura de archivos del proyecto](#14-estructura-de-archivos-del-proyecto)

---

## 1. Concepto de marca

**Idea central:** *“Belleza editorial con calidez cercana”.* Lujo discreto, como una revista de moda, sin perder el trato personal de una artista independiente.

| Atributo | Cómo se traduce en el diseño |
|---|---|
| **Elegante** | Serif de alto contraste, mucho espacio en blanco, detalles en champagne |
| **Femenina y cálida** | Rosas empolvados, fondos marfil (nunca blanco puro de fondo), esquinas suaves |
| **Profesional** | Grid estricto, jerarquía clara, fotografía consistente, precios visibles |
| **Versátil** | Un sistema neutro que admite módulos de temporada (Halloween, grados, bodas) |

**Palabras clave visuales:** satinado · luminoso · nude · rosé · champagne · editorial.

---

## 2. Mejoras frente a la maqueta

| # | En la maqueta | Mejora propuesta | Por qué |
|---|---|---|---|
| 1 | Rosa CTA claro con texto blanco (bajo contraste) | Rosa Kirina `#B04A6A` → contraste 5.2:1 (AA) | Legibilidad y apariencia más “premium” |
| 2 | Sin acento metálico | Acento **Champagne** `#C9A46A` para estrellas, líneas y detalles | Eleva la percepción de lujo; conecta con joyería de las fotos |
| 3 | “Precios” en el menú, pero sin sección | Sección **Paquetes y precios** con tarjeta destacada | Reduce fricción; filtra clientes antes del contacto |
| 4 | No explica cómo reservar | Sección **Cómo funciona** (4 pasos) | Genera confianza y claridad |
| 5 | Sin prueba social cuantitativa | **Barra de cifras** (años, clientas, eventos, valoración) | Credibilidad inmediata |
| 6 | Galería estática | Filtros + **lightbox** + slider **antes/después** | Muestra la transformación, que es lo que vende |
| 7 | Contacto solo en el footer | Sección **Reserva** con formulario → WhatsApp + mapa + horarios | Canal de conversión principal |
| 8 | Sin preguntas frecuentes | **FAQ** en acordeón | Resuelve objeciones (domicilio, anticipo, prueba) |
| 9 | Sin acceso rápido a WhatsApp | **Botón flotante de WhatsApp** + CTA en header | El canal preferido en Colombia |
| 10 | Banner de Halloween fijo | **Módulo de temporada intercambiable** | Reutilizable todo el año (grados, bodas, Navidad) |
| 11 | Íconos genéricos de relleno | Íconos lineales finos (Phosphor Light) coherentes | Estética más fina y unificada |
| 12 | Sin firma personal | Firma manuscrita en “Sobre mí” + certificaciones/marcas | Humaniza la marca y aporta autoridad |

---

## 3. Paleta de colores

### 3.1 Colores de marca

| Nombre | Token | HEX | RGB | Uso |
|---|---|---|---|---|
| **Rosa Kirina** | `--color-primary` | `#B04A6A` | 176, 74, 106 | CTA, enlaces, íconos activos |
| Rosa Profundo | `--color-primary-strong` | `#93395A` | 147, 57, 90 | Hover/pressed de CTA, títulos acento |
| Rosa Pétalo | `--color-primary-soft` | `#E7A9B8` | 231, 169, 184 | Acentos sobre fondo oscuro, ilustraciones |
| Blush | `--color-blush` | `#F6E3E6` | 246, 227, 230 | Fondos de sección, chips, hero |
| Niebla Rosa | `--color-mist` | `#FBEFF1` | 251, 239, 241 | Fondos sutiles, hover de tarjetas |

### 3.2 Neutros

| Nombre | Token | HEX | Uso |
|---|---|---|---|
| **Noir** | `--color-noir` | `#151012` | Secciones oscuras (galería, footer) |
| Tinta | `--color-ink` | `#1E1517` | Texto principal y títulos |
| Cacao | `--color-cocoa` | `#5E5052` | Texto secundario, párrafos largos |
| Taupe | `--color-taupe` | `#8C7A7D` | Metadatos grandes, placeholders, deshabilitado |
| Línea | `--color-line` | `#EADFDB` | Bordes y divisores |
| **Marfil** | `--color-ivory` | `#FBF7F3` | Fondo base del sitio |
| Blanco | `--color-white` | `#FFFFFF` | Tarjetas, campos de formulario |

### 3.3 Acento metálico

| Nombre | Token | HEX | Uso |
|---|---|---|---|
| **Champagne** | `--color-gold` | `#C9A46A` | Estrellas, líneas finas, overlines sobre oscuro |
| Champagne Oscuro | `--color-gold-strong` | `#A88452` | Detalles decorativos sobre claro (solo íconos o ≥ 24 px) |

### 3.4 Paleta de temporada (Halloween)

| Nombre | Token | HEX | Uso |
|---|---|---|---|
| Borgoña | `--season-wine` | `#6E1A2B` | Fondo del banner de temporada |
| Carmesí | `--season-crimson` | `#A3202F` | Degradados y brillos |
| Luz de vela | `--season-candle` | `#E89B4C` | Halo cálido, detalles puntuales |

### 3.5 Estados

| Estado | HEX | Uso |
|---|---|---|
| Éxito | `#2F7D5B` | Formulario enviado, disponibilidad |
| Aviso | `#B7791F` | Fechas con poca disponibilidad |
| Error | `#B3261E` | Validación de campos |
| Info | `#3A6EA5` | Mensajes neutros |

### 3.6 Proporción de uso (regla 60 · 30 · 10)

- **60 %** Marfil / Blanco — respiración, fondos.
- **30 %** Tinta / Noir / Blush — texto, secciones de contraste.
- **10 %** Rosa Kirina + Champagne — CTA y detalles. *El rosa nunca se usa como fondo de grandes áreas.*

### 3.7 Contraste verificado (WCAG 2.2)

| Texto / Fondo | Ratio | Nivel |
|---|---|---|
| Tinta `#1E1517` sobre Marfil `#FBF7F3` | 16.8 : 1 | AAA |
| Cacao `#5E5052` sobre Marfil | 7.2 : 1 | AAA |
| Blanco sobre Rosa Kirina `#B04A6A` | 5.2 : 1 | AA |
| Blanco sobre Rosa Profundo `#93395A` | 7.1 : 1 | AAA |
| Rosa Kirina sobre Marfil | 4.9 : 1 | AA |
| Marfil sobre Noir `#151012` | 17.7 : 1 | AAA |
| Rosa Pétalo sobre Noir | 9.7 : 1 | AAA |
| Champagne sobre Noir | 8.1 : 1 | AAA |
| Taupe `#8C7A7D` sobre Marfil | 3.8 : 1 | Solo texto grande / decorativo |

---

## 4. Tipografía

### 4.1 Familias

| Rol | Familia | Pesos | Carácter |
|---|---|---|---|
| **Display / Títulos** | **Cormorant Garamond** | 500, 600, 600 *itálica* | Serif editorial de alto contraste, lujo clásico |
| **Texto / UI** | **Jost** | 300, 400, 500, 600 | Sans geométrica, moderna y limpia (estilo moda) |
| **Firma / Logo** | **Pinyon Script** | 400 | Caligráfica — *solo* logo y firma, nunca en párrafos |

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Jost:wght@300;400;500;600&family=Pinyon+Script&display=swap" rel="stylesheet">
```

> Recurso de estilo: resaltar una palabra del título en *itálica* y Rosa Kirina. Ej.: “Tu belleza en cada *momento especial*”.

### 4.2 Escala tipográfica (razón 1.25 · fluida)

| Estilo | Familia / peso | Escritorio | Móvil | Interlineado | Tracking | Uso |
|---|---|---|---|---|---|---|
| **Display** | Cormorant 600 | 76 px | 44 px | 1.02 | −0.01em | Título del hero |
| **H1** | Cormorant 600 | 60 px | 38 px | 1.08 | −0.01em | Títulos de página |
| **H2** | Cormorant 600 | 46 px | 32 px | 1.12 | 0 | Títulos de sección |
| **H3** | Cormorant 600 | 30 px | 25 px | 1.2 | 0 | Subtítulos, nombre en “Sobre mí” |
| **H4** | Jost 500 | 20 px | 18 px | 1.35 | 0.01em | Títulos de tarjeta |
| **Lead** | Jost 300 | 20 px | 18 px | 1.6 | 0 | Bajadas e introducciones |
| **Body** | Jost 400 | 17 px | 16 px | 1.7 | 0 | Párrafos |
| **Small** | Jost 400 | 14 px | 14 px | 1.6 | 0.01em | Descripciones de tarjeta, legales |
| **Overline** | Jost 500 | 12 px | 12 px | 1.4 | 0.2em MAYÚS | Etiqueta sobre títulos (“SOBRE MÍ”) |
| **Botón** | Jost 500 | 15 px | 15 px | 1 | 0.04em | Botones y chips |

### 4.3 Reglas

- Longitud de línea de párrafos: **60–72 caracteres** (`max-width: 65ch`).
- Títulos alineados a la izquierda en bloques de texto; centrados solo en cabeceras de sección.
- Máximo **2 familias** visibles por bloque (el script cuenta como imagen).
- Nunca usar Cormorant por debajo de 22 px (pierde legibilidad).

---

## 5. Espaciado, grid y breakpoints

### 5.1 Escala de espaciado (base 4 px)

| Token | px | Uso típico |
|---|---|---|
| `--space-1` | 4 | Separación ícono–texto mínima |
| `--space-2` | 8 | Dentro de chips, gaps pequeños |
| `--space-3` | 12 | Padding de chips, gap de íconos |
| `--space-4` | 16 | Gutter móvil, padding de inputs |
| `--space-5` | 24 | Padding de tarjetas, gutter escritorio |
| `--space-6` | 32 | Entre título y contenido |
| `--space-7` | 48 | Entre bloques dentro de una sección |
| `--space-8` | 64 | Cabecera de sección → contenido |
| `--space-9` | 96 | Padding vertical de sección (tablet) |
| `--space-10` | 128 | Padding vertical de sección (escritorio) |

**Padding de sección:** 128 px escritorio · 96 px tablet · 72 px móvil.

### 5.2 Grid

| | Móvil | Tablet | Escritorio |
|---|---|---|---|
| Columnas | 4 | 8 | 12 |
| Gutter | 16 px | 24 px | 24 px |
| Margen lateral | 16 px | 32 px | auto |
| Contenedor máx. | 100 % | 100 % | **1240 px** (texto largo: 720 px) |

### 5.3 Breakpoints (mobile-first)

| Nombre | Mín. | Dispositivo |
|---|---|---|
| `sm` | 480 px | Móvil grande |
| `md` | 768 px | Tablet |
| `lg` | 1024 px | Laptop |
| `xl` | 1280 px | Escritorio |
| `2xl` | 1536 px | Pantallas grandes |

---

## 6. Bordes, sombras y degradados

### 6.1 Radios

| Token | Valor | Uso |
|---|---|---|
| `--radius-sm` | 8 px | Inputs, miniaturas |
| `--radius-md` | 14 px | Imágenes de galería |
| `--radius-lg` | 20 px | Tarjetas |
| `--radius-xl` | 32 px | Imágenes destacadas, banners |
| `--radius-pill` | 999 px | Botones, chips, badges |

### 6.2 Sombras (cálidas, tintadas — nunca gris puro)

| Token | Valor | Uso |
|---|---|---|
| `--shadow-sm` | `0 1px 2px rgba(30,21,23,.06)` | Inputs, chips |
| `--shadow-md` | `0 10px 30px -12px rgba(30,21,23,.14)` | Tarjetas en reposo |
| `--shadow-lg` | `0 28px 60px -20px rgba(30,21,23,.22)` | Tarjetas hover, modales |
| `--shadow-glow` | `0 12px 32px -10px rgba(176,74,106,.45)` | Botón primario hover |

### 6.3 Degradados

| Token | Valor | Uso |
|---|---|---|
| `--grad-cta` | `linear-gradient(135deg, #B04A6A 0%, #93395A 100%)` | Botón primario |
| `--grad-hero` | `linear-gradient(100deg, #F6E3E6 0%, #FBF7F3 55%, rgba(251,247,243,0) 100%)` | Hero (fusión con la foto) |
| `--grad-noir` | `linear-gradient(180deg, #151012 0%, #231A1C 100%)` | Galería, footer |
| `--grad-season` | `radial-gradient(120% 120% at 80% 50%, #A3202F 0%, #6E1A2B 45%, #151012 100%)` | Banner de temporada |
| `--grad-gold-line` | `linear-gradient(90deg, transparent, #C9A46A, transparent)` | Divisores decorativos |

---

## 7. Iconografía e imágenes

### 7.1 Íconos

- **Librería:** Phosphor Icons — estilo *Light* (trazo fino, coherente con la serif).
- **Tamaños:** 20 px (UI), 24 px (listas), 32 px (beneficios), 40 px (servicios).
- **Color:** Rosa Kirina sobre claro · Rosa Pétalo o Champagne sobre oscuro.
- Contenedor opcional: círculo de 56 px en Blush.

| Concepto | Ícono sugerido |
|---|---|
| Alta calidad | `diamond` |
| Productos profesionales | `paint-brush` / `drop` |
| Estilo personalizado | `heart` |
| Eventos | `champagne` |
| Grados | `graduation-cap` |
| Bodas | `rings` / `flower-lotus` |
| Halloween | `skull` / `ghost` |
| Agenda | `calendar-heart` |
| WhatsApp | `whatsapp-logo` |

### 7.2 Fotografía — dirección de arte

- **Contenido real:** usar trabajos reales de Kirina (no imágenes genéricas). La autenticidad es el principal factor de confianza.
- **Luz:** suave, cálida y difusa; fondos neutros o desenfocados.
- **Encuadre:** primer plano (rostro y hombros) para servicios; plano medio para “Sobre mí”.
- **Edición:** tono de piel natural, sin sobre-suavizado; misma temperatura en todo el set.
- **Proporciones:**

| Ubicación | Ratio | Tamaño exportado |
|---|---|---|
| Hero escritorio | 16 : 9 | 2400 × 1350 |
| Hero móvil (art direction) | 4 : 5 | 1080 × 1350 |
| Tarjeta de servicio | 4 : 5 | 800 × 1000 |
| Galería | 1 : 1 y 4 : 5 (mosaico) | 1200 px lado mayor |
| Sobre mí | 3 : 4 | 1200 × 1600 |
| Avatar testimonio | 1 : 1 | 160 × 160 |

- **Formato:** AVIF + WebP de respaldo, `loading="lazy"` excepto el hero, `srcset` responsivo.
- **Peso objetivo:** < 250 KB por imagen grande, < 80 KB miniaturas.

### 7.3 Logo

- Monograma (corazón + pincel) + “Kirina Maoly Alba” en Pinyon Script + “MAKEUP ARTIST” en Jost 500, tracking 0.3em.
- Versiones: color sobre claro · marfil sobre oscuro · monograma solo (favicon, avatar).
- Área de respeto: altura de la “K” alrededor. Tamaño mínimo: 120 px de ancho.

---

## 8. Componentes

### 8.1 Botones

| Variante | Fondo | Texto | Borde | Hover |
|---|---|---|---|---|
| **Primario** | `--grad-cta` | Blanco | — | Eleva 2 px + `--shadow-glow` |
| **Secundario** | Transparente | Rosa Kirina | 1.5 px Rosa Kirina | Fondo Niebla Rosa |
| **Sobre oscuro** | Transparente | Marfil | 1 px rgba(255,255,255,.35) | Fondo rgba(255,255,255,.08) |
| **Texto / enlace** | — | Rosa Kirina | Subrayado animado | Rosa Profundo |
| **WhatsApp** | `#25D366` | Tinta | — | Oscurece 6 % |

| Tamaño | Alto | Padding H | Texto |
|---|---|---|---|
| S | 40 px | 20 px | 14 px |
| M (por defecto) | 48 px | 28 px | 15 px |
| L | 56 px | 36 px | 16 px |

Reglas: forma *pill*, ícono opcional (20 px) a la izquierda o flecha a la derecha que se desplaza 4 px en hover. Área táctil mínima 44 × 44 px. Estado `:focus-visible` con anillo de 3 px `rgba(176,74,106,.35)`.

### 8.2 Tarjeta de servicio

- Imagen 4 : 5 con radio superior 20 px, zoom suave (1.04) en hover.
- Ícono en círculo Blush superpuesto al borde de la imagen.
- Título H4, descripción Small (máx. 3 líneas), **“Desde $XXX.XXX”** y duración.
- CTA secundario “Ver más” + enlace “Reservar”.
- Fondo Blanco, `--shadow-md`, padding 24 px.

### 8.3 Chips de filtro (galería)

- Alto 40 px, pill, Jost 500 14 px.
- Inactivo: borde 1 px rgba(255,255,255,.25), texto Marfil.
- Activo: fondo Rosa Pétalo, texto Noir.

### 8.4 Galería

- Mosaico de 4 columnas (escritorio), 3 (tablet), 2 (móvil); gap 16 px.
- Hover: overlay degradado inferior + categoría + ícono de lupa.
- Clic: lightbox con navegación por teclado y swipe.
- **Antes / Después:** slider con manija circular Champagne.

### 8.5 Tarjeta de testimonio

- Comillas decorativas Cormorant 80 px en Rosa Pétalo.
- Estrellas Champagne (16 px), texto Body itálico ligero, avatar 56 px + nombre + servicio.
- Carrusel con puntos de paginación; en escritorio 3 visibles.

### 8.6 Tarjeta de precio

- 3 columnas; la destacada lleva badge “Más elegido”, borde 1.5 px Rosa Kirina y elevación.
- Nombre (H4), precio (Cormorant 600 44 px), lista de inclusiones con check, CTA.

### 8.7 Formularios

- Input: alto 52 px, fondo Blanco, borde 1 px Línea, radio 8 px, label flotante.
- Focus: borde Rosa Kirina + anillo. Error: borde y mensaje en `#B3261E` con ícono.
- Campos de reserva: Nombre · WhatsApp · Servicio (select) · Fecha · Lugar (estudio / domicilio) · Mensaje.

### 8.8 Header

- Alto 80 px (64 px al hacer scroll), sticky.
- Transparente sobre el hero → fondo Marfil 90 % + `backdrop-filter: blur(12px)` al hacer scroll.
- Enlace activo con punto Champagne debajo. CTA “Agenda tu cita” a la derecha.
- Móvil: menú hamburguesa a pantalla completa en Noir con enlaces en Cormorant 36 px.

### 8.9 Otros

| Componente | Especificación |
|---|---|
| Badge | Pill 24 px, Jost 500 12 px MAYÚS, fondo Blush, texto Rosa Profundo |
| Divisor | Línea 1 px `--grad-gold-line`, 120 px de ancho, con rombo central opcional |
| Acordeón FAQ | Fila de 72 px, ícono “+” que rota 45°, transición de altura 300 ms |
| WhatsApp flotante | 60 px, esquina inferior derecha (24 px), aparece tras 400 px de scroll |
| Overline | Jost 500 12 px MAYÚS 0.2em, Rosa Kirina, con línea de 32 px a la izquierda |

---

## 9. Movimiento e interacción

| Token | Valor | Uso |
|---|---|---|
| `--dur-fast` | 150 ms | Hover de color |
| `--dur-base` | 250 ms | Botones, chips |
| `--dur-slow` | 450 ms | Tarjetas, acordeón |
| `--dur-reveal` | 800 ms | Aparición al hacer scroll |
| `--ease-out` | `cubic-bezier(.22, 1, .36, 1)` | Curva principal |

- **Reveal:** fade + desplazamiento de 24 px hacia arriba, escalonado de 80 ms entre elementos.
- **Hero:** entrada del título palabra por palabra; ligero parallax de la foto (máx. 30 px).
- **Imágenes:** zoom suave 1.04 en hover (600 ms).
- **Respeto:** desactivar todo con `prefers-reduced-motion: reduce`.

---

## 10. Arquitectura del sitio

### 10.1 Página de inicio — orden de secciones

| # | Sección | Fondo | Contenido clave | Objetivo |
|---|---|---|---|---|
| 0 | **Header** | Transparente → Marfil | Logo · Inicio · Servicios · Galería · Sobre mí · Precios · Contacto · CTA | Navegación + CTA siempre visible |
| 1 | **Hero** | `--grad-hero` + foto | Display + lead + 3 beneficios + CTA primario “Agenda tu cita” + secundario “Ver portafolio” + mini prueba social (★ 5.0 · +300 clientas) | Impacto y conversión inmediata |
| 2 | **Cifras** | Blanco, banda fina | Años de experiencia · Clientas felices · Novias · Valoración | Credibilidad |
| 3 | **Servicios** | Marfil | 4 tarjetas: Eventos · Grados · Bodas · Halloween/Artístico (precio desde + duración) | Mostrar oferta |
| 4 | **Cómo funciona** | Blush | 1 Agenda → 2 Asesoría → 3 Tu día → 4 Retoque/Kit | Reducir dudas |
| 5 | **Galería** | Noir | Filtros + mosaico + lightbox + antes/después + “Ver más trabajos” | Demostrar calidad |
| 6 | **Sobre mí** | Marfil (split 50/50) | Foto · overline · nombre · bio · 3 valores · firma · marcas/certificaciones · CTA | Conexión personal |
| 7 | **Paquetes y precios** | Blanco | 3 tarjetas (Social · Grado · Novia ★) + nota de domicilio | Calificar al cliente |
| 8 | **Testimonios** | Niebla Rosa | Carrusel + valoración de Google | Prueba social |
| 9 | **Temporada** | `--grad-season` | Módulo intercambiable (Halloween ahora) + CTA | Campañas puntuales |
| 10 | **FAQ** | Marfil | 6–8 preguntas (domicilio, anticipo, prueba, duración, productos, alergias) | Resolver objeciones |
| 11 | **Reserva / Contacto** | Blush | Formulario → WhatsApp · mapa · horario · redes | Conversión |
| 12 | **Footer** | Noir | Logo · frase · enlaces · servicios · contacto · redes · legal | Cierre |
| — | **WhatsApp flotante** | — | Botón fijo | Contacto en un toque |

### 10.2 Mapa del sitio

```
/                     Inicio (one-page con anclas)
/servicios/eventos    Detalle del servicio (fase 2)
/servicios/grados
/servicios/bodas
/servicios/halloween
/galeria              Portafolio completo con filtros
/sobre-mi
/precios
/contacto
/politica-de-privacidad
```

> **Fase 1:** sitio de una página con anclas. **Fase 2:** páginas de detalle por servicio (mejor SEO local: “maquillaje de novia Bucaramanga”).

### 10.3 Wireframe del hero (escritorio)

```
┌──────────────────────────────────────────────────────────────────────┐
│ [Logo]        Inicio Servicios Galería Sobre mí Precios   (Agenda ▸) │
├───────────────────────────────┬──────────────────────────────────────┤
│ — MAQUILLAJE PROFESIONAL      │                                      │
│ Tu belleza                    │                                      │
│ en cada *momento especial*    │            FOTOGRAFÍA                │
│ Lead de 2 líneas…             │           (fundido con               │
│ ◇ Calidad  ✎ Productos  ♡ Estilo│          degradado blush)          │
│ (Agenda tu cita ▸) (Ver portafolio)                                  │
│ ★★★★★ 5.0 · +300 clientas     │                                      │
└───────────────────────────────┴──────────────────────────────────────┘
```

---

## 11. Voz y tono

| Sí | No |
|---|---|
| Cercana, cálida, en segunda persona (“tú”) | Fría o corporativa |
| Frases cortas y seguras | Exceso de signos de exclamación |
| Enfocada en cómo se sentirá la clienta | Tecnicismos sin explicar |
| Llamados claros: “Agenda tu cita”, “Reserva tu fecha” | “Haz clic aquí”, “Enviar” |

**Ejemplos de microcopy:** “Tu fecha es importante: reserva con anticipación” · “Respondo en menos de 2 horas por WhatsApp” · “Productos profesionales e hipoalergénicos”.

---

## 12. Accesibilidad, SEO y rendimiento

**Accesibilidad**
- Contraste mínimo AA en todo el texto (ver 3.7).
- Navegación completa por teclado; `:focus-visible` visible siempre.
- `alt` descriptivo en cada foto (“Maquillaje de novia con tonos nude y delineado suave”).
- Áreas táctiles ≥ 44 px; `lang="es-CO"`.

**SEO local**
- Título: “Kirina Maoly Alba · Maquilladora profesional en Bucaramanga”.
- Schema.org `BeautySalon` / `LocalBusiness` con dirección, horario, teléfono y valoraciones.
- Open Graph con imagen 1200 × 630.
- Perfil de Google Business enlazado.

**Rendimiento (objetivos)**
- LCP < 2.5 s · CLS < 0.1 · INP < 200 ms · Lighthouse ≥ 90.
- Fuentes con `font-display: swap` y precarga de la principal.
- Imágenes AVIF/WebP, dimensiones explícitas para evitar saltos.

---

## 13. Tokens CSS

```css
:root {
  /* ── Marca ── */
  --color-primary:        #B04A6A;
  --color-primary-strong: #93395A;
  --color-primary-soft:   #E7A9B8;
  --color-blush:          #F6E3E6;
  --color-mist:           #FBEFF1;

  /* ── Neutros ── */
  --color-noir:   #151012;
  --color-ink:    #1E1517;
  --color-cocoa:  #5E5052;
  --color-taupe:  #8C7A7D;
  --color-line:   #EADFDB;
  --color-ivory:  #FBF7F3;
  --color-white:  #FFFFFF;

  /* ── Acento ── */
  --color-gold:        #C9A46A;
  --color-gold-strong: #A88452;

  /* ── Temporada ── */
  --season-wine:    #6E1A2B;
  --season-crimson: #A3202F;
  --season-candle:  #E89B4C;

  /* ── Estados ── */
  --color-success: #2F7D5B;
  --color-warning: #B7791F;
  --color-error:   #B3261E;
  --color-info:    #3A6EA5;

  /* ── Tipografía ── */
  --font-display: "Cormorant Garamond", "Times New Roman", serif;
  --font-body:    "Jost", "Helvetica Neue", Arial, sans-serif;
  --font-script:  "Pinyon Script", cursive;

  --fs-display: clamp(2.75rem, 1.9rem + 3.6vw, 4.75rem);   /* 44 → 76 */
  --fs-h1:      clamp(2.375rem, 1.7rem + 2.8vw, 3.75rem);  /* 38 → 60 */
  --fs-h2:      clamp(2rem, 1.6rem + 1.8vw, 2.875rem);     /* 32 → 46 */
  --fs-h3:      clamp(1.5625rem, 1.4rem + 0.6vw, 1.875rem);/* 25 → 30 */
  --fs-h4:      clamp(1.125rem, 1.08rem + 0.2vw, 1.25rem); /* 18 → 20 */
  --fs-lead:    clamp(1.125rem, 1.08rem + 0.2vw, 1.25rem); /* 18 → 20 */
  --fs-body:    clamp(1rem, 0.98rem + 0.1vw, 1.0625rem);   /* 16 → 17 */
  --fs-small:   0.875rem;                                  /* 14 */
  --fs-overline:0.75rem;                                   /* 12 */

  --lh-tight: 1.05;
  --lh-heading: 1.15;
  --lh-body: 1.7;
  --ls-overline: 0.2em;

  /* ── Espaciado ── */
  --space-1: 0.25rem;  --space-2: 0.5rem;  --space-3: 0.75rem;
  --space-4: 1rem;     --space-5: 1.5rem;  --space-6: 2rem;
  --space-7: 3rem;     --space-8: 4rem;    --space-9: 6rem;
  --space-10: 8rem;
  --section-y: clamp(4.5rem, 3rem + 6vw, 8rem);
  --container: 1240px;
  --container-text: 720px;
  --gutter: clamp(1rem, 0.6rem + 1.6vw, 1.5rem);

  /* ── Radios ── */
  --radius-sm: 8px;  --radius-md: 14px;  --radius-lg: 20px;
  --radius-xl: 32px; --radius-pill: 999px;

  /* ── Sombras ── */
  --shadow-sm:   0 1px 2px rgba(30,21,23,.06);
  --shadow-md:   0 10px 30px -12px rgba(30,21,23,.14);
  --shadow-lg:   0 28px 60px -20px rgba(30,21,23,.22);
  --shadow-glow: 0 12px 32px -10px rgba(176,74,106,.45);

  /* ── Degradados ── */
  --grad-cta:    linear-gradient(135deg, #B04A6A 0%, #93395A 100%);
  --grad-hero:   linear-gradient(100deg, #F6E3E6 0%, #FBF7F3 55%, rgba(251,247,243,0) 100%);
  --grad-noir:   linear-gradient(180deg, #151012 0%, #231A1C 100%);
  --grad-season: radial-gradient(120% 120% at 80% 50%, #A3202F 0%, #6E1A2B 45%, #151012 100%);
  --grad-gold-line: linear-gradient(90deg, transparent, #C9A46A, transparent);

  /* ── Movimiento ── */
  --dur-fast: 150ms; --dur-base: 250ms; --dur-slow: 450ms; --dur-reveal: 800ms;
  --ease-out: cubic-bezier(.22, 1, .36, 1);

  /* ── Capas ── */
  --z-header: 100; --z-float: 200; --z-modal: 300;
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation: none !important; transition: none !important; }
}
```

---

## 14. Estructura de archivos del proyecto

```
Kirina-Maoly/
├── index.html
├── docs/
│   └── design-system/
│       ├── KIRINA_DESIGN_SYSTEM.md     ← este documento
│       ├── KIRINA_DESIGN_SYSTEM.pdf    ← versión visual
│       └── source/                     ← HTML fuente del PDF
├── assets/
│   ├── css/
│   │   ├── tokens.css        (sección 13)
│   │   ├── base.css          (reset, tipografía, utilidades)
│   │   ├── components.css    (botones, tarjetas, formularios…)
│   │   └── sections.css      (hero, servicios, galería…)
│   ├── js/
│   │   ├── main.js           (header, menú, scroll reveal)
│   │   ├── gallery.js        (filtros, lightbox, antes/después)
│   │   └── booking.js        (formulario → WhatsApp)
│   ├── img/
│   │   ├── hero/  services/  gallery/  about/  testimonials/
│   └── icons/                (logo SVG, favicon, monograma)
└── README.md
```

---

*Kirina Maoly Alba · Makeup Artist — Sistema de diseño v1.0 · Bucaramanga, Colombia*
