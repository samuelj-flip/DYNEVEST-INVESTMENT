// Translation Dictionaries (Public & Dashboard keys)
const translations = {
    en: {
        "nav_home": "Home",
        "nav_plans": "Investment Plans",
        "nav_about": "About",
        "nav_blog": "Blog",
        "nav_contact": "Contact",
        "nav_login": "Login",
        "nav_register": "Register",
        "toast_success": "Language changed to English!"
    },
    de: {
        "nav_home": "Startseite",
        "nav_plans": "Pläne",
        "nav_about": "Über uns",
        "nav_blog": "Blog",
        "nav_contact": "Kontakt",
        "nav_login": "Anmelden",
        "nav_register": "Registrieren",
        "toast_success": "Sprache auf Deutsch umgestellt!"
    },
    es: {
        "nav_home": "Inicio",
        "nav_plans": "Planes",
        "nav_about": "Nosotros",
        "nav_blog": "Blog",
        "nav_contact": "Contacto",
        "nav_login": "Iniciar Sesión",
        "nav_register": "Registrarse",
        "toast_success": "¡Idioma cambiado a Español!"
    }
};

// Main translation function
function applyTranslations(lang) {
    // 1. Scan and update all visible text keys
    document.querySelectorAll("[data-i18n]").forEach(element => {
        const key = element.getAttribute("data-i18n");
        if (translations[lang] && translations[lang][key]) {
            element.textContent = translations[lang][key];
        }
    });

    // 2. Save language selection to browser memory
    localStorage.setItem("preferredLanguage", lang);

    // 3. Trigger the success toast notification
    showLanguageToast(lang);
}

// Function to trigger the toast alert
function showLanguageToast(lang) {
    const toastMessage = document.getElementById("toastMessage");
    const toastElement = document.getElementById("langToast");

    if (toastMessage && toastElement) {
        // Set context message dynamically
        toastMessage.textContent = translations[lang]["toast_success"] || "Language changed successfully!";

        // Initialize and trigger Bootstrap Toast
        const toast = new bootstrap.Toast(toastElement, { delay: 3000 });
        toast.show();
    }
}

// Automatically load the saved language when page loads (without showing toast)
document.addEventListener("DOMContentLoaded", () => {
    const savedLang = localStorage.getItem("preferredLanguage") || "de";

    document.querySelectorAll("[data-i18n]").forEach(element => {
        const key = element.getAttribute("data-i18n");
        if (translations[savedLang] && translations[savedLang][key]) {
            element.textContent = translations[savedLang][key];
        }
    });
});