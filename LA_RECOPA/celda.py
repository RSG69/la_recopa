import json
import reflex as rx

def crear_celda(titulo, lista, direccion, gradiente, link=None):
    textos = [t for (t, _) in lista]
    rutas = [img for (_, img) in lista]

    return rx.box(
        rx.vstack(
            rx.heading(titulo, class_name="heading"),

            rx.box(
                rx.image(src=rutas[0]),
                class_name="carousel-box",
                #data_direction=direccion,
                data_direction=direccion if direccion else "none",
                data_images=json.dumps(rutas),
                data_texts=json.dumps(textos),
            ),

            rx.text(textos[0], class_name="carousel-item-text"),
            class_name="vstack-wrapper",
        ),
        class_name="carousel-item",
        background=gradiente,

        cursor="pointer" if link else "default",
        on_click=rx.redirect(link) if link else None,
    )
