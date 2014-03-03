from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from contact.models import ContactForm

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            telephone = form.cleaned_data['sender_telephone']
            sender_name = form.cleaned_data['sender_name']
            cc_myself = form.cleaned_data['cc_myself']

            message += "\n\nTelefon nummer: %s" % telephone
            message += "\nEmail: %s" % sender
            subject = "Royal Fashion Copenhagen: %s" % subject
            
            recipients = [{
                'email': 'info@royalfashioncph.dk',
                'name': 'Royal Fashion Copenhagen'}]
            if cc_myself:
                recipients.append({
                    'email': sender,
                    'name': sender_name})

            import mandrill
            try:
                mandrill_client = mandrill.Mandrill('LvrMoSVENHFZTMVuT2pyIQ')
                message = {
                    'from_email': sender,
                    'from_name': sender_name,
                    'subject': subject,
                    'text': message,
                    'to': recipients,
                }
                result = mandrill_client.messages.send(message=message, async=False)

            except mandrill.Error, e:
                # Mandrill errors are thrown as exceptions
                print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
                raise

            return HttpResponseRedirect(reverse('thanks'))
    else:
        form = ContactForm()

    return render(request, 'omos.html', {'form': form})

def thanks(request):
    feedback = "Tak fordi du kontaktede os. Vi vender tilbage til dig snarest muligt."

    return render(request, 'omos.html', {'feedback': feedback})
