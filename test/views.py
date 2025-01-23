from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, "html/index.html")

def main_page(request):
  return render(request, "html/main.html")
  
