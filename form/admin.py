from django.contrib import admin
from form.models import Btech, BtechTemp, AllowedIP, Login, BtechLE, BtechLETemp, Bba, BbaTemp, Mba, MbaTemp, BankDetails
from import_export.admin import ExportActionMixin
from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.contrib import messages

# For Temporary Btech
class BtechTempAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['jee_rank']         #for adding filter option
    search_fields = ['jee_rank', 'candidate_first_name']         # for adding search option
    readonly_fields = ['photograph_preview']       # non editable field
    list_display = ('id', 'candidate_first_name', 'jee_rank', 'application_id','ip_address','created_at')    # telling which fields to display
    ordering = ['jee_rank']   # allowing to sort by jee rank


# For Btech
class BtechAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['allow_for_counselling', 'allow_editing', 'jee_rank']         #for adding filter option
    search_fields = ['jee_rank', 'candidate_first_name']         # for adding search option
    readonly_fields = ['photograph_preview']       # non editable field
    list_display = ('id','ipu_registration', 'candidate_first_name', 'allow_for_counselling', 'allow_editing', 'jee_rank', 'application_id','ip_address','created_at')    # telling which fields to display
    list_editable = ('allow_for_counselling', 'allow_editing' )   # to allow editing without opening the record
    ordering = ['jee_rank']   # allowing to sort by jee rank

    #for PDF generation
    #We are just rendering the pdfs.html page and passing desired records as context
    #The 'queryset' parameter defines which records are selected by user before pressing the action button
    @admin.action(description='Generate PDF file')
    def generatePDF(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Btech.objects.filter(pk__in = all_ids) #pk is primary key
        # print(btech_records)
        context = {'all_records' : all_records}
        return render(request,'btech/pdfs-btech.html', context)
    
    @admin.action(description='Allow for Counselling')
    def allowCounselling(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Btech.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_for_counselling = True
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were allowed for counselling."
        modeladmin.message_user(request, message, messages.SUCCESS)
    
    @admin.action(description='Do NOT Allow for Counselling')
    def disallowCounselling(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Btech.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_for_counselling = False
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were not allowed for counselling."
        modeladmin.message_user(request, message, messages.SUCCESS)

    @admin.action(description='Allow Editing')
    def allowEditing(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Btech.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_editing = True
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were given editing access."
        modeladmin.message_user(request, message, messages.SUCCESS)
    
    @admin.action(description='Do NOT Allow Editing')
    def disallowEditing(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Btech.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_editing = False
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were denied editing access."
        modeladmin.message_user(request, message, messages.SUCCESS)

    actions = [generatePDF, allowCounselling, disallowCounselling, allowEditing, disallowEditing]  # a list of action buttons in admin panel


# For Temporary BtechLE
class BtechLETempAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['cet_rank']         #for adding filter option
    search_fields = ['cet_rank', 'candidate_first_name']         # for adding search option
    readonly_fields = ['photograph_preview']       # non editable field
    list_display = ('id', 'candidate_first_name', 'cet_rank', 'application_id','ip_address','created_at')    # telling which fields to display
    ordering = ['cet_rank']   # allowing to sort by jee rank


# For BtechLE
class BtechLEAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['allow_for_counselling', 'allow_editing','cet_rank']         #for adding filter option
    search_fields = ['cet_rank', 'candidate_first_name']         # for adding search option
    readonly_fields = ['photograph_preview']       # non editable field
    list_display = ('id', 'ipu_registration', 'candidate_first_name','allow_for_counselling', 'allow_editing', 'cet_rank', 'application_id','ip_address','created_at')    # telling which fields to display
    list_editable = ('allow_for_counselling', 'allow_editing' )   # to allow editing without opening the record
    ordering = ['cet_rank']   # allowing to sort by cet rank

    #for PDF generation
    #We are just rendering the pdfs-btechle.html page and passing desired records as context
    #The 'queryset' parameter defines which records are selected by user before pressing the action button
    @admin.action(description='Generate PDF file')
    def generatePDF(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = BtechLE.objects.filter(pk__in = all_ids) #pk is primary key
        context = {'all_records' : all_records}
        return render(request,'btechle/pdfs-btechle.html', context)
    
    @admin.action(description='Allow for Counselling')
    def allowCounselling(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = BtechLE.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_for_counselling = True
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were allowed for counselling."
        modeladmin.message_user(request, message, messages.SUCCESS)
    
    @admin.action(description='Do NOT Allow for Counselling')
    def disallowCounselling(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = BtechLE.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_for_counselling = False
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were not allowed for counselling."
        modeladmin.message_user(request, message, messages.SUCCESS)

    @admin.action(description='Allow Editing')
    def allowEditing(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = BtechLE.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_editing = True
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were given editing access."
        modeladmin.message_user(request, message, messages.SUCCESS)
    
    @admin.action(description='Do NOT Allow Editing')
    def disallowEditing(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = BtechLE.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_editing = False
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were denied editing access."
        modeladmin.message_user(request, message, messages.SUCCESS)

    actions = [generatePDF, allowCounselling, disallowCounselling, allowEditing, disallowEditing]  # a list of action buttons in admin panel


# For Temporary Bba
class BbaTempAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['cet_or_cuet', 'cet_rank']         #for adding filter option
    search_fields = ['cet_rank', 'candidate_first_name']         # for adding search option
    readonly_fields = ['photograph_preview']       # non editable field
    list_display = ('id', 'candidate_first_name', 'cet_rank', 'application_id','ip_address','created_at')    # telling which fields to display
    ordering = ['cet_rank']   # allowing to sort by cet rank


# For Bba
class BbaAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['allow_for_counselling', 'allow_editing', 'cet_or_cuet','cet_rank']         #for adding filter option
    search_fields = ['cet_rank', 'candidate_first_name']         # for adding search option
    readonly_fields = ['photograph_preview']       # non editable field
    list_display = ('id','ipu_registration', 'candidate_first_name', 'allow_for_counselling', 'allow_editing', 'cet_rank', 'application_id','ip_address','created_at')    # telling which fields to display
    list_editable = ('allow_for_counselling', 'allow_editing' )   # to allow editing without opening the record
    ordering = ['cet_rank']   # allowing to sort by cet rank

    #for PDF generation
    #We are just rendering the pdfs.html page and passing desired records as context
    #The 'queryset' parameter defines which records are selected by user before pressing the action button
    @admin.action(description='Generate PDF file')
    def generatePDF(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bba.objects.filter(pk__in = all_ids) #pk is primary key
        context = {'all_records' : all_records}
        return render(request,'bba/pdfs-bba.html', context)
    
    @admin.action(description='Allow for Counselling')
    def allowCounselling(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bba.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_for_counselling = True
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were allowed for counselling."
        modeladmin.message_user(request, message, messages.SUCCESS)
    
    @admin.action(description='Do NOT Allow for Counselling')
    def disallowCounselling(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bba.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_for_counselling = False
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were not allowed for counselling."
        modeladmin.message_user(request, message, messages.SUCCESS)

    @admin.action(description='Allow Editing')
    def allowEditing(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bba.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_editing = True
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were given editing access."
        modeladmin.message_user(request, message, messages.SUCCESS)
    
    @admin.action(description='Do NOT Allow Editing')
    def disallowEditing(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Bba.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_editing = False
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were denied editing access."
        modeladmin.message_user(request, message, messages.SUCCESS)

    actions = [generatePDF, allowCounselling, disallowCounselling, allowEditing, disallowEditing]  # a list of action buttons in admin panel


# For Temporary Mba
class MbaTempAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['cat_or_cmat', 'cat_or_cmat_rank']         #for adding filter option
    search_fields = ['cat_or_cmat_rank', 'candidate_first_name']         # for adding search option
    readonly_fields = ['photograph_preview']       # non editable field
    list_display = ('id', 'candidate_first_name', 'cat_or_cmat_rank', 'application_id','ip_address','created_at')    # telling which fields to display
    ordering = ['cat_or_cmat_rank']   # allowing to sort by cat rank


# For Mba
class MbaAdmin(ExportActionMixin, admin.ModelAdmin):
    list_filter = ['allow_for_counselling', 'allow_editing','cat_or_cmat', 'cat_or_cmat_rank']         #for adding filter option
    search_fields = ['cat_or_cmat_rank', 'candidate_first_name']         # for adding search option
    readonly_fields = ['photograph_preview']       # non editable field
    list_display = ('id','ipu_registration', 'candidate_first_name', 'allow_for_counselling', 'allow_editing', 'cat_or_cmat_rank', 'cat_or_cmat', 'application_id','ip_address','created_at')    # telling which fields to display
    list_editable = ('allow_for_counselling', 'allow_editing' )   # to allow editing without opening the record
    ordering = ['cat_or_cmat_rank']   # allowing to sort by cat rank

    #for PDF generation
    #We are just rendering the pdfs.html page and passing desired records as context
    #The 'queryset' parameter defines which records are selected by user before pressing the action button
    @admin.action(description='Generate PDF file')
    def generatePDF(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Mba.objects.filter(pk__in = all_ids) #pk is primary key
        context = {'all_records' : all_records}
        return render(request,'mba/pdfs-mba.html', context)
    
    @admin.action(description='Allow for Counselling')
    def allowCounselling(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Mba.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_for_counselling = True
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were allowed for counselling."
        modeladmin.message_user(request, message, messages.SUCCESS)
    
    @admin.action(description='Do NOT Allow for Counselling')
    def disallowCounselling(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Mba.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_for_counselling = False
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were not allowed for counselling."
        modeladmin.message_user(request, message, messages.SUCCESS)

    @admin.action(description='Allow Editing')
    def allowEditing(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Mba.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_editing = True
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were given editing access."
        modeladmin.message_user(request, message, messages.SUCCESS)
    
    @admin.action(description='Do NOT Allow Editing')
    def disallowEditing(modeladmin, request, queryset):
        all_ids = []  # storing ids from the queryset in a list
        for query in queryset:
            all_ids.append(query.id)
        all_records = Mba.objects.filter(pk__in = all_ids) #pk is primary key
        for record in all_records:
            record.allow_editing = False
            record.save()
        count = len(all_records)
        message = f"{count} {'record' if count == 1 else 'records'} were denied editing access."
        modeladmin.message_user(request, message, messages.SUCCESS)

    actions = [generatePDF, allowCounselling, disallowCounselling, allowEditing, disallowEditing]  # a list of action buttons in admin panel


# For Login
class LoginAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('candidate_name','ipu_registration','password', 'candidate_email','course','ip_address','created_at')
    list_filter = ['course']         #for adding filter option
    search_fields = ['ipu_registration',]


# For bank details
class BankDetailsAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('ipu_registration','course', 'account_number','account_holder_name')
    list_filter = ['course']         #for adding filter option


# register method takes at most 2 arguements at a time
admin.site.register(BtechTemp, BtechTempAdmin)
admin.site.register(Btech, BtechAdmin)

admin.site.register(BtechLETemp, BtechLETempAdmin)
admin.site.register(BtechLE, BtechLEAdmin)

admin.site.register(BbaTemp, BbaTempAdmin)
admin.site.register(Bba, BbaAdmin)

admin.site.register(MbaTemp, MbaTempAdmin)
admin.site.register(Mba, MbaAdmin)

admin.site.register(Login, LoginAdmin)

admin.site.register(BankDetails, BankDetailsAdmin)

admin.site.register(AllowedIP)
admin.site.register(Session)


admin.site.site_header = "MAIT Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "MAIT"