from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *
# Create your views here.


def home(request):
    
    popularblogs = popularblog.objects.all()
    context = {'popularBlogs': popularblogs, 'name':'Mr Ram', 'titles':'Home - IIMT Blogs'}
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html',{'titles':'About - IIMT Blogs'})

def contact(request):
    if request.method == 'POST':
       cname = request.POST['fullname']
       cemail = request.POST['emailadd'] 
       cphone = request.POST['phone']
       caddress = request.POST['address']
       cmsg = request.POST['msg']
       
       if len(cname)>1 and len(cemail)>1 and len(cphone)==10 and len(caddress)>1 and len(cmsg)>1:
           
       
         contactobj = ContactUsTb(name=cname, email = cemail, phone=cphone,address = caddress,message = cmsg)
         contactobj.save()
    
       else:
           return render(request, 'contact.html', {'titles':'Contact - IIMT Blogs'})
       
       
    #    return HttpResponse('your form submitted')
       
    return render(request,'contact.html',{'titles':'Contact - IIMT Blogs'} )



def view_blog(request,pk):
    
    viewBlog = popularblog.objects.get(pk = pk)
    return render(request, 'viewBlog.html',{'viewBlog':viewBlog,'titles':'viewBlogs - IIMT Blogs'})
    