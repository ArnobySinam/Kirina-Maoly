#!/usr/bin/env python3
"""Genera las páginas HTML del sitio de Kirina Maoly Alba.

Header, footer, íconos y datos (servicios, precios, galería, testimonios)
viven aquí en un solo lugar para que todas las páginas queden consistentes.

Uso:  python3 tools/build_pages.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ─────────────────────────── Datos de contacto ───────────────────────────
SITE = {
    "name": "Kirina Maoly Alba",
    "url": "https://kirinamaolyalba.com",
    "city": "Bucaramanga, Colombia",
    "phone": "+57 311 555 1234",
    "phone_href": "+573115551234",
    "whatsapp": "573115551234",
    "email": "kirinamaolyalba@gmail.com",
    "instagram": "https://www.instagram.com/",
    "tiktok": "https://www.tiktok.com/",
    "facebook": "https://www.facebook.com/",
    "hours": "Lunes a sábado · 7:00 a. m. – 7:00 p. m.",
}
WA_LINK = f"https://wa.me/{SITE['whatsapp']}?text=" + "%C2%A1Hola%20Kirina!%20Quiero%20informaci%C3%B3n%20para%20agendar%20una%20cita%20%E2%9C%A8"

# ─────────────────────────── Íconos (trazo 1.5, 24×24) ───────────────────────────
ICONS = {
    "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "calendar-heart": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/><path d="M12 18.5s-3-1.8-3-3.8a1.5 1.5 0 0 1 3-.6 1.5 1.5 0 0 1 3 .6c0 2-3 3.8-3 3.8z"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "chevron-left": '<path d="M15 6l-6 6 6 6"/>',
    "chevron-right": '<path d="M9 6l6 6-6 6"/>',
    "close": '<path d="M6 6l12 12M18 6L6 18"/>',
    "diamond": '<path d="M6 3h12l4 6-10 12L2 9z"/><path d="M2 9h20M12 21 8 9l4-6 4 6z"/>',
    "brush": '<path d="M14 4l6 6-8 8c-2 2-5 2-7 1 1-2 1-5 3-7z"/><path d="M12 6l6 6"/>',
    "heart": '<path d="M12 20s-8-5-8-11a4.5 4.5 0 0 1 8-2.8A4.5 4.5 0 0 1 20 9c0 6-8 11-8 11z"/>',
    "champagne": '<path d="M8 3h3l-.5 7a2.5 2.5 0 0 1-2 0zM13 3h3l.5 7a2.5 2.5 0 0 1-2 0z"/><path d="M9.5 10.3V20M14.5 10.3V20M7 20h5M12 20h5"/>',
    "cap": '<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5M22 9v6"/>',
    "rings": '<circle cx="9" cy="14" r="5"/><circle cx="15" cy="14" r="5"/><path d="M10 5l2-2 2 2-2 2z"/>',
    "skull": '<path d="M12 3a8 8 0 0 0-8 8c0 3 1.5 5 3.5 6V20h9v-3c2-1 3.5-3 3.5-6a8 8 0 0 0-8-8z"/><circle cx="9" cy="11" r="1.6"/><circle cx="15" cy="11" r="1.6"/><path d="M11 20v-2M13 20v-2"/>',
    "sparkle": '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 16l.7 1.8 1.8.7-1.8.7L19 21l-.7-1.8-1.8-.7 1.8-.7z"/>',
    "palette": '<path d="M12 3a9 9 0 1 0 0 18c1.2 0 2-.8 2-1.8 0-.5-.2-.9-.5-1.3-.3-.3-.5-.8-.5-1.2 0-1 .8-1.7 1.8-1.7H17a4 4 0 0 0 4-4c0-4.4-4-8-9-8z"/><circle cx="7.5" cy="11" r="1"/><circle cx="10" cy="7" r="1"/><circle cx="15" cy="7.5" r="1"/>',
    "chat": '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 10h8M8 13h5"/>',
    "camera": '<path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/>',
    "gift": '<rect x="3" y="9" width="18" height="12" rx="1"/><path d="M3 13h18M12 9v12M12 9S10.5 4 8 4.5 7 9 12 9zM12 9s1.5-5 4-4.5S17 9 12 9z"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 7"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "home": '<path d="M4 11l8-7 8 7v9H4z"/><path d="M10 20v-6h4v6"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14c2.8 0 5 2.2 5 5"/>',
    "leaf": '<path d="M5 19c0-9 6-14 15-14 0 9-5 15-14 15"/><path d="M5 19l8-8"/>',
    "shield": '<path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-4.5"/>',
    "award": '<circle cx="12" cy="9" r="6"/><path d="M8.5 14L7 21l5-2.5 5 2.5-1.5-7"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>',
    "drop": '<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/>',
    "mirror": '<ellipse cx="12" cy="9" rx="6" ry="7"/><path d="M12 16v5M9 21h6"/>',
}
FILLED = {
    "star": '<path d="M12 2.8l2.8 5.8 6.4.9-4.6 4.5 1.1 6.3L12 17.3l-5.7 3 1.1-6.3L2.8 9.5l6.4-.9z"/>',
    "whatsapp": '<path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.4.8 3.2.7.5-.1 1.5-.6 1.8-1.2.2-.6.2-1.1.1-1.2l-.5-.3z"/>',
    "instagram": '<path d="M12 7.3a4.7 4.7 0 1 0 0 9.4 4.7 4.7 0 0 0 0-9.4zm0 7.7a3 3 0 1 1 0-6 3 3 0 0 1 0 6zm6-7.9a1.1 1.1 0 1 1-2.2 0 1.1 1.1 0 0 1 2.2 0zM21.9 8c-.1-1.5-.4-2.8-1.5-3.9S18 2.6 16.5 2.5C15 2.4 9 2.4 7.5 2.5S4.8 2.9 3.6 4 2.2 6.5 2.1 8C2 9.5 2 14.5 2.1 16c.1 1.5.4 2.8 1.5 3.9s2.4 1.4 3.9 1.5c1.5.1 7.5.1 9 0s2.8-.4 3.9-1.5 1.4-2.4 1.5-3.9c.1-1.5.1-6.5 0-8zm-2 9.6a3 3 0 0 1-1.7 1.7c-1.2.5-4 .4-5.2.4s-4.1.1-5.2-.4a3 3 0 0 1-1.7-1.7c-.5-1.2-.4-4-.4-5.3s-.1-4.1.4-5.2a3 3 0 0 1 1.7-1.7c1.2-.5 4-.4 5.2-.4s4.1-.1 5.2.4a3 3 0 0 1 1.7 1.7c.5 1.2.4 4 .4 5.2s.1 4.1-.4 5.3z"/>',
    "tiktok": '<path d="M16.6 2h-3.3v13.2a2.8 2.8 0 1 1-2-2.7V9.1a6.2 6.2 0 1 0 5.3 6.1V8.6a8 8 0 0 0 4.4 1.4V6.6a4.5 4.5 0 0 1-4.4-4.6z"/>',
    "facebook": '<path d="M14 8.5V6.6c0-.9.6-1.1 1-1.1h2.6V2h-3.6C10.1 2 9.4 4.9 9.4 6.7v1.8H7v3.6h2.4V22H14v-9.9h3.2l.4-3.6z"/>',
}


def icon(name, cls=""):
    extra = f" {cls}" if cls else ""
    if name in FILLED:
        return f'<svg class="icon icon--fill{extra}" viewBox="0 0 24 24" aria-hidden="true">{FILLED[name]}</svg>'
    return f'<svg class="icon{extra}" viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'


ARROW = icon("arrow", "icon--arrow")
STARS = '<div class="stars" aria-label="5 de 5 estrellas">' + icon("star") * 5 + "</div>"

LOGO_MARK = (
    '<svg class="brand__mark" viewBox="0 0 48 48" fill="none" stroke="currentColor" '
    'stroke-width="1.4" stroke-linecap="round" aria-hidden="true">'
    '<path d="M24 40C14 32 7 26 7 17.5 7 12 11 8 16 8c3.5 0 6.4 2 8 5 1.6-3 4.5-5 8-5 5 0 9 4 9 9.5 0 3.5-1.2 6.5-3.4 9.4"/>'
    '<path d="M29 38l11-13M40 25c1.5-1.6 3.5-1.8 4.6-.8s.8 3.1-.8 4.6L33 39.5" stroke="#C9A46A"/></svg>'
)

# ─────────────────────────── Contenido ───────────────────────────
# Precios ilustrativos: confirmar con Kirina antes de publicar.
SERVICES = [
    {
        "key": "eventos",
        "name": "Reuniones y Eventos",
        "short": "Eventos",
        "icon": "champagne",
        "tagline": "Elegancia que se nota en cada foto",
        "desc": "Maquillaje elegante y sofisticado para que te veas increíble en cualquier ocasión: cumpleaños, cenas, bautizos, quinceañeras o una sesión de fotos.",
        "long": "Diseño un look que acompañe tu vestuario, la hora del evento y tu estilo personal. Trabajo con productos de larga duración que se ven impecables tanto en persona como en cámara, para que solo te preocupes por disfrutar.",
        "price": "120.000",
        "duration": "60 min",
        "ideal": "Cumpleaños, cenas, quinces, fotos",
        "includes": [
            "Asesoría de look según tu vestuario y evento",
            "Preparación e hidratación de la piel",
            "Maquillaje de larga duración, apto para fotos",
            "Pestañas en tira incluidas",
            "Fijación profesional",
        ],
        "faq": [
            ("¿Con cuánta anticipación debo reservar?", "Te recomiendo reservar con al menos una semana de anticipación; los fines de semana se llenan rápido."),
            ("¿Puedo llevar una foto de referencia?", "¡Claro! Me ayuda mucho a entender lo que imaginas. Lo adaptamos a tus rasgos y tono de piel."),
            ("¿Cuánto dura el maquillaje?", "Entre 10 y 12 horas con los productos y la técnica de fijación que uso."),
        ],
    },
    {
        "key": "grados",
        "name": "Grados",
        "short": "Grados",
        "icon": "cap",
        "tagline": "Un look especial para un día inolvidable",
        "desc": "Un look especial para un día inolvidable. Resalta tu belleza en tu graduación y luce radiante en la ceremonia y en las fotos con tu familia.",
        "long": "La graduación es un logro que merece celebrarse. Creo un maquillaje fresco y luminoso que resiste la toga, el birrete, los abrazos y las fotos bajo cualquier luz, desde la ceremonia hasta la fiesta.",
        "price": "130.000",
        "duration": "60 min",
        "ideal": "Grados de colegio y universidad",
        "includes": [
            "Look luminoso pensado para fotografía con flash",
            "Preparación de piel y corrección de ojeras",
            "Pestañas en tira incluidas",
            "Labial de retoque recomendado",
            "Descuento para grupos de 3 o más",
        ],
        "faq": [
            ("¿Atiendes grupos de graduandas?", "Sí. Para grupos de 3 o más personas hay tarifa especial y puedo llevar asistente para cumplir los tiempos."),
            ("¿Vas a domicilio?", "Sí, dentro del área metropolitana de Bucaramanga con un recargo según la zona."),
            ("¿A qué hora debo agendar?", "Lo ideal es terminar 1 hora antes de la ceremonia. Calculamos juntas la hora exacta."),
        ],
    },
    {
        "key": "bodas",
        "name": "Bodas",
        "short": "Bodas",
        "icon": "rings",
        "tagline": "Tu versión más radiante para el sí",
        "desc": "Maquillaje profesional para novias, invitadas y todo el equipo del evento. Incluye prueba previa para que llegues tranquila a tu gran día.",
        "long": "Acompaño a cada novia desde la primera asesoría. Hacemos una prueba previa para definir el look perfecto según tu vestido, peinado, flores y la luz del lugar. El día de la boda llego a tiempo, con todo lo necesario, y también puedo maquillar a mamá, damas de honor e invitadas.",
        "price": "450.000",
        "duration": "2 – 3 h",
        "ideal": "Novias, damas de honor, mamás",
        "includes": [
            "Asesoría personalizada y prueba de maquillaje",
            "Maquillaje HD de larga duración y a prueba de lágrimas",
            "Pestañas premium",
            "Kit de retoque para la noche",
            "Servicio a domicilio en el área metropolitana",
            "Tarifas especiales para el cortejo",
        ],
        "faq": [
            ("¿Cuándo debo hacer la prueba?", "Entre 3 y 6 semanas antes de la boda, idealmente cuando ya tengas el vestido y el peinado definidos."),
            ("¿Cómo separo la fecha?", "Con un anticipo del 30 %. El saldo se paga el día del evento."),
            ("¿Viajas fuera de Bucaramanga?", "Sí, a toda Santander y a otras ciudades. Los viáticos se cotizan según el destino."),
        ],
    },
    {
        "key": "halloween",
        "name": "Halloween y Artístico",
        "short": "Halloween",
        "icon": "skull",
        "tagline": "Looks creativos que se roban la noche",
        "desc": "Looks creativos, artísticos y llenos de detalle para destacar en esta temporada: catrinas, fantasía, efectos especiales y caracterización.",
        "long": "Aquí el maquillaje se vuelve arte. Diseñamos juntos un personaje único —catrina, fantasía, terror elegante o caracterización completa— con pintura profesional, pedrería y efectos que duran toda la fiesta.",
        "price": "150.000",
        "duration": "90 min",
        "ideal": "Halloween, disfraces, sesiones y concursos",
        "includes": [
            "Diseño del personaje a partir de tu idea",
            "Pintura facial profesional e hipoalergénica",
            "Pedrería, glitter y detalles a mano",
            "Opción de efectos especiales",
            "Fijación de larga duración",
        ],
        "faq": [
            ("¿Cuándo debo reservar para Halloween?", "Octubre es la temporada más alta. Reserva desde septiembre para asegurar tu horario."),
            ("¿Los productos son seguros para la piel?", "Sí, uso pinturas cosméticas profesionales e hipoalergénicas, aptas para el rostro."),
            ("¿Puedo traer mi propia idea?", "¡Me encanta! Envíame tus referencias por WhatsApp y la diseñamos juntas."),
        ],
    },
]
SERVICE_BY_KEY = {s["key"]: s for s in SERVICES}

PACKAGES = [
    {
        "name": "Social",
        "desc": "Para cumpleaños, cenas y eventos.",
        "price": "$120.000",
        "note": "Por persona",
        "items": ["Asesoría de look", "Preparación de piel", "Maquillaje de larga duración", "Pestañas en tira"],
        "service": "eventos",
        "featured": False,
    },
    {
        "name": "Novia",
        "desc": "La experiencia completa para tu boda.",
        "price": "$450.000",
        "note": "Incluye prueba previa",
        "items": ["Asesoría y prueba de maquillaje", "Maquillaje HD a prueba de lágrimas", "Pestañas premium", "Kit de retoque", "Domicilio en el área metropolitana"],
        "service": "bodas",
        "featured": True,
    },
    {
        "name": "Grado",
        "desc": "Radiante en la ceremonia y en las fotos.",
        "price": "$130.000",
        "note": "Tarifa especial para grupos",
        "items": ["Look luminoso para fotografía", "Corrección de ojeras", "Pestañas en tira", "Fijación profesional"],
        "service": "grados",
        "featured": False,
    },
]

EXTRAS = [
    ("Prueba de maquillaje (adicional)", "Para eventos sociales o grados", "$80.000"),
    ("Pestañas premium o por punto", "Efecto más natural y duradero", "$25.000"),
    ("Servicio a domicilio", "Área metropolitana de Bucaramanga", "Desde $20.000"),
    ("Maquillaje para invitadas o cortejo", "Por persona, el día de la boda", "$110.000"),
    ("Clase de automaquillaje", "Sesión personalizada de 2 horas", "$180.000"),
]

GALLERY = [
    ("g01", "eventos", "Glam nude con delineado suave", "4x5"),
    ("g02", "halloween", "Catrina con rosas rojas", "4x5"),
    ("g03", "bodas", "Novia luminosa con velo", "4x5"),
    ("g04", "eventos", "Ahumado en tonos cálidos", "4x5"),
    ("g05", "halloween", "Fantasía helada con pedrería", "4x5"),
    ("g06", "grados", "Grado con labios rosados", "4x5"),
    ("g07", "bodas", "Novia romántica con flores", "4x5"),
    ("g08", "grados", "Look fresco para graduación", "4x5"),
    ("g09", "halloween", "Telaraña negra y labios oscuros", "4x5"),
    ("g10", "eventos", "Bronceado dorado para la noche", "4x5"),
    ("g11", "bodas", "Mamá de la novia, elegante", "4x5"),
    ("g12", "eventos", "Ojo cut-crease en rosa", "4x5"),
    ("g13", "grados", "Glam suave con iluminador", "4x5"),
    ("g14", "halloween", "Catrina elegante en dorado", "4x5"),
    ("g15", "bodas", "Dama de honor en tonos malva", "4x5"),
    ("g16", "eventos", "Piel glow para sesión de fotos", "4x5"),
]
CATS = [("todos", "Todos"), ("eventos", "Eventos"), ("grados", "Grados"), ("bodas", "Bodas"), ("halloween", "Halloween")]

TESTIMONIALS = [
    ("Daniela R.", "Grado · 2026", "Me maquilló para mi grado y quedé encantada. Súper profesional y el resultado fue increíble. ¡100 % recomendada!", "t1"),
    ("Valentina M.", "Novia · 2026", "Mi maquillaje de novia fue perfecto. Kirina hizo que me sintiera hermosa y segura en mi gran día. Duró intacto toda la noche.", "t2"),
    ("Mariana L.", "Halloween · 2025", "Los maquillajes de Halloween son espectaculares, súper creativos y con un nivel de detalle increíble. Gané el concurso de disfraces.", "t3"),
    ("Laura P.", "Evento social · 2026", "Puntual, amable y muy detallista. Entendió exactamente lo que quería y me sentí regia en el matrimonio de mi hermana.", "t4"),
    ("Camila S.", "Sesión de fotos · 2026", "La piel se veía natural y luminosa en todas las fotos. El fotógrafo me preguntó quién me había maquillado.", "t5"),
    ("Andrea G.", "Mamá de la novia · 2025", "Maquilló a todo el cortejo y todas quedamos divinas. Organizada y tranquila en medio del corre-corre.", "t6"),
]

FAQ_GENERAL = [
    ("¿Haces servicio a domicilio?", "Sí. Atiendo a domicilio en Bucaramanga, Floridablanca, Girón y Piedecuesta. El recargo depende de la zona; también puedes venir a mi estudio."),
    ("¿Cómo separo mi cita?", "Escríbeme por WhatsApp o llena el formulario. Para eventos y bodas se separa la fecha con un anticipo del 30 %."),
    ("¿Qué productos utilizas?", "Trabajo con marcas profesionales, de larga duración e hipoalergénicas. Si tienes alguna alergia o piel sensible, cuéntamelo con anticipación."),
    ("¿Cuánto tiempo toma el maquillaje?", "Entre 60 y 90 minutos según el look. El maquillaje de novia toma alrededor de 2 horas."),
    ("¿Cómo debo llegar a la cita?", "Con el rostro limpio e hidratado, sin maquillaje. Si usas lentes de contacto, ten listos los tuyos."),
    ("¿Qué pasa si debo cancelar?", "Puedes reprogramar sin costo avisando con 48 horas de anticipación. El anticipo no es reembolsable, pero se abona a una nueva fecha."),
]

PROCESS = [
    ("calendar-heart", "Agenda", "Escríbeme por WhatsApp o llena el formulario con tu fecha y servicio."),
    ("chat", "Asesoría", "Conversamos sobre tu evento, vestuario y el look que imaginas."),
    ("sparkle", "Tu día", "Llego puntual con todo lo necesario y creamos tu look con calma."),
    ("gift", "Retoque", "Te llevas recomendaciones y, en bodas, un kit de retoque para la noche."),
]

NAV = [
    ("index.html", "Inicio", "inicio"),
    ("servicios/index.html", "Servicios", "servicios"),
    ("galeria.html", "Galería", "galeria"),
    ("sobre-mi.html", "Sobre mí", "sobre-mi"),
    ("precios.html", "Precios", "precios"),
    ("contacto.html", "Contacto", "contacto"),
]


# ─────────────────────────── Piezas compartidas ───────────────────────────
def media(src, label, ratio="4x5", cls="", alt=None, eager=False, dark=False):
    """Imagen con respaldo: si el archivo no existe se ve un degradado con etiqueta."""
    extra = " media--dark" if dark else ""
    ratio_cls = f" ratio-{ratio}" if ratio else ""
    loading = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (
        f'<div class="media{ratio_cls}{extra} {cls}" data-label="{label}">'
        f'<img src="{src}" alt="{alt or label}" {loading} decoding="async"></div>'
    )


def header(r, active):
    links = "".join(
        f'<li><a class="nav__link" href="{r}{href}"{" aria-current=\"page\"" if key == active else ""}>{label}</a></li>'
        for href, label, key in NAV
    )
    mobile = "".join(
        f'<li><a href="{r}{href}"{" aria-current=\"page\"" if key == active else ""}>{label}</a></li>'
        for href, label, key in NAV
    )
    return f"""<a class="skip-link" href="#contenido">Saltar al contenido</a>
