from django.db import models
from . import utils  # utils.py file
from django.utils.html import mark_safe
    


#Login Credentials Model
class Login(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    ipu_registration = models.PositiveBigIntegerField(unique=True)   
    password = models.CharField(max_length=25)
    candidate_name = models.CharField(max_length=100)
    candidate_email = models.EmailField(max_length=100, unique=False)
    candidate_mobile = models.PositiveBigIntegerField(unique=False)
    course = models.CharField(max_length=100, blank=True)     
    ip_address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Login"    #so that Django doesnt add the default 's' for plural in table name
        db_table = "login"


# Allowed IP addresses
class AllowedIP(models.Model):
    ip_address = models.CharField(max_length=100)

    def __str__(self):         # for showing record by ip in admin panel
        return (self.ip_address)
    class Meta:
        verbose_name_plural = "Allowed IP Addresses"    #so that Django doesnt add the default 's' for plural in table name
        db_table = "allowed_ip_addresses"




# Btech Temporary Records Model:
class BtechTemp(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    #GGSIPU registration no.
    ipu_registration = models.PositiveBigIntegerField(blank=True, unique=True)
    #candidate details
    candidate_first_name = models.CharField(max_length=100, blank=True)
    candidate_middle_name = models.CharField(max_length=100, blank=True)
    candidate_last_name = models.CharField(max_length=100, blank=True)
    #other candidate details
    dob = models.DateField()
    complete_address = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=False)
    candidate_number = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    #father mother details
    father_first_name = models.CharField(max_length=100, blank=True)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_last_name = models.CharField(max_length=100, blank=True)
    mother_first_name = models.CharField(max_length=100, blank=True)
    mother_middle_name = models.CharField(max_length=100, blank=True)
    mother_last_name = models.CharField(max_length=100, blank=True)
    father_qualification = models.CharField(max_length=100, blank=True)
    mother_qualification = models.CharField(max_length=100, blank=True)
    father_job = models.CharField(max_length=100, blank=True)
    mother_job = models.CharField(max_length=100, blank=True)
    father_job_designation = models.CharField(max_length=100, blank=True)
    mother_job_designation = models.CharField(max_length=100, blank=True)
    father_business_type = models.CharField(max_length=100, blank=True)
    mother_business_type = models.CharField(max_length=100, blank=True)
    father_number = models.CharField(max_length=100, blank=True)
    mother_number = models.CharField(max_length=100, blank=True)
    father_office_address = models.CharField(max_length=100, blank=True)
    mother_office_address = models.CharField(max_length=100, blank=True)
    #guardian details
    guardian_name = models.CharField(max_length=75, blank=True)
    #12th class details
    board_12th = models.CharField(max_length=255, blank=True)
    year_of_12th = models.PositiveIntegerField(blank=True, null=True)
    rollno_12th = models.PositiveBigIntegerField(blank=True, null=True)
    school_12th = models.CharField(max_length=255, blank=True)
    aggregate_12th = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    maths_12th = models.PositiveIntegerField(blank=True, null=True)
    physics_12th = models.PositiveIntegerField(blank=True, null=True)
    chemistry_12th = models.PositiveIntegerField(blank=True, null=True)
    english_12th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_12th = models.CharField(max_length=100, blank=True)     # because integer field was giving error even with null=True and Blank=True
    other_subject_2_12th =  models.CharField(max_length=100, blank=True)
    #10th class details
    board_10th = models.CharField(max_length=255, blank=True)
    year_of_10th = models.PositiveIntegerField(blank=True, null=True)
    rollno_10th = models.PositiveBigIntegerField(blank=True, null=True)
    school_10th = models.CharField(max_length=255, blank=True)
    aggregate_10th = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    maths_10th = models.PositiveIntegerField(blank=True, null=True)
    science_10th = models.PositiveIntegerField(blank=True, null=True)
    english_10th = models.PositiveIntegerField(blank=True, null=True)
    sst_10th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_10th = models.CharField(max_length=100, blank=True)   # because integer field was giving error even with null=True and Blank=True
    other_subject_2_10th =  models.CharField(max_length=100, blank=True)
    #JEE details
    jee_rank = models.PositiveIntegerField(blank=True, null=True)
    jee_percentile = models.DecimalField(max_digits=15, decimal_places=11, null=True)
    jee_rollno = models.CharField(max_length=100, blank=True)
    #special acheivements
    special_achievements = models.CharField(max_length=255, blank=True)
    #preference list
    preference1 = models.CharField(max_length=125, blank=True)
    preference2 = models.CharField(max_length=125, blank=True)
    preference3 = models.CharField(max_length=125, blank=True)
    preference4 = models.CharField(max_length=125, blank=True)
    preference5 = models.CharField(max_length=125, blank=True)
    preference6 = models.CharField(max_length=125, blank=True)
    preference7 = models.CharField(max_length=125, blank=True)
    preference8 = models.CharField(max_length=125, blank=True)
    preference9 = models.CharField(max_length=125, blank=True)
    preference10 = models.CharField(max_length=125, blank=True)
    preference11 = models.CharField(max_length=125, blank=True)
    preference12 = models.CharField(max_length=125, blank=True)
    preference13 = models.CharField(max_length=125, blank=True)
    #images and files
    passport_photo = models.ImageField(upload_to=utils.btech_photo_rename, blank=True)
    jee_result = models.FileField(upload_to=utils.btech_jeeresult_rename, blank=True)
    marksheet_10th = models.FileField(upload_to=utils.btech_10thmarksheet_rename, blank=True)
    marksheet_12th = models.FileField(upload_to=utils.btech_12thmarksheet_rename, blank=True)
    aadhaar = models.FileField(upload_to=utils.btech_aadhar_rename, blank=True)
    pancard = models.FileField(upload_to=utils.btech_pancard_rename, blank=True)
    ipuregistrationproof = models.FileField(upload_to=utils.btech_ipuregistration_rename, blank=True)
    # Transaction Details
    transaction_id = models.CharField(max_length=255, blank=True)
    transaction_proof = models.FileField(upload_to=utils.btech_transaction_rename, blank=True)
    # Counselling Fee Details
    counselling_transaction_id = models.CharField(max_length=255, blank=True)
    counselling_transaction_proof = models.FileField(upload_to=utils.btech_counselling_transaction_rename, blank=True)
    # To track IP address and other information of users
    ip_address = models.CharField(max_length=100, blank=True)
    forwarded_address = models.CharField(max_length=255, blank=True)
    browser_info = models.CharField(max_length=1000, blank=True)
    created_at = models.CharField(max_length=255, blank=True)

    def __str__(self):         # for showing record by name in admin panel
        return (self.candidate_first_name+' '+self.candidate_last_name)

    def photograph_preview(self):   #for previewing photo in admin panel
        return mark_safe(f'<img src = "{self.passport_photo.url}" width = "100"/>')

    class Meta:
        verbose_name_plural = "B. Tech Temporary"    # to show table by this name in admin panel
        db_table = "btech_temp"             # to use the name "Btech_Temp" instead of "form_btech" in db 


# Btech Model:
class Btech(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    #GGSIPU registration no.
    ipu_registration = models.PositiveBigIntegerField(blank=True, unique=True)
    # allowed for counselling
    allow_for_counselling = models.BooleanField(default=False)
    # allow for editing of record
    allow_editing = models.BooleanField(default=False)
    #candidate details
    candidate_first_name = models.CharField(max_length=100, blank=True)
    candidate_middle_name = models.CharField(max_length=100, blank=True)
    candidate_last_name = models.CharField(max_length=100, blank=True)
    #other candidate details
    dob = models.DateField()
    complete_address = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=False)
    candidate_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    #father mother details
    father_first_name = models.CharField(max_length=100, blank=True)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_last_name = models.CharField(max_length=100, blank=True)
    mother_first_name = models.CharField(max_length=100, blank=True)
    mother_middle_name = models.CharField(max_length=100, blank=True)
    mother_last_name = models.CharField(max_length=100, blank=True)
    father_qualification = models.CharField(max_length=100, blank=True)
    mother_qualification = models.CharField(max_length=100, blank=True)
    father_job = models.CharField(max_length=100, blank=True)
    mother_job = models.CharField(max_length=100, blank=True)
    father_job_designation = models.CharField(max_length=100, blank=True)
    mother_job_designation = models.CharField(max_length=100, blank=True)
    father_business_type = models.CharField(max_length=100, blank=True)
    mother_business_type = models.CharField(max_length=100, blank=True)
    father_number = models.CharField(max_length=100, blank=True)
    mother_number = models.CharField(max_length=100, blank=True)
    father_office_address = models.CharField(max_length=100, blank=True)
    mother_office_address = models.CharField(max_length=100, blank=True)
    #guardian details
    guardian_name = models.CharField(max_length=75, blank=True)
    #12th class details
    board_12th = models.CharField(max_length=255, blank=True)
    year_of_12th = models.PositiveIntegerField(blank=True)
    rollno_12th = models.PositiveBigIntegerField(blank=True)
    school_12th = models.CharField(max_length=255, blank=True)
    aggregate_12th = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    maths_12th = models.PositiveIntegerField(blank=True)
    physics_12th = models.PositiveIntegerField(blank=True)
    chemistry_12th = models.PositiveIntegerField(blank=True)
    english_12th = models.PositiveIntegerField(blank=True)
    other_subject_12th = models.CharField(max_length=100, blank=True)     # because integer field was giving error even with null=True and Blank=True
    other_subject_2_12th =  models.CharField(max_length=100, blank=True)
    #10th class details
    board_10th = models.CharField(max_length=255, blank=True)
    year_of_10th = models.PositiveIntegerField(blank=True)
    rollno_10th = models.PositiveBigIntegerField(blank=True)
    school_10th = models.CharField(max_length=255, blank=True)
    aggregate_10th = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    maths_10th = models.PositiveIntegerField(blank=True)
    science_10th = models.PositiveIntegerField(blank=True)
    english_10th = models.PositiveIntegerField(blank=True)
    sst_10th = models.PositiveIntegerField(blank=True)
    other_subject_10th = models.CharField(max_length=100, blank=True)   # because integer field was giving error even with null=True and Blank=True
    other_subject_2_10th =  models.CharField(max_length=100, blank=True)
    #JEE details
    jee_rank = models.PositiveIntegerField(blank=True)
    jee_percentile = models.DecimalField(max_digits=15, decimal_places=11)
    jee_rollno = models.CharField(max_length=100, blank=True)
    #special acheivements
    special_achievements = models.CharField(max_length=255, blank=True)
    #preference list
    preference1 = models.CharField(max_length=125, blank=True)
    preference2 = models.CharField(max_length=125, blank=True)
    preference3 = models.CharField(max_length=125, blank=True)
    preference4 = models.CharField(max_length=125, blank=True)
    preference5 = models.CharField(max_length=125, blank=True)
    preference6 = models.CharField(max_length=125, blank=True)
    preference7 = models.CharField(max_length=125, blank=True)
    preference8 = models.CharField(max_length=125, blank=True)
    preference9 = models.CharField(max_length=125, blank=True)
    preference10 = models.CharField(max_length=125, blank=True)
    preference11 = models.CharField(max_length=125, blank=True)
    preference12 = models.CharField(max_length=125, blank=True)
    preference13 = models.CharField(max_length=125, blank=True)
    #images and files
    passport_photo = models.ImageField(upload_to=utils.btech_photo_rename, blank=True)
    jee_result = models.FileField(upload_to=utils.btech_jeeresult_rename, blank=True)
    marksheet_10th = models.FileField(upload_to=utils.btech_10thmarksheet_rename, blank=True)
    marksheet_12th = models.FileField(upload_to=utils.btech_12thmarksheet_rename, blank=True)
    aadhaar = models.FileField(upload_to=utils.btech_aadhar_rename, blank=True)
    pancard = models.FileField(upload_to=utils.btech_pancard_rename, blank=True)
    ipuregistrationproof = models.FileField(upload_to=utils.btech_ipuregistration_rename, blank=True)
    # Transaction Details
    transaction_id = models.CharField(max_length=255, blank=True)
    transaction_proof = models.FileField(upload_to=utils.btech_transaction_rename, blank=True)
    # Counselling Fee Details
    counselling_transaction_id = models.CharField(max_length=255, blank=True)
    counselling_transaction_proof = models.FileField(upload_to=utils.btech_counselling_transaction_rename, blank=True)
    # To track IP address and other information of users
    ip_address = models.CharField(max_length=100, blank=True)
    forwarded_address = models.CharField(max_length=255, blank=True)
    browser_info = models.CharField(max_length=1000, blank=True)
    created_at = models.CharField(max_length=255, blank=True)

    def __str__(self):         # for showing record by name in admin panel
        return (self.candidate_first_name+' '+self.candidate_last_name)

    def photograph_preview(self):   #for previewing photo in admin panel
        return mark_safe(f'<img src = "{self.passport_photo.url}" width = "100"/>')

    class Meta:
        verbose_name_plural = "B. Tech"    # to show table by this name in admin panel
        db_table = "btech"             # to use the name "Btech" instead of "form_btech" in db




# BtechLE Temporary Records Model:
class BtechLETemp(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    #GGSIPU registration no.
    ipu_registration = models.PositiveBigIntegerField(blank=True, unique=True)
    #candidate details
    candidate_first_name = models.CharField(max_length=100, blank=True)
    candidate_middle_name = models.CharField(max_length=100, blank=True)
    candidate_last_name = models.CharField(max_length=100, blank=True)
    #other candidate details
    dob = models.DateField()
    complete_address = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=False)
    candidate_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    #father mother details
    father_first_name = models.CharField(max_length=100, blank=True)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_last_name = models.CharField(max_length=100, blank=True)
    mother_first_name = models.CharField(max_length=100, blank=True)
    mother_middle_name = models.CharField(max_length=100, blank=True)
    mother_last_name = models.CharField(max_length=100, blank=True)
    father_qualification = models.CharField(max_length=100, blank=True)
    mother_qualification = models.CharField(max_length=100, blank=True)
    father_job = models.CharField(max_length=100, blank=True)
    mother_job = models.CharField(max_length=100, blank=True)
    father_job_designation = models.CharField(max_length=100, blank=True)
    mother_job_designation = models.CharField(max_length=100, blank=True)
    father_business_type = models.CharField(max_length=100, blank=True)
    mother_business_type = models.CharField(max_length=100, blank=True)
    father_number = models.CharField(max_length=100, blank=True)
    mother_number = models.CharField(max_length=100, blank=True)
    father_office_address = models.CharField(max_length=100, blank=True)
    mother_office_address = models.CharField(max_length=100, blank=True)
    #guardian details
    guardian_name = models.CharField(max_length=75, blank=True)
    #12th class details
    board_12th = models.CharField(max_length=75, blank=True)
    year_of_12th = models.CharField(max_length=75, blank=True)
    rollno_12th = models.CharField(max_length=75, blank=True)
    school_12th = models.CharField(max_length=125, blank=True)
    aggregate_12th = models.CharField(max_length=75, blank=True)
    maths_12th = models.CharField(max_length=75, blank=True)
    physics_12th = models.CharField(max_length=75, blank=True)
    chemistry_12th = models.CharField(max_length=75, blank=True)
    english_12th = models.CharField(max_length=75, blank=True)
    other_subject_12th = models.CharField(max_length=10, blank=True)     # because integer field was giving error even with null=True and Blank=True
    other_subject_2_12th =  models.CharField(max_length=10, blank=True)
    #10th class details
    board_10th = models.CharField(max_length=100, blank=True)
    year_of_10th = models.PositiveIntegerField(blank=True, null=True)
    rollno_10th = models.PositiveBigIntegerField(blank=True, null=True)
    school_10th = models.CharField(max_length=255, blank=True)
    aggregate_10th = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    maths_10th = models.PositiveIntegerField(blank=True, null=True)
    science_10th = models.PositiveIntegerField(blank=True, null=True)
    english_10th = models.PositiveIntegerField(blank=True, null=True)
    sst_10th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_10th = models.CharField(max_length=100, blank=True)   # because integer field was giving error even with null=True and Blank=True
    other_subject_2_10th =  models.CharField(max_length=100, blank=True)
    #Diploma Fields
    diploma_bsc_type = models.CharField(max_length=75, blank=True, null=True)
    board_diploma_bsc = models.CharField(max_length=75, blank=True, null=True)
    year_of_diploma_bsc = models.CharField(max_length=75, blank=True, null=True)
    rollno_diploma_bsc = models.CharField(max_length=75, blank=True, null=True)
    school_diploma_bsc = models.CharField(max_length=125, blank=True, null=True)
    aggregate_diploma_bsc = models.CharField(max_length=75, blank=True, null=True)
    ug_degree = models.FileField(upload_to=utils.btechle_ug_degree_rename, blank=True)
    #CET IPU details
    cet_rank = models.PositiveIntegerField(blank=True, null=True)
    cet_rollno = models.CharField(max_length=20)
    #special acheivements
    special_achievements = models.CharField(max_length=255, blank=True)
    #preference list
    preference1 = models.CharField(max_length=100, blank=True)
    preference2 = models.CharField(max_length=100, blank=True)
    preference3 = models.CharField(max_length=100, blank=True)
    preference4 = models.CharField(max_length=100, blank=True)
    preference5 = models.CharField(max_length=100, blank=True)
    preference6 = models.CharField(max_length=100, blank=True)
    preference7 = models.CharField(max_length=100, blank=True)
    preference8 = models.CharField(max_length=100, blank=True)
    preference9 = models.CharField(max_length=100, blank=True)
    preference10 = models.CharField(max_length=100, blank=True)
    preference11 = models.CharField(max_length=100, blank=True)
    preference12 = models.CharField(max_length=100, blank=True)
    preference13 = models.CharField(max_length=100, blank=True)
    #images and files
    passport_photo = models.ImageField(upload_to=utils.btech_le_photo_rename, blank=True)
    cet_result = models.FileField(upload_to=utils.btech_le_cetresult_rename, blank=True)
    diploma_result = models.FileField(upload_to=utils.btech_le_diplomaresult_rename, blank=True)
    marksheet_10th = models.FileField(upload_to=utils.btech_le_10thmarksheet_rename, blank=True)
    marksheet_12th = models.FileField(upload_to=utils.btech_le_12thmarksheet_rename, blank=True)
    aadhaar = models.FileField(upload_to=utils.btech_le_aadhar_rename, blank=True)
    pancard = models.FileField(upload_to=utils.btech_le_pancard_rename, blank=True)
    ipuregistrationproof = models.FileField(upload_to=utils.btech_le_ipuregistration_rename, blank=True)
    # Transaction Details
    transaction_id = models.CharField(max_length=255, blank=True)
    transaction_proof = models.FileField(upload_to=utils.btech_le_transaction_rename, blank=True)
    # Counselling Fee Details
    counselling_transaction_id = models.CharField(max_length=255, blank=True)
    counselling_transaction_proof = models.FileField(upload_to=utils.btech_counselling_transaction_rename, blank=True)
    # To track IP address and other information of users
    ip_address = models.CharField(max_length=100, blank=True)
    forwarded_address = models.CharField(max_length=255, blank=True)
    browser_info = models.CharField(max_length=1000, blank=True)
    created_at = models.CharField(max_length=255, blank=True)

    def __str__(self):         # for showing record by name in admin panel
        return (self.candidate_first_name+' '+self.candidate_last_name)

    def photograph_preview(self):   #for previewing photo in admin panel
        return mark_safe(f'<img src = "{self.passport_photo.url}" width = "100"/>')

    class Meta:
        verbose_name_plural = "B. Tech LE Temporary"    # to show table by this name in admin panel
        db_table = "btech_le_temp"             # to use the name "Btech_Temp" instead of "form_btech" in db 


# BtechLE Model:
class BtechLE(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    #GGSIPU registration no.
    ipu_registration = models.PositiveBigIntegerField(blank=True, unique=True)
    # allowed for counselling
    allow_for_counselling = models.BooleanField(default=False)
    # allow for editing of record
    allow_editing = models.BooleanField(default=False)
    #candidate details
    candidate_first_name = models.CharField(max_length=100, blank=True)
    candidate_middle_name = models.CharField(max_length=100, blank=True)
    candidate_last_name = models.CharField(max_length=100, blank=True)
    #other candidate details
    dob = models.DateField()
    complete_address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=False)
    candidate_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=255, blank=True)
    #father mother details
    father_first_name = models.CharField(max_length=100, blank=True)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_last_name = models.CharField(max_length=100, blank=True)
    mother_first_name = models.CharField(max_length=100, blank=True)
    mother_middle_name = models.CharField(max_length=100, blank=True)
    mother_last_name = models.CharField(max_length=100, blank=True)
    father_qualification = models.CharField(max_length=100, blank=True)
    mother_qualification = models.CharField(max_length=100, blank=True)
    father_job = models.CharField(max_length=100, blank=True)
    mother_job = models.CharField(max_length=100, blank=True)
    father_job_designation = models.CharField(max_length=100, blank=True)
    mother_job_designation = models.CharField(max_length=100, blank=True)
    father_business_type = models.CharField(max_length=100, blank=True)
    mother_business_type = models.CharField(max_length=100, blank=True)
    father_number = models.CharField(max_length=100, blank=True)
    mother_number = models.CharField(max_length=100, blank=True)
    father_office_address = models.CharField(max_length=100, blank=True)
    mother_office_address = models.CharField(max_length=100, blank=True)
    #guardian details
    guardian_name = models.CharField(max_length=75, blank=True)
    #12th class details
    board_12th = models.CharField(max_length=75, blank=True)
    year_of_12th = models.CharField(max_length=75, blank=True)
    rollno_12th = models.CharField(max_length=75, blank=True)
    school_12th = models.CharField(max_length=125, blank=True)
    aggregate_12th = models.CharField(max_length=75, blank=True)
    maths_12th = models.CharField(max_length=75, blank=True)
    physics_12th = models.CharField(max_length=75, blank=True)
    chemistry_12th = models.CharField(max_length=75, blank=True)
    english_12th = models.CharField(max_length=75, blank=True)
    other_subject_12th = models.CharField(max_length=10, blank=True)     # because integer field was giving error even with null=True and Blank=True
    other_subject_2_12th =  models.CharField(max_length=10, blank=True)
    #10th class details
    board_10th = models.CharField(max_length=255, blank=True)
    year_of_10th = models.PositiveIntegerField(blank=True)
    rollno_10th = models.PositiveBigIntegerField(blank=True)
    school_10th = models.CharField(max_length=255, blank=True)
    aggregate_10th = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    maths_10th = models.PositiveIntegerField(blank=True)
    science_10th = models.PositiveIntegerField(blank=True)
    english_10th = models.PositiveIntegerField(blank=True)
    sst_10th = models.PositiveIntegerField(blank=True)
    other_subject_10th = models.CharField(max_length=100, blank=True)   # because integer field was giving error even with null=True and Blank=True
    other_subject_2_10th =  models.CharField(max_length=100, blank=True)
    #Diploma Fields
    diploma_bsc_type = models.CharField(max_length=75, blank=True, null=True)
    board_diploma_bsc = models.CharField(max_length=75, blank=True, null=True)
    year_of_diploma_bsc = models.CharField(max_length=75, blank=True, null=True)
    rollno_diploma_bsc = models.CharField(max_length=75, blank=True, null=True)
    school_diploma_bsc = models.CharField(max_length=125, blank=True, null=True)
    aggregate_diploma_bsc = models.CharField(max_length=75, blank=True, null=True)
    ug_degree = models.FileField(upload_to=utils.btechle_ug_degree_rename, blank=True)
    #CET IPU details
    cet_rank = models.PositiveIntegerField(null=True, blank=True)
    cet_rollno = models.CharField(max_length=20)
    #special acheivements
    special_achievements = models.CharField(max_length=255, blank=True)
    #preference list
    preference1 = models.CharField(max_length=100, blank=True)
    preference2 = models.CharField(max_length=100, blank=True)
    preference3 = models.CharField(max_length=100, blank=True)
    preference4 = models.CharField(max_length=100, blank=True)
    preference5 = models.CharField(max_length=100, blank=True)
    preference6 = models.CharField(max_length=100, blank=True)
    preference7 = models.CharField(max_length=100, blank=True)
    preference8 = models.CharField(max_length=100, blank=True)
    preference9 = models.CharField(max_length=100, blank=True)
    preference10 = models.CharField(max_length=100, blank=True)
    preference11 = models.CharField(max_length=100, blank=True)
    preference12 = models.CharField(max_length=100, blank=True)
    preference13 = models.CharField(max_length=100, blank=True)
    #images and files
    passport_photo = models.ImageField(upload_to=utils.btech_le_photo_rename, blank=True)
    cet_result = models.FileField(upload_to=utils.btech_le_cetresult_rename, blank=True)
    diploma_result = models.FileField(upload_to=utils.btech_le_diplomaresult_rename, blank=True)
    marksheet_10th = models.FileField(upload_to=utils.btech_le_10thmarksheet_rename, blank=True)
    marksheet_12th = models.FileField(upload_to=utils.btech_le_12thmarksheet_rename, blank=True)
    aadhaar = models.FileField(upload_to=utils.btech_le_aadhar_rename, blank=True)
    pancard = models.FileField(upload_to=utils.btech_le_pancard_rename, blank=True)
    ipuregistrationproof = models.FileField(upload_to=utils.btech_le_ipuregistration_rename, blank=True)
    # Transaction Details
    transaction_id = models.CharField(max_length=255, blank=True)
    transaction_proof = models.FileField(upload_to=utils.btech_le_transaction_rename, blank=True)
    # Counselling Fee Details
    counselling_transaction_id = models.CharField(max_length=255, blank=True)
    counselling_transaction_proof = models.FileField(upload_to=utils.btechle_counselling_transaction_rename, blank=True)
    # To track IP address and other information of users
    ip_address = models.CharField(max_length=100, blank=True)
    forwarded_address = models.CharField(max_length=255, blank=True)
    browser_info = models.CharField(max_length=1000, blank=True)
    created_at = models.CharField(max_length=255, blank=True)

    def __str__(self):         # for showing record by name in admin panel
        return (self.candidate_first_name+' '+self.candidate_last_name)

    def photograph_preview(self):   #for previewing photo in admin panel
        return mark_safe(f'<img src = "{self.passport_photo.url}" width = "100"/>')

    class Meta:
        verbose_name_plural = "B. Tech LE"    # to show table by this name in admin panel
        db_table = "btechle"             # to use the name "Btech" instead of "form_btech" in db





