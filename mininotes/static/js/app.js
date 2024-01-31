const shrink_btn = document.querySelector(".shrink-btn");
const sidebar_links = document.querySelectorAll(".sidebar-links a");
const active_tab = document.querySelector(".active-tab");
const tooltip_elements = document.querySelectorAll(".tooltip-element");

const dashboard = document.querySelector(".dashboard");
const noteDetails = document.querySelector(".note-details");

let activeIndex;

shrink_btn.addEventListener("click", () => {
  document.body.classList.toggle("shrink");
  setTimeout(moveActiveTab, 400);

  shrink_btn.classList.add("hovered");

  setTimeout(() => {
    shrink_btn.classList.remove("hovered");
  }, 500);

  updateElementMargin(dashboard, "5.4rem", "16rem");
  updateElementMargin(noteDetails, "5.4rem", "16rem");
});

function updateElementMargin(element, shrinkedMargin, expandedMargin) {
  const isShrinked = document.body.classList.contains("shrink");
  const screenWidth = window.innerWidth;

  if (screenWidth < 768) {
    element.style.marginLeft = "5.4rem";
  } else {
    element.style.marginLeft = isShrinked ? shrinkedMargin : expandedMargin;
  }
}

function checkScreenWidth(element) {
  const screenWidth = window.innerWidth;
  if (screenWidth < 768) {
    element.style.marginLeft = "5.4rem";
  } else {
    element.style.marginLeft = isShrinked ? shrinkedMargin : expandedMargin;
  }
  updateElementMargin(dashboard, "5.4rem", "16rem");
  updateElementMargin(noteDetails, "5.4rem", "16rem");
}

checkScreenWidth(dashboard);
checkScreenWidth(noteDetails);

function moveActiveTab() {
  let topPosition = activeIndex * 58 + 2.5;

  if (activeIndex > 3) {
    topPosition += sidebar_links.clientHeight;
  }

  active_tab.style.top = `${topPosition}px`;
}

function changeLink() {
  sidebar_links.forEach((sideLink) => sideLink.classList.remove("active"));
  this.classList.add("active");

  activeIndex = this.dataset.active;

  moveActiveTab();
}

sidebar_links.forEach((link) => link.addEventListener("click", changeLink));

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

window.addEventListener("resize", checkScreenWidth);
