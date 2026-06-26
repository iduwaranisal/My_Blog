from django.contrib import admin
from .models import HeroSection, AboutSection, Project, ContactMessage

admin.site.register(HeroSection)
admin.site.register(AboutSection)
admin.site.register(Project)
admin.site.register(ContactMessage)