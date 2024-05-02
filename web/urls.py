from django.urls import path
from web import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('jobs',views.jobs,name="jobs"),
    path('apply',views.apply,name="apply")
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
