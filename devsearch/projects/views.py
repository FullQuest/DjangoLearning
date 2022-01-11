from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


def projects(request):
    projects = Project.objects.all()  # pylint: disable=maybe-no-member
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)  # pylint: disable=maybe-no-member
    return render(request, 'projects/single-project.html', {'project': projectObj})


def createProject(request):
    context = {'projects': projects}
    return render(request, "projects/project_form.html", context)

# Create your views here.