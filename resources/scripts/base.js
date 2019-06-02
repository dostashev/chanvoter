window.addEventListener('load', () => {
    document.getElementById('profile-btn').addEventListener('click', () => {
        private_key = document.getElementById('profile-form').value;
        document.location.href = `/profile/${private_key}`;
    });
});
