/* =====================================================================
   Shared line-art SVG library for the Bible Activity Packs.
   All art is stroke-only (fill:none) so it prints as clean coloring
   outlines. Call Art.name() to get an SVG string, or use the helper
   in the HTML.  Colors are the current stroke (var(--line)).
   ===================================================================== */
window.Art = (function () {
  const S = 'fill="none" stroke="#2b2b2b" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"';
  const S2 = 'fill="none" stroke="#2b2b2b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"';

  function wrap(w, h, inner) {
    return `<svg viewBox="0 0 ${w} ${h}" width="${w}" height="${h}" xmlns="http://www.w3.org/2000/svg">${inner}</svg>`;
  }

  const art = {
    /* --- A royal crown (Esther) --- */
    crown(size = 300) {
      const inner = `
        <path ${S} d="M40 170 L60 70 L110 130 L150 50 L190 130 L240 70 L260 170 Z"/>
        <path ${S} d="M40 170 L260 170 L255 205 L45 205 Z"/>
        <circle ${S} cx="60" cy="66" r="8"/>
        <circle ${S} cx="150" cy="44" r="9"/>
        <circle ${S} cx="240" cy="66" r="8"/>
        <circle ${S2} cx="90" cy="188" r="8"/>
        <circle ${S2} cx="150" cy="188" r="9"/>
        <circle ${S2} cx="210" cy="188" r="8"/>
        <path ${S2} d="M70 150 q30 20 60 0"/>
        <path ${S2} d="M170 150 q30 20 60 0"/>`;
      return wrap(300, 230, inner);
    },

    /* --- Queen Esther (simple figure) --- */
    esther(size = 300) {
      const inner = `
        <circle ${S} cx="150" cy="80" r="42"/>
        <path ${S} d="M108 78 q42 -60 84 0"/>
        <path ${S} d="M120 55 L135 40 L150 52 L165 40 L180 55"/>
        <circle cx="136" cy="82" r="3" fill="#2b2b2b"/>
        <circle cx="164" cy="82" r="3" fill="#2b2b2b"/>
        <path ${S2} d="M140 100 q10 8 20 0"/>
        <path ${S} d="M110 120 q-8 60 0 150 q40 20 80 0 q8 -90 0 -150 q-40 -25 -80 0Z"/>
        <path ${S2} d="M150 130 L150 260"/>
        <path ${S2} d="M110 160 q40 20 80 0"/>
        <path ${S} d="M110 135 q-30 30 -25 70"/>
        <path ${S} d="M190 135 q30 30 25 70"/>`;
      return wrap(300, 300, inner);
    },

    /* --- Scroll / decree --- */
    scroll(size = 300) {
      const inner = `
        <path ${S} d="M60 60 q-20 0 -20 20 q0 20 20 20 h150 q20 0 20 -20 q0 -20 -20 -20Z"/>
        <path ${S} d="M60 200 q-20 0 -20 20 q0 20 20 20 h150 q20 0 20 -20 q0 -20 -20 -20Z"/>
        <path ${S} d="M60 100 L60 200 M210 100 L210 200"/>
        <path ${S2} d="M85 130 h100 M85 150 h100 M85 170 h70"/>`;
      return wrap(280, 300, inner);
    },

    /* --- Lion (Daniel) --- */
    lion(size = 300) {
      const inner = `
        <circle ${S} cx="150" cy="130" r="55"/>
        <path ${S} d="M150 75 m0 0 a70 70 0 1 0 0 0" transform="translate(0,0)"/>
        <g ${S2}>
          <path d="M150 60 l0 -25 M120 66 l-14 -20 M180 66 l14 -20 M96 90 l-24 -12 M204 90 l24 -12 M92 130 l-28 0 M208 130 l28 0 M96 170 l-24 12 M204 170 l24 12 M120 194 l-14 20 M180 194 l14 20 M150 200 l0 25"/>
        </g>
        <circle cx="132" cy="122" r="4" fill="#2b2b2b"/>
        <circle cx="168" cy="122" r="4" fill="#2b2b2b"/>
        <path ${S} d="M140 140 q10 10 20 0"/>
        <path ${S2} d="M150 150 l0 12 M150 162 q-12 8 -22 0 M150 162 q12 8 22 0"/>`;
      return wrap(300, 240, inner);
    },

    /* --- Ark / boat (Noah) --- */
    ark(size = 300) {
      const inner = `
        <path ${S} d="M30 160 q0 60 120 60 q120 0 120 -60 Z"/>
        <rect ${S} x="70" y="70" width="160" height="90" rx="8"/>
        <path ${S} d="M60 70 L150 20 L240 70Z"/>
        <rect ${S2} x="100" y="100" width="30" height="30" rx="4"/>
        <rect ${S2} x="170" y="100" width="30" height="30" rx="4"/>
        <path ${S2} d="M30 200 q30 -14 60 0 q30 14 60 0 q30 -14 60 0 q30 14 60 0"/>`;
      return wrap(300, 240, inner);
    },

    /* --- Big fish / whale (Jonah) --- */
    fish(size = 300) {
      const inner = `
        <path ${S} d="M40 130 q60 -70 180 -40 q50 14 50 40 q0 26 -50 40 q-120 30 -180 -40Z"/>
        <path ${S} d="M270 100 q30 30 0 60"/>
        <circle ${S2} cx="90" cy="115" r="6"/>
        <path ${S2} d="M120 150 q30 20 60 0"/>
        <path ${S2} d="M150 90 q10 -30 30 -20 M175 92 q10 -26 26 -14"/>`;
      return wrap(300, 200, inner);
    },

    /* --- Sheep (Lost Sheep) --- */
    sheep(size = 300) {
      const inner = `
        <ellipse ${S} cx="150" cy="140" rx="80" ry="55"/>
        <circle ${S2} cx="90" cy="110" r="18"/><circle ${S2} cx="120" cy="95" r="20"/>
        <circle ${S2} cx="155" cy="90" r="22"/><circle ${S2} cx="190" cy="98" r="20"/>
        <circle ${S2} cx="215" cy="120" r="18"/><circle ${S2} cx="210" cy="155" r="18"/>
        <circle ${S} cx="90" cy="150" r="26"/>
        <path ${S2} d="M74 138 q-14 -6 -18 8 M106 138 q14 -6 18 8"/>
        <circle cx="84" cy="150" r="3" fill="#2b2b2b"/><circle cx="98" cy="150" r="3" fill="#2b2b2b"/>
        <path ${S2} d="M120 190 l0 24 M150 195 l0 22 M180 190 l0 24"/>`;
      return wrap(300, 230, inner);
    },

    /* --- Loaves & fishes (Feeding 5000) --- */
    basket(size = 300) {
      const inner = `
        <path ${S} d="M60 130 h180 l-20 100 h-140Z"/>
        <path ${S2} d="M70 160 h160 M64 190 h172"/>
        <path ${S2} d="M90 130 l10 100 M150 130 l0 100 M210 130 l-10 100"/>
        <ellipse ${S} cx="120" cy="110" rx="34" ry="22"/>
        <ellipse ${S} cx="180" cy="110" rx="34" ry="22"/>
        <path ${S2} d="M92 108 q28 -16 56 0 M152 108 q28 -16 56 0"/>`;
      return wrap(300, 250, inner);
    },

    /* --- Slingshot & stones (David) --- */
    sling(size = 300) {
      const inner = `
        <path ${S} d="M80 40 q40 100 40 180"/>
        <path ${S} d="M120 40 q-10 90 0 180"/>
        <path ${S2} d="M80 40 q40 -20 40 0"/>
        <circle ${S} cx="200" cy="150" r="22"/>
        <circle ${S2} cx="240" cy="190" r="16"/>
        <circle ${S2} cx="210" cy="210" r="14"/>`;
      return wrap(300, 240, inner);
    },

    /* --- Waves (Moses / Red Sea) --- */
    waves(size = 300) {
      const inner = `
        <path ${S} d="M20 80 q30 -40 60 0 q30 40 60 0 q30 -40 60 0 q30 40 60 0"/>
        <path ${S} d="M20 130 q30 -40 60 0 q30 40 60 0 q30 -40 60 0 q30 40 60 0"/>
        <path ${S} d="M20 180 q30 -40 60 0 q30 40 60 0 q30 -40 60 0 q30 40 60 0"/>`;
      return wrap(300, 220, inner);
    },

    /* --- Star border decoration --- */
    star(size = 40) {
      const inner = `<path ${S2} d="M20 4 l5 11 l12 1 l-9 8 l3 12 l-11 -6 l-11 6 l3 -12 l-9 -8 l12 -1Z"/>`;
      return wrap(40, 40, inner);
    },

    /* --- Heart --- */
    heart(size = 60) {
      const inner = `<path ${S} d="M30 52 C6 34 6 14 22 14 C30 14 30 22 30 22 C30 22 30 14 38 14 C54 14 54 34 30 52Z"/>`;
      return wrap(60, 56, inner);
    },

    /* --- Stone tablets (Ten Commandments) --- */
    tablets(size = 300) {
      const inner = `
        <path ${S} d="M40 60 q0 -20 30 -20 h60 q30 0 30 20 v170 q0 15 -20 15 h-80 q-20 0 -20 -15 Z"/>
        <path ${S} d="M170 60 q0 -20 30 -20 h60 q30 0 30 20 v170 q0 15 -20 15 h-80 q-20 0 -20 -15 Z"/>
        <g ${S2}>
          <path d="M70 90 h60 M70 115 h60 M70 140 h60 M70 165 h60 M70 190 h40"/>
          <path d="M200 90 h60 M200 115 h60 M200 140 h60 M200 165 h60 M200 190 h40"/>
        </g>
        <text x="88" y="78" font-size="14" fill="#2b2b2b">I - V</text>
        <text x="215" y="78" font-size="14" fill="#2b2b2b">VI - X</text>`;
      return wrap(300, 250, inner);
    },

    /* --- Shield (Armor of God) --- */
    shield(size = 300) {
      const inner = `
        <path ${S} d="M150 30 L250 60 q0 130 -100 190 q-100 -60 -100 -190 Z"/>
        <path ${S2} d="M150 60 L150 210 M80 120 L220 120"/>
        <path ${S2} d="M120 90 q30 -18 60 0 M120 160 q30 18 60 0"/>`;
      return wrap(300, 240, inner);
    },

    /* --- Helmet (Armor of God) --- */
    helmet(size = 300) {
      const inner = `
        <path ${S} d="M60 150 q0 -110 90 -110 q90 0 90 110 Z"/>
        <path ${S} d="M60 150 h180 v30 h-180 Z"/>
        <path ${S2} d="M150 40 v-18 M150 22 q20 0 20 20"/>
        <path ${S2} d="M110 90 h80"/>`;
      return wrap(300, 200, inner);
    },

    /* --- Sword (Sword of the Spirit) --- */
    sword(size = 300) {
      const inner = `
        <path ${S} d="M150 20 L165 60 L165 200 L150 220 L135 200 L135 60 Z"/>
        <path ${S} d="M100 210 h100"/>
        <path ${S} d="M150 220 L150 270"/>
        <circle ${S2} cx="150" cy="278" r="10"/>`;
      return wrap(300, 300, inner);
    },

    /* --- Cross --- */
    cross(size = 200) {
      const inner = `
        <path ${S} d="M120 20 h60 v80 h80 v60 h-80 v160 h-60 v-160 h-80 v-60 h80 Z"/>`;
      return wrap(300, 340, inner);
    },

    /* --- Two children (Jesus loves children) --- */
    children(size = 300) {
      const inner = `
        <circle ${S} cx="100" cy="80" r="30"/>
        <path ${S} d="M75 110 q25 40 50 0 v90 h-50 Z"/>
        <path ${S2} d="M75 130 l-20 30 M125 130 l20 30"/>
        <path ${S2} d="M85 200 v40 M115 200 v40"/>
        <circle ${S} cx="200" cy="90" r="26"/>
        <path ${S} d="M178 116 q22 34 44 0 v80 h-44 Z"/>
        <path ${S2} d="M178 132 l-18 26 M222 132 l18 26"/>
        <path ${S2} d="M188 196 v36 M212 196 v36"/>
        <path ${S2} d="M40 250 h230"/>`;
      return wrap(300, 270, inner);
    },

    /* --- Palace / arch --- */
    palace(size = 300) {
      const inner = `
        <rect ${S} x="40" y="120" width="220" height="120"/>
        <path ${S} d="M30 120 L150 50 L270 120Z"/>
        <path ${S} d="M120 240 v-70 a30 30 0 0 1 60 0 v70"/>
        <rect ${S2} x="60" y="150" width="34" height="50" rx="4"/>
        <rect ${S2} x="206" y="150" width="34" height="50" rx="4"/>
        <path ${S2} d="M150 50 l0 -24 M144 30 h12"/>`;
      return wrap(300, 250, inner);
    }
  };

  return art;
})();
