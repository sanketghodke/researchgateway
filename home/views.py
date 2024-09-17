from django.shortcuts import render
from home.models import ResearchPapers
# Create your views here.
def post_list(request):
    papers = ResearchPapers.objects.all()
    return render(request, 'home/post_list.html', {'papers': papers})