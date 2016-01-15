from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template

# Create your views here.
def index(request):
    link_list = ['Machines', 
                 'Operations', 
                 'Post Processors']
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
               'post_processors': post_processors}

    #print(get_template("/ConvGCodeGenerator/index.html"))
    
    return render(request, 'ConvGCodeGenerator/index.html', context)
