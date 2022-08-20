from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import *
from dal import autocomplete
from .models import *
from .API import CategoryListApi, UserSignUpApi,UserSignIn

app_name = 'UJUZI'

urlpatterns = [
    path('', views.index, name="index"),
    path('base/', views.base_view, name="base_view"),
    path('home/', views.home_view, name="home_view"),
    path('course-detail/<course_name>', views.course_detail, name="course_detail"),
    path('course-module/<module_id>', views.module_content, name="module_content"),
    path('pdf-view-save/<object_pk>', views.save_pdf_view, name="save_pdf_view"),
    path('letter-view/<letter_id>', views.letter_view, name="letter_view"),

    path('user-registration/', views.registration, name='registration'),
    path('guest-registration/', guest_registration, name="guest_registration"),
    path('check-username/', check_username, name="check_username"),
    path('user-profile/<object_pk>', views.user_profile, name="user_profile"),
    path('login/', loginView, name="login"),
    path('guest-login/', LoginViewApi, name="guest_login"),

    path('teaching-request/', views.teaching_request, name="teaching_request"),
    path('change-password/', views.change_password, name="change_password"),

    path('course-enrollment/<course_id>', views.course_enrollment, name='course_enrollment'),
    path('change-instructor-status/<object_pk>', views.change_instructor_status, name='change_instructor_status'),


    path('enrolled-course/', views.enrolled_course, name='enrolled_course'),
    path('my-courses/', views.my_course, name='my_course'),
    path('course-module-contents/<course_id>', views.course_module_contents, name='course_module_contents'),
    path('delete-module/<module_id>', views.delete_module, name="delete_module"),


    path('teaching-verification/', views.teaching_verification, name='teaching_verification'),
    path('instructor-management/', views.instructor_management, name='instructor_management'),

    path('view-pdf/<letter_id>', views.pdf_view, name='pdf_view'),

    path('accept-request/<request_id>', views.accept_request,name='accept_request'),
    path('deny-request/<request_id>', views.deny_request,name='deny_request'),

    path('course-content-verification-status/<contents>', views.content_verification, name='content_verification'),

    path('course-content-verification-revert/<contents>', views.content_verification_revert,
         name='content_verification_revert'),

    path('course-content-verification-re-upload/<contents>', views.content_verification_re_upload,
         name='content_verification_re_upload'),

    path('module-content/<course>/<module>', views.module_contents, name='module_content'),
    path('course-module-content/<module_name>', views.get_module_contents, name='get_module_contents'),
    path('edit-module-content/<object_pk>/', views.update_module_content, name='update_module_content'),
    path('edit-course/<object_pk>/', views.update_course, name='edit_course'),

    path('test-autocomplete/', autocomplete.Select2QuerySetView.as_view(model=Category), name='select2_fk'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password_reset/', auth_views.PasswordResetView.
         as_view(template_name='password/password_reset.html'), name='password_reset'),

    # APP'S urls
    path("category-list/", CategoryListApi.as_view(), name="category_list"),
    path("user-signup-api/", UserSignUpApi.as_view(), name="user_signup"),
    path("user-signin/", UserSignIn.as_view(), name="user_signin"),
]

# import djhacker
# from django import forms
# djhacker.formfield(
#     Course.category,
#     forms.ModelChoiceField,
#     widget=autocomplete.ModelSelect2(url='select2_djhacker_formfield')
# )

'''
    Password view For reseting password
------------------------------------------
1 - PasswordResetView submit email from user
2 - PasswordResetDoneView email sent successfull
3 - link to password Rest form in email
4 - Password successfully changed
'''
