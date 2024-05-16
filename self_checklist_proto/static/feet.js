
const Footsteps = ({load: () => {
  const template = document.getElementById('footstep-template');
  const footsteps = document.getElementById('footsteps');

  const STRIDE_LENGTH = 30;
  const FOOT_SPACING = 20;
  const LINE_BUFFER = 130;
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
    console.log(transform);
    el.style.left = `${x}px`;
    el.style.top = `${y}px`;
    el.style.transform = transform;
    console.log(el);
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

  const footstepLineTo = (startX, startY, endX, endY) => {
    const dx = endX - startX;
    const dy = endY - startY;
    let angle = Math.atan2(dy, dx) + (Math.PI * 0.5);
    if (angle < 0) {
      angle += Math.PI * 2;
    }

    const dist = Math.sqrt((dx * dx) + (dy * dy));
    const steps = Math.floor((dist - LINE_BUFFER) / STRIDE_LENGTH);
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
  for (let index = 0; index < steps.length - 1; index++) {
    const step = steps[index];
    if (step.classList.contains("next")) {
      return;
    }
    const nextStep = steps[index + 1];

    const rect = step.getBoundingClientRect();
    const nextRect = nextStep.getBoundingClientRect();

    footstepLineTo(
      rect.x + (rect.width / 2),
      rect.y + (rect.height / 2) + HEIGHT_OFFSET,
      nextRect.x + (nextRect.width / 2),
      nextRect.y + (nextRect.height / 2) + HEIGHT_OFFSET
    )
  }
}});
