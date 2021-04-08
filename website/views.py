from django.shortcuts import render


# Create your views here.
def index(request):
    """
    函数视图，返回模板文件中的html
    """
    return render(request, 'website/index.html')
