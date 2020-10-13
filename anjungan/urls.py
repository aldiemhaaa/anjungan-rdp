
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('pilihdokter/cetaksep/',views.cetakSep),
    path('pilihdokter/',views.pilihDokter),
    path('bpjs/',views.menuBpjs, name='menuBpjs'),
    path('registration/',views.registration),
    # path('rujukan/search/<nomor>/', views.searchRujukan, name='search_rujukan'),
    path('rujukan/search', views.searchRujukan, name='search_rujukan'),
    path('referensi/bpjs/poliklinik/search', views.showPoliBpjs, name='show_poli_bpjs'),
    path('referensi/bpjs/poliklinik/list', views.listPoliBpjs, name='list_poli_bpjs'),
    path('referensi/bpjs/dpjp/rj', views.showDpjpBpjsRj, name='get_dpjp_bpjs_rj'),
    path('referensi/dokter/poli', views.listDokterPoli, name='list_dokter_poli'),
    path('pasien/kontrol', views.checkPasienKontrol, name='check_pasien_kontrol'),
]
