from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import *
from dal import autocomplete
from .models import *

app_name = 'UJUZI'

urlpatterns = [
    path('', views.index, name="index"),
    path('base/', views.base_view, name="base_view"),
    path('home/', views.home_view, name="home_view"),
    path('course-detail/<course_name>', views.course_detail, name="course_detail"),
    path('course-module/<module_id>', views.module_content, name="module_content"),

    path('user-registration/', views.registration, name='registration'),
    path('guest-registration/', guest_registration, name="guest_registration"),
    path('check-username/', check_username, name="check_username"),
    path('user-profile/<object_pk>', views.user_profile, name="user_profile"),
    path('login/', loginView, name="login"),
    path('guest-login/', LoginViewApi, name="guest_login"),

    path('teaching-request/', views.teaching_request, name="teaching_request"),
    path('change-password/', views.change_password, name="change_password"),

    # path('instructor-home/', views.instructor_home, name='instructor_home'),
    #
    # path('course-verification-list/', views.verifier_home, name='course_verification'),
    # path('staff-verification/', views.verify_staff, name='verify_staff'),
    # path('staff-verification/<staff_code>', views.accept_verification, name='accept_verification'),
    # path('get_course/<id>', views.get_course, name='get_course'),
    #
    # path('instructor-home/<course>', views.course_module, name='course_module'),
    path('course-enrollment/<course_id>', views.course_enrollment, name='course_enrollment'),
    # path('course-details/', views.course_details, name='course_details'),
    # path('detailed_course/<code>', views.detailed_course, name='detailed_course'),
    # path('edit-module/<object_pk>/<course>', views.update_module, name='edit_module'),
    #
    # path('comment/', commentView, name="list_of_comment"),
    #
    # path('save-comment/', saveCommentView, name="save_comment"),
    #
    # path('list-comment/', listComment, name="list_new"),
    #
    # path('browse-courses', views.browseCourseView, name="browse-courses"),
    #
    # path('course_url/<slug:slug>', views.CourseItemView.as_view(), name="course_url"),

    path('enrolled-course/', views.enrolled_course, name='enrolled_course'),
    path('my-courses/', views.my_course, name='my_course'),
    path('course-module-contents/<course_id>', views.course_module_contents, name='course_module_contents'),

    # path('enrollment-course-module/<course_name>', views.course_enrollment_modules, name='course_enrollment_modules'),

    path('content-verification-request/<course>', views.request_verification, name='request_verification'),

    path('course-content-verification/<course>', views.course_content, name='course_contents'),

    path('course-content-verification_reverted/<course>', views.course_contents_reverted,
         name='course_contents_reverted'),

    path('course-content-verification-status/<contents>', views.content_verification, name='content_verification'),

    path('course-content-verification-revert/<contents>', views.content_verification_revert,
         name='content_verification_revert'),

    path('course-content-verification-re-upload/<contents>', views.content_verification_re_upload,
         name='content_verification_re_upload'),

    path('module-content/<course>/<module>', views.module_contents, name='module_content'),
    path('course-module-content/<module_name>', views.get_module_contents, name='get_module_contents'),
    path('edit-module-content/<object_pk>/<course>/<module>', views.update_module_content, name='edit_module_content'),
    path('edit-course/<object_pk>/', views.update_course, name='edit_course'),

    path('test-autocomplete/', autocomplete.Select2QuerySetView.as_view(model=Category), name='select2_fk'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password_reset/', auth_views.PasswordResetView.
         as_view(template_name='password/password_reset.html'), name='password_reset'),

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
