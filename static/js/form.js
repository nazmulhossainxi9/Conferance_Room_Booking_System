document.addEventListener("DOMContentLoaded", function() {
    const timeInputs = document.querySelectorAll("input[type='time']");
    
    timeInputs.forEach(input => {
        if (!input.value) {
            input.setAttribute("placeholder", input.getAttribute("data-placeholder"));
        }
        
        input.addEventListener("focus", () => {
            input.removeAttribute("placeholder");
        });
        
        input.addEventListener("blur", () => {
            if (!input.value) {
                input.setAttribute("placeholder", input.getAttribute("data-placeholder"));
            }
        });
    });
});