<header class="site-header">
  <div class="container">
    <a class="brand" href="{r}index.html" aria-label="Kirina Maoly Alba, inicio">
      {LOGO_MARK}
      <span class="brand__text"><span class="brand__name">Kirina Maoly Alba</span><span class="brand__tag">Makeup Artist</span></span>
    </a>
    <nav class="nav" aria-label="Principal">
      <ul class="nav__list">{links}</ul>
    </nav>
    <a class="btn btn--primary btn--sm header-cta" href="{r}contacto.html">{icon("calendar")}Agenda tu cita</a>
    <button class="menu-toggle" type="button" aria-controls="mobile-menu" aria-expanded="false" aria-label="Abrir menú"><span></span></button>
  </div>
</header>
<div class="mobile-menu" id="mobile-menu" aria-hidden="true">
  <nav aria-label="Menú móvil"><ul>{mobile}</ul></nav>
  <div class="mobile-menu__foot">
    <a class="btn btn--primary btn--lg" href="{r}contacto.html">{icon("calendar")}Agenda tu cita</a>
    <p>{SITE["city"]} · {SITE["phone"]}</p>
  </div>
</div>"""


def footer(r):
    services = "".join(f'<li><a href="{r}servicios/{s["key"]}.html">{s["name"]}</a></li>' for s in SERVICES)
    links = "".join(f'<li><a href="{r}{href}">{label}</a></li>' for href, label, _ in NAV)
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-about">
        <a class="brand" href="{r}index.html" aria-label="Kirina Maoly Alba, inicio">
          {LOGO_MARK}
          <span class="brand__text"><span class="brand__name">Kirina Maoly Alba</span><span class="brand__tag">Makeup Artist</span></span>
        </a>
        <p>Maquillaje profesional para resaltar tu belleza en cada momento especial.</p>
        <div class="socials">
          <a href="{SITE["instagram"]}" target="_blank" rel="noopener" aria-label="Instagram">{icon("instagram")}</a>
          <a href="{SITE["tiktok"]}" target="_blank" rel="noopener" aria-label="TikTok">{icon("tiktok")}</a>
          <a href="{SITE["facebook"]}" target="_blank" rel="noopener" aria-label="Facebook">{icon("facebook")}</a>
          <a href="{WA_LINK}" target="_blank" rel="noopener" aria-label="WhatsApp">{icon("whatsapp")}</a>
        </div>
      </div>
      <div>
        <h3>Enlaces rápidos</h3>
        <ul>{links}</ul>
      </div>
      <div>
        <h3>Servicios</h3>
        <ul>{services}</ul>
      </div>
      <div>
        <h3>Contacto</h3>
        <ul class="footer-contact">
          <li>{icon("pin")}<span>{SITE["city"]}</span></li>
          <li>{icon("whatsapp")}<a href="{WA_LINK}" target="_blank" rel="noopener">{SITE["phone"]}</a></li>
          <li>{icon("mail")}<a href="mailto:{SITE["email"]}">{SITE["email"]}</a></li>
          <li>{icon("clock")}<span>{SITE["hours"]}</span></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> Kirina Maoly Alba · Makeup Artist</span>
      <a href="{r}politica-de-privacidad.html">Política de privacidad</a>
    </div>
  </div>
</footer>
<a class="wa-float" href="{WA_LINK}" target="_blank" rel="noopener" aria-label="Escríbeme por WhatsApp">{icon("whatsapp")}</a>"""


