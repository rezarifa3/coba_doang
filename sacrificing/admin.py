from django.contrib import admin
from sacrificing.models import *

class BukuAdmin(admin.ModelAdmin):
    list_display = ['judul','penulis','penerbit','jumlah']
    search_fields = ['judul','penulis','penerbit']
    list_filter = ('kelompok_id',)
    list_per_page = 4

admin.site.register(Buku, BukuAdmin)
admin.site.register(Kelompok)
