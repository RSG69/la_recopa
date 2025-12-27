(function() {
  const TIME_IN  = 1000; 
  const TIME_OUT = 1000;
  const PAUSE    = 3500;
  const SWIPE_THRESHOLD = 40; 

  const wait = ms => new Promise(res => setTimeout(res, ms));

  const directions = {
    up:    { in_from: "translateY(100%)",  out_to: "translateY(-100%)" },
    down:  { in_from: "translateY(-100%)", out_to: "translateY(100%)" },
    left:  { in_from: "translateX(100%)",  out_to: "translateX(-100%)" },
    right: { in_from: "translateX(-100%)", out_to: "translateX(100%)" }
  };

  function applyImageStyle(img) {
    Object.assign(img.style, {
      width: "100%", height: "100%", objectFit: "cover",
      position: "absolute", top: "0", left: "0",
      touchAction: "none", userSelect: "none",
      pointerEvents: "none" 
    });
    img.setAttribute('draggable', 'false');
  }

  async function transition(box, state, nextIndex, newText, directionOverride) {
    if (state.isTransitioning) return;
    
    // 🔑 CAMBIO: Validar si la dirección es "none" para abortar la animación
    const direction = directionOverride || box.dataset.direction || "up";
    if (direction === "none") return; 

    const conf = directions[direction];
    if (!conf) return; // Seguridad extra por si llega un valor inesperado

    state.isTransitioning = true;
    state.textEl.style.transition = "opacity 0.3s";
    state.textEl.style.opacity = "0";
    await wait(300);
    state.textEl.innerText = newText;
    state.textEl.style.opacity = "1";

    const oldImg = box.querySelector("img");
    const imgNew = document.createElement("img");
    imgNew.src = state.images[nextIndex];
    applyImageStyle(imgNew);
    imgNew.style.transform = conf.in_from;
    box.appendChild(imgNew);

    const aIn = imgNew.animate(
      [{ transform: conf.in_from }, { transform: "translate(0,0)" }],
      { duration: TIME_IN, easing: "ease-out", fill: "forwards" }
    );

    const aOut = oldImg.animate(
      [{ transform: "translate(0,0)" }, { transform: conf.out_to }],
      { duration: TIME_OUT, easing: "ease-out", fill: "forwards" }
    );

    await Promise.all([aIn.finished, aOut.finished]);
    if (oldImg && oldImg !== imgNew) oldImg.remove();
    
    state.index = nextIndex;
    state.isTransitioning = false;
  }

  function addUnifiedEvents(box, state) {
    // 🔑 CAMBIO: No añadir eventos de swipe si la dirección es "none"
    if (box.dataset.initialized === "true" || box.dataset.direction === "none") return;
    box.dataset.initialized = "true";

    let startX = 0, startY = 0;
    let lastX = 0, lastY = 0;
    let isDragging = false;

    box.style.touchAction = "none";

    box.addEventListener('pointerdown', (e) => {
      if (e.pointerType === 'mouse') e.preventDefault();
      startX = lastX = e.clientX;
      startY = lastY = e.clientY;
      isDragging = true;
      box.setPointerCapture(e.pointerId);
    });

    box.addEventListener('pointermove', (e) => {
      if (!isDragging) return;
      lastX = e.clientX;
      lastY = e.clientY;
    });

    box.addEventListener('pointerup', (e) => {
      if (!isDragging) return;
      isDragging = false;
      box.releasePointerCapture(e.pointerId);

      if (state.isTransitioning) return;

      const diffX = startX - lastX;
      const diffY = startY - lastY;
      const absX = Math.abs(diffX), absY = Math.abs(diffY);

      if (Math.max(absX, absY) < SWIPE_THRESHOLD) return;

      let nextIndex = -1, tDir = "";

      if (absX > absY) {
        if (diffX > 0) { nextIndex = (state.index + 1) % state.images.length; tDir = 'left'; }
        else { nextIndex = (state.index - 1 + state.images.length) % state.images.length; tDir = 'right'; }
      } else {
        if (diffY > 0) { nextIndex = (state.index + 1) % state.images.length; tDir = 'up'; }
        else { nextIndex = (state.index - 1 + state.images.length) % state.images.length; tDir = 'down'; }
      }

      if (nextIndex !== -1) {
        state.isManual = true;
        transition(box, state, nextIndex, state.texts[nextIndex], tDir).then(() => {
          setTimeout(() => { state.isManual = false; }, PAUSE);
        });
      }
    });

    box.addEventListener('pointercancel', (e) => {
      isDragging = false;
      box.releasePointerCapture(e.pointerId);
    });
  }

  function init() {
    document.querySelectorAll(".carousel-box").forEach(box => {
      if (box.dataset.initialized === "true") return;

      const state = {
        images: JSON.parse(box.dataset.images || "[]"),
        texts: JSON.parse(box.dataset.texts || "[]"),
        index: 0, isTransitioning: false, isManual: false,
        textEl: box.parentElement.querySelector(".carousel-item-text")
      };

      const img = box.querySelector("img");
      if (img) {
        img.src = state.images[0];
        applyImageStyle(img);
      }
      state.textEl.innerText = state.texts[0];

      // 🔑 CAMBIO: Solo inicializar eventos y loop si hay dirección
      if (box.dataset.direction !== "none") {
        addUnifiedEvents(box, state);
        
        const loop = async () => {
          await wait(PAUSE);
          if (!state.isManual && !state.isTransitioning && document.contains(box)) {
            const nextIndex = (state.index + 1) % state.images.length;
            await transition(box, state, nextIndex, state.texts[nextIndex]);
            loop();
          } else if (document.contains(box)) {
            loop();
          }
        };
        loop();
      } else {
        // Marcamos como inicializado aunque no tenga loop para que el Observer no lo repita
        box.dataset.initialized = "true";
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  const observer = new MutationObserver(() => init());
  observer.observe(document.body, { childList: true, subtree: true });
})();