from django.contrib import admin
from django.urls import path
from django.views.decorators.cache import cache_page


from News.views import HomeNews, NewsByCategory, view_news, AddNews, register, user_login, user_logout
# from News.views import index, get_category,add_news login


urlpatterns = [
    path('', HomeNews.as_view(), name='Home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='Category'),
    path('news/<int:news_id>/', view_news, name='View_news'),
    path('news/add_news/', AddNews.as_view(), name='Add_news'),
    path('register/', register, name='Register'),
    path('login/', user_login, name='Login'),
    path('logout/', user_logout, name='Logout'),
]

