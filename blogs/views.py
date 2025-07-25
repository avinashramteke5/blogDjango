from django.shortcuts import get_object_or_404, render

from blogs.models import Blog

def home_page(request):
    return render(request, "index.html")

def about_page(request):
    return render(request, "about.html")

def blogs_page(request):
    blogs = Blog.objects.all()
    return render(request, "blogs.html", {"allblogs":blogs})


def blog_detail_page(request,pk):
    blog_detail = get_object_or_404(Blog, pk=pk)
    return render(request, "details.html", {"myblogsdeatail":blog_detail})