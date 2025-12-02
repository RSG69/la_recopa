import json
import reflex as rx

# ==========================================================
#   TEMA (debe ir arriba)
# ==========================================================
custom_theme = rx.theme(color_scheme="orange")

# ==========================================================
#   LISTAS DE IMÁGENES (fuera del State)
# ==========================================================
DESAYUNOS = [
    ["Café con leche y croissant", "/Cafe_con_leche_y_cruasan.jpg"],
    ["Café con leche y tostadas", "/cafe_con_leche_y_tostada_con_mermelada.jpg"],
    ["Zumo natural y pan con tomate", "/zumo_natural_y_tostada_con_tomate.jpg"],
]

ALMUERZOS = [
    ["Ensalada César", "/ensalada_cesar.jpg"],
    ["Pasta boloñesa", "/pasta_bolonesa.jpg"],
    ["Sopa del día", "/sopa_de_fideos.jpg"],
]

TAPAS = [
    ["Tortilla española", "/tortilla.jpg"],
    ["Calamares a la romana", "/calamares.jpg"],
    ["Patatas bravas", "/patatas_bravas.jpg"],
]

PLATOS = [
    ["Filete con patatas", "/filete_con_patatas.jpg"],
    ["Paella valenciana", "/paella.jpg"],
    ["Lentejas caseras", "/lentejas.jpg"],
]

# ==========================================================
#   STATE (solo para textos)
# ==========================================================
class State(rx.State):

    @rx.var
    def desayuno_text(self) -> str:
        return DESAYUNOS[0][0]

    @rx.var
    def almuerzo_text(self) -> str:
        return ALMUERZOS[0][0]

    @rx.var
    def tapa_text(self) -> str:
        return TAPAS[0][0]

    @rx.var
    def plato_text(self) -> str:
        return PLATOS[0][0]

# ==========================================================
#   COMPONENTE DE CELDA
# ==========================================================
def crear_celda(titulo, texto, lista, direccion, gradiente):
    """
    lista: lista de pares [texto, ruta]
    direccion: "up" | "down" | "left" | "right"
    """
    rutas = [img for (_, img) in lista]

    # data_images debe ser un string JSON para compatibilidad con todas las versiones
    return rx.box(
        rx.vstack(
            rx.heading(
                titulo,
                font_family="Playfair Display",
                font_size="3xl",
                color="white",
                text_shadow="1px 1px 4px rgba(0,0,0,0.5)",
            ),

            # SOLO UNA IMG en el DOM inicial. El JS usará data-images para el carrusel.
            rx.box(
                rx.image(src=rutas[0], class_name="carousel-img"),
                class_name="carousel-box",
                data_direction=direccion,
                data_images=json.dumps(rutas),
            ),

            rx.text(texto, class_name="carousel-item-text"),
        ),
        padding="12px",
        border_radius="18px",
        background=gradiente,
        border="3px solid rgba(255,255,255,0.4)",
        box_shadow="0 6px 16px rgba(0,0,0,0.25)",
    )


# ==========================================================
#   HEADER / FOOTER
# ==========================================================
def header():
    return rx.box(
        rx.hstack(
            rx.heading("🌅 La Recopa", font_size="2xl", color="orange.600"),
            rx.spacer(),
        ),
        bg="white",
        height="70px",
        width="100%",
        position="fixed",
        top="0",
        border_bottom="2px solid #ddd",
        padding_x="20px",
        z_index="100",
    )


def footer():
    return rx.box(
        rx.text(
            "© 2025 La Recopa — Todos los derechos reservados",
            font_size="sm",
            color="gray.600",
        ),
        bg="white",
        height="60px",
        width="100%",
        position="fixed",
        bottom="0",
        border_top="2px solid #ddd",
        display="flex",
        align_items="center",
        justify_content="center",
    )


