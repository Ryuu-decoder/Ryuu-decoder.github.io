// ------------------ Search filter ------------------
const searchInput = document.getElementById("searchInput");
if (searchInput) {
  searchInput.addEventListener("keyup", () => {
    const filter = searchInput.value.toLowerCase();
    const list = document.getElementById("topicList").getElementsByTagName("li");
    for (let i = 0; i < list.length; i++) {
      const item = list[i];
      item.style.display = item.textContent.toLowerCase().includes(filter) ? "" : "none";
    }
  });
}

// ------------------ Navigation helpers ------------------
function openDetail(condition) {
  localStorage.setItem("selectedCondition", condition);
  window.location.href = "detail.html";
}

// ------------------ load correct condition when entering detail.html ------------------
window.addEventListener("DOMContentLoaded", () => {
  const selected = localStorage.getItem("selectedCondition");

  if (selected) {
    openCondition(selected);   // <-- THIS UPDATES THE TITLE + VIDEO + CONTENT
  }
});

// get the main data from app.py
let firstAidData = {};

// ------------------ Populate topic list ------------------
function populateTopicList() {
  const listEl = document.getElementById("topicList");
  if (!listEl) return;

  listEl.innerHTML = ""; // clear list

  Object.keys(firstAidData).forEach(topic => {
    const li = document.createElement("li");
    li.textContent = topic;              // display emergency name
    li.onclick = () => openDetail(topic);
    listEl.appendChild(li);
  });
}

// ------------------ Open detail page ------------------
function openDetail(condition) {
  localStorage.setItem("selectedCondition", condition);
  window.location.href = "detail.html";
}

// ------------------ Fetch data from Flask ------------------
fetch('/get_data')
  .then(res => res.json())
  .then(data => {
    firstAidData = data;
    populateTopicList();
    enableHoverPreviews();
  })
  .catch(err => console.error("Failed to load /get_data:", err));

// ------------------ Hover previews ------------------
function enableHoverPreviews() {
  const hoverBox = document.getElementById("hoverPreview");
  const hoverImg = document.getElementById("hoverImage");
  const hoverTxt = document.getElementById("hoverText");
  const items = document.querySelectorAll("#topicList li");
  let lastX = 0, lastY = 0;

  items.forEach(li => {
    li.addEventListener("mousemove", e => {
      const name = li.textContent.trim();
      const info = firstAidData[name];
      if (!info) return;

      hoverImg.src = info.visual || "";
      hoverTxt.innerHTML = info.steps ? info.steps[0] : "No info available.";

      lastX = e.clientX; lastY = e.clientY;
      updateHoverPosition();
      hoverBox.classList.add("visible"); hoverBox.classList.remove("hidden");
    });

    li.addEventListener("mouseleave", () => {
      hoverBox.classList.add("hidden"); hoverBox.classList.remove("visible");
    });
  });

  function updateHoverPosition() {
    if (!hoverBox) return;
    const padding = 20;
    const boxW = hoverBox.offsetWidth, boxH = hoverBox.offsetHeight;
    let posX = lastX + padding, posY = lastY + padding;

    if (posX + boxW > window.innerWidth) posX = lastX - boxW - padding;
    if (posY + boxH > window.innerHeight) posY = lastY - boxH - padding;

    hoverBox.style.left = posX + "px";
    hoverBox.style.top = posY + "px";
  }

  document.addEventListener("scroll", updateHoverPosition, true);
}

// Show a default visual + short intro when opening detail page
function displayDefault(condition) {
  const box = document.getElementById("infoBox");
  const data = firstAidData[condition];
  if (data) {
    const imgTag = data.visual ? `<img src="${data.visual}" alt="${condition}" class="info-image">` : "";
    box.innerHTML = `
      <h3>${condition}</h3>
      ${imgTag}
      <p class="lead">Quick first-aid companion for <strong>${condition}</strong>. Use the buttons above to view procedures, medicine guidance, or emergency tips.</p>
    `;
  } 
}

