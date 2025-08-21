from django.http import HttpResponse
from django.template import loader
import datetime

def Home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))

def Developers(request):
    template = loader.get_template('developer_list.html')
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
    return HttpResponse(template.render(context, request))

def CV(request, cv_id):
    template = loader.get_template('developer_cv.html')
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

    return HttpResponse(template.render({"developer": developer}, request))