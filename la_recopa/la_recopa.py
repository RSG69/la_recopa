import reflex as rx

custom_theme = rx.theme(color_scheme="orange")

class State(rx.State):
    DESAYUNOS = [
        ["Café con leche y croissant", "/Cafe_con_leche_y_cruasan.jpg"],
        ["Café con leche y tostadas con mermelada", "/cafe_con_leche_y_tostada_con_mermelada.jpg"],
        ["Zumo natural y pan con tomate", "/zumo_natural_y_tostada_con_tomate.jpg"]
    ]
    ALMUERZOS = [
        ["Ensalada César", "/ensalada_cesar.jpg"],
        ["Pasta boloñesa", "/pasta_bolonesa.jpg"],
        ["Sopa del día", "/sopa_de_fideos.jpg"]
    ]
    TAPAS = [
        ["Tortilla española", "/tortilla.jpg"],
        ["Calamares a la romana", "/calamares.jpg"],
        ["Patatas bravas", "/patatas_bravas.jpg"]
    ]
    PLATOS = [
        ["Filete con patatas", "/filete_con_patatas.jpg"],
        ["Paella valenciana", "/paella.jpg"],
        ["Lentejas caseras", "/lentejas.jpg"]
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


def crear_celda(titulo: str, texto: rx.Var, imagen: rx.Var, direccion: str, gradiente: str) -> rx.Component:
    """Celda con doble imagen para animación suave."""
    return rx.box(
        rx.vstack(
            rx.heading(
                titulo,
                font_family="Playfair Display, serif",
                font_size="3xl",
                font_weight="bold",
                color="white",
                text_align="center",
                text_shadow="1px 1px 4px rgba(0,0,0,0.5)",
            ),
            rx.box(
                rx.box(
                    # IMAGEN DOBLE: current + next
                    rx.image(
                        src=imagen,
                        class_name="img-current",
                        data_direction=direccion,
                    ),
                    rx.image(
                        src=imagen,
                        class_name="img-next",
                        data_direction=direccion,
                    ),
                    class_name="carousel-dual",
                ),
                rx.text(texto, class_name="carousel-item-text"),
                class_name="carousel-item",
            ),
        ),
        border="3px solid rgba(255,255,255,0.4)",
        border_radius="18px",
        padding="12px",
        background=gradiente,
        box_shadow="0 6px 16px rgba(0,0,0,0.25)",
    )


def header():
    return rx.box(
        rx.hstack(
            rx.heading("🌅 Mi Galería", font_size="2xl", color="orange.600"),
            rx.spacer(),
            rx.text("Inicio | Galería | Contacto", font_size="md"),
        ),
        bg="white",
        height="70px",
        width="100%",
        position="fixed",
        top="0",
        left="0",
        shadow="md",
        border_bottom="2px solid #ddd",
        z_index="100",
        padding_x="20px",
        align_items="center",
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
        left="0",
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
                align_items="center",
                width="90%",
                max_width="1200px",
            ),
            padding_top="100px",
            padding_bottom="100px",
            width="100%",
            overflow="visible",
            display="flex",
            justify_content="center",
            align_items="flex-start",
            position="relative",
            class_name="grid-background",
        ),

        # BOTONES OCULTOS
        rx.button("next", id="next-desayuno", on_click=State.next_desayuno, style={"display": "none"}),
        rx.button("next", id="next-almuerzo", on_click=State.next_almuerzo, style={"display": "none"}),
        rx.button("next", id="next-tapa", on_click=State.next_tapa, style={"display": "none"}),
        rx.button("next", id="next-plato", on_click=State.next_plato, style={"display": "none"}),

        # SCRIPT con animación suave + doble imagen
        rx.script(r"""
(function(){
  const IN_DURATION  = 2000;
  const OUT_DURATION = 1800;
  const VISIBLE_MS   = 3000;

  const anims = {
    up: {
      in:  [{ transform: "translateY(40%)", opacity: 0 },
            { transform: "translateY(0)", opacity: 1 }],
      out: [{ transform: "translateY(0)", opacity: 1 },
            { transform: "translateY(-40%)", opacity: 0 }]
    },
    down: {
      in:  [{ transform: "translateY(-40%)", opacity: 0 },
            { transform: "translateY(0)", opacity: 1 }],
      out: [{ transform: "translateY(0)", opacity: 1 },
            { transform: "translateY(40%)", opacity: 0 }]
    },
    left: {
      in:  [{ transform: "translateX(40%)", opacity: 0 },
            { transform: "translateX(0)", opacity: 1 }],
      out: [{ transform: "translateX(0)", opacity: 1 },
            { transform: "translateX(-40%)", opacity: 0 }]
    },
    right: {
      in:  [{ transform: "translateX(-40%)", opacity: 0 },
            { transform: "translateX(0)", opacity: 1 }],
      out: [{ transform: "translateX(0)", opacity: 1 },
            { transform: "translateX(40%)", opacity: 0 }]
    },
    fade: {
      in:  [{ opacity: 0 }, { opacity: 1 }],
      out: [{ opacity: 1 }, { opacity: 0 }]
    }
  };

  const buttons = ["next-desayuno","next-almuerzo","next-tapa","next-plato"];
  const wait = ms => new Promise(res => setTimeout(res, ms));

  async function runDual(current, next, idx) {
    const dir = current.dataset.direction || "fade";
    const anim = anims[dir];
    const btnId = buttons[idx];

    while (true) {
      const nextSrc = next.src;

      await next.animate(anim.in, { duration: IN_DURATION, fill: "forwards" }).finished;
      await wait(VISIBLE_MS);
      await current.animate(anim.out, { duration: OUT_DURATION, fill: "forwards" }).finished;

      document.getElementById(btnId)?.click();

      await wait(40);

      current.src = nextSrc;
      current.style.opacity = 1;
      current.style.transform = "none";

      next.style.opacity = 0;
      next.style.transform = "none";
    }
  }

  setTimeout(() => {
    const pairs = [...document.querySelectorAll(".carousel-dual")]
      .map(box => [
        box.querySelector(".img-current"),
        box.querySelector(".img-next")
      ]);

    pairs.forEach((pair, idx) => runDual(pair[0], pair[1], idx));
  }, 400);

})();
        """)
    )


def galeria():
    return rx.box(
        header(),
        cuerpo(),
        footer(),
        height="100vh",
        width="100vw",
        overflow="visible",
    )


app = rx.App(stylesheets=["/carousel.css"], theme=custom_theme)
app.add_page(galeria, title="Galería con animaciones suaves", route="/")

if __name__ == "__main__":
    app.run()















