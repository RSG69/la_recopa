import json
import reflex as rx

# ================================================
#   TEMA GENERAL
# ================================================
custom_theme = rx.theme(color_scheme="orange")

# ================================================
#   LISTAS
# ================================================
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

# ================================================
#   CELDAS
# ================================================
def crear_celda(titulo, lista, direccion, gradiente):
    textos = [t for (t, _) in lista]
    rutas = [img for (_, img) in lista]

    return rx.box(
        rx.vstack(
            rx.heading(
                titulo,
                font_family="Playfair Display",
                font_size="28px",
                font_weight="700",
                color="white",
                text_shadow="1px 2px 6px rgba(0,0,0,0.4)",
                class_name="heading",
                width="100%",
                text_align="left"
            ),

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

            class_name="vstack-wrapper",
            width="100%",
            align_items="stretch",
        ),

        class_name="carousel-item",
        background=gradiente,
    )


# ================================================
#   HEADER
# ================================================
def header():
    return rx.box(
        rx.hstack(
            rx.heading(
                "La Recopa",
                font_size="2xl",
                font_weight="700",
                color="#ffffff",
                padding_left="20px",
                text_shadow="1px 2px 6px rgba(0,0,0,0.4)",
            ),
        ),
        width="100%",
        height="80px",
        display="flex",
        align_items="center",
        bg="linear-gradient(135deg,#8360c3,#2ebf91)",
        position="fixed",
        top="0",
        left="0",
        border_bottom="2px solid rgba(255,255,255,0.5)",
        z_index="100",
    )


# ================================================
#   FOOTER (CORREGIDO Y VISIBLE)
# ================================================
def footer():
    return rx.box(
        rx.text(
            "© 2025 La Recopa — Todos los derechos reservados",
            font_size="md",
            color="#333",          # ← AHORA SE VE
        ),
        bg="white",
        height="50px",
        width="100%",
        position="fixed",
        bottom="0",
        display="flex",
        align_items="center",
        justify_content="center",
        border_top="1px solid #ccc",
        z_index="300",
    )


# ================================================
#   CUERPO
# ================================================
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
                crear_celda("DESAYUNOS", DESAYUNOS, "up",
                            "linear-gradient(135deg,#e6c193,#ED8F03)"),
                crear_celda("ALMUERZOS", ALMUERZOS, "down",
                            "linear-gradient(135deg,#43C6AC,#191654)"),
                crear_celda("TAPAS", TAPAS, "left",
                            "linear-gradient(135deg,#F7971E,#FFD200)"),
                crear_celda("PLATOS", PLATOS, "right",
                            "linear-gradient(135deg,#8360c3,#2ebf91)"),

                columns=rx.breakpoints(sm="1", md="2", lg="3"),
                spacing="6",
                justify="center",
                class_name="grid"
            ),
            class_name="grid-background",
        ),

        rx.script(src="/JS/animation.js")
    )


# ================================================
#   PÁGINA FINAL
# ================================================
def galeria():
    return rx.box(
        header(),
        cuerpo(),
        rx.box(class_name="footer-spacer"),  # ← ÚNICO SPACER
        footer(),
    )


# ================================================
#   APP
# ================================================
app = rx.App(
    stylesheets=["/carousel.css"],
    theme=custom_theme,
)

app.add_page(galeria, title="La Recopa", route="/")

if __name__ == "__main__":
    app.run()
