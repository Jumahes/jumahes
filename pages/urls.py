from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path("codage/", views.codage, name="codage"),
    path("webdesign/", views.webdesign, name="webdesign"),
    path("intropython/", views.intropython, name="intropython"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("education/", views.education, name="education"),
    path("translate/", views.translate, name="translate"),
    path("training/", views.training, name="training"),
    path("workshop/", views.workshop, name="workshop"),
]