def page(path, title, description, active, body, scripts=(), jsonld=None):
    depth = path.count("/")
    r = "../" * depth
    canonical = SITE["url"] + "/" + ("" if path == "index.html" else path)
    js = "\n".join(f'<script src="{r}assets/js/{s}" defer></script>' for s in ("main.js", *scripts))
    ld = f'\n<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>' if jsonld else ""
    html = f"""<!doctype html>
<html lang="es-CO">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#F6E3E6">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_CO">
<meta property="og:site_name" content="Kirina Maoly Alba · Makeup Artist">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE["url"]}/assets/img/og-image.jpg">
<link rel="icon" href="{r}assets/icons/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500;1,600&family=Jost:wght@300;400;500;600&family=Pinyon+Script&display=swap">
<link rel="stylesheet" href="{r}assets/css/tokens.css">
<link rel="stylesheet" href="{r}assets/css/base.css">
<link rel="stylesheet" href="{r}assets/css/components.css">
<link rel="stylesheet" href="{r}assets/css/sections.css">
<script>document.documentElement.classList.add("js")</script>{ld}
{js}
</head>
<body>
{header(r, active)}
<main id="contenido">
{body(r)}
</main>
{footer(r)}
</body>
</html>
"""
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print("✓", path)


# ─────────────────────────── Bloques reutilizables ───────────────────────────
def section_head(overline, title, text="", left=False):
    cls = "section-head section-head--left" if left else "section-head"
    ov = "overline" if left else "overline overline--center"
    p = f"<p>{text}</p>" if text else ""
    return f'<header class="{cls}" data-reveal><span class="{ov}">{overline}</span><h2>{title}</h2>{p}</header>'


