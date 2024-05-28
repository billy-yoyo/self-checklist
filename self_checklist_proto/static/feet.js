
const Footsteps = ({load: () => {
  const template = document.getElementById('footstep-template');
  const footsteps = document.getElementById('footsteps');
  const main = document.querySelector("main");
  const topImage = document.querySelector(".top-image img");

  const IS_MOBILE = window.innerWidth < 641;

  const STRIDE_LENGTH = IS_MOBILE ? 20 : 30;
  const FOOT_SPACING = 20;
  const LINE_BUFFER = 130;
  const FIRST_LINE_BUFFER = 20;
  const HEIGHT_OFFSET = 20;
  const FOOTSTEP_INTERVAL = 200;

  const createFootstepAt = (x, y, rotation, flipped) => {
    const el = template.cloneNode();
    el.id = "";
    el.classList.add("footstep");
    el.classList.remove("hidden");
    const transforms = [`rotate(${rotation}rad)`];
    if (flipped) {
      transforms.push(`scaleX(-1)`);
    }
    const transform = transforms.join(" ");
    el.style.left = `${x}px`;
    el.style.top = `${y}px`;
    el.style.transform = transform;
    footsteps.appendChild(el);
  };

  const queuedFootsteps = [];
  const queueFootstepAt = (x, y, rotation, flipped) => {
    queuedFootsteps.push([x, y, rotation, flipped]);
  };

  setInterval(() => {
    if (queuedFootsteps.length > 0) {
      const [x, y, rotation, flipped] = queuedFootsteps.shift();
      createFootstepAt(x, y, rotation, flipped);
    }
  }, FOOTSTEP_INTERVAL);

  const footstepLineTo = (startX, startY, endX, endY, buffer) => {
    const dx = endX - startX;
    const dy = endY - startY;
    let angle = Math.atan2(dy, dx) + (Math.PI * 0.5);
    if (angle < 0) {
      angle += Math.PI * 2;
    }

    const dist = Math.sqrt((dx * dx) + (dy * dy));
    const steps = Math.floor((dist - buffer) / STRIDE_LENGTH);
    const remainder = dist - (steps * STRIDE_LENGTH);
    const offset = remainder / 2;
    const ux = dx / dist;
    const uy = dy / dist;

    const px = -uy;
    const py = ux;

    for (let step = 0; step < steps; step++) {
      let sx = startX + (ux * (offset + (step * STRIDE_LENGTH)));
      let sy = startY + (uy * (offset + (step * STRIDE_LENGTH)));

      const flipped = step % 2 == 0;
      const footOff = flipped ? FOOT_SPACING / 2 : -FOOT_SPACING / 2;
      sx += footOff * px;
      sy += footOff * py;

      queueFootstepAt(sx, sy, angle, flipped);
    }
  };

  const steps = Array.from(document.querySelectorAll(".progression-step"));
  let step = topImage;
  const mainRect = main.getBoundingClientRect();
  for (let index = 0; index < steps.length; index++) {
    if (step.classList.contains("next")) {
      return;
    }
    const nextStep = steps[index];

    const rect = step.getBoundingClientRect();
    const nextRect = nextStep.getBoundingClientRect();

    const rectHeight = index === 0 && rect.height < 10 ? 100 : rect.height;

    footstepLineTo(
      rect.x - mainRect.x + (rect.width / 2),
      rect.y - mainRect.y + (index === 0 ? rectHeight : (rectHeight / 2) + HEIGHT_OFFSET),
      nextRect.x - mainRect.x + (nextRect.width / 2),
      nextRect.y - mainRect.y + (nextRect.height / 2) + HEIGHT_OFFSET,
      index === 0 ? FIRST_LINE_BUFFER : LINE_BUFFER
    );

    step = nextStep;
  }
}});