# BBA Temporary Records Model:
class BbaTemp(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    #GGSIPU registration no.
    ipu_registration = models.PositiveBigIntegerField(blank=True, unique=True)
    #candidate details
    candidate_first_name = models.CharField(max_length=100, blank=True)
    candidate_middle_name = models.CharField(max_length=100, blank=True)
    candidate_last_name = models.CharField(max_length=100, blank=True)
    #other candidate details
    dob = models.DateField()
    complete_address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=False)
    candidate_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    #father mother details
    father_first_name = models.CharField(max_length=100, blank=True)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_last_name = models.CharField(max_length=100, blank=True)
    mother_first_name = models.CharField(max_length=100, blank=True)
    mother_middle_name = models.CharField(max_length=100, blank=True)
    mother_last_name = models.CharField(max_length=100, blank=True)
    father_qualification = models.CharField(max_length=100, blank=True)
    mother_qualification = models.CharField(max_length=100, blank=True)
    father_job = models.CharField(max_length=100, blank=True)
    mother_job = models.CharField(max_length=100, blank=True)
    father_job_designation = models.CharField(max_length=100, blank=True)
    mother_job_designation = models.CharField(max_length=100, blank=True)
    father_business_type = models.CharField(max_length=100, blank=True)
    mother_business_type = models.CharField(max_length=100, blank=True)
    father_number = models.CharField(max_length=100, blank=True)
    mother_number = models.CharField(max_length=100, blank=True)
    father_office_address = models.CharField(max_length=100, blank=True)
    mother_office_address = models.CharField(max_length=100, blank=True)
    #guardian details
    guardian_name = models.CharField(max_length=75, blank=True)
    #12th class details
    board_12th = models.CharField(max_length=255, blank=True)
    year_of_12th = models.PositiveIntegerField(blank=True, null=True)
    rollno_12th = models.PositiveBigIntegerField(blank=True, null=True)
    school_12th = models.CharField(max_length=255, blank=True)
    aggregate_12th = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    first_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    second_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    third_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    fourth_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_12th = models.CharField(max_length=10, blank=True)     # because integer field was giving error even with null=True and Blank=True
    other_subject_2_12th =  models.CharField(max_length=10, blank=True)
    #10th class details
    board_10th = models.CharField(max_length=255, blank=True)
    year_of_10th = models.PositiveIntegerField(blank=True, null=True)
    rollno_10th = models.PositiveBigIntegerField(blank=True, null=True)
    school_10th = models.CharField(max_length=255, blank=True)
    aggregate_10th = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    maths_10th = models.PositiveIntegerField(blank=True, null=True)
    science_10th = models.PositiveIntegerField(blank=True, null=True)
    english_10th = models.PositiveIntegerField(blank=True, null=True)
    sst_10th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_10th = models.CharField(max_length=100, blank=True)   # because integer field was giving error even with null=True and Blank=True
    other_subject_2_10th =  models.CharField(max_length=100, blank=True)
    #CET details
    cet_or_cuet = models.CharField(max_length=10)    # to ask user which paper did he/she appear for
    cet_rank = models.PositiveIntegerField(blank=True, null=True)
    cet_rollno = models.CharField(max_length=100, blank=True)
    #special acheivements
    special_achievements = models.CharField(max_length=255, blank=True)
    #images and files
    passport_photo = models.ImageField(upload_to=utils.bba_photo_rename, blank=True)
    cet_result = models.FileField(upload_to=utils.bba_cetresult_rename, blank=True)
    marksheet_10th = models.FileField(upload_to=utils.bba_10thmarksheet_rename, blank=True)
    marksheet_12th = models.FileField(upload_to=utils.bba_12thmarksheet_rename, blank=True)
    aadhaar = models.FileField(upload_to=utils.bba_aadhar_rename, blank=True)
    pancard = models.FileField(upload_to=utils.bba_pancard_rename, blank=True)
    ipuregistrationproof = models.FileField(upload_to=utils.bba_ipuregistration_rename, blank=True)
    # Transaction Details
    transaction_id = models.CharField(max_length=255, blank=True)
    transaction_proof = models.FileField(upload_to=utils.bba_transaction_rename, blank=True)
    # Counselling Fee Details
    counselling_transaction_id = models.CharField(max_length=255, blank=True)
    counselling_transaction_proof = models.FileField(upload_to=utils.bba_counselling_transaction_rename, blank=True)
    # To track IP address and other information of users
    ip_address = models.CharField(max_length=100, blank=True)
    forwarded_address = models.CharField(max_length=255, blank=True)
    browser_info = models.CharField(max_length=1000, blank=True)
    created_at = models.CharField(max_length=255, blank=True)

    def __str__(self):         # for showing record by name in admin panel
        return (self.candidate_first_name+' '+self.candidate_last_name)

    def photograph_preview(self):   #for previewing photo in admin panel
        return mark_safe(f'<img src = "{self.passport_photo.url}" width = "100"/>')

    class Meta:
        verbose_name_plural = "BBA Temporary"    # to show table by this name in admin panel
        db_table = "bba_temp"             # to use the name "bba" instead of "form_bba" in db 


