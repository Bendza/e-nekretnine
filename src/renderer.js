const { ipcRenderer } = require("electron");

document.addEventListener("DOMContentLoaded", () => {
  console.log("DOM is loaded. Requesting data...");
  ipcRenderer.send("request-data");
});

function applyFilters() {
  // Get filter values from the select elements
  const adType = document.getElementById("adType").value;
  const objectType = document.getElementById("objectType").value;
  const streetFilter = document.getElementById("street").value;
  const cityFilter = document.getElementById("city").value;

  const priceFrom = document.getElementById("priceFrom").value;
  const priceTo = document.getElementById("priceTo").value;

  const surfaceFrom = document.getElementById("surfaceFrom").value;
  const surfaceTo = document.getElementById("surfaceTo").value;

  const dateFrom = document.getElementById("dateFrom").value;

  // Construct the filters object
  const filters = {
    adType,
    objectType,
    street: streetFilter,
    city: cityFilter,
    price: {
      from: parseFloat(priceFrom) || undefined,
      to: parseFloat(priceTo) || undefined,
    },
    surface: {
      from: parseFloat(surfaceFrom) || undefined,
      to: parseFloat(surfaceTo) || undefined,
    },
    date: {
      from: dateFrom || undefined,
    },
  };

  // Send the filters to the main process for querying
  ipcRenderer.send("apply-filters", filters);
}

document.getElementById("applyFilters").addEventListener("click", applyFilters);

ipcRenderer.on("data-response", (event, data) => {
  const itemsElement = document.getElementById("items");

  let htmlContent = data
    .map(item => 
      `<div class="ad-item bg-white p-4 rounded-lg hover:bg-gray-200 transition-shadow duration-300 mb-4 flex">
        <div class="image-container w-1/4 flex-shrink-0 mr-4">
            <img src="${item.image}" alt="${item.title}" class="h-32 w-full object-cover rounded-md">
        </div>
        <div class="details flex-1 flex flex-col">
            <h2 class="text-xl font-bold mb-4 truncate">${item.title}</h2>
            <div class="info-grid grid grid-cols-2 gap-2">
                <p class="text-sm truncate capitalize"><span class="font-semibold">Tip Oglasa:</span> ${item.adType}</p>
                <p class="text-sm truncate"><span class="font-semibold">Cena:</span> ${formatPrice(item.price)} €</p>
                <p class="text-sm truncate capitalize"><span class="font-semibold">Tip Objekta:</span> ${item.objectType}</p>
                <p class="text-sm truncate"><span class="font-semibold">Površina:</span> ${item.surface} m²</p>
                <p class="text-sm truncate"><span class="font-semibold">Grad:</span> ${item.city}</p>
                <p class="text-sm truncate"><span class="font-semibold">Datum:</span> ${item.date}</p>
                <p class="text-sm truncate"><span class="font-semibold">Ulica:</span> ${item.street}</p>
                <a href="${item.url}" target="_blank" class="text-blue-500 hover:underline self-start">View on ${item.host}</a>
            </div>
        </div>
    </div>`)
    .join("");

  itemsElement.innerHTML = htmlContent;
});



function formatPrice(price) {
  return price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}
