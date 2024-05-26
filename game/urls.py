from django.contrib import admin
from django.urls import path, re_path
from game.views import Game, Test_Flitter, compute, Test_If_For
urlpatterns = [
        path('page/<int:number>', Game, name='Game'),#path转换器,number作为参数传入Game函数中去，number可指定类型
        path('playground/', compute, name='PlayGround'),
        path('test_flitter/', Test_Flitter, name="test_flitter"),
        path('test_if_for/', Test_If_For, name="test_if_for"),
        ]

