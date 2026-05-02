from django.shortcuts import render

def addViewReportPage(request):
    return render(request, "viewReport.html")
