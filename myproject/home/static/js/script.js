////////////////////////////Soumission du formulaire de declaration d'incendie/////////////////////////

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('fireDeclarationForm');
  
  form.addEventListener('submit', (e) => {
    e.preventDefault();  // Empêche le rechargement de la page lors de la soumission du formulaire

    // Récupérer les valeurs des champs du formulaire
    const reporterName = document.getElementById('reporter-name').value;
    const contactNumber = document.getElementById('contact-number').value;
    const address = document.getElementById('address').value;
    const fireType = document.getElementById('fire-type').value;
    const fireSeverity = document.getElementById('fire-severity').value;

    // Créer un objet FormData pour envoyer les données
    const formData = new FormData();
    formData.append('reporter_name', reporterName);
    formData.append('contact_number', contactNumber);
    formData.append('address', address);
    formData.append('fire_type', fireType);
    formData.append('fire_severity', fireSeverity);
    //////////////// Envoi des données via Fetch API////////////
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    fetch(form.action, {  // Utilise l'action du formulaire pour envoyer les données à la bonne URL
      method: 'POST',
      headers: {
        'X-CSRFToken': csrfToken,
      },
      body: formData,
    })
    .then(response => response.json())  // Assurez-vous que la réponse est au format JSON
    .then(data => {
      if (data.success) {
        alert('Incendie déclaré avec succès!');
        form.reset(); // Réinitialise le formulaire après le succès
      } else {
        alert('Erreur lors de la déclaration de l\'incendie. Veuillez réessayer.');
      }
    })
    .catch(error => {
      console.error('Erreur:', error);
      alert('Une erreur est survenue. Veuillez réessayer.');
    });
  });
});


////////////////////////////////////////////////////////////////////////////////////////////////////
                              //carte geographique//
// Initialisation de la carte
const map = L.map('mapid').setView([36.7169, 4.0497], 13);

// Ajout des tuiles OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

// Marqueur pour l'unité de pompiers à Tizi Ouzou
const fireStation = L.marker([36.71165378796484, 4.075426689905211]).addTo(map)
  .bindPopup("<b>Unité de Pompiers Principale</b><br>Tizi Ouzou")
  .openPopup();

// Marqueur temporaire
let marker;

// Initialiser le contrôle de routage
let routeControl = L.Routing.control({
  waypoints: [fireStation.getLatLng()], // Point de départ : l'unité de pompiers
  routeWhileDragging: true,
}).addTo(map);

// Fonction pour gérer le clic sur la carte
map.on('click', function (e) {
  const { lat, lng } = e.latlng;

  // Ajout ou mise à jour du marqueur
  if (marker) {
    marker.setLatLng([lat, lng]);
  } else {
    marker = L.marker([lat, lng]).addTo(map);
  }

  // Remplissage des champs du formulaire
 
  document.getElementById('address').value = `Lat: ${lat.toFixed(6)}, Lng: ${lng.toFixed(6)}`;

   // Mettre à jour l'itinéraire avec la nouvelle localisation de l'incendie
   routeControl.setWaypoints([fireStation.getLatLng(), marker.getLatLng()]);
});

// Gestion du focus sur le champ "Adresse'
document.getElementById('address').addEventListener('focus', function () {
  if (document.getElementById('mapid').classList.contains('visible')) {
    document.getElementById('mapid').scrollIntoView({ behavior: 'smooth' });
  }
});


// Gestion de l'envoi du formulaire


//activation des effets de l'apparition de la carte 
document.addEventListener('DOMContentLoaded', () => {
  const mapElement = document.getElementById('mapid');

  // Ajouter un délai pour afficher la carte avec l'effet
  setTimeout(() => {
    mapElement.classList.add('visible');
  }, 700); // Attendre 700 ms avant de lancer l'animation
});

                              


//////////////////////////// Les touches de claviers ////////////////////////////////?
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('fireDeclarationForm');

  form.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      e.preventDefault(); // Empêche le comportement par défaut (soumettre le formulaire)

      const formElements = Array.from(form.elements); // Obtenir une liste des éléments du formulaire
      const currentIndex = formElements.indexOf(e.target); // Trouver l'élément actuel (celui qui a le focus)

      // Passer au champ suivant s'il existe
      if (currentIndex > -1 && currentIndex < formElements.length - 1) {
        const nextElement = formElements[currentIndex + 1];
        nextElement.focus(); // Donner le focus au champ suivant
      }
    }
  });
});



////////////////////////////////sauvegarde des donnees du chemin ////////////////////////////////