def service_card(r, s, i=0):
    return f"""<article class="service-card" data-reveal style="--i:{i}">
  {media(f"{r}assets/img/services/{s['key']}.jpg", s["short"], alt=f"Maquillaje para {s['name'].lower()}")}
  <div class="service-card__icon">{icon(s["icon"])}</div>
  <div class="service-card__body">
    <h3 class="h4">{s["name"]}</h3>
    <p>{s["desc"]}</p>
    <div class="service-card__meta"><span class="price-from">${s["price"]}</span> · desde · {s["duration"]}</div>
    <div class="btn-row"><a class="btn btn--secondary btn--sm" href="{r}servicios/{s['key']}.html">Ver más</a></div>
  </div>
</article>"""


def services_grid(r):
    return '<div class="services-grid">' + "".join(service_card(r, s, i) for i, s in enumerate(SERVICES)) + "</div>"


def process_block():
    steps = "".join(
        f"""<div class="step" data-reveal style="--i:{i}">
  <div class="step__num">0{i + 1}</div>
  <div class="step__icon">{icon(ic)}</div>
  <h3>{t}</h3>
  <p>{d}</p>
</div>"""
        for i, (ic, t, d) in enumerate(PROCESS)
    )
    return f'<div class="process-grid">{steps}</div>'


def gallery_items(r, items):
    out = []
    for i, (gid, cat, cap, ratio) in enumerate(items):
        label = dict(CATS)[cat]
        out.append(
            f"""<button class="gallery-item" type="button" data-cat="{cat}" data-full="{r}assets/img/gallery/{gid}.jpg" data-caption="{cap}" aria-label="Ampliar: {cap}">
  {media(f"{r}assets/img/gallery/{gid}.jpg", label, ratio=ratio, alt=cap, dark=True)}
  <span class="gallery-item__overlay"><span>{label}</span>{icon("search")}</span>
</button>"""
        )
    return "".join(out)


def gallery_block(r, items, light=False):
    chips = "".join(
        f'<button class="chip" type="button" data-filter="{k}" aria-pressed="{str(k == "todos").lower()}">{v}</button>'
        for k, v in CATS
    )
    cls = "chips chips--light" if light else "chips"
    return f"""<div data-gallery>
  <div class="{cls}" role="group" aria-label="Filtrar galería" data-reveal>{chips}</div>
  <div class="gallery-grid mt-7">{gallery_items(r, items)}</div>
</div>"""


def lightbox():
    return f"""<dialog class="lightbox" id="lightbox" aria-label="Imagen ampliada">
  <figure class="lightbox__figure"><div class="media ratio-4x5"></div><figcaption></figcaption></figure>
  <button class="lightbox__btn lightbox__close" type="button" aria-label="Cerrar">{icon("close")}</button>
  <button class="lightbox__btn lightbox__prev" type="button" aria-label="Anterior">{icon("chevron-left")}</button>
  <button class="lightbox__btn lightbox__next" type="button" aria-label="Siguiente">{icon("chevron-right")}</button>
</dialog>"""


def testimonial(r, t, i=0):
    name, kind, text, img = t
    return f"""<figure class="testimonial" data-reveal style="--i:{i % 3}">
  <div class="testimonial__quote" aria-hidden="true">“</div>
  {STARS}
  <blockquote><p>{text}</p></blockquote>
  <figcaption>{media(f"{r}assets/img/testimonials/{img}.jpg", "", ratio="1x1", cls="avatar", alt=name)}<div><b>{name}</b><span>{kind}</span></div></figcaption>
</figure>"""


def testimonials_block(r, items):
    return '<div class="testimonials-track">' + "".join(testimonial(r, t, i) for i, t in enumerate(items)) + "</div>"


def price_card(r, p, i=0):
    feat = " price-card--featured" if p["featured"] else ""
    tag = '<span class="price-card__tag">Más elegido</span>' if p["featured"] else ""
    btn = "btn--primary" if p["featured"] else "btn--secondary"
    items = "".join(f"<li>{icon('check')}<span>{it}</span></li>" for it in p["items"])
    return f"""<article class="price-card{feat}" data-reveal style="--i:{i}">
  {tag}
  <h3 class="price-card__name">{p["name"]}</h3>
  <p class="price-card__desc">{p["desc"]}</p>
  <div class="price-card__value">{p["price"]}<small>{p["note"]}</small></div>
  <ul class="check-list">{items}</ul>
  <a class="btn {btn} btn--block" href="{r}contacto.html?servicio={p["service"]}">Reservar</a>
</article>"""


def pricing_block(r):
    return '<div class="pricing-grid">' + "".join(price_card(r, p, i) for i, p in enumerate(PACKAGES)) + "</div>"


def faq_block(items):
    rows = "".join(
        f'<details><summary>{q}</summary><div class="faq__answer"><p>{a}</p></div></details>' for q, a in items
    )
    return f'<div class="faq" data-reveal>{rows}</div>'


def booking_form(selected=None):
    opts = "".join(
        f'<option data-key="{s["key"]}"{" selected" if s["key"] == selected else ""}>{s["name"]}</option>' for s in SERVICES
    )
    return f"""<form class="form" data-booking novalidate>
  <div class="form__row form__row--2">
    <div class="field">
      <label for="f-nombre">Nombre completo</label>
      <input id="f-nombre" name="nombre" type="text" autocomplete="name" placeholder="¿Cómo te llamas?" required>
      <span class="field__error">Cuéntame tu nombre.</span>
    </div>
    <div class="field">
      <label for="f-telefono">WhatsApp</label>
      <input id="f-telefono" name="telefono" type="tel" autocomplete="tel" inputmode="tel" placeholder="311 555 1234" required>
      <span class="field__error">Ingresa un número válido de 10 dígitos.</span>
    </div>
  </div>
  <div class="form__row form__row--2">
    <div class="field">
      <label for="f-servicio">Servicio</label>
      <select id="f-servicio" name="servicio" required>
        <option value="" disabled{"" if selected else " selected"}>Elige un servicio</option>
        {opts}
        <option data-key="otro">Otro / personalizado</option>
      </select>
      <span class="field__error">Elige un servicio.</span>
    </div>
    <div class="field">
      <label for="f-fecha">Fecha del evento</label>
      <input id="f-fecha" name="fecha" type="date" required>
      <span class="field__error">Elige la fecha de tu evento.</span>
    </div>
  </div>
  <div class="form__row form__row--2">
    <fieldset class="field" style="border:0;padding:0">
      <legend class="visually-hidden">Lugar del servicio</legend>
      <span style="font-size:13px;font-weight:500;letter-spacing:.04em;color:var(--color-cocoa)">Lugar</span>
      <div class="radio-group">
        <label><input type="radio" name="lugar" value="Estudio" checked> Estudio</label>
        <label><input type="radio" name="lugar" value="A domicilio"> A domicilio</label>
      </div>
    </fieldset>
    <div class="field">
      <label for="f-personas">Número de personas</label>
      <input id="f-personas" name="personas" type="number" min="1" max="20" value="1">
    </div>
  </div>
  <div class="field">
    <label for="f-mensaje">Cuéntame de tu evento <span style="color:var(--color-taupe);font-weight:400">(opcional)</span></label>
    <textarea id="f-mensaje" name="mensaje" placeholder="Hora, lugar, estilo que imaginas, referencias…"></textarea>
  </div>
  <button class="btn btn--primary btn--lg btn--block" type="submit">{icon("whatsapp")}Enviar por WhatsApp</button>
  <p class="form__note">Al enviar se abrirá WhatsApp con tu mensaje listo. Respondo en menos de 2 horas en horario de atención.</p>
  <p class="form__success" role="status">¡Gracias! Se abrió WhatsApp con tu solicitud. Si no se abrió, escríbeme al {SITE["phone"]}.</p>
</form>"""


