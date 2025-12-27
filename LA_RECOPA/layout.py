import reflex as rx

# ================================================
#   HEADER
# ================================================
def header():
    return rx.box(
        rx.hstack(
            #rx.image(src="/Bar_Cafeteria.png", height="80px", class_name="logo-bar"),
            rx.image(src="/cafeteria.png", height="80px", class_name="logo-bar"),
            rx.image(src="/escudo.png", height="60px", class_name="logo-escudo"),
            rx.image(src="/la_recopa.png", height="80px", class_name="logo-recopa"),
            spacing="9",
            align="center",
            justify="center",
            class_name="header-logos",
        ),
        width="100%",
        #height="95px",
        position="fixed",
        top="0",
        z_index="1000",
        display="flex",
        align_items="center",
        justify_content="center",
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
        """,
    )

# ================================================
#   FOOTER
# ================================================
def footer():
    return rx.box(
        rx.hstack(
            rx.box(width="120px"),
            rx.text(
                "Direccion: C/ Mosen Andres Vicente , nº 27 - Zaragoza - Telefono: 976 31 57 15",
                class_name="footer-text",
                width="100%",
                text_align="center",
            ),
            rx.vstack(
                rx.image(src="/rsg69.png", width="28px", height="28px", border_radius="6px"),
                rx.text("©Robert69", font_size="12px", color="#555"),
                spacing="0",
                align="center",
                width="120px",
            ),
            justify="between",
            align="center",
            width="100%",
            padding_x="12px",
        ),
        bg="white",
        height="auto",
        width="100%",
        position="fixed",
        bottom="0",
        border_top="1px solid #ccc",
        z_index="300",
    )