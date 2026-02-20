// Script pour afficher plus d'informations au clic sur le bouton
document.getElementById('moreInfoBtn').addEventListener('click', function() {
    var moreInfoSection = document.getElementById('moreInfo');
    if (moreInfoSection.style.display === 'none' || moreInfoSection.style.display === '') {
        moreInfoSection.style.display = 'block';
        this.textContent = 'Afficher moins d\'informations';
    } else {
        moreInfoSection.style.display = 'none';
        this.textContent = 'Afficher plus d\'informations';
    }
});