# bba Model:
class Bba(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    #GGSIPU registration no.
    ipu_registration = models.PositiveBigIntegerField(blank=True, unique=True)
    # allowed for counselling
    allow_for_counselling = models.BooleanField(default=False)
    # allow for editing of record
    allow_editing = models.BooleanField(default=False)
    #candidate details
    candidate_first_name = models.CharField(max_length=100, blank=True)
    candidate_middle_name = models.CharField(max_length=100, blank=True)
    candidate_last_name = models.CharField(max_length=100, blank=True)
    #other candidate details
    dob = models.DateField()
    complete_address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=False)
    candidate_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    #father mother details
    father_first_name = models.CharField(max_length=100, blank=True)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_last_name = models.CharField(max_length=100, blank=True)
    mother_first_name = models.CharField(max_length=100, blank=True)
    mother_middle_name = models.CharField(max_length=100, blank=True)
    mother_last_name = models.CharField(max_length=100, blank=True)
    father_qualification = models.CharField(max_length=100, blank=True)
    mother_qualification = models.CharField(max_length=100, blank=True)
    father_job = models.CharField(max_length=100, blank=True)
    mother_job = models.CharField(max_length=100, blank=True)
    father_job_designation = models.CharField(max_length=100, blank=True)
    mother_job_designation = models.CharField(max_length=100, blank=True)
    father_business_type = models.CharField(max_length=100, blank=True)
    mother_business_type = models.CharField(max_length=100, blank=True)
    father_number = models.CharField(max_length=100, blank=True)
    mother_number = models.CharField(max_length=100, blank=True)
    father_office_address = models.CharField(max_length=100, blank=True)
    mother_office_address = models.CharField(max_length=100, blank=True)
    #guardian details
    guardian_name = models.CharField(max_length=75, blank=True)
    #12th class details
    board_12th = models.CharField(max_length=255, blank=True)
    year_of_12th = models.PositiveIntegerField(blank=True)
    rollno_12th = models.PositiveBigIntegerField(blank=True)
    school_12th = models.CharField(max_length=255, blank=True)
    aggregate_12th = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    first_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    second_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    third_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    fourth_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_12th = models.CharField(max_length=10, blank=True)     # because integer field was giving error even with null=True and Blank=True
    other_subject_2_12th =  models.CharField(max_length=10, blank=True)
    #10th class details
    board_10th = models.CharField(max_length=255, blank=True)
    year_of_10th = models.PositiveIntegerField(blank=True)
    rollno_10th = models.PositiveBigIntegerField(blank=True)
    school_10th = models.CharField(max_length=255, blank=True)
    aggregate_10th = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    maths_10th = models.PositiveIntegerField(blank=True)
    science_10th = models.PositiveIntegerField(blank=True)
    english_10th = models.PositiveIntegerField(blank=True)
    sst_10th = models.PositiveIntegerField(blank=True)
    other_subject_10th = models.CharField(max_length=100, blank=True)   # because integer field was giving error even with null=True and Blank=True
    other_subject_2_10th =  models.CharField(max_length=100, blank=True)
    #CET details
    cet_or_cuet = models.CharField(max_length=10)    # to ask user which paper did he/she appear for
    cet_rank = models.PositiveIntegerField(blank=True, null=True)
    cet_rollno = models.CharField(max_length=255, blank=True)
    #special acheivements
    special_achievements = models.CharField(max_length=255, blank=True)
    #images and files
    passport_photo = models.ImageField(upload_to=utils.bba_photo_rename, blank=True)
    cet_result = models.FileField(upload_to=utils.bba_cetresult_rename, blank=True)
    marksheet_10th = models.FileField(upload_to=utils.bba_10thmarksheet_rename, blank=True)
    marksheet_12th = models.FileField(upload_to=utils.bba_12thmarksheet_rename, blank=True)
    aadhaar = models.FileField(upload_to=utils.bba_aadhar_rename, blank=True)
    pancard = models.FileField(upload_to=utils.bba_pancard_rename, blank=True)
    ipuregistrationproof = models.FileField(upload_to=utils.bba_ipuregistration_rename, blank=True)
    # Transaction Details
    transaction_id = models.CharField(max_length=255, blank=True)
    transaction_proof = models.FileField(upload_to=utils.bba_transaction_rename, blank=True)
    # Counselling Fee Details
    counselling_transaction_id = models.CharField(max_length=255, blank=True)
    counselling_transaction_proof = models.FileField(upload_to=utils.bba_counselling_transaction_rename, blank=True)
    # To track IP address and other information of users
    ip_address = models.CharField(max_length=100, blank=True)
    forwarded_address = models.CharField(max_length=255, blank=True)
    browser_info = models.CharField(max_length=1000, blank=True)
    created_at = models.CharField(max_length=255, blank=True)

    def __str__(self):         # for showing record by name in admin panel
        return (self.candidate_first_name+' '+self.candidate_last_name)

    def photograph_preview(self):   #for previewing photo in admin panel
        return mark_safe(f'<img src = "{self.passport_photo.url}" width = "100"/>')

    class Meta:
        verbose_name_plural = "BBA"    # to show table by this name in admin panel
        db_table = "bba"             # to use the name "bba" instead of "form_bba" in db






