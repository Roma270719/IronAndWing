from .models import AboutInfo, Navbar


def about_info_processor(request):
    return {
        'about_info': AboutInfo.objects.first()
    }

def navbar_processor(request):
    return {
        'navbar': Navbar.objects.first()
    }