
  

  // Appeler la fonction pour récupérer les incendies
  fetchFireData();

  // Rafraîchir les données périodiquement
  setInterval(fetchFireData, 60000);  // Mettre à jour toutes les minutes
  L.circle([latitude, longitude], {
    color: 'red',
    fillColor: 'red',
    fillOpacity: 0.3,
    radius: 500 // Rayon de 500 mètres
  }).addTo(map).bindPopup(`Incendie en cours: ${description}`);


  // Définir un point de départ et une destination (à modifier selon vos besoins)
  const start = [36.7167, 4.0481];  // Par exemple, Tizi Ouzou
  const end = [36.7528, 3.0799];    // Par exemple, un autre point à Tizi Ouzou (à adapter)

  // Créer l'itinéraire avec Leaflet Routing Machine
  L.Routing.control({
    waypoints: [
      L.latLng(start),  // Point de départ
      L.latLng(end)     // Destination
    ],
    routeWhileDragging: true,  // Permet de voir l'itinéraire pendant qu'on déplace les points
    createMarker: function() { return null; },  // Ne pas afficher de marqueur
    lineOptions: {
      styles: [{ color: 'lime', weight: 5, opacity: 0.8 }]  // Définir la couleur de la ligne en vert fluo
    }
  }).addTo(map);
  