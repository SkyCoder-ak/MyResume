from django.shortcuts import render

# Create your views here.
def skill_view(request):
    return render(request,'skills/skills.html',{'skills':'active'})