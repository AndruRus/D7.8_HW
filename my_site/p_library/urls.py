from django.contrib import admin
from django.urls import path
from django.urls import reverse_lazy
from p_library.views import index, RegisterView, CreateUserProfile
from p_library.views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many
from django.contrib.auth.views import LoginView, LogoutView
from allauth.account.views import login, logout

app_name = 'p_library'
urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', RegisterView.as_view(
        template_name='register.html',
        success_url=reverse_lazy('common:profile-create')),
        name='register'),
    path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),
    path('author/create', AuthorEdit.as_view(), name='author_create'),
    path('author', AuthorList.as_view(), name='author_list'),
    path('author/create_many', author_create_many, name='author_create_many'),
    path('author_book/create_many', books_authors_create_many, name='author_book_create_many'),
]
