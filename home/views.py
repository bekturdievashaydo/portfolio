from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import

# Create your views here.
def home_view(request):
    return render(request,'index.html')




def blog_view(request):
    return render(request,'blog-post.html')





def blogg_view(request):
    return render(request,'blog.html')




#
# def contact_view(request):
#     return render(request,'contact.html')
#
#
# def gallery_view(request):
#     return render(request,'gallery.html')
#
#
# def project_view(request):
#     return render(request,'project.html')
#
#
# def project_detail_view(request):
#     return render(request,'project-detail.html')
#
#
# def projects_view(request):
#     return render(request,'projects.html')
#
#
#
# def yourfilename_view(request):
#     return render(request,'yourfilename.html')
#
#
