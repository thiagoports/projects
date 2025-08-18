document.addEventListener("DOMContentLoaded", () => {
  const btnWhatsApp = document.querySelector(".btn-whatsapp");
  const btnInfo = document.querySelector(".btn-info");

  if (btnWhatsApp) {
    btnWhatsApp.classList.add("pulsar-green");
  }
  if (btnInfo) {
    btnInfo.classList.add("pulsar-white");
  }
});
