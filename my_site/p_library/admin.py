from django.contrib import admin
from p_library.models import Book, Author, PublishingHouse, WhenTook, Friend, UserProfile

@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
          @staticmethod
          def author_full_name(obj):
                     return obj.author.full_name
          list_display = ('title', 'author_full_name',)
          fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'copy_count', 'pub_house', 'image')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(PublishingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):
    pass

@admin.register(Friend)
class WhenTookAdmin(admin.ModelAdmin):
    pass


@admin.register(WhenTook)
class WhenTookAdmin(admin.ModelAdmin):
    pass