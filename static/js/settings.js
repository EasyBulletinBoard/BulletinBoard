document.addEventListener('DOMContentLoaded', function() {
    const settingsButton = document.getElementsByClassName('settings-btn')[0];

    settingsButton.addEventListener('click', function() {
        window.location.href = '/boards/settings';
    });
});