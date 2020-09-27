from django.shortcuts import render
from .forms import ContactForm
from django.shortcuts import redirect
from ResumeProject import settings
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            com_name = form.cleaned_data['com_name']
            com_add = form.cleaned_data['com_add']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            message = form.cleaned_data['message']
            all_data = f"Name: {name}\nCompany Name: {com_name}\nCompany Address: {com_add}\nEmail: {email}\nMobile: {mobile}\nMessage: {message}"
            subject = "Message from my resume site"
            sender = 'beyondhorrizon7@gmail.com'
            recipients = ['akashmothe1@gmail.com']

            sent = send_mail(subject, all_data, sender, recipients,fail_silently=False,auth_user=settings.EMAIL_HOST_USER,auth_password=settings.EMAIL_HOST_PASSWORD)
            if sent == 1:
                messages.success(request,'Success, Your message has been sent successfully. Thanks for contacting me, I will be shortly in touch with you.')
                return redirect('/')
            else:
                messages.error(request,'Sending Failed, Something went wrong please try again once.')
                return redirect('/')
    else:
        form = ContactForm()
    return render(request,'contact/contact.html',{'contact':'active','form':form})