// Display procedure / medicine / emergency content
function showContent(type) {
  const condition = localStorage.getItem("selectedCondition");
  const data = firstAidData[condition];
  const box = document.getElementById("infoBox");

  if (type === "procedure") {
    box.innerHTML = `
      <h3>Step-by-Step Procedure for ${condition}</h3>
      ${data.visual ? `<img src="${data.visual}" alt="${condition}" class="info-image">` : ""}
      <ol>${data.steps.map(s => `<li>${s}</li>`).join("")}</ol>
      <p><em>Reminder:</em> These are general first-aid steps. Always seek professional medical advice for severe cases.</p>
    `;
 } else if (type === "medicine") {
  box.innerHTML = `
    <h3>Treatment & Medicine Notes for ${condition}</h3>
    <ol>
      ${(data.medicine || []).map((m) => {
        if (typeof m === "string") {
          // Directly render string entries (like acute poisoning cases)
          return `<li>${m}</li>`;
        } else {
          // Render objects with optional purpose/examples
          const details = [];
          if (m.purpose) details.push(`<li><strong>Purpose:</strong> ${m.purpose}</li>`);
          if (m.examples) details.push(`<li><strong>Examples:</strong> ${m.examples}</li>`);
          return `<li>
                    <em>${m.name}</em>
                    ${details.length ? `<ul>${details.join("")}</ul>` : ""}
                  </li>`;
        }
      }).join("")}
    </ol>
    <p><strong>Note:</strong> Medicines should be used according to label instructions or medical advice. This information is educational only.</p>
  `;
  } else if (type === "emergency") {
    box.innerHTML = `
      <h3>Emergency Tips for ${condition}</h3>
      <p>${data.emergency}</p>
      <p><strong>Emergency hotline:</strong> Call your local emergency number (e.g., 911) if the situation is life-threatening.</p>
    `;
  } else {
    displayDefault(condition);
  }
}

// ------------------ Populate topic list dynamically  ------------------
function populateTopicList() {
  const listEl = document.getElementById("topicList");
  if (!listEl) return;
  listEl.innerHTML = "";
  Object.keys(firstAidData).forEach(topic => {
    const li = document.createElement("li");
    li.textContent = topic;
    li.onclick = () => openDetail(topic);
    listEl.appendChild(li);
  });
}
// call populateTopicList on pages that have topicList
populateTopicList();

// ------------------ Accessibility: keyboard support for search+list ------------------
if (searchInput) {
  searchInput.setAttribute("aria-label", "Search first aid topics");
}

// for offline mode
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('./sw.js')
      .then(reg => console.log('Service Worker registered.', reg))
      .catch(err => console.log('Service Worker registration failed:', err));
  });
}


//----------------- videos -----------------
const videos = {
  "Acute Poisoning": "https://www.youtube.com/embed/EkYnxd65t6Y",
  "Allergic Reactions": "https://www.youtube.com/embed/zRSxAL-twdc", // replace with real ID
  "Animal Bites": "https://www.youtube.com/embed/J5AeWWQ3eN0",
  "Asthma Attack": "https://www.youtube.com/embed/1dV2vFAcqIw",
  "Bleeding": "https://www.youtube.com/embed/9XpJZv_YsGM",
  "Burns": "https://www.youtube.com/embed/sauqm3mvJ40",
  "Choking": "https://www.youtube.com/embed/pzlwOI7xQRc",
  "Cold": "https://www.youtube.com/embed/3q0s8uKfE8I",
  "Cramps": "https://www.youtube.com/embed/sxXQhuVgzRs",
  "Dry Cough":"https://www.youtube.com/embed/XZizoyJ8BCw",
  "Fracture": "https://www.youtube.com/embed/2v8vlXgGXwE",
  "Head Injuries": "https://www.youtube.com/embed/a4cIFZx1f2E",
  "Heat Exhaustion": "https://www.youtube.com/embed/R6VdoV8dZRc",
  "Laceration": "https://www.youtube.com/embed/4e7evinsfm0",
  "Menstrual Cramps": "https://www.youtube.com/embed/516wWsO7Rzs",
  "Minor Cuts and Scrapes": "https://www.youtube.com/embed/L77rERL64zc",
  "Nosebleeds": "https://www.youtube.com/embed/opUZX8f0wgA",
  "Open Wounds": "https://www.youtube.com/embed/WILIPVhd-nA",
  "Shoulder Dislocation": "https://www.youtube.com/embed/6m3Hhy6G8Wc",
  "Sore Throat": "https://www.youtube.com/embed/pvfDLIsrkjo",
  "Splinter": "https://www.youtube.com/embed/MKZf8hoqWFE",
  "Sprain": "https://www.youtube.com/embed/3CEiFmVzzyc",
  "Superficial Injuries": "https://www.youtube.com/embed/Rkmn20e8X8w",
  "Tonsillitis": "https://www.youtube.com/embed/wCFtZGps69Y",
  "Wet Cough": "https://www.youtube.com/embed/TEeOlqLTEwE",
};

//----------------- load video -----------------
function loadVideo(conditionName) {
  const frame = document.getElementById("videoFrame");
  const videoURL = videos[conditionName];

  if (videoURL) {
    frame.src = videoURL;
  } else {
    // fallback video if condition not found
    frame.src = "https://www.youtube.com/embed/dQw4w9WgXcQ";
    console.warn(`Video not found for condition: ${conditionName}`);
  }
}

//----------------- open condition -----------------
function openCondition(name) {
  document.getElementById("conditionTitle").innerText = name;
  
  // Load the YouTube video
  loadVideo(name);

  // Optional: show the procedure content by default
  if (typeof showContent === "function") {
    showContent("procedure");
  }
}

