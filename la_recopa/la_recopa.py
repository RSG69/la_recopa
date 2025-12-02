import json
import reflex as rx

# ==========================================================
#   TEMA
# ==========================================================
custom_theme = rx.theme(color_scheme="orange")

# ==========================================================
#   LISTAS (texto + imagen)
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
#   COMPONENTE DE CELDA
# ==========================================================
def crear_celda(titulo, lista, direccion, gradiente):

    textos = [t for (t, _) in lista]
    rutas = [img for (_, img) in lista]

    return rx.box(

        rx.vstack(
            rx.heading(titulo, font_family="Playfair Display, serif", font_size="4xl",
                       font_weight="bold", color="white", text_align="center",
                       text_shadow="1px 1px 4px rgba(0,0,0,0.5)"),

            

            # SOLO UNA IMAGEN. El JS cambia las demás.
            rx.box(
                rx.image(src=rutas[0], class_name="carousel-img"),
                class_name="carousel-box",
                data_direction=direccion,
                data_images=json.dumps(rutas),
                data_texts=json.dumps(textos),
            ),

            rx.text(
                textos[0],
                class_name="carousel-item-text carousel-text",
            ),
        ),

        class_name="carousel-item",
        background=gradiente,
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
#   CUERPO + JS
# ==========================================================
def cuerpo():
    return rx.box(

        rx.box(
            rx.grid(

                crear_celda("DESAYUNOS", DESAYUNOS, "up",
                            "linear-gradient(135deg,#e6c193,#ED8F03)"),

                crear_celda("ALMUERZOS", ALMUERZOS, "down",
                            "linear-gradient(135deg,#43C6AC,#191654)"),

                crear_celda("TAPAS", TAPAS, "left",
                            "linear-gradient(135deg,#F7971E,#FFD200)"),

                crear_celda("PLATOS", PLATOS, "right",
                            "linear-gradient(135deg,#8360c3,#2ebf91)"),

                columns=rx.breakpoints(sm="1", md="2", lg="3"),
                spacing="5",
                justify="center",
            ),

            padding_top="100px",
            padding_bottom="100px",
            class_name="grid-background",
        ),

        # -------------------------------------------------------
        # JS COMPLETO: texto sale antes + dimensiones fijas
        # -------------------------------------------------------
        rx.script(r"""
(function(){

  const TIME_IN  = 1500;
  const TIME_OUT = 1500;
  const PAUSE    = 3500;

  const wait = ms => new Promise(res => setTimeout(res, ms));

  const directions = {
    up:    { in_from: "translateY(120%)", out_to: "translateY(-120%)" },
    down:  { in_from: "translateY(-120%)", out_to: "translateY(120%)" },
    left:  { in_from: "translateX(120%)", out_to: "translateX(-120%)" },
    right: { in_from: "translateX(-120%)", out_to: "translateX(120%)" }
  };

  function animateCell(box) {
    const images = JSON.parse(box.dataset.images || "[]");
    const texts  = JSON.parse(box.dataset.texts  || "[]");

    if (images.length === 0) return;

    const direction = box.dataset.direction;
    const conf = directions[direction];

    let index = 0;

    let imgOld = box.querySelector("img");
    imgOld.src = images[0];

    const textEl = box.parentElement.querySelector(".carousel-text");
    textEl.innerText = texts[0];

    async function loop() {
      const oldImg = box.querySelector("img");

      index = (index + 1) % images.length;
      const newSrc  = images[index];
      const newText = texts[index];

      /* 1) EL TEXTO SALE ANTES */
      await textEl.animate(
        [
          { opacity: 1, transform: "translateY(0)" },
          { opacity: 0, transform: "translateY(-20px)" }
        ],
        { duration: 450, easing: "ease-in", fill: "forwards" }
      ).finished;

      /* 2) LA IMAGEN CAMBIA */
      const imgNew = document.createElement("img");
      imgNew.src = newSrc;
      imgNew.style.position = "absolute";
      imgNew.style.top = "0";
      imgNew.style.left = "0";
      imgNew.style.width = "100%";
      imgNew.style.height = "100%";
      imgNew.style.objectFit = "cover";
      imgNew.style.transform = conf.in_from;

      box.appendChild(imgNew);

      const aIn = imgNew.animate(
        [{ transform: conf.in_from }, { transform: "translate(0,0)" }],
        { duration: TIME_IN, easing: "ease-out", fill: "forwards" }
      );

      const aOut = oldImg.animate(
        [{ transform: "translate(0,0)" }, { transform: conf.out_to }],
        { duration: TIME_OUT, easing: "ease-in", fill: "forwards" }
      );

      await Promise.all([aIn.finished, aOut.finished]);

      oldImg.remove();

      /* 3) EL TEXTO ENTRA DESPUÉS */
      textEl.innerText = newText;
      textEl.animate(
        [
          { opacity: 0, transform: "translateY(20px)" },
          { opacity: 1, transform: "translateY(0)" }
        ],
        { duration: 600, easing: "ease-out", fill: "forwards" }
      );

      await wait(PAUSE);
      loop();
    }

    loop();
  }

  setTimeout(() => {
    document.querySelectorAll(".carousel-box").forEach(animateCell);
  }, 300);

})();

        """)
    )


def galeria():
    return rx.box(
        header(),
        cuerpo(),
        footer(),
    )


app = rx.App(
    stylesheets=["/carousel.css"],
    theme=custom_theme,
)

app.add_page(galeria, title="La Recopa", route="/")

if __name__ == "__main__":
    app.run()






















