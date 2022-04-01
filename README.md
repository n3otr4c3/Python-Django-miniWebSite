# Python-Django-miniWebSite
First exercice and website using Python-Django framework 

## Courte introduction
Il s'agit de mon premiers mini projet de type WebSite sur le framework Django que j'affectionne particulièrement, et ce, dans le cadre d'une formation.


![alt text](https://zupimages.net/up/22/13/vi6l.png)

## Explications :

Le but était de comprendre comment fonctionne les différents éléments
```python
- views.py
- urls.py
- settings.py
```

La notion d'App (d'ou le blog séparé)
Les routes, les balises, les syntaxes, etc. 

Exemple 1 : 
```python
urlpatterns = [
    path('', index, name="blog-index"),
    path('article-<str:numero_article>/', article, name="blog-article"),  
```
Exemple 2 :
```python
def article(request, numero_article):
    return render(request, f"blog/article_{numero_article}.html") 
```

Le site en lui même est full responsive et assez simple dans son ensemble.

