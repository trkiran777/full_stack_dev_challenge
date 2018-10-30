from django.shortcuts import render

# Shows the views for rendering web pages.


def landing_page(request):
    return render(request, "landingPage.html")

def admin_home_page(request):
    return render(request, "adminHomePage.html")

def performance_reviews_page(request):
    return render(request, "performanceReviewsPage.html")
