from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, get_user_model
from .forms import ContactForm,LoginForm,RegisterForm
from django.contrib.auth import logout


def home(request):
    if request.user.is_authenticated:
        context={
        "premium_content": "Woah! It's gonna be amazing am telling you!"
        }
    else:
        context={"premium_content":""}
    return render(request, "home_page.html",context)

def contact(request):
    form=ContactForm()
    context= {
    "form": form,

    }
    return render(request, "contact/view.html",context)



def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
    "form": form
    }
    print("User logged in")
    #print(request.user.is_authenticated()) #Built in django
    if form.is_valid():
        print(form.cleaned_data)
        #context['form'] = LoginForm()

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        #print(user)
        #print(request.user.is_authenticated())

        if user is not None:
            #print(request.user.is_authenticated())
            login(request, user)

            return redirect("/")
        else:
            print("Error")
        #context['form'] = LoginForm()


    return render(request, "auth/login.html", context)
User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
    "form": form
    }

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")


        new_user = User.objects.create_user(username, email, password)
        print(new_user)
        return redirect("/login")
    return render(request, "auth/register.html", context)

def logout_x(request):
    logout(request)

    return render(request,"home_page.html")
