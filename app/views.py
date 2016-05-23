#coding = utf-8
from django.shortcuts import render,redirect
from app.models import Item,UserProfile,Blog
import time
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User 

def home_page(request):
    if request.method == 'POST':
        username=request.POST['user'] 
        password=request.POST['mima']  
        user = authenticate(username=username,password=password)
        if user and user.is_active:  
            login(request, user) 
            return redirect('list/')
        else:
            return redirect('/')
    return render(request,'home.html')
def list_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'],times = time.strftime("%Y-%m-%d %X", time.localtime()))
    items = Item.objects.all()
    return render(request,'list.html',{'items':items})
def logout_view(request):
    logout(request)
    return store_view(request)
def gy_page(request):
	return render(request,'gy.html')
def photo_page(request):
	return render(request,'photo.html')
def day_page(request):
	return render(request,'day.html')
def blog_page(request):
	return render(request,'blog.html')
def dt_page(request):
	return render(request,'dt.html')
def gd_page(request):
	return render(request,'gd.html')
def xx_page(request):
	return render(request,'xx.html')
def blog_page(request):
    blogs = Blog.objects.all().order_by('-created')
    return render(request,'blog.html', {"blogs": blogs})
def userRegister(request):  
    try:  
        if request.method=='POST':  
            username=request.POST['name']  
            password1=request.POST['password1'] 
            password2=request.POST['password2'] 
            email=request.POST['email'] 
            phone=request.POST['phone'] 
            errors=[]
            filterResult=User.objects.filter(username=username)
            if len(filterResult)>0:  
                errors.append("用户名已存在")  
                return render(request,'zhuce.html',{'errors':errors}) 
            if len(password1) < 6:
                errors.append("请输入大于6位数密码")
                return render(request,'zhuce.html',{'errors':errors})  
            if password1!=password2:  
                errors.append("两次输入的密码不一致!")  
                return render(request,'zhuce.html',{'errors':errors}) 
            if len(email) < 9:
                errors.append("请输入有效邮箱")
                return render(request,'zhuce.html',{'errors':errors})
            user=User()
            user.username=username  
            user.set_password(password1)  
            user.email=email  
            user.save()   
            profile=UserProfile() 
            profile.user_id=user.id  
            profile.phone=phone  
            profile.save()  
            newUser=authenticate(username=username,password=password1)
            if newUser is not None:  
                login(request, newUser)
                return redirect("http://127.0.0.1:8000/list/")  
    except Exception as e:  
        errors.append(str(e))  
        return render(request,'zhuce.html',{'errors':errors}) 
    return render(request,'zhuce.html') 


