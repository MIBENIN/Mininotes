document.addEventListener("DOMContentLoaded", function () {
  const currentPath = window.location.pathname;
  const links = document.querySelectorAll(".sidebar-links a");

  links.forEach((link) => {
    if (link.getAttribute("href") === currentPath) {
      link.classList.add("active");
    }
  });
});

// toast

const messageBox = document.getElementById("message-box");

function showToast(messageElement) {
  const messageType = getMessageType(messageElement);
  messageElement.classList.add("visible", messageType);

  // Automatically hide the toast after 3 seconds
  setTimeout(() => {
    hideToast(messageElement);
  }, 3000);
}

function hideToast(messageElement) {
  messageElement.style.display = "none";
}

function getMessageType(messageElement) {
  const classes = messageElement.classList;
  if (classes.contains("success")) return "success";
  if (classes.contains("error")) return "error";
  if (classes.contains("info")) return "info";
  if (classes.contains("warning")) return "warning";
  return "info"; // Default to 'info' if no specific type found
}

// Fetch message elements from the DOM
const messageElements = document.querySelectorAll(".message");

// Loop through each message and display it as a toast
messageElements.forEach((messageElement) => {
  showToast(messageElement);
});

// Add event listener to close button
const closeButtons = document.querySelectorAll(".toast-close-btn");
closeButtons.forEach((button) => {
  button.addEventListener("click", function () {
    const messageElement = this.closest(".message");
    hideToast(messageElement);
  });
});

const shrink_btn = document.querySelector(".shrink-btn");
// const sidebar_links = document.querySelectorAll(".sidebar-links a");
const tooltip_elements = document.querySelectorAll(".tooltip-element");

shrink_btn.addEventListener("click", () => {
  document.body.classList.toggle("shrink");
  setTimeout(moveActiveTab, 400);

  shrink_btn.classList.add("hovered");

  setTimeout(() => {
    shrink_btn.classList.remove("hovered");
  }, 500);
});

function showTooltip() {
  let tooltip = this.parentNode.lastElementChild;
  let spans = tooltip.children;
  let tooltipIndex = this.dataset.tooltip;

  Array.from(spans).forEach((sp) => sp.classList.remove("show"));
  spans[tooltipIndex].classList.add("show");

  tooltip.style.top = `${(100 / (spans.length * 2)) * (tooltipIndex * 2 + 1)}%`;
}

tooltip_elements.forEach((elem) => {
  elem.addEventListener("mouseover", showTooltip);
});

// theme
// const storedTheme = localStorage.getItem("theme");

// if (storedTheme === "dark") {
//   setDarkMode();
// } else {
//   setLightMode();
// }

// function setLightMode() {
//   document.documentElement.setAttribute("data-theme", "light");
//   document.querySelector(".day-mode-btn").classList.add("active");
//   document.querySelector(".night-mode-btn").classList.remove("active");

//   // Store the selected theme mode in local storage
//   localStorage.setItem("theme", "light");
// }

// function setDarkMode() {
//   document.documentElement.setAttribute("data-theme", "dark");
//   document.querySelector(".night-mode-btn").classList.add("active");
//   document.querySelector(".day-mode-btn").classList.remove("active");

//   // Store the selected theme mode in local storage
//   localStorage.setItem("theme", "dark");
// }
