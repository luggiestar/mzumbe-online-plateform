import json

import base64
import decimal
from datetime import datetime

from django.db.models import Sum
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Course, CourseSummary, ContentViewers, TotalContentViewers


@receiver(post_save, sender=User, dispatch_uid='add_first_name_to user')
def create_module(sender, instance, created, **kwargs):
    if created:
        get_name_from_email = instance.email.split("@")[0]

        get_user = instance
        get_user.first_name = get_name_from_email
        get_user.save()


@receiver(post_save, sender=Course, dispatch_uid='create_course_summary')
def create_course_summary(sender, instance, created, **kwargs):
    if created:
        CourseSummary.objects.create(course=instance)


#
@receiver(post_save, sender=ContentViewers, dispatch_uid='count_views')
def count_viewers(sender, instance, created, **kwargs):
    if created:
        today = datetime.today().date()
        get_current_total_views = TotalContentViewers.objects.filter(content=instance.content).first()

        count_views = ContentViewers.objects.filter(date=today).count()
        get_latest_total = get_current_total_views.total + count_views

        get_current_total_views.total = get_latest_total
        get_current_total_views.save()


@receiver(post_save, sender=TotalContentViewers, dispatch_uid='course_summary')
def store_total_views(sender, instance, created, **kwargs):
    if instance:
        get_current_total_views = TotalContentViewers.objects.filter(content__course=instance.content.course).annotate(
            total_views=Sum('total',
                            distinct=True))
        for i in get_current_total_views:

            save_views = CourseSummary.objects.filter(course=instance.content.course).fisrt()
            save_views.views = i.total_views
            save_views.save()

#
#
# @receiver(post_save, sender=Module, dispatch_uid='create_default_views')
# def create_default_views(sender, instance, created, **kwargs):
#     if created:
#         TotalContentViewers.objects.create(content=instance)


#
#
# @receiver(post_save, sender=Content, dispatch_uid='check_amount_of_content_available')
# def create_content(sender, instance, created, **kwargs):
#     if created:
#         check_number_of_content = Content.objects.filter(
#             module=instance.module).count()
#         if check_number_of_content == instance.module.contents:
#             get_module = Module.objects.get(id=instance.module.id)
#             get_module.is_complete = True
#             get_module.save()
#         get_all_module_status = Module.objects.filter(course=instance.module.course, is_complete=False).count()
#         if get_all_module_status < 1:
#             get_course_update = Course.objects.get(id=instance.module.course.id)
#             get_course_update.is_valid = True
#             get_course_update.save()


# @receiver(post_save, sender=Verification, dispatch_uid='check_amount_of_content_approved')
# def save_verification(sender, instance, created, **kwargs):
#     if instance:
#
#         get_course = Verification.objects.filter(content__module__course=instance.content.module.course).count()
#         get_course_verified = Verification.objects.filter(content__module__course=instance.content.module.course,
#                                                           status__code="APP").count()
#         if get_course_verified == get_course:
#             update_course = Course.objects.get(id=instance.content.module.course.id)
#             update_course.is_verified = True
#             update_course.save()

# @receiver(post_save, sender=Withdraw, dispatch_uid='update_balance_after_withdraw')
# def create_withdraw(sender, instance, created, **kwargs):
#     if created:
#         get_latest_balance = InvestmentTracking.objects.filter(
#             investment__account=instance.investment.account).order_by(
#             '-id').first()
#         # print(get_latest_balance.balance)
#
#         save_balance = InvestmentTracking(
#             investment=instance.investment,
#             total_referral=get_latest_balance.total_referral,
#             total_earning=get_latest_balance.total_earning,
#             total_withdraw=get_latest_balance.total_withdraw + instance.amount,
#             balance=get_latest_balance.balance - instance.amount
#         )
#         save_balance.save()
#
#
# @receiver(post_save, sender=InvitationEarning, dispatch_uid='update_balance_after_invitation')
# def create_referral(sender, instance, created, **kwargs):
#     if created:
#         get_latest_balance = InvestmentTracking.objects.filter(
#             investment__account__code=instance.investment.account.invite).order_by(
#             '-id').first()
#         get_user = Investment.objects.filter(account__code=instance.investment.account.invite).order_by('-id').first()
#
#         # print(get_latest_balance.balance)
#
#         save_balance = InvestmentTracking(
#             investment=get_user,
#             total_referral=get_latest_balance.total_referral + instance.amount,
#             total_earning=get_latest_balance.total_earning,
#             total_withdraw=get_latest_balance.total_withdraw,
#
#             balance=get_latest_balance.balance + instance.amount
#         )
#         save_balance.save()


# @receiver(post_save, sender=Account, dispatch_uid='send_sms_to_account_activation')
# def save_activation(sender, instance, **kwargs):
#     if instance.is_activated:
#         detail = instance
#         URL = 'https://apisms.beem.africa/v1/send'
#         api_key = '2799f1a807695012'
#         secret_key = 'YTU2NTkxZjQxZDc4NTY2NGZiZTVkYzI5ZWU1MzFmYzM4NzA4MTBkYjk5NWE4MzZmZmU0MjQ2OTU3YjJjN2IxZg===='
#         content_type = 'application/json'
#         source_addr = 'EHGETS'
#         apikey_and_apisecret = api_key + ':' + secret_key
#
#         # data = []
#
#         # user_detail = Investment.objects.filter(is_active=True, is_sent=False)
#
#         # if user_detail:
#         #     for i in user_detail:
#         '''Get name and concatenate them'''
#         first_name = detail.user.first_name
#         last_name = detail.user.last_name
#         full_name = f"{first_name} {last_name}"
#
#         # congaturation = f"Dear {full_name} your withdraw of "
#
#         '''Get amount invested and daily amount earning'''
#
#         '''Get phone detail and convert and user id as recipient_id on api'''
#         phone = str(detail.user.phone)
#         phone = phone[1:10]
#         phone = '255' + phone
#
#         user_id = detail.user.id
#
#         message_body = f"Congratulation, Dear {full_name} your Gramoney Account has been Activated Successfully, you can make investment today to start earning \n\n Gramoney Inv Team"
#
#         print(message_body)
#         first_request = requests.post(url=URL, data=json.dumps({
#             'source_addr': source_addr,
#             'schedule_time': '',
#             'encoding': '0',
#             'message': message_body,
#             'recipients': [
#                 {
#                     'recipient_id': user_id,
#                     'dest_addr': phone,
#                 },
#             ],
#         }),
#
#                                       headers={
#                                           'Content-Type': content_type,
#                                           'Authorization': 'Basic ' + api_key + ':' + secret_key,
#                                       },
#
#                                       auth=(api_key, secret_key), verify=False)
#
#         print(first_request.status_code)
#         if first_request.status_code == 200:
#             full_name = ''
#             phone = ''
#         print(first_request.json())
#
#         return (first_request.json())
