from django.urls import path
from vendor import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('data-vendor', views.dataVendor, name='data'),
    path('summary-data-vendor', views.summaryDataVendor),
    path('ajax/c1', views.dataVendorC1),
    path('ajax/c2', views.dataVendorC2),
    path('ajax/c3', views.dataVendorC3),
    path('ajax/c4', views.dataVendorC4),
    path('ajax/c5', views.dataVendorC5),
    path('ajax/c6', views.dataVendorC6),
    path('ajax/b', views.dataVendorB),
    path('ajax/c7', views.dataVendorC7),
    path('ajax/c8', views.dataVendorC8),
    path('ajax/c91', views.dataVendorC91),
    path('ajax/c92', views.dataVendorC92),
    path('ajax/c93', views.dataVendorC93),
    path('ajax/getkotabypropinsi/<id>', views.jsonGetKotabyPropinsi),
    path('ajax/getpropinsi', views.jsonGetPropinsi),
    path('ajax/getkbli', views.jsonGetKbli),
    path('ajax/getdocuments', views.jsonGetDokumen),
    path('ajax/senddocuments', views.dataVendorD),
    path('ajax/cekpkp', views.jsonCekPkp),
    path('ajax/ceknpwp', views.jsonCekNpwp),
    path('ajax/verifytoadministrator', views.verifyToAdministrator),
    path('ajax/testjson', views.test),
    path('ajax/fakejson', views.fakejson),
]
