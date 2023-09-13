const sphere = document.getElementById('sphere');
const rows = []

for(i = 0; i < 180; i += 9) {
  rows.push(`<div class="line" style="transform: rotateY(${i}deg);"></div>`)
}

sphere.innerHTML = rows.join("");
