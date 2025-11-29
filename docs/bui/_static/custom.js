// document.addEventListener("DOMContentLoaded", function () {
//     const links = document.querySelectorAll("a.image-reference");
//     links.forEach((link) => {
//         link.setAttribute("target", "_blank");
//         link.setAttribute("rel", "noopener noreferrer");
//     });
// });

document.addEventListener("DOMContentLoaded", function() {
    const links = document.querySelectorAll("a.image-reference");

    const lightbox = document.createElement("div");
    lightbox.id = "lightbox-overlay";
    Object.assign(lightbox.style, {
        position: "fixed",
        top: 0,
        left: 0,
        width: "100%",
        height: "100%",
        background: "rgba(0,0,0,0.8)",
        display: "none",
        justifyContent: "center",
        alignItems: "center",
        zIndex: 10000,
        cursor: "pointer"
    });

    const img = document.createElement("img");
    Object.assign(img.style, {
        maxWidth: "90%",
        maxHeight: "90%",
        boxShadow: "0 0 20px rgba(0,0,0,0.5)"
    });

    lightbox.appendChild(img);
    document.body.appendChild(lightbox);

    links.forEach(link => {
        link.addEventListener("click", e => {
            e.preventDefault();
            img.src = link.href;
            lightbox.style.display = "flex";
        });
    });

    lightbox.addEventListener("click", () => {
        lightbox.style.display = "none";
        img.src = "";
    });
});
