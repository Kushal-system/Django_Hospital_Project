from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.index,name="index"),
    path('login',views.log_in,name="login"),
    path('login_check', views.login_check, name="login_check"),
    path('admin_dashboard', views.admin_dashboard, name="admin_dashboard"),
    path('hospital_head_profile',views.hospital_head_profile,name='hospital_head_profile'),
    path('head_profile',views.head_profile,name='head_profile'),
    path('admin_appointment_list',views.admin_appointment_list,name="admin_appointment_list"),
    path('doctor_register',views.doctor_register,name="doctor_register"),
    path('doc_reg',views.doc_reg,name="doc_reg"),
    path('patient_register', views.patient_register, name="patient_register"),
    path('patient_reg', views.patient_reg, name="patient_reg"),
    path('admin_doctor_list',views.admin_doctor_list,name="admin_doctor_list"),
    path('doctor_dashboard',views.doctor_dashboard,name="doctor_dashboard"),
    # path('doctor_profile_setting',views.doctor_profile_setting,name="doctor_profile_setting"),
    # path('update_doctor_profile',views.update_doctor_profile,name="update_doctor_profile"),
    path('patient_dashboard',views.patient_dashboard,name="patient_dashboard"),
    path('schedule_timing', views.schedule_timing, name="schedule_timing"),
    path('doctor_booking', views.booking, name="doctor_booking"),
    path('search_doctor',views.search_doctor,name="search_doctor"),
    path('select_doctor',views.select_doctor,name="select_doctor"),
    path('book_slot',views.book_slot,name="book_slot"),
    path('reset_password',views.reset_password,name="reset_password"),
    path('logout',views.log_out,name='logout'),
    path('fetch_appointment',views.fetch_appointment,name='fetch_appointment')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