# ==========================================================
#   CUERPO CON EL JS EMBEBIDO
# ==========================================================
def cuerpo():
    return rx.box(
        rx.box(
            rx.grid(
                crear_celda(
                    "DESAYUNOS",
                    State.desayuno_text,
                    DESAYUNOS,
                    "up",
                    "linear-gradient(135deg, #e6c193, #ED8F03)",
                ),
                crear_celda(
                    "ALMUERZOS",
                    State.almuerzo_text,
                    ALMUERZOS,
                    "down",
                    "linear-gradient(135deg, #43C6AC, #191654)",
                ),
                crear_celda(
                    "TAPAS",
                    State.tapa_text,
                    TAPAS,
                    "left",
                    "linear-gradient(135deg, #F7971E, #FFD200)",
                ),
                crear_celda(
                    "PLATOS",
                    State.plato_text,
                    PLATOS,
                    "right",
                    "linear-gradient(135deg, #8360c3, #2ebf91)",
                ),
                columns=rx.breakpoints(sm="1", md="2", lg="3"),
                spacing="6",
                justify="center",
            ),
            padding_top="100px",
            padding_bottom="100px",
            class_name="grid-background",
        ),

        # JAVASCRIPT: carrusel que toma data-images (string JSON) y controla todo el flujo
        rx.script(
            r"""
(function(){

  const TIME_IN  = 1800;   // ms entrada
  const TIME_OUT = 1800;   // ms salida
  const PAUSE    = 3800;   // ms pausa entre cambios

  const wait = ms => new Promise(res => setTimeout(res, ms));

  const directions = {
    up:    { in_from: "translateY(100%)", out_to: "translateY(-100%)" },
    down:  { in_from: "translateY(-100%)", out_to: "translateY(100%)" },
    left:  { in_from: "translateX(100%)", out_to: "translateX(-100%)" },
    right: { in_from: "translateX(-100%)", out_to: "translateX(100%)" }
  };

  function safeParseJson(s) {
    try { return JSON.parse(s); }
    catch(e){ console.error("JSON parse error for data-images:", s); return []; }
  }

  function animateCell(box) {
    const images = safeParseJson(box.dataset.images || "[]");
    const direction = box.dataset.direction || "up";
    const conf = directions[direction] || directions.up;
    if (!images.length) return;

    let idx = 0;
    // img inicial
    const imgInitial = box.querySelector("img");
    if (imgInitial) imgInitial.src = images[0];

    async function loop() {
      while (true) {
        // Obtener la imagen visible actual
        const oldImg = box.querySelector("img");

        // Calcular siguiente índice y src
        idx = (idx + 1) % images.length;
        const newSrc = images[idx];

        // Crear nueva imagen fuera del viewport según dirección
        const imgNew = document.createElement("img");
        imgNew.src = newSrc;
        imgNew.style.position = "absolute";
        imgNew.style.top = "0";
        imgNew.style.left = "0";
        imgNew.style.width = "100%";
        imgNew.style.height = "100%";
        imgNew.style.objectFit = "cover";
        imgNew.style.borderRadius = "15px";
        imgNew.style.willChange = "transform, opacity";
        imgNew.style.transform = conf.in_from;

        box.appendChild(imgNew);

        // Animaciones: entrada de imgNew y salida de oldImg simultáneas
        const aIn = imgNew.animate(
          [
            { transform: conf.in_from },
            { transform: "translateX(0) translateY(0)" }
          ],
          { duration: TIME_IN, easing: "ease-out", fill: "forwards" }
        );

        const aOut = oldImg.animate(
          [
            { transform: "translateX(0) translateY(0)" },
            { transform: conf.out_to }
          ],
          { duration: TIME_OUT, easing: "ease-in", fill: "forwards" }
        );

        await Promise.all([aIn.finished, aOut.finished]);

        // Remover la vieja y dejar la nueva en su sitio
        oldImg.remove();
        imgNew.style.transform = "none";

        // Esperar pausa antes del siguiente cambio
        await wait(PAUSE);
      }
    }

    // lanzamos el loop (no bloqueante)
    loop();
  }

  // Inicialización: buscar todas las cajas y arrancar su animación
  setTimeout(() => {
    document.querySelectorAll(".carousel-box").forEach(animateCell);
  }, 400);

})();
"""
        )
    )


def galeria():
    return rx.box(header(), cuerpo(), footer())


# ==========================================================
#   APP
# ==========================================================
app = rx.App(stylesheets=["/carousel.css"], theme=custom_theme)
app.add_page(galeria, title="La Recopa", route="/")

if __name__ == "__main__":
    app.run()



















