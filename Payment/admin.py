# -*- coding: utf-8 -*-
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import PaymentInfo, SimInfo


@admin.register(PaymentInfo)
class PaymentInfoAdmin(ImportExportModelAdmin):
    list_display = ('id', 'username', 'aadhar',
                    'mobile', 'payment', 'type', 'time')
    list_filter = ('time', 'aadhar')
    search_fields = ('aadhar', 'username', 'mobile', 'type')


@admin.register(SimInfo)
class SimInfoAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'mobile', 'address', 'company', 'time')
    list_filter = ('company', 'time',)
    search_fields = ('name', 'mobile', 'company')
