from .models import AboutInfo


def about_info_processor(request):
    return {
        'about_info': AboutInfo.objects.first()
    }