from django.shortcuts import render, get_object_or_404
from home.models import ResearchPapers


# Create your views here.
def post_list(request):
    papers = ResearchPapers.objects.all()
    return render(request, 'home/post_list.html', {'papers': papers})


def post_detail(request, pk):
    paper = get_object_or_404(ResearchPapers, pk=pk)
    return render(request, 'home/post_detail.html', {'paper': paper})
