function getRandomNeonColor() {
    const neonColors = [
      "#FF00FF", // Neon magenta
      "#00FFFF", // Neon cyan
      "#00FF00", // Neon green
      "#FFFF00", // Neon yellow
      "#FFA500", // Neon orange
      "#FF69B4"  // Neon pink
    ];
  
    return neonColors[Math.floor(Math.random() * neonColors.length)];
  }
  
  document.addEventListener("DOMContentLoaded", () => {
    const postContainers = document.querySelectorAll(".post");
  
    postContainers.forEach((postContainer) => {
      const randomNeonColor = getRandomNeonColor();
      postContainer.style.borderColor = randomNeonColor;
      postContainer.querySelector(".post-title").style.color = randomNeonColor;
    });
  });
  