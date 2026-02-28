// Inicializar tooltips de Bootstrap en toda la página
document.addEventListener('DOMContentLoaded', function () {
    var tooltips = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    tooltips.forEach(function (el) {
        new bootstrap.Tooltip(el);
    });
});