# MBA Temporary Records Model:
class MbaTemp(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    #GGSIPU registration no.
    ipu_registration = models.PositiveBigIntegerField(blank=True, unique=True)
    #candidate details
    candidate_first_name = models.CharField(max_length=100, blank=True)
    candidate_middle_name = models.CharField(max_length=100, blank=True)
    candidate_last_name = models.CharField(max_length=100, blank=True)
    #other candidate details
    dob = models.DateField()
    complete_address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=False)
    candidate_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    #father mother details
    father_first_name = models.CharField(max_length=100, blank=True)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_last_name = models.CharField(max_length=100, blank=True)
    mother_first_name = models.CharField(max_length=100, blank=True)
    mother_middle_name = models.CharField(max_length=100, blank=True)
    mother_last_name = models.CharField(max_length=100, blank=True)
    father_qualification = models.CharField(max_length=100, blank=True)
    mother_qualification = models.CharField(max_length=100, blank=True)
    father_job = models.CharField(max_length=100, blank=True)
    mother_job = models.CharField(max_length=100, blank=True)
    father_job_designation = models.CharField(max_length=100, blank=True)
    mother_job_designation = models.CharField(max_length=100, blank=True)
    father_business_type = models.CharField(max_length=100, blank=True)
    mother_business_type = models.CharField(max_length=100, blank=True)
    father_number = models.CharField(max_length=100, blank=True)
    mother_number = models.CharField(max_length=100, blank=True)
    father_office_address = models.CharField(max_length=100, blank=True)
    mother_office_address = models.CharField(max_length=100, blank=True)
    #guardian details
    guardian_name = models.CharField(max_length=75, blank=True)
    #12th class details
    board_12th = models.CharField(max_length=255, blank=True)
    year_of_12th = models.PositiveIntegerField(blank=True, null=True)
    rollno_12th = models.PositiveBigIntegerField(blank=True, null=True)
    school_12th = models.CharField(max_length=255, blank=True)
    aggregate_12th = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    first_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    second_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    third_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    fourth_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_12th = models.CharField(max_length=10, blank=True)     # because integer field was giving error even with null=True and Blank=True
    other_subject_2_12th =  models.CharField(max_length=10, blank=True)
    #10th class details
    board_10th = models.CharField(max_length=255, blank=True)
    year_of_10th = models.PositiveIntegerField(blank=True, null=True)
    rollno_10th = models.PositiveBigIntegerField(blank=True, null=True)
    school_10th = models.CharField(max_length=255, blank=True)
    aggregate_10th = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    maths_10th = models.PositiveIntegerField(blank=True, null=True)
    science_10th = models.PositiveIntegerField(blank=True, null=True)
    english_10th = models.PositiveIntegerField(blank=True, null=True)
    sst_10th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_10th = models.CharField(max_length=100, blank=True)   # because integer field was giving error even with null=True and Blank=True
    other_subject_2_10th =  models.CharField(max_length=100, blank=True)
    #CAT or CMAT details
    cat_or_cmat = models.CharField(max_length=10)    # to ask user which paper did he/she appear for
    cat_or_cmat_rank = models.PositiveIntegerField(blank=True, null=True)
    cat_or_cmat_rollno = models.PositiveBigIntegerField(blank=True, null=True)
    #UG Fields
    ug_type = models.CharField(max_length=75)
    board_ug = models.CharField(max_length=75)
    year_of_ug = models.PositiveIntegerField(blank=True, null=True)
    rollno_ug = models.PositiveBigIntegerField(blank=True, null=True)
    school_ug = models.CharField(max_length=125)
    aggregate_ug = models.CharField(max_length=25)
    #special acheivements
    special_achievements = models.CharField(max_length=255, blank=True)
    #images and files
    passport_photo = models.ImageField(upload_to=utils.mba_photo_rename, blank=True)
    cat_or_cmat_result = models.FileField(upload_to=utils.mba_cat_or_cmat_result_rename, blank=True)
    marksheet_10th = models.FileField(upload_to=utils.mba_10thmarksheet_rename, blank=True)
    marksheet_12th = models.FileField(upload_to=utils.mba_12thmarksheet_rename, blank=True)
    aadhaar = models.FileField(upload_to=utils.mba_aadhar_rename, blank=True)
    pancard = models.FileField(upload_to=utils.mba_pancard_rename, blank=True)
    ipuregistrationproof = models.FileField(upload_to=utils.mba_ipuregistration_rename, blank=True)
    ug_degree = models.FileField(upload_to=utils.mba_ug_degree_rename, blank=True)
    # Transaction Details
    transaction_id = models.CharField(max_length=255, blank=True)
    transaction_proof = models.FileField(upload_to=utils.mba_transaction_rename, blank=True)
    # Counselling Fee Details
    counselling_transaction_id = models.CharField(max_length=255, blank=True)
    counselling_transaction_proof = models.FileField(upload_to=utils.mba_counselling_transaction_rename, blank=True)
    # To track IP address and other information of users
    ip_address = models.CharField(max_length=100, blank=True)
    forwarded_address = models.CharField(max_length=255, blank=True)
    browser_info = models.CharField(max_length=1000, blank=True)
    created_at = models.CharField(max_length=255, blank=True)

    def __str__(self):         # for showing record by name in admin panel
        return (self.candidate_first_name+' '+self.candidate_last_name)

    def photograph_preview(self):   #for previewing photo in admin panel
        return mark_safe(f'<img src = "{self.passport_photo.url}" width = "100"/>')

    class Meta:
        verbose_name_plural = "MBA Temporary"    # to show table by this name in admin panel
        db_table = "mba_temp"             # to use the name "mba_temp" instead of "form_mba_temp" in db 


