from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.
#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)

class BooksInline(admin.TabularInline):
    model = Book

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    #"""
    #Administration object for Author models.
    #Defines:
    # - fields to be displayed in list view (list_display)
    # - orders fields in detail view (fields), grouping the date fields horizontally
    # - adds inline addition of books in author view (inlines)
    # """
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = [('first_name', 'last_name'), ('date_of_birth', 'date_of_death')]
    #fields coloca para exbir os campos na vertical e os entre () ficam na hrozontal
    inlines = [BooksInline] #adds inline addition of books in author view (inlines)

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status', 'due_back','id')
    list_filter = ('status', 'due_back')

    #grouping of fields into sections (fieldsets)
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )