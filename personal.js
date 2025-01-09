document.addEventListener("DOMContentLoaded", () => {
  // Elements
  const profileCard = document.querySelector(".profile-card");
  const profileImg = document.querySelector(".profile-img");
  const kebabMenu = document.querySelector(".kebab-menu");
  const leftPopup = document.querySelector(".left-popup");
  const rightPopup = document.querySelector(".right-popup");
  const closeButtons = document.querySelectorAll(".popup-close");

  let popupsVisible = false;

  // Initial animation for profile card
  profileCard.style.opacity = "0";
  profileCard.style.transform = "translateY(20px)";

  setTimeout(() => {
    profileCard.style.transition = "all 0.8s ease";
    profileCard.style.opacity = "1";
    profileCard.style.transform = "translateY(0)";
  }, 200);

  // Profile image hover effect
  profileImg.addEventListener("mouseover", () => {
    profileImg.style.transform = "scale(1.1)";
    profileImg.style.transition = "transform 0.3s ease";
  });

  profileImg.addEventListener("mouseout", () => {
    profileImg.style.transform = "scale(1)";
  });

  // Popup functionality
  function togglePopups() {
    if (popupsVisible) {
      leftPopup.classList.remove("active");
      rightPopup.classList.remove("active");
    } else {
      leftPopup.classList.add("active");
      rightPopup.classList.add("active");
    }
    popupsVisible = !popupsVisible;
  }

  function closePopups() {
    leftPopup.classList.remove("active");
    rightPopup.classList.remove("active");
    popupsVisible = false;
  }

  // Event listeners
  kebabMenu.addEventListener("click", togglePopups);

  closeButtons.forEach((button) => {
    button.addEventListener("click", closePopups);
  });

  // Close popups with Escape key
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      closePopups();
    }
  });

  // Close popups when clicking outside
  document.addEventListener("click", (e) => {
    if (
      popupsVisible &&
      !leftPopup.contains(e.target) &&
      !rightPopup.contains(e.target) &&
      !kebabMenu.contains(e.target)
    ) {
      closePopups();
    }
  });
});
