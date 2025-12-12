import json
import reflex as rx

custom_theme = rx.theme(color_scheme="orange")

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


def crear_celda(titulo, lista, direccion, gradiente):
    textos = [t for (t, _) in lista]
    rutas = [img for (_, img) in lista]

    return rx.box(
        rx.vstack(
            rx.heading(titulo, class_name="heading"),
            rx.box(
                rx.image(src=rutas[0]),
                class_name="carousel-box",
                data_direction=direccion,
                data_images=json.dumps(rutas),
                data_texts=json.dumps(textos),
            ),
            rx.text(textos[0], class_name="carousel-item-text"),
            class_name="vstack-wrapper",
        ),
        class_name="carousel-item",
        background=gradiente,
    )


def header():
    # header FIXED by CSS class app-header
    return rx.box(
        rx.hstack(
            rx.image(src="/escudo.png", width="90px", height="90px", border_radius="8px"),
            rx.vstack(
                rx.heading("Bar - Cafeteria",
                           font_size="clamp(16px,3vw,26px)",
                           font_weight="700",
                           color="white"),
                rx.heading("La Recopa",
                           font_size="clamp(20px,4vw,32px)",
                           font_weight="700",
                           color="white",
                           margin_top="-6px"),
                spacing="2",
                align="start",
            ),
            spacing="4",
            align="center",
            justify="center",
        ),
        class_name="app-header",
    )


def footer():
    return rx.box(
        rx.hstack(
            rx.box(width="120px"),  # left spacer so center is exact
            rx.text(
                "Dir.: C/ Mosen Andres Vicente , nº 27 - Zaragoza - Tfno.: 976 31 57 15",
                class_name="footer-text",
                width="100%",
                text_align="center",
            ),
            rx.hstack(
                rx.text("©Robert69", font_size="12px", color="#555", margin_right="4px"),
                rx.image(src="/rsg69.png", width="28px", height="28px", border_radius="6px"),
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
        class_name="app-footer",
    )


def cuerpo_grid():
    # returns ONLY the grid container (no scroll props here)
    return rx.box(
        rx.grid(
            crear_celda("DESAYUNOS", DESAYUNOS, "up", "linear-gradient(135deg,#e6c193,#ED8F03)"),
            crear_celda("ALMUERZOS", ALMUERZOS, "down", "linear-gradient(135deg,#43C6AC,#191654)"),
            crear_celda("TAPAS", TAPAS, "left", "linear-gradient(135deg,#F7971E,#FFD200)"),
            crear_celda("PLATOS", PLATOS, "right", "linear-gradient(135deg,#8360c3,#2ebf91)"),
            crear_celda("DESAYUNOS", DESAYUNOS, "up", "linear-gradient(135deg,#e6c193,#ED8F03)"),
            crear_celda("ALMUERZOS", ALMUERZOS, "down", "linear-gradient(135deg,#43C6AC,#191654)"),
            crear_celda("TAPAS", TAPAS, "left", "linear-gradient(135deg,#F7971E,#FFD200)"),
            crear_celda("PLATOS", PLATOS, "right", "linear-gradient(135deg,#8360c3,#2ebf91)"),
            columns=rx.breakpoints(sm="1", md="2", lg="3"),
            spacing="6",
            justify="center",
            class_name="grid",
        ),
        class_name="grid-background",
    )


def cuerpo():
    # Note: rx.script must come BEFORE keyword props to avoid SyntaxError
    return rx.box(
        cuerpo_grid(),
        rx.script(src="/JS/animation.js"),
        class_name="scroll-area",
    )


def galeria():
    return rx.box(
        header(),
        cuerpo(),   # this element has class scroll-area and is the only scroller
        footer(),
    )


app = rx.App(stylesheets=["/carousel.css"], theme=custom_theme)
app.add_page(galeria, title="La Recopa", route="/")

if __name__ == "__main__":
    app.run()
