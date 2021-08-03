from django.shortcuts import render, redirect
from accounts.models import user_register , user_post
from django.contrib import messages
from django.http import JsonResponse , HttpResponse
import json

from .scraper import scraper
from .result_score import score

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        fb_username = request.POST['Facebook_username']
        fb_email = request.POST['Facebook_email']
        fb_password = request.POST['Facebook_password']
        fb_link = request.POST['Facebook_link']
        item_checked = request.POST.get('term_checked')
        if item_checked is None:
            messages.info(request,'Please make sure you accept our term and policy')
            return redirect('register')
        elif username == "" or password =="":
            messages.info(request,'Please make sure you fill username and password')
            return redirect('register')
        elif user_register.objects.filter(username=username).exists():
            messages.info(request,'Username Taken')
            return redirect('register')
        else:
            post = user_register.objects.create(username=username,password=password,facebook_name=fb_username,facebook_email=fb_email,facebook_password=fb_password,facebook_link=fb_link)
            post.save()
            created_text = "Account created successfully"
            created_text_1 ="Please login"
            created_alert = {
                'account':created_text,
                'account_1':created_text_1
            }
            return render(request,'login.html', created_alert)
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        # user
        login_username = request.POST.get('login_username')
        login_password = request.POST.get('login_password')
        if login_password == "" or login_username == "":
             messages.info(request,'Your information is empty')
             return redirect('login')
        elif user_register.objects.filter(username=login_username).exists():
            if user_register.objects.filter(password=login_password).exists():
                context = score(login_username) #to get the score
                print("Login Sucess")
                return render(request,'self.html', context)
            else:
                messages.info(request,'Your password is incorrect')
                return redirect('login')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def main(request):
    if request.method == 'POST':
        username = request.POST.get('profile_username')
        password = request.POST.get('profile_password')
        fb_username = request.POST.get('profile_fb_name')
        fb_email = request.POST.get('profile_fb_email')
        fb_password = request.POST.get('profile_fb_password')
        fb_link = request.POST.get('profile_fb_link')
        if user_register.objects.filter(username=username).exists():
            post = user_register.objects.get(username=username)
            post.facebook_name = fb_username
            post.facebook_email = fb_email
            post.facebook_password = fb_password
            post.facebook_link = fb_link
            post.save()
            print("done")
            obj = user_register.objects.get(username=username)
            context = score(username)
            return render(request,'profile.html', context)
        else:
            print("error")
            return redirect('profile')
    else:
        return render(request,'profile.html')

def profile(request):
    if request.method == 'POST':
        username = request.POST.get('profile_input')
        if user_register.objects.filter(username=username).exists():
            context = score(username)
            return render(request,'profile.html', context)
        else:
            print("error")
            return redirect('profile')
    else:
        return render(request,'profile.html')

def self(request):
    if request.method == 'POST':
        username = request.POST.get('self_input')
        print("test",username)
        if user_register.objects.filter(username=username).exists():
            context = score(username)
            return render(request,'self.html', context)
        else:
            print("error")
            return redirect('self')
    else:
        return render(request,'self.html')

def friend(request):
    if request.method == 'POST':
        username = request.POST.get('friend_input')
        print("test_friend",username)
        if user_register.objects.filter(username=username).exists():
            context = score(username)
            return render(request,'friend.html', context)
        else:
            print("error")
            return redirect('friend')
    else:
        return render(request,'friend.html')


def logout(request):
    return render(request,'index.html')

def get_wiki_summary(request):
    ext_username = request.GET.get('username', None)
    ext_password = request.GET.get('password', None)
    print('Ext_username:', ext_username)
    print('Ext_Password:', ext_password)
    if user_register.objects.filter(username=ext_username).exists():
            if user_register.objects.filter(password=ext_password).exists():
                obj = user_register.objects.get(username=ext_username)
                if user_post.objects.filter(fb_username=obj.facebook_name).exists():
                    result = user_post.objects.get(fb_username=obj.facebook_name)
                    context = score(ext_username)
                    fb_name = obj.facebook_name
                    bully_score = context['real_bully_score']
                    friend_score = context['ranking']
                else:
                    bully_score = "0"
                    friend_score =[]
                    fb_name = obj.facebook_name
                print("Login Success")
                data = {
                'Username': ext_username,
                'Password':ext_password,
                'Fb_name':fb_name,
                'bully_score':bully_score,
                'friend_rank':friend_score,
                'raw': 'Successful',
                }
            else:
                data = {
                'raw': 'Failed',
                }
    else:
        data = {
        'raw': 'Invalid',
        }

    print('json-data to be sent: ', data)

    return JsonResponse(data)

def get_scraper(request):
    print("testing")
    content_username = request.GET.get('username', None)
    #content_fb_name = request.GET.get('fb_name', None)
    obj = user_register.objects.get(username=content_username)
    user_fb_name = obj.facebook_name
    user_fb_email = obj.facebook_email
    user_fb_password = obj.facebook_password
    user_fb_link = obj.facebook_link
    if not user_fb_email or not user_fb_email or not user_fb_password or not user_fb_link:
        data = {
            'scraped': 'fail',
        }
        print('json-data to be sent: ', data)
        return JsonResponse(data)
    else:
        print("get request from content script:", content_username)
        if user_post.objects.filter(fb_username=user_fb_name).exists():
            scraped_success = scraper(user_fb_name,user_fb_email, user_fb_password, user_fb_link)
            print("boolean",scraped_success)
            if scraped_success is True:
                data = {
                    'scraped': 'success',
                }
            else:
                data = {
                    'scraped': 'fail',
                }
            print('json-data to be sent: ', data)
            return JsonResponse(data)
            #obj = user_post.objects.get(fb_username='Tester Tong')
            #print(obj.post[1]["post_user"])
            #obj.post.append( {'post_user':'Tester Tong 2', 'content': 'ABCDEFG'} )
            #obj.save()
        else:
            post = user_post.objects.create(fb_username=user_fb_name, post=[], comment=[],user_score=0, friend_score=[])
            post.save()
            
            scraped_success = scraper(user_fb_name, user_fb_email, user_fb_password, user_fb_link)
            print("boolean",scraped_success)
            if scraped_success is True:
                data = {
                    'scraped': 'success',
                }
            else:
                data = {
                    'scraped': 'fail',
                }
            print('json-data to be sent: ', data)
            return JsonResponse(data)
    

    

    