from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import  redirect
from .forms import ContactForm
from django.utils.translation import activate

def switch_language(request):
    lang = request.POST.get('language', 'en')
    activate(lang)
    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie('django_language', lang)
    return response



def send_email(request):
    text = 'hello there is a test email'
    email = 'gudr901@gmail.com'
    subject = "TestEmail"

    send_mail(
        subject,
        text,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False
    )

    return HttpResponse("Email sent successfully!")




def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()  # Bazaga saqlash

            # Email yuborish
            send_mail(
                subject=f"Yangi xabar: {contact.name}",
                message=f"Ism: {contact.name}\nEmail: {contact.email}\nXabar: {contact.message}",
                from_email='bekturdiyevashaydo9@gmail.com',
                recipient_list=['bekturdiyevashaydo9@gmail.com'],
                fail_silently=False,
            )

            return redirect('success_page')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


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
