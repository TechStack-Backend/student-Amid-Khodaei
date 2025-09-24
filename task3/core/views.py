from django.shortcuts import render, redirect
from .models import Developer, Skill, Project
from .form import DeveloperForm, ProjectForm
import datetime

def Home(request):
    return render(request, 'home.html')

def Developers(request):
    context = {
    "developers": Developer.objects.all(),
    "skills": Skill.objects.all()
    }
    return render(request, 'developer_list.html', context)

def Projects(request):
    context = {
        "projects": Project.objects.all(),
        "developers": Developer.objects.all()
    }
    return render(request, 'project_list.html', context)

def add_developer(request):
    if request.method == "POST":
        form = DeveloperForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = DeveloperForm()
    
    return render(request, 'add_developer.html', {'form': form})

def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            form.save_m2m()
            return redirect('Home')
    else:
        form = ProjectForm()

    return render(request, 'add_project.html', {'form': form})