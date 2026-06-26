from django.db import models

class HeroSection(models.Model):
    name = models.CharField(max_length=100, default="Iduwara Nisal")
    title = models.CharField(max_length=200, help_text="e.g., Aspiring AI Engineer & Machine Learning Enthusiast 🚀")
    description = models.TextField()
    location = models.CharField(max_length=100, help_text="e.g., Matara, Sri Lanka")
    degree = models.CharField(max_length=100, help_text="e.g., Information Systems")
    interest = models.CharField(max_length=100, help_text="e.g., Deep Learning")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True, help_text="e.g., https://linkedin.com/in/iduwaranisal")
    github_link = models.URLField(blank=True, null=True, help_text="e.g., https://github.com/iduwaranisal")

    def __str__(self):
        return f"Hero Section - {self.name}"

class AboutSection(models.Model):
    heading = models.CharField(max_length=100, default="Behind the Screen")
    paragraph_1 = models.TextField()
    paragraph_2 = models.TextField()

    def __str__(self):
        return "About Section Content"

class Project(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, help_text="e.g., Machine Learning")
    description = models.TextField()
    tech_stack = models.CharField(max_length=255, help_text="Comma separated, e.g., Python, Flask, Pandas")
    project_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    order = models.IntegerField(default=0, help_text="To sort projects")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"