# mba Model:
class Mba(models.Model):
    # application id (auto generated)
    application_id = models.CharField(max_length=100, unique=True)
    #GGSIPU registration no.
    ipu_registration = models.PositiveBigIntegerField(blank=True, unique=True)
    # allowed for counselling
    allow_for_counselling = models.BooleanField(default=False)
    # allow for editing of record
    allow_editing = models.BooleanField(default=False)
    #candidate details
    candidate_first_name = models.CharField(max_length=100, blank=True)
    candidate_middle_name = models.CharField(max_length=100, blank=True)
    candidate_last_name = models.CharField(max_length=100, blank=True)
    #other candidate details
    dob = models.DateField()
    complete_address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True, unique=False)
    candidate_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    #father mother details
    father_first_name = models.CharField(max_length=100, blank=True)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_last_name = models.CharField(max_length=100, blank=True)
    mother_first_name = models.CharField(max_length=100, blank=True)
    mother_middle_name = models.CharField(max_length=100, blank=True)
    mother_last_name = models.CharField(max_length=100, blank=True)
    father_qualification = models.CharField(max_length=100, blank=True)
    mother_qualification = models.CharField(max_length=100, blank=True)
    father_job = models.CharField(max_length=100, blank=True)
    mother_job = models.CharField(max_length=100, blank=True)
    father_job_designation = models.CharField(max_length=100, blank=True)
    mother_job_designation = models.CharField(max_length=100, blank=True)
    father_business_type = models.CharField(max_length=100, blank=True)
    mother_business_type = models.CharField(max_length=100, blank=True)
    father_number = models.CharField(max_length=100, blank=True)
    mother_number = models.CharField(max_length=100, blank=True)
    father_office_address = models.CharField(max_length=100, blank=True)
    mother_office_address = models.CharField(max_length=100, blank=True)
    #guardian details
    guardian_name = models.CharField(max_length=75, blank=True)
    #12th class details
    board_12th = models.CharField(max_length=255, blank=True)
    year_of_12th = models.PositiveIntegerField(blank=True)
    rollno_12th = models.PositiveBigIntegerField(blank=True)
    school_12th = models.CharField(max_length=255, blank=True)
    aggregate_12th = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    first_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    second_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    third_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    fourth_subject_12th = models.PositiveIntegerField(blank=True, null=True)
    other_subject_12th = models.CharField(max_length=100, blank=True)     # because integer field was giving error even with null=True and Blank=True
    other_subject_2_12th =  models.CharField(max_length=100, blank=True)
    #10th class details
    board_10th = models.CharField(max_length=255, blank=True)
    year_of_10th = models.PositiveIntegerField(blank=True)
    rollno_10th = models.PositiveBigIntegerField(blank=True)
    school_10th = models.CharField(max_length=255, blank=True)
    aggregate_10th = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    maths_10th = models.PositiveIntegerField(blank=True)
    science_10th = models.PositiveIntegerField(blank=True)
    english_10th = models.PositiveIntegerField(blank=True)
    sst_10th = models.PositiveIntegerField(blank=True)
    other_subject_10th = models.CharField(max_length=100, blank=True)   # because integer field was giving error even with null=True and Blank=True
    other_subject_2_10th =  models.CharField(max_length=100, blank=True)
    #CAT or CMAT details
    cat_or_cmat = models.CharField(max_length=10)    # to ask user which paper did he/she appear for
    cat_or_cmat_rank = models.PositiveIntegerField(blank=True, null=True)
    cat_or_cmat_rollno = models.PositiveBigIntegerField(blank=True, null=True)
    #UG Fields
    ug_type = models.CharField(max_length=75)
    board_ug = models.CharField(max_length=75)
    year_of_ug = models.PositiveIntegerField(blank=True, null=True)
    rollno_ug = models.PositiveBigIntegerField(blank=True, null=True)
    school_ug = models.CharField(max_length=125)
    aggregate_ug = models.CharField(max_length=25)
    #special acheivements
    special_achievements = models.CharField(max_length=255, blank=True)
    #images and files
    passport_photo = models.ImageField(upload_to=utils.mba_photo_rename, blank=True)
    cat_or_cmat_result = models.FileField(upload_to=utils.mba_cat_or_cmat_result_rename, blank=True)
    marksheet_10th = models.FileField(upload_to=utils.mba_10thmarksheet_rename, blank=True)
    marksheet_12th = models.FileField(upload_to=utils.mba_12thmarksheet_rename, blank=True)
    aadhaar = models.FileField(upload_to=utils.mba_aadhar_rename, blank=True)
    pancard = models.FileField(upload_to=utils.mba_pancard_rename, blank=True)
    ipuregistrationproof = models.FileField(upload_to=utils.mba_ipuregistration_rename, blank=True)
    ug_degree = models.FileField(upload_to=utils.mba_ug_degree_rename, blank=True)
    # Transaction Details
    transaction_id = models.CharField(max_length=255, blank=True)
    transaction_proof = models.FileField(upload_to=utils.mba_transaction_rename, blank=True)
    # Counselling Fee Details
    counselling_transaction_id = models.CharField(max_length=255, blank=True)
    counselling_transaction_proof = models.FileField(upload_to=utils.mba_counselling_transaction_rename, blank=True)
    # To track IP address and other information of users
    ip_address = models.CharField(max_length=100, blank=True)
    forwarded_address = models.CharField(max_length=255, blank=True)
    browser_info = models.CharField(max_length=1000, blank=True)
    created_at = models.CharField(max_length=255, blank=True)

    def __str__(self):         # for showing record by name in admin panel
        return (self.candidate_first_name+' '+self.candidate_last_name)

    def photograph_preview(self):   #for previewing photo in admin panel
        return mark_safe(f'<img src = "{self.passport_photo.url}" width = "100"/>')

    class Meta:
        verbose_name_plural = "MBA"    # to show table by this name in admin panel
        db_table = "mba"             # to use the name "mba" instead of "form_mba" in db