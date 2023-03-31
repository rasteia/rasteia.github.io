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
  
  
  const client = createClient({
    space: process.env.CONTENTFUL_SPACE_ID,
    accessToken: process.env.IS_PREVIEW === "true" ?
      process.env.CONTENTFUL_PREVIEW_TOKEN :
      process.env.CONTENTFUL_DELIVERY_TOKEN
  })
  
  // Alternatively you can use the CDN API as follows...
  const baseUrl = process.env.IS_PREVIEW === "true" ? "preview.contentful.com" : "cdn.contentful.com"
  