def contact_info():
    return f"""<div class="info-card">
  <div class="info-card__icon">{icon("whatsapp")}</div>
  <div><h3>WhatsApp</h3><a href="{WA_LINK}" target="_blank" rel="noopener">{SITE["phone"]}</a></div>
</div>
<div class="info-card">
  <div class="info-card__icon">{icon("mail")}</div>
  <div><h3>Correo</h3><a href="mailto:{SITE["email"]}">{SITE["email"]}</a></div>
</div>
<div class="info-card">
  <div class="info-card__icon">{icon("pin")}</div>
  <div><h3>Ubicación</h3><p>{SITE["city"]}<br>Estudio y servicio a domicilio</p></div>
</div>
<div class="info-card">
  <div class="info-card__icon">{icon("clock")}</div>
  <div><h3>Horario</h3><p>{SITE["hours"]}<br>Domingos y festivos con cita previa</p></div>
</div>"""


def cta_band(r, title="¿Lista para tu <em>próximo momento especial</em>?", text="Cuéntame de tu evento y diseñemos juntas el look perfecto para ti."):
    return f"""<section class="section">
  <div class="container">
    <div class="cta-band" data-reveal>
      <span class="overline overline--center" style="color:var(--color-gold)">Reserva tu fecha</span>
      <h2>{title}</h2>
      <p>{text}</p>
      <div class="btn-row">
        <a class="btn btn--primary btn--lg" href="{r}contacto.html">{icon("calendar")}Agenda tu cita</a>
        <a class="btn btn--dark btn--lg" href="{WA_LINK}" target="_blank" rel="noopener">{icon("whatsapp")}Escríbeme</a>
      </div>
    </div>
  </div>
</section>"""


def page_hero(r, overline, title, text, crumb):
    return f"""<section class="page-hero">
  <div class="container">
    <nav aria-label="Ruta"><ol class="breadcrumbs"><li><a href="{r}index.html">Inicio</a></li>{crumb}</ol></nav>
    <span class="overline overline--center">{overline}</span>
    <h1>{title}</h1>
    <p class="lead">{text}</p>
  </div>
</section>"""


# ─────────────────────────── Páginas ───────────────────────────
def build_index():
    def body(r):
        return f"""
<section class="hero" aria-labelledby="hero-title">
  <div class="hero__media">{media(f"{r}assets/img/hero/hero.jpg", "Foto principal", ratio="", alt="Kirina Maoly Alba maquillando a una novia", eager=True)}</div>
  <div class="container">
    <div class="hero__content">
      <span class="overline">Maquilladora profesional · Bucaramanga</span>
      <h1 class="display hero__title" id="hero-title" data-split><span data-line>Tu belleza</span> <span data-line>en cada</span> <em data-line>momento especial</em></h1>
      <p class="lead">Maquillaje profesional para resaltar lo mejor de ti, en tu boda, tu grado o esa noche que no quieres olvidar.</p>
      <ul class="hero__perks">
        <li>{icon("diamond")}Resultados de alta calidad</li>
        <li>{icon("brush")}Productos profesionales</li>
        <li>{icon("heart")}Estilo personalizado</li>
      </ul>
      <div class="btn-row">
        <a class="btn btn--primary btn--lg" href="{r}contacto.html">{icon("calendar")}Agenda tu cita</a>
        <a class="btn btn--secondary btn--lg" href="{r}galeria.html">Ver portafolio{ARROW}</a>
      </div>
      <div class="hero__proof">
        <div class="hero__avatars" aria-hidden="true"><span></span><span></span><span></span></div>
        <span><b>5.0</b> <span style="color:var(--color-gold)">★★★★★</span> · +300 clientas felices</span>
      </div>
    </div>
  </div>
</section>

<section class="stats" aria-label="Cifras">
  <div class="container">
    <div class="stats__grid">
      <div class="stat" data-reveal><b>6+</b><span>Años de experiencia</span></div>
      <div class="stat" data-reveal style="--i:1"><b>300+</b><span>Clientas felices</span></div>
      <div class="stat" data-reveal style="--i:2"><b>80+</b><span>Novias maquilladas</span></div>
      <div class="stat" data-reveal style="--i:3"><b>5.0</b><span>Valoración en Google</span></div>
    </div>
  </div>
</section>

<section class="section" id="servicios">
  <div class="container">
    {section_head("Servicios", "Mis <em>servicios</em>", "Maquillaje profesional para cada ocasión, adaptado a tu estilo y personalidad.")}
    {services_grid(r)}
    <div class="text-center mt-7"><a class="link" href="{r}servicios/index.html">Ver todos los servicios{ARROW}</a></div>
  </div>
</section>

<section class="section section--blush">
  <div class="container">
    {section_head("Cómo funciona", "Reservar es <em>muy fácil</em>", "Cuatro pasos para que llegues tranquila y radiante a tu evento.")}
    {process_block()}
  </div>
</section>

<section class="section section--noir" id="galeria">
  <div class="container">
    {section_head("Portafolio", "Galería de <em>maquillajes</em>", "Algunos de mis trabajos para diferentes ocasiones.")}
    {gallery_block(r, GALLERY[:8])}
    <div class="text-center mt-7"><a class="btn btn--dark" href="{r}galeria.html">Ver más trabajos{ARROW}</a></div>
  </div>
</section>

<section class="about" id="sobre-mi">
  <div class="about__media">{media(f"{r}assets/img/about/kirina.jpg", "Kirina Maoly Alba", ratio="", alt="Retrato de Kirina Maoly Alba")}</div>
  <div class="about__content" data-reveal>
    <span class="overline">Sobre mí</span>
    <div class="about__name"><h2>Kirina Maoly Alba</h2><span class="h3">Makeup Artist</span></div>
    <p>Soy una apasionada del maquillaje y del arte de resaltar la belleza única de cada persona. Mi objetivo es que te sientas segura, hermosa y auténtica en cada momento especial de tu vida.</p>
    <ul class="values">
      <li>{icon("heart")}Estilo personalizado</li>
      <li>{icon("diamond")}Técnicas profesionales</li>
      <li>{icon("sparkle")}Atención al detalle</li>
    </ul>
    <div class="signature" aria-hidden="true">Kirina</div>
    <div><a class="btn btn--primary" href="{r}sobre-mi.html">Conoce más sobre mí{ARROW}</a></div>
  </div>
</section>

<section class="section section--white" id="precios">
  <div class="container">
    {section_head("Paquetes", "Precios <em>claros</em>", "Elige el paquete ideal para tu ocasión. Todos incluyen asesoría personalizada.")}
    {pricing_block(r)}
    <p class="pricing-note">Servicio a domicilio desde $20.000 según la zona. <a class="link" href="{r}precios.html">Ver precios y extras</a></p>
  </div>
</section>

<section class="section section--mist">
  <div class="container">
    {section_head("Testimonios", "Lo que dicen <em>mis clientas</em>", "La satisfacción de mis clientas es mi mayor inspiración.")}
    {testimonials_block(r, TESTIMONIALS[:3])}
    <div class="text-center mt-6"><span class="rating-summary"><b>5.0</b>{STARS}<span>basado en reseñas de Google</span></span></div>
  </div>
</section>

<section class="season" aria-labelledby="season-title">
  <div class="container season__inner">
    <div class="season__content" data-reveal>
      <span class="overline">Temporada · Octubre</span>
      <h2 id="season-title">¡Prepárate para <em>Halloween</em>!</h2>
      <p class="lead" style="color:rgba(251,247,243,.85)">Looks únicos y personalizados para que destaques en la noche más creativa del año. Cupos limitados.</p>
      <div class="btn-row">
        <a class="btn btn--primary btn--lg" href="{r}contacto.html?servicio=halloween">Agenda tu maquillaje de Halloween{ARROW}</a>
        <a class="btn btn--dark btn--lg" href="{r}servicios/halloween.html">Ver looks</a>
      </div>
    </div>
  </div>
  <div class="season__media"><div class="media media--season" data-label="Halloween"><img src="{r}assets/img/season/halloween.jpg" alt="Maquillaje de catrina con rosas rojas" loading="lazy"></div></div>
</section>

<section class="section" id="faq">
  <div class="container faq-layout">
    {section_head("Preguntas frecuentes", "Resolvemos tus <em>dudas</em>", "¿No encuentras tu respuesta? Escríbeme por WhatsApp y te ayudo.", left=True)}
    {faq_block(FAQ_GENERAL)}
  </div>
</section>

<section class="section section--blush" id="reserva">
  <div class="container">
    {section_head("Reserva", "Agenda tu <em>cita</em>", "Completa el formulario y se abrirá WhatsApp con tu solicitud lista para enviar.")}
    <div class="booking">
      <div class="booking__form" data-reveal>{booking_form()}</div>
      <div class="booking__info" data-reveal style="--i:1">{contact_info()}</div>
    </div>
  </div>
</section>
{lightbox()}"""

    jsonld = {
        "@context": "https://schema.org",
        "@type": "BeautySalon",
        "name": "Kirina Maoly Alba · Makeup Artist",
        "description": "Maquilladora profesional en Bucaramanga: bodas, grados, eventos y maquillaje artístico de Halloween.",
        "url": SITE["url"],
        "telephone": SITE["phone_href"],
        "email": SITE["email"],
        "image": SITE["url"] + "/assets/img/og-image.jpg",
        "priceRange": "$$",
        "address": {"@type": "PostalAddress", "addressLocality": "Bucaramanga", "addressRegion": "Santander", "addressCountry": "CO"},
        "areaServed": ["Bucaramanga", "Floridablanca", "Girón", "Piedecuesta"],
        "openingHours": "Mo-Sa 07:00-19:00",
        "sameAs": [SITE["instagram"], SITE["tiktok"], SITE["facebook"]],
    }
    page(
        "index.html",
        "Kirina Maoly Alba · Maquilladora profesional en Bucaramanga",
        "Maquillaje profesional para bodas, grados, eventos y Halloween en Bucaramanga. Looks personalizados, productos profesionales y servicio a domicilio.",
        "inicio",
        body,
        scripts=("gallery.js", "booking.js"),
        jsonld=jsonld,
    )


