from django.shortcuts import render, redirect
import datetime

def Home(request):
    return render(request, 'home.html')

def Developers(request):
    context = {
    "developers": [
        {
            "id": 1,
            "username": "hassan",
            "first_name": "Hassan",
            "last_name": "Kabirian",
            "skills": ["Python", "Django", "Vue.js"],
        },
        {
            "id": 2,
            "username": "sara",
            "first_name": "Sara",
            "last_name": "Ajmadi",
            "skills": ["JavaScript", "React", "Css"],
        },
        {
            "id": 3,
            "username": "ali",
            "first_name": "Ali",
            "last_name": "Rezayi",
            "skills": ["Java", "Spring Boot", "SQL"],
        },
     ]
    }
    return render(request, 'developer_list.html', context)

def CV(request, cv_id):
    developers = [
        {
            "id": 1,
            "username": "hassan",
            "first_name": "Hassan",
            "last_name": "Kabirian",
            "skills": ["Python", "Django", "Vue.js"],
        },
        {
            "id": 2,
            "username": "sara",
            "first_name": "Sara",
            "last_name": "Ajmadi",
            "skills": ["JavaScript", "React", "Css"],
        },
        {
            "id": 3,
            "username": "ali",
            "first_name": "Ali",
            "last_name": "Rezayi",
            "skills": ["Java", "Spring Boot", "SQL"],
        },
    ]

    developer = next((dev for dev in developers if dev["id"] == cv_id), None)

    if (developer == None):
        return redirect('Developers')

    return render(request, 'developer_cv.html', {"developer": developer})