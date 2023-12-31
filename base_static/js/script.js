const activeUrl = () => {
    const url = window.location.pathname;

    if (url === "/") {
        document.getElementById("home").classList.add("active");
        document.getElementById("home").ariaCurrent = "page";
    }

    if (url === "/tasks/") {
        document.getElementById("tasks").classList.add("active");
        document.getElementById("tasks").ariaCurrent = "page";
    }

    if (url === "/contact/") {
        document.getElementById("contact").classList.add("active");
        document.getElementById("contact").ariaCurrent = "page";
    }   
}

document.addEventListener("DOMContentLoaded", function () {
    activeUrl();
})

window.addEventListener('load', () => {
    const messages = document.querySelectorAll('.alert');
    messages.forEach(message => {
        setTimeout(() => {
            message.style.opacity = '0';
        }, "3000");

        message.addEventListener('transitionend', () => {
            if (message.style.opacity <= "30") {
                message.style.display = "none";
            }
        })
    });
});