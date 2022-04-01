from django.urls import path
from .views import index, article

# Séparation du fichier URL pour respecter ce qui se fait en général et le fait que ce soit une app à part.
urlpatterns = [
    path('', index, name="blog-index"),
    path('article-<str:numero_article>/', article, name="blog-article"),

]