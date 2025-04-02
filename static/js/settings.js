document.addEventListener('DOMContentLoaded', function() {
    const settingsButton = document.getElementById('settings_btn');
    settingsButton.addEventListener('click', function() {
        window.location.href = '/boards/settings';
    });
});