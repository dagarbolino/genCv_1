from django.db import models



from config import settings

USER = settings.AUTH_USER_MODEL


class Info(models.Model):
    title = models.CharField("titre du curriculm", max_length=120)
    lastname = models.CharField("nom de la personne", max_length=120)
    firstname = models.CharField("prénom de la personne", max_length=120, blank=True, null=True)
    type_of_Contract = models.CharField("type de contrat", max_length=120, blank=True, null=True)
    date_of_birth = models.DateField("date de naissance de la personne", blank=True, null=True)
    place_of_birth = models.CharField("lieu de naissance de la personne", max_length=120, blank=True, null=True)
    address = models.CharField("adresse de la personne", max_length=120, blank=True, null=True)
    city = models.CharField("ville", max_length=120, blank=True, null=True)
    state = models.CharField("état", max_length=120, blank=True, null=True)
    zip_code = models.IntegerField("code postal", blank=True, null=True)  
    phone = models.IntegerField("téléphone de la personne", blank=True, null=True)  
    email = models.EmailField("email de la personne", max_length=100, blank=True, null=True)
    photo = models.ImageField("photo de la personne", upload_to='photos/', blank=True, null=True)
    motivation = models.TextField("motivation de la personne", blank=True, null=True)
    
    is_active = models.BooleanField("curriculum is active?", default=False)
    created_at = models.DateTimeField("date de création", auto_now_add=True)
    updated_at = models.DateTimeField("date de modification", auto_now=True)

    hobbies = models.ManyToManyField(to="Hobby", related_name="hobbies", blank=True)  
    formations = models.ManyToManyField(to="Formation", related_name="formations", blank=True)  
    experiences = models.ManyToManyField(to="Experience", related_name="experiences", blank=True)  
    skills = models.ManyToManyField(to="Skill", related_name="skills", blank=True)  
    languages = models.ManyToManyField(to="Language", related_name="languages", blank=True)  
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='users')
    
    


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Info"
        verbose_name_plural = "Infos"  



class Hobby(models.Model):
    title_hobby = models.CharField("titre du hobbie", max_length=120)
    info = models.ForeignKey(Info, on_delete=models.CASCADE, related_name='hobby_info', null=True)
    
    def __str__(self):
        return self.title_hobby
    
    class Meta:
        verbose_name = "Hobbie"
        verbose_name_plural = "Hobbies"  


class Formation(models.Model):
    title_formation = models.CharField("titre de la formation", max_length=120)
    description_formation = models.TextField("description de la formation")
    business = models.CharField("école ou entreprise", max_length=120, blank=True, null=True)
    start_date_of_formation = models.DateField("date de début de la formation", blank=True, null=True)   
    end_date_of_formation = models.DateField("date de fin de la formation", blank=True, null=True)
    location_formation = models.CharField("lieu de la formation", max_length=100)
    info = models.ForeignKey(Info, on_delete=models.CASCADE, related_name='formations_info', null=True)
        
    def __str__(self):
        return self.title_formation
    
    class Meta:
        verbose_name = "Formation"
        verbose_name_plural = "Formations"  
    
    
    
class Experience(models.Model):
    title_experience = models.CharField("titre de la l'expérience", max_length=120)
    description_experience = models.TextField("description de l'expérience")
    business = models.CharField("école ou entreprise", max_length=120, blank=True, null=True)
    start_date_of_experience = models.DateField("date de début de l'expérience", blank=True, null=True)
    end_date_of_experience = models.DateField("date de fin de l'expérience", blank=True, null=True)
    location_experience = models.CharField("lieu de l'expérience", max_length=100)
    info = models.ForeignKey(Info, on_delete=models.CASCADE, related_name='experience_info', null=True)

    
    def __str__(self):
        return self.title_experience  
    
    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"      
    

class Skill(models.Model):
    title_Skill = models.CharField("titre de la compétence", max_length=120)
    info = models.ForeignKey(Info, on_delete=models.CASCADE, related_name='skill_info', null=True)
    
    def __str__(self):
        return self.title_Skill
    
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"  
    
    
class Language(models.Model):
    title_language = models.CharField("titre de la langue", max_length=120)
    niveau_choices = [
        ('Débutant', 'Débutant'),
        ('Intermédiaire', 'Intermédiaire'),
        ('Avancé', 'Avancé'),
    ]
    niveau_language = models.CharField("niveau de la langue choisie", max_length=120, choices=niveau_choices)
    info = models.ForeignKey(Info, on_delete=models.CASCADE, related_name='language_info', null=True)

    def __str__(self):
        return self.title_language
    
    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"  


