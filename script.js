(() => {
  const canvas = document.getElementById('bg');
  const ctx = canvas.getContext('2d');
  const toggle = document.getElementById('interactionToggle');

  let w, h, dpr;
  let particles = [];
  let mouse = { x: 0, y: 0, active: false };
  let lastTime = 0;

  const baseDensity = 0.18; // particles per 1000 px²
  const maxParticles = 260;
  const minParticles = 120;
  const linkDist = 120;
  const influenceRadius = 140;

  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    w = window.innerWidth;
    h = window.innerHeight;
    canvas.width = w * dpr;
    canvas.height = h * dpr;
    canvas.style.width = w + 'px';
    canvas.style.height = h + 'px';
    ctx.scale(dpr, dpr);
    initParticles();
  }

  function rand(min, max) {
    return Math.random() * (max - min) + min;
  }

  function initParticles() {
    const targetCount = Math.min(
      maxParticles,
      Math.max(minParticles, Math.floor((w * h / 1000) * baseDensity))
    );
    particles = new Array(targetCount).fill(0).map(() => ({
      x: rand(0, w),
      y: rand(0, h),
      baseX: 0,
      baseY: 0,
      vx: rand(-0.05, 0.05),
      vy: rand(-0.05, 0.05),
      size: rand(1.2, 2.8),
      alpha: rand(0.25, 0.7),
      hue: [rand(190, 210), rand(310, 330), rand(130, 150)][Math.floor(Math.random() * 3)],
      parallax: rand(0.2, 0.7)
    }));
  }

  function drawParticle(p) {
    ctx.beginPath();
    ctx.fillStyle = `hsla(${p.hue}, 75%, 70%, ${p.alpha})`;
    ctx.shadowColor = `hsla(${p.hue}, 75%, 65%, ${p.alpha})`;
    ctx.shadowBlur = 14;
    ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
    ctx.fill();
  }

  function drawLink(a, b, dist) {
    const opacity = 0.12 * (1 - dist / linkDist);
    ctx.strokeStyle = `rgba(226, 232, 240, ${opacity})`;
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(a.x, a.y);
    ctx.lineTo(b.x, b.y);
    ctx.stroke();
  }

  function update(dt) {
    const driftStrength = 0.015;
    const mouseOn = toggle.checked && mouse.active;

    for (let i = 0; i < particles.length; i++) {
      const p = particles[i];

      // gentle random drift
      p.vx += rand(-driftStrength, driftStrength);
      p.vy += rand(-driftStrength, driftStrength);

      // parallax pull toward mouse for depth
      if (mouseOn) {
        const dx = (mouse.x - w / 2) * 0.0003 * p.parallax;
        const dy = (mouse.y - h / 2) * 0.0003 * p.parallax;
        p.vx += dx;
        p.vy += dy;
      }

      // cap velocity for stability
      const maxV = 0.35;
      p.vx = Math.max(-maxV, Math.min(maxV, p.vx));
      p.vy = Math.max(-maxV, Math.min(maxV, p.vy));

      // mouse repulsion
      if (mouseOn) {
        const dx = p.x - mouse.x;
        const dy = p.y - mouse.y;
        const dist = Math.hypot(dx, dy);
        if (dist < influenceRadius) {
          const force = (1 - dist / influenceRadius) * 0.6;
          p.vx += (dx / dist || 0) * force;
          p.vy += (dy / dist || 0) * force;
        }
      }

      // move
      p.x += p.vx * dt * 60;
      p.y += p.vy * dt * 60;

      // gentle wrap
      if (p.x < -20) p.x = w + 20;
      if (p.x > w + 20) p.x = -20;
      if (p.y < -20) p.y = h + 20;
      if (p.y > h + 20) p.y = -20;
    }
  }

  function render() {
    ctx.clearRect(0, 0, w, h);

    // draw links selectively (sparse for perf)
    for (let i = 0; i < particles.length; i++) {
      const a = particles[i];
      for (let j = i + 1; j < particles.length; j++) {
        const b = particles[j];
        const dx = a.x - b.x;
        const dy = a.y - b.y;
        const dist = dx * dx + dy * dy;
        if (dist < linkDist * linkDist && Math.random() < 0.2) {
          drawLink(a, b, Math.sqrt(dist));
        }
      }
    }

    particles.forEach(drawParticle);
  }

  function loop(ts) {
    const dt = Math.min(0.05, (ts - lastTime) / 1000 || 0.016);
    lastTime = ts;
    update(dt);
    render();
    requestAnimationFrame(loop);
  }

  function onMove(e) {
    mouse.active = true;
    mouse.x = e.clientX;
    mouse.y = e.clientY;
  }

  window.addEventListener('pointermove', onMove, { passive: true });
  window.addEventListener('pointerdown', onMove, { passive: true });
  window.addEventListener('resize', resize);

  resize();
  requestAnimationFrame(loop);
})();