def build_services_index():
    def body(r):
        rows = "".join(
            f"""<article class="service-row">
  <div class="service-row__media" data-reveal>{media(f"{r}assets/img/services/{s['key']}.jpg", s["short"], ratio="4x5", alt=f"Maquillaje para {s['name'].lower()}")}</div>
  <div class="service-row__content" data-reveal style="--i:1">
    <span class="overline">0{i + 1} · {s["short"]}</span>
    <h2>{s["name"]}</h2>
    <p class="lead">{s["tagline"]}.</p>
    <p>{s["desc"]}</p>
    <div class="service-row__meta">
      <span>{icon("sparkle")}Desde ${s["price"]}</span>
      <span>{icon("clock")}{s["duration"]}</span>
      <span>{icon("users")}{s["ideal"]}</span>
    </div>
    <div class="btn-row">
      <a class="btn btn--primary" href="{r}servicios/{s['key']}.html">Ver detalles{ARROW}</a>
      <a class="btn btn--secondary" href="{r}contacto.html?servicio={s['key']}">Reservar</a>
    </div>
  </div>
</article>"""
            for i, s in enumerate(SERVICES)
        )
        return f"""
{page_hero(r, "Servicios", "Maquillaje para <em>cada ocasión</em>", "Cada look se diseña a tu medida: tu rostro, tu estilo, tu evento.", '<li aria-current="page">Servicios</li>')}
<section class="section">
  <div class="container">{rows}</div>
</section>
<section class="section section--white">
  <div class="container">
    {section_head("Hecho a tu medida", "Maquillaje <em>personalizado</em>", "¿Tu evento no encaja en ninguna categoría? Sesiones de fotos, videoclips, pasarelas o clases de automaquillaje: cuéntame tu idea.")}
    <div class="cards-3">
      <div class="feature-card" data-reveal><div class="feature-card__icon">{icon("camera")}</div><h3>Sesiones y producciones</h3><p>Maquillaje para fotografía, video, campañas y pasarela, con piel impecable en cámara.</p></div>
      <div class="feature-card" data-reveal style="--i:1"><div class="feature-card__icon">{icon("mirror")}</div><h3>Clases de automaquillaje</h3><p>Aprende a maquillarte para el día a día o para eventos, con tus propios productos.</p></div>
      <div class="feature-card" data-reveal style="--i:2"><div class="feature-card__icon">{icon("users")}</div><h3>Grupos y empresas</h3><p>Equipos para eventos corporativos, quinces, cortejos y celebraciones grandes.</p></div>
    </div>
  </div>
</section>
<section class="section section--blush">
  <div class="container">
    {section_head("Cómo funciona", "Del primer mensaje <em>a tu gran día</em>")}
    {process_block()}
  </div>
</section>
{cta_band(r)}"""

    page(
        "servicios/index.html",
        "Servicios de maquillaje · Kirina Maoly Alba",
        "Maquillaje para bodas, grados, eventos sociales y Halloween en Bucaramanga. Conoce cada servicio, qué incluye y cómo reservar.",
        "servicios",
        body,
    )


def build_service_detail(s):
    others = [o for o in SERVICES if o["key"] != s["key"]]
    gallery = [g for g in GALLERY if g[1] == s["key"]][:4] or GALLERY[:4]

    def body(r):
        includes = "".join(f"<li>{icon('check')}<span>{it}</span></li>" for it in s["includes"])
        related = "".join(service_card(r, o, i) for i, o in enumerate(others[:3]))
        return f"""
<section class="split-hero">
  <div class="container split-hero__grid">
    <div class="split-hero__content" data-reveal>
      <nav aria-label="Ruta"><ol class="breadcrumbs"><li><a href="{r}index.html">Inicio</a></li><li><a href="{r}servicios/index.html">Servicios</a></li><li aria-current="page">{s["short"]}</li></ol></nav>
      <span class="overline">{s["name"]}</span>
      <h1>{s["tagline"]}</h1>
      <p class="lead">{s["desc"]}</p>
      <ul class="split-hero__facts">
        <li><small>Desde</small><b>${s["price"]}</b></li>
        <li><small>Duración</small><b>{s["duration"]}</b></li>
        <li><small>Ideal para</small><b style="font-size:20px">{s["ideal"]}</b></li>
      </ul>
      <div class="btn-row">
        <a class="btn btn--primary btn--lg" href="{r}contacto.html?servicio={s['key']}">{icon("calendar")}Reservar este servicio</a>
        <a class="btn btn--secondary btn--lg" href="{WA_LINK}" target="_blank" rel="noopener">{icon("whatsapp")}Preguntar</a>
      </div>
    </div>
    <div class="split-hero__media" data-reveal style="--i:1">{media(f"{r}assets/img/services/{s['key']}.jpg", s["short"], ratio="4x5", alt=f"Maquillaje para {s['name'].lower()}", eager=True)}</div>
  </div>
</section>

<section class="section">
  <div class="container two-col">
    <div class="prose" data-reveal>
      <span class="overline">La experiencia</span>
      <h2>Un look pensado <em>solo para ti</em></h2>
      <p>{s["long"]}</p>
      <p>Antes de empezar revisamos juntas tu piel, tus rasgos y el estilo que buscas. Así el resultado se ve como tú, en tu mejor versión.</p>
    </div>
    <div class="price-card" data-reveal style="--i:1;text-align:left">
      <h3 class="price-card__name">¿Qué incluye?</h3>
      <ul class="check-list">{includes}</ul>
      <a class="btn btn--primary btn--block" href="{r}contacto.html?servicio={s['key']}">Reservar · desde ${s["price"]}</a>
    </div>
  </div>
</section>

<section class="section section--noir">
  <div class="container">
    {section_head("Portafolio", f"Trabajos de <em>{s['short'].lower()}</em>")}
    <div class="gallery-grid">{gallery_items(r, gallery)}</div>
    <div class="text-center mt-7"><a class="btn btn--dark" href="{r}galeria.html">Ver galería completa{ARROW}</a></div>
  </div>
</section>

<section class="section section--blush">
  <div class="container">
    {section_head("Paso a paso", "Así trabajamos <em>juntas</em>")}
    {process_block()}
  </div>
</section>

<section class="section">
  <div class="container faq-layout">
    {section_head("Preguntas frecuentes", f"Sobre <em>{s['short'].lower()}</em>", "Si tienes otra duda, escríbeme con confianza.", left=True)}
    {faq_block(s["faq"])}
  </div>
</section>

<section class="section section--white">
  <div class="container">
    {section_head("También te puede interesar", "Otros <em>servicios</em>")}
    <div class="services-grid services-grid--3">{related}</div>
  </div>
</section>
{cta_band(r)}
{lightbox()}"""

    page(
        f"servicios/{s['key']}.html",
        f"Maquillaje de {s['short'].lower()} en Bucaramanga · Kirina Maoly Alba",
        f"{s['desc']} Desde ${s['price']}. Reserva por WhatsApp.",
        "servicios",
        body,
        scripts=("gallery.js",),
    )


