document.getElementById("btn-switch-theme").addEventListener("click", (event) => {
    target = event.target;
    currentTheme = target.getAttribute("data-current-theme");

    switch (currentTheme) {
        case "dark":
            document.getElementById("html").className = "light";
            target.setAttribute("data-current-theme", "light");
            break;
        case "light":
            document.getElementById("html").className = "dark";
            target.setAttribute("data-current-theme", "dark");
            break;
        default:
            document.getElementById("html").className = "dark";
            target.setAttribute("data-current-theme", "light");
            break;
    }
})