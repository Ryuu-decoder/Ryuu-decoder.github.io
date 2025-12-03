const CACHE_NAME = "react-first-aid-v1";

const urlsToCache = [
  "index.html",
  "detail.html",
  "firstaid.html",
  "style.css",
  "script.js",
  "manifest.json",

  // Add all images
  "images/logo.png",
  "images/backgroundfront.png",

  // Add your first aid images
  // Example:
  "images/acute.jpg",
  "images/acute.jpg",
  "images/animal_bite.jpg",
  "images/asthma.jpg",
  "images/bleeding.jpg",
  "images/burns.jpg",
  "images/cold.jpg",
  "images/choking.jpg",
  "images/cramps.webp",
  "images/dry_cough.jpg",
  "images/fracture.jpg",
  "images/head_injuries.jpg",
  "images/heat_exhaustion.jpg",
  "images/laceration.jpg",
  "images/menstrual_cramps.jpg",
  "images/minor_cuts_scrapes.webp",
  "images/nosebleeds.jpg",
  "images/open_wounds.jpeg",
  "images/shoulder_dislocation.jpg",
  "images/sore_throat.jpg",
  "images/splinter.jpg",
  "images/sprain.jpg",
  "images/superficial_injuries.jpg",
  "images/tonsillitis.jpeg",
  "images/wet_cough.jpeg"

  
  // Add more files if needed
];

// Install SW → cache files
self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(urlsToCache);
    })
  );
});

// Load offline cached files
self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});

// Update cache when changing version
self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((names) => {
      return Promise.all(
        names.map((name) => {
          if (name !== CACHE_NAME) {
            return caches.delete(name);
          }
        })
      );
    })
  );
});
