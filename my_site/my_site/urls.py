from django.contrib import admin
from django.urls import path, include
from p_library import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('p_library.urls', namespace='p_library')),
    path('accounts/', include('allauth.urls')),
    path('list_book/book_increment/', views.book_increment),
    path('list_book/book_decrement/', views.book_decrement),
    path('books/', views.books_list, name='list_book'),
    path('publishinghouses/', views.publishinghouses),
    path('friends-list/', views.friends_list, name='friends_list'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
