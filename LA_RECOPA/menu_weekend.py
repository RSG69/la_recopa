import reflex as rx
from .layout import header, footer
from .celda import crear_celda

# =================================================
#   DATOS (Se mantienen igual)
# =================================================
PLATOS_1 = [
    ["Tomate Rosa con Bonito del Norte y Cebolla", "/platos_1/Tomate Rosa con Bonito del Norte y cebolla.jpg"],
    ["Tallarines a la Bolonesa", "/platos_1/Tallarines a la Bolonesa.jpg"],
    ["Verduritas a la plancha con Salsa Romescu", "/platos_1/Verduritas a la plancha con Salsa Romescu.jpg"],
    ["Tosta Gratinada con Setas, Brie y Jamon", "/platos_1/Tosta Gratinada con Setas, Brie y Jamon.jpg"],
]

PLATOS_2 = [
    ["Entrecotte a la pimienta con Patatas Fritas", "/platos_2/Entrecotte a la pimienta con Patatas Fritas.jpg"],
    ["Codillo Asado con Patatas Panaderas", "/platos_2/Codillo Asado con Patatas Panaderas.jpg"],
    ["Lomo Relleno de Bacon y Cammembert", "/platos_2/Lomo Relleno de Bacon y Cammembert.jpg"],
    ["Salmon Fresco al Horno con Guarnicion", "/platos_2/Salmon Fresco al Horno con Guarnicion.jpg"],
]

POSTRES = [
    ["Tarta al Whisky", "/postres/Tarta al Whisky.jpg"],
    ["Tarta de Queso Casero", "/postres/Tarta de Queso Casero.jpg"],
    ["Postre Navideño Especial", "/postres/Postre Navideño Especial.jpg"],
]

BEBIDA_Y_PAN  = [
    ["Vino '3404' D. O. Somomtano, Agua y Pan", "/Vino Agua y Pan.png"],

]

TITULO = "Menú Fin De Semana - 20 y 21 de Diciembre"

# =================================================
#   PÁGINA
# =================================================
def menu_weekend():
    return rx.box(
        header(), 

        rx.vstack(
            # 1. TÍTULO con margen responsivo
            rx.heading(
                TITULO,
                size=rx.breakpoints(
                    initial="5",    # Tamaño para móvil (se queda igual para que no se corte)
                    sm="8",         # 🔑 MÁS GRANDE para tablet vertical (antes era 6)
                    md="8",         # 🔑 MÁS GRANDE para tablet horizontal / iPad Pro
                    lg="9",         # 🔑 MÁXIMO tamaño para ordenadores (antes era 8)
                ),
                color="#5A0F14",
                font_weight="bold",
                text_align="center",
                width="100%",
                padding_x="1.5rem",
                line_height="1.1",
                # 🔑 MARGEN DINÁMICO: 0 en móvil, aumenta en tablet y PC
                margin_bottom=rx.breakpoints(
                    initial="0.625rem",    # Sin margen en el móvil
                    sm="3.5rem",        # Margen para tablet
                    lg="2rem"         # Margen para ordenador
                ),
            ),

            # 2. CONTENEDOR DEL GRID
            rx.box(
                rx.grid(
                    crear_celda(
                        "Primer Plato",
                        PLATOS_1,
                        "right",
                        "linear-gradient(135deg,#8360c3,#2ebf91)",
                    ),
                    crear_celda(
                        "Segundo Plato",
                        PLATOS_2,
                        "right",
                        "linear-gradient(135deg,#8360c3,#2ebf91)",
                    ),
                    crear_celda(
                        "Postres",
                        POSTRES,
                        "right",
                       "linear-gradient(135deg,#F7971E,#FFD200)",
                    ),
                    crear_celda(
                        "Bebida y Pan",
                        BEBIDA_Y_PAN,
                        None,
                       "linear-gradient(135deg,#43C6AC,#191654)",
                    ),
                    columns=rx.breakpoints(
                        initial="1", 
                        sm="2",      # Forzamos 2 celdas desde el tamaño sm
                        md="2",      
                        lg="2",      
                    ),  
                    spacing="6", 
                    width="100%",
                    justify_items="center",
                    align_items="start",
                ),
                width="100%",
                max_width="1100px",
                display="flex",
                justify_content="center",
                padding_x="1rem",
            ),

            # PROPIEDADES DEL VSTACK
            width="100%",
            align="center",
            # Ponemos spacing en 0 para que solo mande el margin_bottom del título
            spacing="0", 
            padding_top=rx.breakpoints(
                initial="70px",   
                sm="90px",
                lg="100px"        
            ),
            padding_bottom="100px",
        ),

        footer(),
        bg="linear-gradient(135deg, #fddac7, #f7bfa8)",
        min_height="100vh",
    )