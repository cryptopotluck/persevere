from django.shortcuts import render

# Create your views here.


def codingclass(requests):
    return render(requests, 'pages/coding_class.html')


def donate(requests):
    return render(requests, 'pages/donate.html')


def employability(requests):
    return render(requests, 'pages/employability_instruction.html')


def entrepreneurship(requests):
    return render(requests, 'pages/entrepreneurship.html')


def jobplacement(requests):
    return render(requests, 'pages/job_placement.html')


def lifeskills(requests):
    return render(requests, 'pages/life_skills.html')


def workexperience(requests):
    return render(requests, 'pages/work_experience.html')

def about(requests):
    return render(requests, 'pages/about.html')