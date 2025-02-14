function setColorblindMode(mode) {
    localStorage.setItem("colorblindMode", mode);
    applyColorblindMode(mode);
}

function applyColorblindMode(mode) {
    document.body.classList.remove("colorblind-mode", "deuteranopia-mode", "protanopia-mode");

    if (mode === "grayscale") {
        document.body.classList.add("colorblind-mode");
    } else if (mode === "deuteranopia") {
        document.body.classList.add("deuteranopia-mode");
    } else if (mode === "protanopia") {
        document.body.classList.add("protanopia-mode");
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const mode = localStorage.getItem("colorblindMode") || "normal";
    applyColorblindMode(mode);
});
