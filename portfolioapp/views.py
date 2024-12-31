from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail


def index(request):
    return render(request, 'index.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Compose email
            full_message = f"Message from {name} <{email}>\n\n{message}"
            
            try:
                # Send email
                send_mail(
                    subject,
                    full_message,
                    settings.DEFAULT_FROM_EMAIL,  # Sender's email
                    [settings.EMAIL_HOST_USER],  # Recipient's email
                )
                # Render the thank-you page
                return render(request, 'thank_you.html')
            except Exception as e:
                print(f"Error sending email: {e}")
                return render(
                    request,
                    'fail.html',
                    {'form': form, 'error': 'There was an error sending your message. Please try again later.'}
                )
        else:
            # Invalid form, re-render with errors
            return render(request, 'index.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})