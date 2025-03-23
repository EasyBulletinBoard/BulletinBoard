document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('theme-toggle');
    let currentTheme = localStorage.getItem('theme') || null;
    console.debug(currentTheme);
    if (!currentTheme) {
        let isDarkModePreference = window.matchMedia("(prefers-color-scheme: dark)");
        currentTheme = isDarkModePreference.matches ? "dark-mode" : 'light-mode'
    }
    document.body.className = currentTheme;
    updateButtonText();
    toggleButton.addEventListener('click', function() {
        currentTheme = currentTheme === 'light-mode' ? 'dark-mode' : 'light-mode';
        document.body.className = currentTheme;
        localStorage.setItem('theme', currentTheme);
        updateButtonText();
    });
    function updateButtonText() {
        toggleButton.textContent = currentTheme === 'light-mode' 
            ? '🌙 Dark Mode' 
            : '☀️ Light Mode';
    }
});