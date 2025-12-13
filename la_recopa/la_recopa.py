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
    ["Café con leche y croissant", "/desayunos/Cafe_con_leche_y_cruasan.jpg"],
    ["Café con leche y tostadas", "/desayunos/cafe_con_leche_y_tostada_con_mermelada.jpg"],
    ["Zumo natural y pan con tomate", "/desayunos/zumo_natural_y_tostada_con_tomate.jpg"],
]

ALMUERZOS = [
    ["huevos fritos con patatas y jamon", "/almuerzos/huevos fritos con patatas y jamon.jpg"],
    ["Callos", "/almuerzos/callos.jpg"],
    ["Salchichas a la riojana", "/almuerzos/salchichas a la riojana.jpg"],
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
                class_name="heading",
            ),

            rx.box(
                rx.image(src=rutas[0]),
                class_name="carousel-box",
                data_direction=direccion,
                data_images=json.dumps(rutas),
                data_texts=json.dumps(textos),
            ),

            rx.text(
                textos[0],
                class_name="carousel-item-text",
            ),

            class_name="vstack-wrapper",
        ),

        class_name="carousel-item",
        background=gradiente,
    )

# ================================================
#   HEADER (CORREGIDO)
# ================================================
def header():
    return rx.box(
        rx.hstack(
            rx.image(
                src="/Bar_Cafeteria.png",
                height="80px",
                class_name="logo-bar",
            ),
            rx.image(
                src="/escudo.png",
                height="60px",
                class_name="logo-escudo",
            ),
            rx.image(
                src="/la_recopa.png",
                height="80px",
                class_name="logo-recopa",
            ),
            spacing="9",
            align="center",
            justify="center",
            class_name="header-logos",
        ),
        width="100%",
        height="95px",
        bg="""
            linear-gradient(
            135deg,
            rgba(255,255,255,0.06),
            rgba(255,255,255,0)
            ),
            linear-gradient(
            135deg,
            #5A0F14,
            #A4161A
            )
            """ ,
        position="fixed",
        top="0",
        z_index="1000",
        display="flex",
        align_items="center",
        justify_content="center",
        overflow="visible",
    )





# ================================================
#   FOOTER
# ================================================
def footer():
    return rx.box(
        rx.hstack(
            rx.box(width="120px"),

            rx.text(
                "Direccion: C/ Mosen Andres Vicente , nº 27 - Zaragoza - Telefono: 976 31 57 15 ",
                class_name="footer-text",
                text_align="center",
                width="100%",
            ),

            rx.vstack(
                rx.image(
                    src="/rsg69.png",
                    width="28px",
                    height="28px",
                    border_radius="6px",
                ),
                rx.text(
                    "©Robert69",
                    font_size="12px",
                    color="#555",
                    margin_right="2px",
                ),
                spacing="0",
                align="center",
                justify="end",
                width="120px",
            ),
            align="center",
            justify="between",
            width="100%",
            padding_x="12px",
        ),

        bg="white",
        height="60px",
        width="100%",
        position="fixed",
        bottom="0",
        border_top="1px solid #ccc",
        display="flex",
        align_items="center",
        z_index="300",
    )

# ================================================
#   CUERPO (MARGEN AÑADIDO)
# ================================================
def cuerpo():
    return rx.box(
        rx.script(src="/JS/animation.js"),  # ← POSICIONAL PRIMERO

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
                class_name="grid",
            ),
            class_name="grid-background",
        ),

        margin_top="90px",
    )


# ================================================
#   PÁGINA
# ================================================
def galeria():
    return rx.box(
        header(),
        cuerpo(),
        rx.box(class_name="footer-spacer"),
        footer(),
        bg="#fddac7"   # ← elimina franja negra
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
