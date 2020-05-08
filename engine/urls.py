from django.urls import path

from . import views

urlpatterns = [
    path('', views.start_page, name='start'),

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.create_user, name='register'),

    path('intro/', views.video, {'page': 'intro1'}, name='intro1'),
    path('salute/', views.video, {'page': 'intro2'}, name='intro2'),

    path('laboratory/tv/animals', views.video, {'page': 'tv_animals'}, name='tv_v1'),
    path('laboratory/tv/mutations', views.video, {'page': 'tv_mutations'}, name='tv_v2'),
    path('laboratory/table/video/', views.video, {'page': 'tbl_video'}, name='table_v'),
    path('laboratory/small_table/video/', views.video, {'page': 'small_tbl_video'}, name='small_table_v'),
    path('laboratory/microscope/video/', views.video, {'page': 'microscope_video'}, name='microscope_v'),
    path('laboratory/microscope/video/', views.video, {'page': 'symptoms_video'}, name='table_s'),
    path('laboratory/suites/video/', views.video, {'page': 'suites_video'}, name='suites_v'),
    path('laboratory/suites/picture/', views.quest_suites,  name='suites_p'),

    path('laboratory/suites/', views.picture, {'page': 'suites'}, name='suites'),
    path('laboratory/microscope/', views.picture, {'page': 'microscope'}, name='microscope'),
    path('laboratory/microscope/look', views.picture, {'page': 'microscope_look'}, name='microscope_look'),
    path('laboratory/reagents/', views.picture, {'page': 'reagents'}, name='reagents'),
    path('laboratory/tv/', views.picture, {'page': 'tv'}, name='tv'),
    path('laboratory/table/', views.picture, {'page': 'table'}, name='table'),
    path('laboratory/table/paper/', views.picture, {'page': 'paper'}, name='table_p'),
    path('laboratory/small_table/', views.picture, {'page': 'small_table'}, name='small_table'),


    path('laboratory/small_table/probes', views.puzzle, {'page': 'probes'}, name='probes'),
    path('laboratory/small_table/probes/solve', views.check_answers, {'page': 'probes'}, name='check_answers'),
  
    path('laboratory/microscope/loupe', views.puzzle, {'page': 'microscope'}, name='check_microscope'),
    # path('laboratory/microscope/loupe/solve', views.check_answers, {'page': 'microscope'}, name='check_answers'),

    path('laboratory/', views.room_1, name='laboratory'),
    path('laboratory/table/news/', views.lab_table_news, name='table_n'),
    path('laboratory/table/symptoms/', views.lab_table_symptoms, name='table_s'),


    # path('laboratory/small_table/cell', views.cell_check, name='check_cell'), 
    path('laboratory/small_table/cell/solve', views.cell_check, name='check_cell'), 
    path('laboratory/probes/solve', views.lab_probes_check, name='check_probes'),

    path('laboratory/tv/puzzle/', views.lab_tv_puzzle, name='tv_puzzle'),







    # path('main/', views.main, name='main'),
]
    # path('laboratory2D/', views.room_1_2d, name='laboratory3d'),