def build_gallery():
    def body(r):
        return f"""
{page_hero(r, "Portafolio", "Galería de <em>maquillajes</em>", "Trabajos reales para bodas, grados, eventos y Halloween. Toca una imagen para verla en grande.", '<li aria-current="page">Galería</li>')}
<section class="section" style="padding-top:var(--space-7)">
  <div class="container">
    {gallery_block(r, GALLERY, light=True)}
  </div>
</section>
<section class="section section--white">
  <div class="container">
    {section_head("La transformación", "Antes y <em>después</em>", "Desliza para ver el cambio. Piel natural, rasgos realzados.")}
    <div class="compare-grid">
      {compare(r, 1, "Novia")}
      {compare(r, 2, "Evento social")}
    </div>
  </div>
</section>
{cta_band(r, "¿Te imaginas <em>tu look</em> aquí?")}
{lightbox()}"""

    page(
        "galeria.html",
        "Galería de maquillajes · Kirina Maoly Alba",
        "Portafolio de maquillaje de novias, grados, eventos y Halloween en Bucaramanga. Mira el antes y después.",
        "galeria",
        body,
        scripts=("gallery.js",),
    )


def compare(r, n, label):
    return f"""<div class="compare ratio-4x5" data-reveal style="--i:{n - 1}">
  {media(f"{r}assets/img/gallery/antes-{n}.jpg", f"Antes · {label}", ratio="", alt=f"Antes del maquillaje · {label}", dark=True)}
  <div class="compare__after">{media(f"{r}assets/img/gallery/despues-{n}.jpg", f"Después · {label}", ratio="", alt=f"Después del maquillaje · {label}")}</div>
  <span class="compare__label compare__label--before">Antes</span>
  <span class="compare__label compare__label--after">Después</span>
  <span class="compare__handle" aria-hidden="true"></span>
  <input type="range" min="0" max="100" value="50" aria-label="Comparar antes y después · {label}">
</div>"""


def build_about():
    def body(r):
        return f"""
<section class="split-hero">
  <div class="container split-hero__grid">
    <div class="split-hero__content" data-reveal>
      <nav aria-label="Ruta"><ol class="breadcrumbs"><li><a href="{r}index.html">Inicio</a></li><li aria-current="page">Sobre mí</li></ol></nav>
      <span class="overline">Sobre mí</span>
      <h1>Hola, soy <em>Kirina</em></h1>
      <p class="lead">Maquilladora profesional en Bucaramanga. Creo que el mejor maquillaje es el que te hace sentir tú misma, solo que más segura y radiante.</p>
      <ul class="split-hero__facts">
        <li><small>Experiencia</small><b>6+ años</b></li>
        <li><small>Clientas</small><b>300+</b></li>
        <li><small>Valoración</small><b>5.0 ★</b></li>
      </ul>
      <div class="signature" aria-hidden="true">Kirina Maoly Alba</div>
    </div>
    <div class="split-hero__media" data-reveal style="--i:1">{media(f"{r}assets/img/about/kirina.jpg", "Kirina Maoly Alba", ratio="3x4", alt="Retrato de Kirina Maoly Alba", eager=True)}</div>
  </div>
</section>

<section class="section">
  <div class="container two-col">
    <div class="prose" data-reveal>
      <span class="overline">Mi historia</span>
      <h2>El maquillaje como <em>forma de cuidar</em></h2>
      <p>Mi pasión empezó maquillando a mi familia y amigas para sus fechas especiales. Ver cómo cambiaba su manera de mirarse al espejo me hizo entender que el maquillaje es mucho más que técnica: es confianza.</p>
      <p>Me formé profesionalmente en maquillaje social, de novias y artístico, y sigo actualizándome cada año en nuevas técnicas y productos. Hoy acompaño a novias, graduandas y mujeres de todas las edades en algunos de los días más importantes de su vida.</p>
      <p>Cada rostro es diferente, por eso no trabajo con fórmulas: escucho, observo y diseño un look que respete tu esencia.</p>
    </div>
    <div data-reveal style="--i:1">
      <span class="overline">Trayectoria</span>
      <ol class="timeline mt-6">
        <li><b>2019</b><h3>Mis primeros pasos</h3><p>Comienzo a maquillar eventos sociales y sesiones de fotos en Bucaramanga.</p></li>
        <li><b>2020</b><h3>Formación profesional</h3><p>Certificación en maquillaje social y de novias.</p></li>
        <li><b>2022</b><h3>Maquillaje artístico</h3><p>Especialización en caracterización, efectos y maquillaje de fantasía.</p></li>
        <li><b>2024</b><h3>Estudio propio</h3><p>Abro mi estudio y amplío el servicio a domicilio en el área metropolitana.</p></li>
        <li><b>Hoy</b><h3>+300 clientas felices</h3><p>Y cada una con una historia que me inspira a seguir creciendo.</p></li>
      </ol>
    </div>
  </div>
</section>

<section class="section section--blush">
  <div class="container">
    {section_head("Mis valores", "Lo que me <em>define</em>")}
    <div class="cards-3">
      <div class="feature-card" data-reveal><div class="feature-card__icon">{icon("heart")}</div><h3>Estilo personalizado</h3><p>Nada de looks en serie: cada maquillaje nace de tu rostro, tu personalidad y tu evento.</p></div>
      <div class="feature-card" data-reveal style="--i:1"><div class="feature-card__icon">{icon("shield")}</div><h3>Higiene y calidad</h3><p>Brochas desinfectadas en cada servicio y productos profesionales, originales e hipoalergénicos.</p></div>
      <div class="feature-card" data-reveal style="--i:2"><div class="feature-card__icon">{icon("clock")}</div><h3>Puntualidad</h3><p>Sé lo importante que es tu tiempo ese día. Llego a la hora y trabajo con calma.</p></div>
    </div>
  </div>
</section>

<section class="section section--white">
  <div class="container">
    {section_head("Productos", "Marcas con las que <em>trabajo</em>", "Productos profesionales, de larga duración y aptos para piel sensible.")}
    <div class="brands" data-reveal><span>MAC</span><span>NARS</span><span>Huda Beauty</span><span>Urban Decay</span><span>Anastasia</span><span>Kryolan</span></div>
  </div>
</section>

<section class="section section--mist">
  <div class="container">
    {section_head("Testimonios", "Lo que dicen <em>mis clientas</em>")}
    {testimonials_block(r, TESTIMONIALS[3:6])}
  </div>
</section>
{cta_band(r, "Me encantará <em>conocerte</em>", "Cuéntame de tu evento y empecemos a diseñar tu look.")}"""

    page(
        "sobre-mi.html",
        "Sobre mí · Kirina Maoly Alba, maquilladora en Bucaramanga",
        "Conoce a Kirina Maoly Alba, maquilladora profesional en Bucaramanga: su historia, formación, valores y las marcas con las que trabaja.",
        "sobre-mi",
        body,
    )


