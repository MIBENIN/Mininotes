const storedTheme = localStorage.getItem("theme");

if (storedTheme === "dark") {
  setDarkMode();
} else {
  setLightMode();
}

function setLightMode() {
  document.documentElement.setAttribute("data-theme", "light");
  document.querySelector(".day-mode-btn").classList.add("active");
  document.querySelector(".night-mode-btn").classList.remove("active");

  // Store the selected theme mode in local storage
  localStorage.setItem("theme", "light");
}

function setDarkMode() {
  document.documentElement.setAttribute("data-theme", "dark");
  document.querySelector(".night-mode-btn").classList.add("active");
  document.querySelector(".day-mode-btn").classList.remove("active");

  // Store the selected theme mode in local storage
  localStorage.setItem("theme", "dark");
}
