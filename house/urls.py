from django.conf.urls import url
from house.views import *
from django.urls import path
from house import views

urlpatterns = [
    path('login/', views.Login),
    path('tologin/', views.to_login),
    path('denglu/',views.to_denglu),
    path('index/',views.to_index),
    path('new/',views.to_new),
    path('register/',views.register),
    path('showbypage/', views.show_all_bypage),
    path('findall/', views.find_all),
    path('update_ajax/', views.modify_stu_ajax),
    path('update_sec/',views.modify_stu_ajax_sec),
    path('update_new/',views.modify_stu_ajax_new),
    path('update_rent/',views.modify_stu_ajax_rent),
    path('update_buy/',views.modify_stu_ajax_buy),
    path('drop_ajax/', views.drop_stu_ajax),
    path('drop_sec/',views.drop_sec_ajax),
    path('drop_new/',views.drop_new_ajax),
    path('drop_rent/',views.drop_rent_ajax),
    path('drop_buy/', views.drop_buy_ajax),
    path('buyissue/',views.to_buyissue),
    # path('rentissue/',views.to_rentissue),
    path('rentissue/',views.to_buyinfo),
    path('about/',views.to_aboutus),
    path('quanzi/',views.to_quanzi),
    path('secondhandhouse/',views.to_Secondhandhouse),
    path('unsoldhouse/',views.to_unsoldhouse),
    path('buyhouse/',views.to_buyhouse),
    path('showbypagerent/',views.show_all_bypage_rent),
    path('showbypageecond/', views.show_all_bypage_second),
    path('showbypagenew/', views.show_all_bypage_new),
    path('showbypagequanzi/', views.show_all_bypage_quanzi),
    path('addnew/', views.to_addnew),
    path('addrent/', views.to_addrent),
    path('addsec/', views.to_addsec),
    path('add_tablenew/',views.add_tablenew),
    path('add_tablesec/',views.add_tablesec),
    path('add_tablerent/',views.add_tablerent),
    path('add_tablebuy/',views.add_tablebuy),
    path('test/',views.to_test),

    path('echarts/', views.echarts),
    path('echarts_json/', views.echarts_json),
    path('testadd/', views.testadd),
    path('priceandarea/', views.priceandarea),
    path('rosepie/', views.rosepie),
    path('ring/', views.ring),
    path('barstack/', views.barstack),
    path('multy/', views.multy),
]