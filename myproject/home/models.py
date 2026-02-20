from django.db import models

#declaration dd la table fireincident

class FireIncident(models.Model):
    reporter_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    fire_type = models.CharField(max_length=50)
    fire_severity = models.CharField(max_length=50)

    def __str__(self):
        return f"Incendie déclaré par {self.reporter_name}"
    

#declaration de la table Citoyen 


class Citoyen(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname

#declaration de la table incendie

class Incendie(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()
    type = models.CharField(max_length=100)
    severity = models.CharField(max_length=100)
    date_reported = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.type} - {self.severity} - {self.date_reported}"
    
    
    
    
#declaration table vehicule 
class VehiculeDePompier(models.Model):
    # Champs pour la table
    NUM_IMMATRICULATION_CHOICES = [
        ('Camion-citerne', 'Camion-citerne'),
        ('Camion-échelle', 'Camion-échelle'),
        ('Ambulance', 'Ambulance'),
    ]

    ETAT_CHOICES = [
        ('Opérationnel', 'Opérationnel'),
        ('En réparation', 'En réparation'),
    ]

    num_immatriculation = models.CharField(max_length=20, unique=True)
    type_vehicule = models.CharField(max_length=20, choices=NUM_IMMATRICULATION_CHOICES)
    marque = models.CharField(max_length=50)
    etat = models.CharField(max_length=20, choices=ETAT_CHOICES)
    en_service = models.BooleanField()

    # Méthodes pour afficher les informations sur l'objet
    def __str__(self):
        return f'{self.marque} - {self.num_immatriculation}'

    class Meta:
        verbose_name = 'Véhicule de pompier'
        verbose_name_plural = 'Véhicules de pompiers'
    
##########################################################################################
class Pompier(models.Model):
    # Définition des équipes possibles
    NOMS_EQUIPE = [
        ('incendie', 'Équipe de lutte contre les incendies'),
        ('secours', 'Équipe de secours et de sauvetage'),
        ('sauvage', 'Équipe de sauvetage aquatique'),
        ('médical', 'Équipe de secours médical'),
        ('montagne', 'Équipe d\'intervention en milieu montagneux'),
        ('urgence', 'Équipe de gestion des urgences'),
    ]
    
    # Définition des types de missions possibles
    TYPES_MISSION = [
        ('incendie_foret', 'Lutte contre les incendies de forêts'),
        ('incendie_batiment', 'Lutte contre les incendies de bâtiments'),
        ('incendie_vehicule', 'Lutte contre les incendies de véhicules'),
        ('secours_urgence', 'Secours d\'urgence'),
    ]

    # Informations personnelles
    nom = models.CharField(max_length=100, verbose_name="Nom")
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    numero_tel = models.CharField(max_length=15, verbose_name="Numéro de téléphone")

    # Équipe du pompier (choix parmi les équipes définies)
    equipe = models.CharField(
        max_length=50,
        choices=NOMS_EQUIPE,
        verbose_name="Équipe"
    )

    # Grade du pompier
    grade = models.CharField(
        max_length=50,
        choices=[('capitaine', 'Capitaine'),
                 ('lieutenant', 'Lieutenant'),
                 ('sergent', 'Sergent'),
                 ('pompier', 'Pompier')],
        verbose_name="Grade"
    )

    # Date de recrutement
    date_recrutement = models.DateField(verbose_name="Date de recrutement", blank=True, null=True)

    # En mission ou non
    en_mission = models.BooleanField(default=False, verbose_name="En mission")

    # Mission du pompier (choix parmi les missions définies)
    mission = models.CharField(
        max_length=50,
        choices=TYPES_MISSION,
        verbose_name="Mission",
        null=True,
        blank=True  # Si le pompier n'est pas en mission, ce champ peut être vide
    )

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.grade} ({self.equipe})"

