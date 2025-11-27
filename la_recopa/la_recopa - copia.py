import reflex as rx
import json

custom_theme = rx.theme(color_scheme="orange")

# --- Estado ---
class State(rx.State):
    @rx.var
    def desayuno_text(self) -> str: return "Café con leche y croissant"
    @rx.var
    def desayuno_img(self) -> str: return "/Cafe_con_leche_y_cruasan.jpg"

    @rx.var
    def almuerzo_text(self) -> str: return "Ensalada César"
    @rx.var
    def almuerzo_img(self) -> str: return "/ensalada_cesar.jpg"

    @rx.var
    def tapa_text(self) -> str: return "Tortilla española"
    @rx.var
    def tapa_img(self) -> str: return "/tortilla.jpg"

    @rx.var
    def plato_text(self) -> str: return "Filete con patatas"
    @rx.var
    def plato_img(self) -> str: return "/filete_con_patatas.jpg"


# --- Cabecera ---
def header() -> rx.Component:
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
        shadow="md",
        border_bottom="2px solid #ddd",
        z_index="100",
        padding_x="20px",
        align_items="center",
    )


# --- Celda individual ---
def crear_celda(titulo: str, texto: rx.Var, imagen: rx.Var, direccion: str, gradiente: str, lista: list) -> rx.Component:
    images = json.dumps([item[1] for item in lista])
    texts = json.dumps([item[0] for item in lista])

    return rx.box(
        rx.vstack(
            rx.heading(titulo, font_family="Playfair Display, serif", font_size="4xl",
                       font_weight="bold", color="white", text_align="center",
                       text_shadow="1px 1px 4px rgba(0,0,0,0.5)"),
            rx.box(
                rx.box(
                    rx.image(
                        src=imagen,
                        width="100%",
                        height="100%",
                        border_radius="lg",
                        shadow="lg",
                        class_name="carousel-item-img",
                        data_direction=direccion,
                        data_images=images,
                        data_texts=texts,
                    ),
                    class_name="carousel-image-wrapper",
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


# --- Pie ---
def footer() -> rx.Component:
    return rx.box(
        rx.text("© 2025 Mi Galería Reflex — Todos los derechos reservados",
                font_size="sm", color="gray.600"),
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


# --- Cuerpo + SCRIPT ANIMADO ---
def cuerpo() -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.grid(
                    crear_celda("DESAYUNOS", State.desayuno_text, State.desayuno_img, "up",
                                "linear-gradient(135deg, #e6c193, #ED8F03)",
                                [
                                    ["Café con leche y croissant", "/Cafe_con_leche_y_cruasan.jpg"],
                                    ["Café con leche y tostadas con mermelada", "/cafe_con_leche_y_tostada_con_mermelada.jpg"],
                                    ["Zumo natural y pan con tomate", "/zumo_natural_y_tostada_con_tomate.jpg"],
                                ],
                                ),
                    crear_celda("ALMUERZOS", State.almuerzo_text, State.almuerzo_img, "down",
                                "linear-gradient(135deg, #43C6AC, #191654)",
                                [
                                    ["Ensalada César", "/ensalada_cesar.jpg"],
                                    ["Pasta boloñesa", "/pasta_bolonesa.jpg"],
                                    ["Sopa del día", "/sopa_de_fideos.jpg"],
                                ]),
                    crear_celda("TAPAS", State.tapa_text, State.tapa_img, "right",
                                "linear-gradient(135deg, #F7971E, #FFD200)",
                                [
                                    ["Tortilla española", "/tortilla.jpg"],
                                    ["Calamares a la romana", "/calamares.jpg"],
                                    ["Patatas bravas", "/patatas_bravas.jpg"],
                                ]),
                    crear_celda("PLATOS COMBINADOS", State.plato_text, State.plato_img, "fade",
                                "linear-gradient(135deg, #8360c3, #2ebf91)",
                                [
                                    ["Filete con patatas", "/filete_con_patatas.jpg"],
                                    ["Paella valenciana", "/paella.jpg"],
                                    ["Lentejas caseras", "/lentejas.jpg"],
                                ]),
                    columns=rx.breakpoints(sm="1", md="2", lg="3"),
                    spacing="6",
                    justify="center",
                    align_items="center",
                    width="90%",
                    max_width="1200px",
                ),
                class_name="grid-background",
            ),
            padding_top="50px",
            padding_bottom="50px",
        ),

        # --- SCRIPT CON ANIMACIÓN PEGADA Y VISIBLE ---
        rx.script(r"""
(function(){
  const IN_DURATION  = 1600;
  const OUT_DURATION = 1500;
  const VISIBLE_MS   = 2400;
  const START_DELAY  = 500;

  const wait = (ms)=>new Promise(r=>setTimeout(r,ms));

  const anims={
    up:{in:[{transform:"translateY(35%)",opacity:0},{transform:"translateY(0)",opacity:1}],
        out:[{transform:"translateY(0)",opacity:1},{transform:"translateY(-35%)",opacity:0}]},
    down:{in:[{transform:"translateY(-35%)",opacity:0},{transform:"translateY(0)",opacity:1}],
          out:[{transform:"translateY(0)",opacity:1},{transform:"translateY(35%)",opacity:0}]},
    right:{in:[{transform:"translateX(-35%)",opacity:0},{transform:"translateX(0)",opacity:1}],
           out:[{transform:"translateX(0)",opacity:1},{transform:"translateX(35%)",opacity:0}]},
    left:{in:[{transform:"translateX(35%)",opacity:0},{transform:"translateX(0)",opacity:1}],
          out:[{transform:"translateX(0)",opacity:1},{transform:"translateX(-35%)",opacity:0}]},
    fade:{in:[{opacity:0,transform:"scale(1.03)"},{opacity:1,transform:"scale(1)"}],
          out:[{opacity:1,transform:"scale(1)"},{opacity:0,transform:"scale(1.03)"}]}
  };

  async function runCell(wrapper){
    const imgA=wrapper.querySelectorAll("img")[0];
    const imgB=wrapper.querySelectorAll("img")[1];
    const textNode=wrapper.closest(".carousel-item").querySelector(".carousel-item-text");
    let imgs=[],texts=[];

    imgs=JSON.parse(imgA.dataset.images||"[]");
    texts=JSON.parse(imgA.dataset.texts||"[]");

    let idx=0;
    imgA.src=imgs[idx];
    imgA.style.opacity=1;
    imgB.style.opacity=0;
    if(texts.length>0)textNode.textContent=texts[idx];

    const dir=imgA.dataset.direction||"fade";
    const anim=anims[dir]||anims.fade;

    while(true){
      await wait(VISIBLE_MS);
      const next=(idx+1)%imgs.length;
      imgB.src=imgs[next];
      if(texts.length>0)textNode.textContent=texts[next];

      const outAnim=imgA.animate(anim.out,{duration:OUT_DURATION,easing:"ease-in",fill:"forwards"});

      // entrada pegada pero visible (delay corto)
      await wait(200);
      const inAnim=imgB.animate(anim.in,{duration:IN_DURATION,easing:"ease-out",fill:"forwards"});

      await Promise.all([outAnim.finished,inAnim.finished]);

      imgA.src=imgB.src;
      imgA.style.opacity=1;
      imgB.style.opacity=0;
      idx=next;
    }
  }

  function prepare(){
    document.querySelectorAll(".carousel-image-wrapper").forEach(w=>{
      const img=w.querySelector(".carousel-item-img");
      if(!img)return;

      if(w.querySelectorAll("img").length<2){
        const clone=img.cloneNode();
        clone.style.position="absolute";
        clone.style.top="0"; clone.style.left="0";
        clone.style.width="100%"; clone.style.height="100%";
        clone.style.borderRadius=img.style.borderRadius||"15px";
        clone.style.zIndex=1; clone.style.opacity=0;
        w.style.position="relative";
        w.appendChild(clone);
      }

      if(!w.__started){
        w.__started=true;
        runCell(w);
      }
    });
  }

  setTimeout(prepare,START_DELAY);
})();
"""),
    )


# --- Página completa ---
def galeria() -> rx.Component:
    return rx.box(
        header(),
        cuerpo(),
        footer(),
        height="100vh",
        width="100vw",
    )


app = rx.App(stylesheets=["/carousel.css"], theme=custom_theme)
app.add_page(galeria, title="Galería con gradientes y animaciones", route="/")

if __name__ == "__main__":
    app.run()







