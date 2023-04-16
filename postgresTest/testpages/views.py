from django.shortcuts import render

# Create your views here.
def mypage(request):
    return render(request, "mypage.html", context={ "session": request.session.get("user") })