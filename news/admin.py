from django.contrib import admin
from .models import Post, Image
from file_uploader.models import Document


# Register your models here.
class FilesInLine(admin.StackedInline):
    model = Document
    extra = 0


class ImagesInLine(admin.StackedInline):
    model = Image
    extra = 0

class PostAdmin(admin.ModelAdmin):
    fields = ['title',
              'text',
              'date',
              'slug',
              ]
    prepopulated_fields = {
        'slug': ('title',),
    }
    inlines = [ImagesInLine, FilesInLine,]

admin.site.register(Post, PostAdmin)
admin.site.register(Document)
admin.site.register(Image)

