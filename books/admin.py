from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'author',
    )

    ordering = ('title',)
    save_as = True


admin.site.register(Book, BookAdmin)
