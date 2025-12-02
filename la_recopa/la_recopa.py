import reflex as rx

# ===========================
#      TEMA PERSONALIZADO
# ===========================
custom_theme = rx.theme(color_scheme="orange")


# ===========================
#         STATE
# ===========================
class State(rx.State):

    DESAYUNOS = [
        ["Café con leche y croissant", "/Cafe_con_leche_y_cruasan.jpg"],
        ["Café con leche y tostadas con mermelada", "/cafe_con_leche_y_tostada_con_mermelada.jpg"],
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

    index_desayuno: int = 0
    index_almuerzo: int = 0
    index_tapa: int = 0
    index_plato: int = 0

    def next_desayuno(self): self.index_desayuno = (self.index_desayuno + 1) % len(self.DESAYUNOS)
    def next_almuerzo(self): self.index_almuerzo = (self.index_almuerzo + 1) % len(self.ALMUERZOS)
    def next_tapa(self): self.index_tapa = (self.index_tapa + 1) % len(self.TAPAS)
    def next_plato(self): self.index_plato = (self.index_plato + 1) % len(self.PLATOS)

    @rx.var
    def desayuno_text(self) -> str: return self.DESAYUNOS[self.index_desayuno][0]
    @rx.var
    def desayuno_img(self) -> str: return self.DESAYUNOS[self.index_desayuno][1]

    @rx.var
    def almuerzo_text(self) -> str: return self.ALMUERZOS[self.index_almuerzo][0]
    @rx.var
    def almuerzo_img(self) -> str: return self.ALMUERZOS[self.index_almuerzo][1]

    @rx.var
    def tapa_text(self) -> str: return self.TAPAS[self.index_tapa][0]
    @rx.var
    def tapa_img(self) -> str: return self.TAPAS[self.index_tapa][1]

    @rx.var
    def plato_text(self) -> str: return self.PLATOS[self.index_plato][0]
    @rx.var
    def plato_img(self) -> str: return self.PLATOS[self.index_plato][1]


# ===========================
#       COMPONENTES UI
# ===========================

def header():
    return rx.box(
        rx.hstack(
            rx.heading("🌅 Mi Galería", font_size="2xl", color="orange.600"),
            rx.spacer(),
            rx.text("Inicio | Galería | Contacto"),
        ),
        bg="white",
        height="70px",
        width="100%",
        position="fixed",
        top="0",
        left="0",
        border_bottom="2px solid #ddd",
        padding_x="20px",
        z_index="100",
    )


def crear_celda(titulo: str, texto: rx.Var, imagen: rx.Var, direccion: str, gradiente: str):
    return rx.box(
        rx.vstack(
            rx.heading(
                titulo,
                font_family="Playfair Display",
                font_size="3xl",
                color="white",
                text_shadow="1px 1px 4px rgba(0,0,0,0.5)"
            ),

            # solo 1 imagen dentro — el JS generará la otra
            rx.box(
                rx.image(
                    src=imagen,
                    class_name="carousel-img",
                    data_direction=direccion,
                ),
                class_name="carousel-box",
            ),

            rx.text(texto, class_name="carousel-item-text"),
        ),
        padding="12px",
        border_radius="18px",
        background=gradiente,
        border="3px solid rgba(255,255,255,0.4)",
        box_shadow="0 6px 16px rgba(0,0,0,0.25)",
    )


def footer():
    return rx.box(
        rx.text(
            "© 2025 Mi Galería Reflex — Todos los derechos reservados",
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
        z_index="100",
    )


def cuerpo():
    return rx.box(

        rx.box(
            rx.grid(
                crear_celda("DESAYUNOS", State.desayuno_text, State.desayuno_img, "up",
                            "linear-gradient(135deg, #e6c193, #ED8F03)"),

                crear_celda("ALMUERZOS", State.almuerzo_text, State.almuerzo_img, "down",
                            "linear-gradient(135deg, #43C6AC, #191654)"),

                crear_celda("TAPAS", State.tapa_text, State.tapa_img, "left",
                            "linear-gradient(135deg, #F7971E, #FFD200)"),

                crear_celda("PLATOS", State.plato_text, State.plato_img, "right",
                            "linear-gradient(135deg, #8360c3, #2ebf91)"),

                columns=rx.breakpoints(sm="1", md="2", lg="3"),
                spacing="6",
                justify="center",
            ),
            padding_top="100px",
            padding_bottom="100px",
            class_name="grid-background",
        ),

        # Botones ocultos (Reflex actualiza la imagen)
        rx.button("next", id="next-desayuno", on_click=State.next_desayuno, style={"display": "none"}),
        rx.button("next", id="next-almuerzo", on_click=State.next_almuerzo, style={"display": "none"}),
        rx.button("next", id="next-tapa", on_click=State.next_tapa, style={"display": "none"}),
        rx.button("next", id="next-plato", on_click=State.next_plato, style={"display": "none"}),

        # ===========================
        #      JAVASCRIPT COMPLETO
        # ===========================
        rx.script(r"""
(function() {

  const TIME_IN  = 1800; 
  const TIME_OUT = 1800;
  const PAUSE    = 3800;

  const wait = ms => new Promise(res => setTimeout(res, ms));

  const directions = {
    up:    { in_from: "translateY(100%)", out_to: "translateY(-100%)" },
    down:  { in_from: "translateY(-100%)", out_to: "translateY(100%)" },
    left:  { in_from: "translateX(100%)", out_to: "translateX(-100%)" },
    right: { in_from: "translateX(-100%)", out_to: "translateX(100%)" },
  };

  const NEXT_BUTTONS = [
    "next-desayuno",
    "next-almuerzo",
    "next-tapa",
    "next-plato"
  ];

  async function animateCell(box, idx) {

    while (true) {

      let imgOld = box.querySelector("img");

      /* 1️⃣ SI LA IMG NO TIENE DIRECCIÓN, LA TOMAMOS DEL BOX */
      let direction = imgOld.dataset.direction || box.dataset.direction;

      /* 2️⃣ VALIDAMOS DIRECCIÓN */
      if (!direction || !directions[direction]) {
        console.error("Dirección inválida en celda", idx, direction);
        return;
      }

      let conf = directions[direction];

      /* 3️⃣ Guardamos src viejo */
      let oldSrc = imgOld.dataset.realSrc || imgOld.src;

      /* 4️⃣ Pedimos nueva imagen */
      document.getElementById(NEXT_BUTTONS[idx]).click();
      await wait(80);

      let newSrc = imgOld.src;  // Reflex la puso aquí

      /* Restaurar la vieja para animarla */
      imgOld.src = oldSrc;
      imgOld.dataset.realSrc = oldSrc;

      /* 5️⃣ Crear nueva imagen */
      const imgNew = document.createElement("img");
      imgNew.src = newSrc;
      imgNew.dataset.realSrc = newSrc;

      /* ⬅️⬅️⬅️ ***LA LÍNEA QUE FALTABA*** */
      imgNew.dataset.direction = direction;

      /* posición inicial fuera del cuadro */
      imgNew.style.transform = conf.in_from;

      box.appendChild(imgNew);

      /* 6️⃣ Animar entrada */
      const animIn = imgNew.animate(
        [
          { transform: conf.in_from },
          { transform: "translateX(0) translateY(0)" }
        ],
        { duration: TIME_IN, easing: "ease-out" }
      );

      /* 7️⃣ Animar salida */
      const animOut = imgOld.animate(
        [
          { transform: "translateX(0) translateY(0)" },
          { transform: conf.out_to }
        ],
        { duration: TIME_OUT, easing: "ease-in" }
      );

      /* 8️⃣ Esperamos ambas */
      await Promise.all([animIn.finished, animOut.finished]);

      /* 9️⃣ Eliminamos la vieja */
      imgOld.remove();

      /* 1️⃣0️⃣ Reset */
      imgNew.style.transform = "none";

      /* 1️⃣1️⃣ Guardamos dirección en el BOX para seguridad */
      box.dataset.direction = direction;

      await wait(PAUSE);
    }
  }

  /* Inicialización */
  setTimeout(() => {
    const boxes = [...document.querySelectorAll(".carousel-box")];
    boxes.forEach((box, index) => animateCell(box, index));
  }, 600);

})();

        """),
    )


def galeria():
    return rx.box(
        header(),
        cuerpo(),
        footer(),
    )


app = rx.App(
    stylesheets=["/carousel.css"],
    theme=custom_theme
)

app.add_page(galeria, title="Galería con animaciones", route="/")


if __name__ == "__main__":
    app.run()
















