from django.db.models import fields
from django.shortcuts import render
from emaillist.models import Email
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from django.urls import reverse_lazy
# Create your views here.

class EmailCreateView(CreateView):
    model = Email
    template_name = 'emaillist/add_email.html'
    fields = ('email',)
    success_url = reverse_lazy('add_email')

class EmailDeleteView(DeleteView):
    model = Email
    template_name = 'emaillist/delete_email.html'
    success_url = reverse_lazy('list_email')

class EmailListView(ListView):
    model = Email
    template_name = 'emaillist/list_email.html'

from django.core.mail import send_mail

def send_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = {
            'subject': subject,
            'message': message
        }
        message = "{}".format(data['message'])
        send_mail(data['subject'],message,'Dante <adescore@gmail.com>',list(Email.objects.all().values_list('email', flat = True)))
    return render(request, 'emaillist/send_email.html', {})
    