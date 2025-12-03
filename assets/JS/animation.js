(function() {

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

  function applyImageStyle(img) {
    img.style.width = "100%";
    img.style.height = "100%";
    img.style.objectFit = "cover";
    img.style.objectPosition = "center center";
    img.style.borderRadius = "20px";
    img.style.position = "absolute";
    img.style.top = "0";
    img.style.left = "0";
  }

  function animateCell(box) {

    const images = JSON.parse(box.dataset.images || "[]");
    const texts  = JSON.parse(box.dataset.texts  || "[]");

    if (images.length === 0) return;

    const direction = box.dataset.direction || "up";
    const conf = directions[direction];

    let index = 0;

    /* ===== IMAGEN INICIAL ===== */
    let imgOld = box.querySelector("img");
    imgOld.src = images[0];
    applyImageStyle(imgOld);

    /* ===== TEXTO INICIAL ===== */
    const vstack = box.parentElement;
    const textEl = vstack.querySelector(".carousel-item-text");
    textEl.innerText = texts[0];

    async function loop() {
      const oldImg = box.querySelector("img");

      /* PROXIMO INDEX */
      index = (index + 1) % images.length;
      const newSrc  = images[index];
      const newText = texts[index];

      /* 1) EL TEXTO SALE ANTES */
      await textEl.animate(
        [
          { opacity: 1, transform: "translateY(0)" },
          { opacity: 0, transform: "translateY(-20px)" }
        ],
        { duration: 500, easing: "ease-in", fill: "forwards" }
      ).finished;

      /* 2) EL TEXTO NUEVO ENTRA UN POCO ANTES */
      textEl.innerText = newText;

      textEl.animate(
        [
          { opacity: 0, transform: "translateY(10px)" },
          { opacity: 1, transform: "translateY(0)" }
        ],
        {
          duration: 450,       // entra más suave y rápido
          easing: "ease-out",
          fill: "forwards"
        }
      );

      /* ⭐ ADELANTO (OPCIÓN A) */
      await wait(250);   // << el texto queda colocado antes de mover la imagen

      /* 3) NUEVA IMAGEN ENTRA */
      const imgNew = document.createElement("img");
      imgNew.src = newSrc;
      applyImageStyle(imgNew);
      imgNew.style.transform = conf.in_from;
      box.appendChild(imgNew);

      const aIn = imgNew.animate(
        [
          { transform: conf.in_from },
          { transform: "translate(0, 0)" }
        ],
        { duration: TIME_IN, easing: "ease-out", fill: "forwards" }
      );

      /* 4) IMAGEN VIEJA SALE */
      const aOut = oldImg.animate(
        [
          { transform: "translate(0, 0)" },
          { transform: conf.out_to }
        ],
        { duration: TIME_OUT, easing: "ease-in", fill: "forwards" }
      );

      await Promise.all([aIn.finished, aOut.finished]);

      oldImg.remove();

      /* 5) PAUSA */
      await wait(PAUSE);

      loop();
    }

    loop();
  }

  setTimeout(() => {
    document.querySelectorAll(".carousel-box").forEach(animateCell);
  }, 300);

})();