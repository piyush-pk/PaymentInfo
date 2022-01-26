# -*- coding: utf-8 -*-
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import PaymentInfo


@admin.register(PaymentInfo)
class PaymentInfoAdmin(ImportExportModelAdmin):
    list_display = ('id', 'username', 'aadhar', 'mobile', 'payment', 'time')
    list_filter = ('time', 'aadhar')
    search_fields = ('aadhar', 'username', 'mobile')
