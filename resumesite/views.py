from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def home(request):

	if request.method == 'POST':
		message = request.POST['message']
		send_mail('Contact Form', 
			message, 
			settings.EMAIL_HOST_USER, 
			['nicolemoyo48@gmail.com'], 
			fail_silently=False)

	return render(request, 'home.html', {})
