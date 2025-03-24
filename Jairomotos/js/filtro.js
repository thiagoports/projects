document.addEventListener("DOMContentLoaded", function () {
    const brandFilter = document.getElementById("brandFilter");
    const vehicleBlocks = document.querySelectorAll(".vehicle-block");

    // Função para filtrar os veículos com base na marca
    function filterVehicles() {
        const selectedBrand = brandFilter.value;
        vehicleBlocks.forEach((block) => {
            const brand = block.getAttribute("data-brand");

            let showVehicle = true;

            if (selectedBrand !== "all" && selectedBrand !== brand) {
                showVehicle = false;
            }

            if (showVehicle) {
                block.style.display = "block";
            } else {
                block.style.display = "none";
            }
        });
    }

    brandFilter.addEventListener("change", filterVehicles);

    filterVehicles();
});
