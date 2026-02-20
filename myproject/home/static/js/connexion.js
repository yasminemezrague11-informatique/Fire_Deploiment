document.getElementById('registrationForm').addEventListener('submit', function(e) {
    e.preventDefault();
    // Récupérer les valeurs des champs
    const fullname = document.getElementById('fullname').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    // Vérifier si les mots de passe correspondent
    if (password !== confirmPassword) {
        e.preventDefault();  // Empêcher la soumission du formulaire
        alert("Les mots de passe ne correspondent pas.");
        return;  // Arrêter l'exécution de la fonction
    }else {
        // Afficher une petite fenêtre de confirmation
        alert("Votre authentification a bien été envoyé !");
        this.submit();
    }
    

    // Vous pouvez ajouter d'autres validations ici si nécessaire

    // Par exemple, vérifier la validité du numéro de téléphone
    const phonePattern = /^[0-9]{10}$/;
    if (!phone.match(phonePattern)) {
        e.preventDefault();
        alert("Le numéro de téléphone n'est pas valide.");
        return;
    }

    // Autres validations comme la validation de l'email, etc., peuvent être ajoutées ici
});
