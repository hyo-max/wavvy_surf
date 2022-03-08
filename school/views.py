from django.shortcuts import render

def school_list(request):
    return render(request, 'school/school_list.html')


def school_detail(request):
    return render(request, 'school/school_detail.html')