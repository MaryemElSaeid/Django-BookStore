from django.contrib import admin
from .models import Booklet,Category,Isbn,Summary
from .forms import BookletForm,CategoryForm


class BookletAdmin(admin.ModelAdmin):
    form=BookletForm
    list_display=("title","author","content")
    list_filter=("categories",)
    search_fields=("title",)


class BookletInline(admin.StackedInline):
    model=Booklet
    max_num=3
    extra=1

class SummaryAdmin(admin.ModelAdmin):
    inlines=[BookletInline]


class CategoryAdmin(admin.ModelAdmin):
    form=CategoryForm



admin.site.register(Booklet,BookletAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Isbn)
admin.site.register(Summary, SummaryAdmin)