document.addEventListener('DOMContentLoaded', function () {
    const images = document.querySelectorAll('.chart-img');

    images.forEach(img => {
        img.addEventListener('click', () => {
            alert("Chart: " + img.alt);
        });
    });
});
