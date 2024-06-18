const toggleTheme = () => {
    const html = document.documentElement;

    html.classList.toggle("light");

    // .toggle faz todo o trabalho abaixo:

    // if (html.classList.contains("light")) {
    //     html.classList.remove("light");
    // } else {
    //     html.classList.add("light");
    // }
}

window.onload = () => {
    document.getElementById("switch").addEventListener("click", toggleTheme)
}
