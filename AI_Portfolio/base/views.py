from django.shortcuts import render, redirect
from django.contrib import messages
from .models import HeroSection, AboutSection, Project, ContactMessage

def home(request):
    hero = HeroSection.objects.first()
    about = AboutSection.objects.first()
    projects = Project.objects.all()

    for project in projects:
        if project.tech_stack:
            project.tech_list = [tech.strip() for tech in project.tech_stack.split(',')]
        else:
            project.tech_list = []

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(name=name, email=email, message=message)
        messages.success(request, "Thanks for reaching out! I'll get back to you soon.")
        return redirect('home')

    context = {
        'hero': hero,
        'about': about,
        'projects': projects,
    }
    return render(request, 'index.html', context)