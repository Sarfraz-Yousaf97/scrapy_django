from django.contrib import admin
from main.models import Quote, FreePatent

# class QuoteAdmin(admin.ModelAdmin):
#     list_display = ('related_link', 'text', )

# Register your models here.
admin.site.register(Quote)
admin.site.register(FreePatent)