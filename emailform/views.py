from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        #not really needed
        data = {
            'email': email,
            'subject' : subject,
            'message': message
        }
        
        message = '''
        New message: {}

        From: {}
        '''.format(message, email)
        send_mail(data['subject'], data['message'],'', ['olagbenroadeite@gmail.com',])
    return render(request,'emailform/index.html', {})
        
