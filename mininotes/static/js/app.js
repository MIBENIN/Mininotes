document.addEventListener("DOMContentLoaded", function () {
  const currentPath = window.location.pathname;
  const links = document.querySelectorAll(".sidebar-links a");

  links.forEach((link) => {
    if (link.getAttribute("href") === currentPath) {
      link.classList.add("active");
    }
  });
});

handleSidebar();

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
const tooltip_elements = document.querySelectorAll(".tooltip-element");

shrink_btn.addEventListener("click", () => {
  document.body.classList.toggle("shrink");
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

function handleSidebar() {
  if (window.innerWidth < 768) {
    document.body.classList.add("shrink");
    document.body.classList.remove("expanded");
  } else {
    document.body.classList.remove("shrink");
    document.body.classList.add("expanded");
  }
}

// Add event listener for window resize
window.addEventListener("resize", handleSidebar);
