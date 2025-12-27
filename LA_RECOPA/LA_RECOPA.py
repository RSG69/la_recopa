import json
import reflex as rx

from .layout import header, footer
from .menu_weekend import menu_weekend
from .celda import crear_celda

# ================================================
#   TEMA
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
    ["Huevos fritos con patatas y jamón", "/almuerzos/huevos fritos con patatas y jamon.jpg"],
    ["Callos con tomate", "/almuerzos/callos.jpg"],
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
#   CUERPO
# ================================================
def cuerpo():
    return rx.box(
        rx.script(src="/JS/animation.js"),

        rx.box(
            rx.grid(
                crear_celda(
                    "DESAYUNOS",
                    DESAYUNOS,
                    "up",
                    "linear-gradient(135deg,#e6c193,#ED8F03)",
                ),
                crear_celda(
                    "ALMUERZOS",
                    ALMUERZOS,
                    "down",
                    "linear-gradient(135deg,#43C6AC,#191654)",
                ),
                crear_celda(
                    "TAPAS",
                    TAPAS,
                    "left",
                    "linear-gradient(135deg,#F7971E,#FFD200)",
                ),
                crear_celda(
                    "PLATOS",
                    PLATOS,
                    "right",
                    "linear-gradient(135deg,#8360c3,#2ebf91)",
                ),
                crear_celda(
                    "DESAYUNOS",
                    DESAYUNOS,
                    "up",
                    "linear-gradient(135deg,#e6c193,#ED8F03)",
                ),
                crear_celda(
                    "ALMUERZOS",
                    ALMUERZOS,
                    "down",
                    "linear-gradient(135deg,#43C6AC,#191654)",
                ),
                crear_celda(
                    "TAPAS",
                    TAPAS,
                    "left",
                    "linear-gradient(135deg,#F7971E,#FFD200)",
                ),
                crear_celda(
                    "MENU FIN DE SEMANA",
                    PLATOS,
                    "right",
                    "linear-gradient(135deg,#8360c3,#2ebf91)",
                    link="/menu-weekend",   # 👈 SOLO ESTA ES CLICABLE
                ),
                columns=rx.breakpoints(sm="1", md="2", lg="3"),
                spacing="6",
                justify="center",
            ),
            class_name="grid-background",
        ),

        margin_top="70px",
    )

# ================================================
#   PÁGINA PRINCIPAL
# ================================================
def galeria():
    return rx.box(
        header(),
        cuerpo(),
        footer(),
        bg="linear-gradient(135deg, #fddac7, #f7bfa8)",
        min_height="100vh",
    )

# ================================================
#   APP
# ================================================
app = rx.App(
    stylesheets=["/carousel.css"],
    theme=custom_theme,
)

app.add_page(galeria, title="La Recopa", route="/")
app.add_page(menu_weekend, title="Menú Fin de Semana", route="/menu-weekend")

if __name__ == "__main__":
    app.run()