def build_pricing():
    def body(r):
        rows = "".join(f"<tr><td><strong>{a}</strong></td><td>{b}</td><td>{c}</td></tr>" for a, b, c in EXTRAS)
        return f"""
{page_hero(r, "Precios", "Paquetes y <em>precios</em>", "Precios claros, sin sorpresas. Todos los servicios incluyen asesoría personalizada.", '<li aria-current="page">Precios</li>')}
<section class="section" style="padding-top:var(--space-8)">
  <div class="container">
    {pricing_block(r)}
  </div>
</section>
<section class="section section--white">
  <div class="container container--text">
    {section_head("Adicionales", "Servicios <em>extra</em>", "Complementa tu servicio con estas opciones.")}
    <div class="table-wrap" data-reveal>
      <table class="table">
        <thead><tr><th>Servicio</th><th>Detalle</th><th>Precio</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
  </div>
</section>
<section class="section section--blush">
  <div class="container">
    {section_head("Políticas", "Antes de <em>reservar</em>")}
    <div class="cards-3">
      <div class="feature-card" data-reveal><div class="feature-card__icon">{icon("calendar-heart")}</div><h3>Separa tu fecha</h3><p>Para bodas y eventos se separa la fecha con un anticipo del 30 %. El saldo se paga el día del servicio.</p></div>
      <div class="feature-card" data-reveal style="--i:1"><div class="feature-card__icon">{icon("clock")}</div><h3>Reprogramación</h3><p>Puedes cambiar la fecha sin costo avisando con 48 horas de anticipación. El anticipo se abona a la nueva fecha.</p></div>
      <div class="feature-card" data-reveal style="--i:2"><div class="feature-card__icon">{icon("home")}</div><h3>Domicilio</h3><p>Bucaramanga, Floridablanca, Girón y Piedecuesta. Recargo según la zona; fuera del área se cotizan viáticos.</p></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container faq-layout">
    {section_head("Preguntas frecuentes", "Dudas sobre <em>pagos</em>", "Aceptamos transferencia, Nequi, Daviplata y efectivo.", left=True)}
    {faq_block([
        ("¿Qué medios de pago aceptas?", "Transferencia bancaria, Nequi, Daviplata y efectivo."),
        ("¿Hay descuentos para grupos?", "Sí. Para 3 o más personas en el mismo lugar y horario hay tarifa especial. Escríbeme para cotizar."),
        ("¿El precio incluye pestañas?", "Todos los paquetes incluyen pestañas en tira. Las pestañas premium o por punto tienen un costo adicional, excepto en el paquete de novia."),
        ("¿Los precios cambian en temporada?", "En octubre (Halloween) y diciembre la agenda se llena rápido; los precios se mantienen, pero te recomiendo reservar con tiempo."),
    ])}
  </div>
</section>
{cta_band(r)}"""

    page(
        "precios.html",
        "Precios de maquillaje · Kirina Maoly Alba",
        "Paquetes y precios de maquillaje profesional en Bucaramanga: social, grado y novia. Servicios adicionales, políticas y medios de pago.",
        "precios",
        body,
    )


def build_contact():
    def body(r):
        return f"""
{page_hero(r, "Contacto", "Agenda tu <em>cita</em>", "Completa el formulario y se abrirá WhatsApp con tu solicitud lista. Respondo en menos de 2 horas.", '<li aria-current="page">Contacto</li>')}
<section class="section" style="padding-top:var(--space-7)">
  <div class="container booking">
    <div class="booking__form" data-reveal>
      <h2 class="h3" style="margin-bottom:var(--space-5)">Cuéntame de tu evento</h2>
      {booking_form()}
    </div>
    <div class="booking__info" data-reveal style="--i:1">
      {contact_info()}
      <div class="map">
        <iframe src="https://www.google.com/maps?q=Bucaramanga,+Santander,+Colombia&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Mapa de Bucaramanga"></iframe>
      </div>
    </div>
  </div>
</section>
<section class="section section--white">
  <div class="container faq-layout">
    {section_head("Preguntas frecuentes", "Antes de <em>escribirme</em>", "", left=True)}
    {faq_block(FAQ_GENERAL[:4])}
  </div>
</section>"""

    page(
        "contacto.html",
        "Contacto y reservas · Kirina Maoly Alba",
        "Agenda tu cita de maquillaje en Bucaramanga por WhatsApp. Horarios, ubicación y servicio a domicilio.",
        "contacto",
        body,
        scripts=("booking.js",),
    )


def build_privacy():
    def body(r):
        return f"""
{page_hero(r, "Legal", "Política de <em>privacidad</em>", "Tratamiento de datos personales conforme a la Ley 1581 de 2012 de Colombia.", '<li aria-current="page">Política de privacidad</li>')}
<section class="section" style="padding-top:var(--space-7)">
  <div class="container container--text prose">
    <p><strong>Última actualización:</strong> octubre de 2026.</p>
    <h2 class="h3">1. Responsable del tratamiento</h2>
    <p>Kirina Maoly Alba, maquilladora profesional con domicilio en {SITE["city"]}. Correo: <a class="link" href="mailto:{SITE["email"]}">{SITE["email"]}</a> · WhatsApp: {SITE["phone"]}.</p>
    <h2 class="h3">2. Datos que recopilamos</h2>
    <ul>
      <li>Nombre y número de WhatsApp.</li>
      <li>Tipo de servicio, fecha, lugar y detalles del evento que compartas voluntariamente.</li>
      <li>Información sobre alergias o sensibilidad de la piel, solo si decides contarla para cuidar tu salud.</li>
    </ul>
    <h2 class="h3">3. Finalidad</h2>
    <p>Usamos tus datos únicamente para responder tu solicitud, agendar y prestar el servicio, enviarte recordatorios de tu cita y, si lo autorizas, compartir promociones de temporada.</p>
    <h2 class="h3">4. Fotografías</h2>
    <p>Solo publicamos fotos de tu maquillaje en el portafolio o redes sociales con tu autorización expresa. Puedes retirarla en cualquier momento.</p>
    <h2 class="h3">5. Tus derechos</h2>
    <p>Como titular puedes conocer, actualizar, rectificar y solicitar la supresión de tus datos, así como revocar la autorización otorgada. Para ejercerlos, escríbenos al correo indicado; responderemos en los plazos que establece la ley.</p>
    <h2 class="h3">6. Seguridad y conservación</h2>
    <p>No vendemos ni compartimos tus datos con terceros. Los conservamos solo durante el tiempo necesario para la finalidad descrita.</p>
    <h2 class="h3">7. Formulario y WhatsApp</h2>
    <p>El formulario de este sitio no almacena información en servidores: al enviarlo se abre WhatsApp con tu mensaje, y la conversación se rige también por las políticas de WhatsApp.</p>
  </div>
</section>"""

    page(
        "politica-de-privacidad.html",
        "Política de privacidad · Kirina Maoly Alba",
        "Política de tratamiento de datos personales de Kirina Maoly Alba, Makeup Artist.",
        "",
        body,
    )


def build_404():
    def body(r):
        return f"""
<section class="not-found">
  <div>
    <div class="not-found__code">404</div>
    <h1 class="h2">Esta página se <em>desmaquilló</em></h1>
    <p class="lead" style="margin:var(--space-4) auto var(--space-6)">No encontramos lo que buscabas, pero tu próximo look sí te está esperando.</p>
    <div class="btn-row">
      <a class="btn btn--primary btn--lg" href="{r}index.html">Volver al inicio</a>
      <a class="btn btn--secondary btn--lg" href="{r}galeria.html">Ver galería</a>
    </div>
  </div>
</section>"""

    page("404.html", "Página no encontrada · Kirina Maoly Alba", "La página que buscas no existe.", "", body)


if __name__ == "__main__":
    build_index()
    build_services_index()
    for s in SERVICES:
        build_service_detail(s)
    build_gallery()
    build_about()
    build_pricing()
    build_contact()
    build_privacy()
    build_404()
