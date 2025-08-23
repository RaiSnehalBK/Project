document.addEventListener("DOMContentLoaded", function() {
  const toggleBtn = document.querySelector(".sidebar-toggle");
  const sidebar = document.querySelector(".sidebar");
  const overlay = document.querySelector(".overlay");

  if (!toggleBtn || !sidebar || !overlay) {
    console.error("Essential elements missing!");
    return;
  }

  // Match overlay to sidebar initial state
  overlay.style.display = sidebar.classList.contains("active") ? "block" : "none";

  // Toggle sidebar on button click
  toggleBtn.addEventListener("click", function(e) {
    e.stopPropagation();
    sidebar.classList.toggle("active");
    overlay.style.display = sidebar.classList.contains("active") ? "block" : "none";
    // 🚫 Removed document.body.style.overflow changes
  });

  // Close sidebar when clicking overlay
  overlay.addEventListener("click", function() {
    sidebar.classList.remove("active");
    overlay.style.display = "none";
    // 🚫 Removed document.body.style.overflow changes
  });
});


