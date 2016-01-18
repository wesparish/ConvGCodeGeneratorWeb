from django.shortcuts import render

# Create your views here.
def index(request):
    machines = [("Lathe", 'enabled'),
                  ("Mill", 'disabled'),
                  ("EDM", 'disabled'),
                  ("Water Jet ", 'disabled'),
                  ("etc...", 'disabled')]
    operations = [("Tool-Test", 'enabled'),
                  ("OD-Turning", 'disabled'),
                  ("ID-Boring", 'disabled'),
                  ("Drilling ", 'disabled'),
                  ("OD-Threading", 'disabled'),
                  ("ID-Threading", 'disabled'),
                  ("etc...", 'disabled')]
    post_processors = [("Fanuc0tb", 'enabled'),
                  ("LinuxCNC", 'disabled'),
                  ("Mach3", 'disabled'),
                  ("etc...", 'disabled')]
    
    context = {'machines': machines, 
               'operations': operations, 
               'post_processors': post_processors,
               'user': request.user}
    
    return render(request, 'ConvGCodeGenerator/index.html', context)

def contact_us(request):
    if request.method == 'POST':
        import smtplib
        from time import ctime
        from email.mime.text import MIMEText
        
        context = {'alert': {}}
        try:
            msg = MIMEText("""
    Date: """ + ctime() + """
    From: """ + request.POST['name'] + """
    Email: """ + request.POST['email'] + """
    \n\n""" + request.POST['comment'])
            msg['Subject'] = 'New comment email from CG2 website'
            msg['From'] = request.POST['email']
            msg['To'] = 'wes@firstshotprecision.com'
    
            s = smtplib.SMTP('172.16.1.13')
            s.sendmail(msg['From'], msg['To'], msg.as_string())
            s.quit()
            context['alert']['level'] = "success"
            context['alert']['message'] = "Successfully sent comment email. Thank you."
        except Exception as e:
            context['alert']['level'] = "danger"
            context['alert']['message'] = "Unable to send contact email, please try again later. (%s)" % (e)
        return render(request, 'ConvGCodeGenerator/index.html', context)
    
    return render(request, 'ConvGCodeGenerator/contact.html')
    