from django.shortcuts import render, redirect
import datetime
from . models import Btech, BtechTemp, AllowedIP, Login, BtechLE, BtechLETemp, Bba, BbaTemp, Mba, MbaTemp, BankDetails
from django.contrib import messages
# For sending mails:
from django.core.mail import send_mail
from django.conf import settings
# For random password generation
import secrets
import string
from django.db import IntegrityError

import logging

# This will log errors everytime there is a error in handling a request or rendering a response
logger = logging.getLogger(__name__)


# we are taking a flag variable named logged_in
logged_in = False 
# if this logged_in is True, then only user can see pages like /btech or /btech-preview etc.
# if user tries to directly come to /btech or /btech-preview etc, then we will redirect him back to /login

# also we are taking application_id as a global variable at the very beginning of the program
# so that we avoid passing the application_id from one view to other for performing CRUD operations
application_id = ""
ipu_registration = ""
course=""
# this empty string will be filled with value either from the index function or from login function 


# Function for generating random 12 letter/digit password
def get_random_pwd():
    # all uppercase lowercase letters
    letters = string.ascii_letters
    # all digits
    digits = string.digits
    # concatenation
    alphabet = letters + digits
    pwd_length = 12
    pwd = ''
    for i in range(pwd_length):
        pwd += ''.join(secrets.choice(alphabet))

    return pwd

# Function for generating random 8 digit ID
def get_random_id():
    digits = string.digits
    id_length = 8
    id = ''
    for i in range(id_length):
        id += ''.join(secrets.choice(digits))
    # retreiving all existing records
    logins = Login.objects.all()
    credentials = {}         # empty dictionary for storing key value pairs of id:pwd
    for login in logins:
        credentials[login.ipu_registration] = login.password
    # checking if that id doesnt exist then only we will proceed (bcoz we are generating randomly so they can repeat)
    flag_unique = False
    while flag_unique == False:
        if id not in credentials:
            flag_unique = True
            return id
        else:
            id = get_random_id()




# Index Page: The first page user sees after coming on empty path
def index(request):
    if request.method == 'POST':
        # for allowing only specific IP addresses
        allowed_ips = AllowedIP.objects.all()
        allowed_ips_list = []
        # making a list out of this query set
        for ip in allowed_ips:
            allowed_ips_list.append(ip.ip_address)
        ip_address = request.META.get('REMOTE_ADDR')
        # if ip_address not in allowed_ips_list:
        #     return render(request, 'index.html')
        candidate_name = request.POST.get('candidate_name')
        candidate_email = request.POST.get('candidate_email')
        candidate_mobile = request.POST.get('candidate_mobile')
        global ipu_registration
        ipu_registration = request.POST.get('ipu_registration')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        logins = Login.objects.all()
        for login in logins:
            if ((login.candidate_email == candidate_email) or (login.candidate_mobile == candidate_mobile)):
                message="User already exists"
                context = {'message': message}
                return render(request, 'login.html', context) 
        # getting unique password and id
        id = get_random_id()
        pwd = get_random_pwd()
        #sending mail
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [candidate_email, ]
        custom_message = "Your IPU Registration No. is:\n  " + ipu_registration + "\n\nYour password is:\n  " + pwd
        send_mail( 'MAIT Login Credentials', custom_message , email_from, recipient_list, fail_silently=True)
        # After sending mail, now saving user id and password
        final_id = "MAIT/MQ/2023-24/"+id   #only last 8 randomly generated digits to be sent to user but whole id to be stored in database
        global application_id
        application_id = final_id
        newlogin = Login(application_id = application_id, password=pwd, ipu_registration=ipu_registration, candidate_name=candidate_name, candidate_mobile=candidate_mobile, candidate_email=candidate_email, ip_address=ip_address, created_at=created_at)
        # when the ipu_registration number is already exisiting in db, then an error is raised while saving the records
        try:
            newlogin.save()
        except IntegrityError as e:
            message = e
            context = {'message': message}
            return render(request, 'login.html', context) 
        return redirect('login')
    else:
        # GET request
        return render(request, 'index.html')

# Login Page
def login(request):
    message="OK"
    # getting all user ids and correspponding passwords in a list
    logins = Login.objects.all()
    credentials = {}         # empty dictionary for storing key value pairs of id:pwd
    for login in logins:
        credentials[str(login.ipu_registration)] = login.password
    # this post request comes from the 'form action=login' in the login page
    if request.method == 'POST' :
        # for allowing only specific IP addresses
        allowed_ips = AllowedIP.objects.all()
        allowed_ips_list = []
        # making a list out of this query set
        for ip in allowed_ips:
            allowed_ips_list.append(ip.ip_address)
        ip_address = request.META.get('REMOTE_ADDR')
        # if ip_address not in allowed_ips_list:
        #     return render(request, 'login.html')
        global ipu_registration
        ipu_registration = request.POST.get('ipu_registration')
        user_pwd = request.POST.get('user_pwd')
        # now checking id password
        if ipu_registration in credentials:
            if user_pwd == credentials[ipu_registration] :
                # when both ipu_registration no. and password are correct, then redirecting to courses page 
                # and setting global variable application_id to corresponding value
                # and setting flag logged_in to True
                global logged_in
                logged_in = True
                global application_id
                application_id = Login.objects.filter(ipu_registration=ipu_registration).first().application_id
                return redirect('courses')
            else :                   # when ipu_registration is ok but doesnt match the corresponding user password
                message="Invalid Password"
                context = {'message': message}
                return render(request, 'login.html', context) 
        else :
            message="Invalid Registration Number or Password"
            context = {'message': message}
            return render(request, 'login.html', context)
    # GET method
    context = {'message': message}
    return render(request, 'login.html', context)

# Courses: For choice of course
def courses(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Proceed" on the /courses.html page
    if request.method == "POST":
        global course
        course = request.POST.get('course')
        # if user selected btech then three possibilities:
        # either he is a completely new user (then redirect to btech1)
        # or he has some temporary data submitted (then redirect to btech1)
        # or he has permanent data submitted (then redirect to btech-preview)
        # same case is for all courses
        if course == "Btech":
            login_record = Login.objects.filter(application_id=application_id).first()
            login_record.course = course
            login_record.save()
            temp_record = BtechTemp.objects.filter(application_id=application_id).first()
            permanent_record = Btech.objects.filter(application_id=application_id).first()
            if temp_record:
                return redirect ('btech1')
            if permanent_record:
                return redirect ('dashboard')
            return redirect ('btech1')
        if course == "BtechLE":
            login_record = Login.objects.filter(application_id=application_id).first()
            login_record.course = course
            login_record.save()
            temp_record = BtechLETemp.objects.filter(application_id=application_id).first()
            permanent_record = BtechLE.objects.filter(application_id=application_id).first()
            if temp_record:
                return redirect ('btechle1')
            if permanent_record:
                return redirect ('dashboard')
            return redirect ('btechle1')
        if course == "BBA":
            login_record = Login.objects.filter(application_id=application_id).first()
            login_record.course = course
            login_record.save()
            temp_record = BbaTemp.objects.filter(application_id=application_id).first()
            permanent_record = Bba.objects.filter(application_id=application_id).first()
            if temp_record:
                return redirect ('bba1')
            if permanent_record:
                return redirect ('dashboard')
            return redirect ('bba1')
        if course == "MBA":
            login_record = Login.objects.filter(application_id=application_id).first()
            login_record.course = course
            login_record.save()
            temp_record = MbaTemp.objects.filter(application_id=application_id).first()
            permanent_record = Mba.objects.filter(application_id=application_id).first()
            if temp_record:
                return redirect ('mba1')
            if permanent_record:
                return redirect ('dashboard')
            return redirect ('mba1')
    else:
        # GET request
        return render(request, 'courses.html')    

# For resetting password
def password_reset(request):
    if request.method == "POST":
        # getting all user ids and correspponding emails in a list
        logins = Login.objects.all()
        credentials = {}         # empty dictionary for storing key value pairs of id:pwd
        for login in logins:
            credentials[str(login.ipu_registration)] = login.candidate_email
        global ipu_registration
        ipu_registration = request.POST.get('ipu_registration')
        email = request.POST.get('email')
        # now checking id and email
        if ipu_registration in credentials:
            if email == credentials[ipu_registration] :
                # when both ipu_registration no. and email are correct, then we will send the password
                #sending mail
                new_pwd = get_random_pwd()
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email, ]
                custom_message = "Your GGSIPU Registration No. is:\n  " + ipu_registration + "\n\nYour New password is:\n  " + new_pwd
                send_mail( 'MAIT Login Credentials', custom_message , email_from, recipient_list, fail_silently=True)
                newobj = Login.objects.filter(ipu_registration = ipu_registration).first()
                newobj.password = new_pwd
                newobj.save()
                message="New credentials have been sent to your mail."
                messages.info(request, message)
                return redirect('login')
            else :                   
                # when ipu_registration is ok but doesnt match the corresponding user email
                message="The GGSIPU Registration No. "+ipu_registration+" has a different mail associated with it."
                messages.info(request, message)
                return render(request, 'password-reset.html') 
        else :
            message="No record found for GGSIPU Registration Number "+ipu_registration
            messages.info(request, message)
            return render(request, 'password-reset.html')
        

    return render(request, 'password-reset.html')

# Dashboard: For giving preview/edit/counselling fee options
def dashboard(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # GET request: We shall pass the course as context too
    global course
    if course == "Btech":
        record = Btech.objects.all().filter(application_id = application_id).first()
    if course == "BtechLE":
        record = BtechLE.objects.all().filter(application_id = application_id).first()
    if course == "BBA":
        record = Bba.objects.all().filter(application_id = application_id).first()
    if course == "MBA":
        record = Mba.objects.all().filter(application_id = application_id).first()
    context = {'course': course, 'record': record}
    return render(request, 'dashboard.html', context)

# Counselling: For user to pay counselling fees
def counselling(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # When POST, then simply save the two fields
    if request.method == "POST":
        global course
        global ipu_registration
        counselling_transaction_id = request.POST.get('counselling_transaction_id')
        counselling_transaction_proof = request.FILES['counselling_transaction_proof']
        # bank details
        account_holder_name = request.POST.get('account_holder_name')
        account_number = request.POST.get('account_number')
        bank_name = request.POST.get('bank_name')
        ifsc_code = request.POST.get('ifsc_code')
        cheque_copy = request.FILES['cheque_copy']
        # saving bank details
        newobj = BankDetails(ipu_registration=ipu_registration,course=course, account_holder_name=account_holder_name, account_number=account_number,
                             bank_name=bank_name, ifsc_code=ifsc_code, )
        newobj.save()
        # saving file after instance is created
        newobj.cheque_copy = cheque_copy
        newobj.save()
        if course == "Btech":
            record = Btech.objects.filter(application_id = application_id).first()
            record.counselling_transaction_id = counselling_transaction_id
            record.counselling_transaction_proof = counselling_transaction_proof
            record.save()
            return redirect ('btech_preview')
        if course == "BtechLE":
            record = BtechLE.objects.filter(application_id = application_id).first()
            record.counselling_transaction_id = counselling_transaction_id
            record.counselling_transaction_proof = counselling_transaction_proof
            record.save()
            return redirect ('btechle_preview')
        if course == "BBA":
            record = Bba.objects.filter(application_id = application_id).first()
            record.counselling_transaction_id = counselling_transaction_id
            record.counselling_transaction_proof = counselling_transaction_proof
            record.save()
            return redirect ('bba_preview')
        if course == "MBA":
            record = Mba.objects.filter(application_id = application_id).first()
            record.counselling_transaction_id = counselling_transaction_id
            record.counselling_transaction_proof = counselling_transaction_proof
            record.save()
            return redirect ('mba_preview')
    # GET request: simply show counselling page
    return render(request, 'counselling.html')








def btech1(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /btech1.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        candidate_first_name = request.POST.get('candidate_first_name')
        candidate_middle_name = request.POST.get('candidate_middle_name')
        candidate_last_name = request.POST.get('candidate_last_name')
        email = request.POST.get('email')
        candidate_number = request.POST.get('candidate_number')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        category = request.POST.get('category')
        region = request.POST.get('region')
        # To track IP address and other info of user coming from request.META header
        ip_address = request.META.get('REMOTE_ADDR','-1')      # return -1 if no address found
        forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR','-1')
        browser_info = request.META.get('HTTP_USER_AGENT','-1')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BtechTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.candidate_first_name = candidate_first_name   
            existing_record.candidate_middle_name = candidate_middle_name
            existing_record.candidate_last_name = candidate_last_name
            existing_record.email = email
            existing_record.candidate_number = candidate_number
            existing_record.gender = gender
            existing_record.dob = dob
            existing_record.category = category
            existing_record.region = region
            existing_record.ip_address = ip_address
            existing_record.forwarded_address = forwarded_address
            existing_record.browser_info = browser_info
            existing_record.created_at = created_at
            # saving the updated record
            existing_record.save()
            return redirect ('btech2')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BtechTemp(application_id=application_id, ipu_registration=ipu_registration,
                            candidate_first_name=candidate_first_name,
                            candidate_middle_name=candidate_middle_name, candidate_last_name=candidate_last_name,
                            email=email, candidate_number=candidate_number, gender=gender, dob=dob, category=category, region=region,
                            ip_address=ip_address, forwarded_address=forwarded_address, browser_info=browser_info, created_at=created_at,)
            newform.save()
            return redirect ('btech2')
    # if the request method is not POST, then:
    # either user is coming from login page for the very first time
    # or user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of btech form by clicking the step-form (progress bar)
    # in all three cases we can render btech1.html with context
    # to create context we will use the globally available variable application_id
    record = BtechTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'btech/btech1.html', context)

def btech2(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /btech2.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        father_first_name = request.POST.get('father_first_name')
        father_middle_name = request.POST.get('father_middle_name')
        father_last_name = request.POST.get('father_last_name')
        mother_first_name = request.POST.get('mother_first_name')
        mother_middle_name = request.POST.get('mother_middle_name')
        mother_last_name = request.POST.get('mother_last_name')
        father_qualification = request.POST.get('father_qualification')
        mother_qualification = request.POST.get('mother_qualification')
        father_job = request.POST.get('father_job')
        mother_job = request.POST.get('mother_job')
        father_job_designation = request.POST.get('father_job_designation')
        mother_job_designation = request.POST.get('mother_job_designation')
        father_business_type = request.POST.get('father_business_type')
        mother_business_type = request.POST.get('mother_business_type')
        father_number = request.POST.get('father_number')
        mother_number = request.POST.get('mother_number')
        father_office_address = request.POST.get('father_office_address')
        mother_office_address = request.POST.get('mother_office_address')
        guardian_name = request.POST.get('guardian_name')
        complete_address = request.POST.get('complete_address')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BtechTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.father_first_name = father_first_name   
            existing_record.father_middle_name = father_middle_name
            existing_record.father_last_name = father_last_name
            existing_record.mother_first_name = mother_first_name   
            existing_record.mother_middle_name = mother_middle_name
            existing_record.mother_last_name = mother_last_name
            existing_record.father_qualification = father_qualification
            existing_record.mother_qualification = mother_qualification
            existing_record.father_job = father_job
            existing_record.mother_job = mother_job
            existing_record.father_job_designation = father_job_designation
            existing_record.mother_job_designation = mother_job_designation
            existing_record.father_business_type = father_business_type   
            existing_record.mother_business_type = mother_business_type
            existing_record.father_office_address = father_office_address
            existing_record.mother_office_address = mother_office_address   
            existing_record.father_number = father_number
            existing_record.mother_number = mother_number
            existing_record.guardian_name = guardian_name   
            existing_record.complete_address = complete_address
            # saving the updated record
            existing_record.save()
            return redirect ('btech3')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BtechTemp(application_id=application_id, ipu_registration=ipu_registration, 
                            father_first_name=father_first_name, father_middle_name=father_middle_name, father_last_name=father_last_name,
                            mother_first_name=mother_first_name, mother_middle_name=mother_middle_name, mother_last_name=mother_last_name,
                            father_qualification=father_qualification, mother_qualification=mother_qualification,
                            father_job=father_job, mother_job=mother_job,
                            father_job_designation=father_job_designation, mother_job_designation=mother_job_designation,
                            father_business_type=father_business_type, mother_business_type=mother_business_type,
                            father_number=father_number, mother_number=mother_number,
                            father_office_address=father_office_address, mother_office_address=mother_office_address,
                            complete_address=complete_address, guardian_name=guardian_name,)
            newform.save()
            return redirect ('btech3')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of btech form by clicking the step-form (progress bar)
    # or user is coming from btech1.html after saving his record
    # in all three cases we can render btech2.html with context
    # to create context we will use the globally available variable application_id
    record = BtechTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'btech/btech2.html', context)

def btech3(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /btech3.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        board_12th = request.POST.get('board_12th')
        year_of_12th = request.POST.get('year_of_12th')
        rollno_12th = request.POST.get('rollno_12th')
        school_12th = request.POST.get('school_12th')
        aggregate_12th = float(request.POST.get('aggregate_12th'))
        maths_12th = request.POST.get('maths_12th')
        physics_12th = request.POST.get('physics_12th')
        chemistry_12th = request.POST.get('chemistry_12th')
        english_12th = request.POST.get('english_12th')
        other_subject_12th = request.POST.get('other_subject_12th')
        other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        board_10th = request.POST.get('board_10th')
        year_of_10th = request.POST.get('year_of_10th')
        rollno_10th = request.POST.get('rollno_10th')
        school_10th = request.POST.get('school_10th')
        aggregate_10th = float(request.POST.get('aggregate_10th'))
        maths_10th = request.POST.get('maths_10th')
        science_10th = request.POST.get('science_10th')
        english_10th = request.POST.get('english_10th')
        sst_10th = request.POST.get('sst_10th')
        other_subject_10th = request.POST.get('other_subject_10th')
        other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BtechTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.board_12th = board_12th   
            existing_record.year_of_12th = year_of_12th
            existing_record.rollno_12th = rollno_12th
            existing_record.school_12th = school_12th
            existing_record.aggregate_12th = aggregate_12th
            existing_record.maths_12th = maths_12th
            existing_record.physics_12th = physics_12th
            existing_record.chemistry_12th = chemistry_12th
            existing_record.english_12th = english_12th
            existing_record.other_subject_12th = other_subject_12th
            existing_record.other_subject_2_12th = other_subject_2_12th
            existing_record.board_10th = board_10th   
            existing_record.year_of_10th = year_of_10th
            existing_record.rollno_10th = rollno_10th
            existing_record.school_10th = school_10th
            existing_record.aggregate_10th = aggregate_10th
            existing_record.maths_10th = maths_10th
            existing_record.science_10th = science_10th
            existing_record.english_10th = english_10th
            existing_record.sst_10th = sst_10th
            existing_record.other_subject_10th = other_subject_10th
            existing_record.other_subject_2_10th = other_subject_2_10th
            # saving the updated record
            existing_record.save()
            return redirect ('btech4')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BtechTemp(application_id=application_id, ipu_registration=ipu_registration,
                            board_12th=board_12th, year_of_12th=year_of_12th, rollno_12th=rollno_12th, school_12th=school_12th,
                            maths_12th=maths_12th, physics_12th=physics_12th, chemistry_12th=chemistry_12th, english_12th=english_12th,
                            other_subject_12th=other_subject_12th, other_subject_2_12th=other_subject_2_12th, aggregate_12th=aggregate_12th, 
                            board_10th=board_10th, year_of_10th=year_of_10th, rollno_10th=rollno_10th, school_10th=school_10th,
                            maths_10th=maths_10th, science_10th=science_10th, english_10th=english_10th, sst_10th=sst_10th,
                            other_subject_10th=other_subject_10th, other_subject_2_10th=other_subject_2_10th, aggregate_10th=aggregate_10th,)
            newform.save()
            return redirect ('btech4')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of btech form by clicking the step-form (progress bar)
    # or user is coming from btech2.html after saving his record
    # in all three cases we can render btech3.html with context
    # to create context we will use the globally available variable application_id
    record = BtechTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'btech/btech3.html', context)

def btech4(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /btech4.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        jee_rank = request.POST.get('jee_rank')
        jee_percentile = request.POST.get('jee_percentile')
        jee_rollno = request.POST.get('jee_rollno')
        special_achievements = request.POST.get('special_achievements')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BtechTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.jee_rank = jee_rank   
            existing_record.jee_percentile = jee_percentile
            existing_record.jee_rollno = jee_rollno
            existing_record.special_achievements = special_achievements
            # saving the updated record
            existing_record.save()
            return redirect ('btech5')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BtechTemp(application_id=application_id, ipu_registration=ipu_registration,
                            jee_rank=jee_rank, jee_percentile=jee_percentile, jee_rollno=jee_rollno,
                            special_achievements=special_achievements,)
            newform.save()
            return redirect ('btech5')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of btech form by clicking the step-form (progress bar)
    # or user is coming from btech3.html after saving his record
    # in all three cases we can render btech4.html with context
    # to create context we will use the globally available variable application_id
    record = BtechTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'btech/btech4.html', context)

def btech5(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /btech5.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        preference1 = request.POST.get('preference1')
        preference2 = request.POST.get('preference2')
        preference3 = request.POST.get('preference3')
        preference4 = request.POST.get('preference4')
        preference5 = request.POST.get('preference5')
        preference6 = request.POST.get('preference6')
        preference7 = request.POST.get('preference7')
        preference8 = request.POST.get('preference8')
        preference9 = request.POST.get('preference9')
        preference10 = request.POST.get('preference10')
        preference11 = request.POST.get('preference11')
        preference12 = request.POST.get('preference12')
        preference13 = request.POST.get('preference13')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BtechTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.preference1 = preference1   
            existing_record.preference2 = preference2
            existing_record.preference3 = preference3
            existing_record.preference4 = preference4
            existing_record.preference5 = preference5
            existing_record.preference6 = preference6
            existing_record.preference7 = preference7
            existing_record.preference8 = preference8
            existing_record.preference9 = preference9
            existing_record.preference10 = preference10
            existing_record.preference11 = preference11
            existing_record.preference12 = preference12
            existing_record.preference13 = preference13
            # saving the updated record
            existing_record.save()
            return redirect ('btech6')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BtechTemp(application_id=application_id, ipu_registration=ipu_registration,
                            preference1=preference1, preference2=preference2, preference3=preference3,
                            preference4=preference4, preference5=preference5, preference6=preference6,
                            preference7=preference7, preference8=preference8, preference9=preference9, 
                            preference10=preference10, preference11=preference11, preference12=preference12, preference13=preference13,)
            newform.save()
            return redirect ('btech6')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of btech form by clicking the step-form (progress bar)
    # or user is coming from btech4.html after saving his record
    # in all three cases we can render btech5.html with context
    # to create context we will use the globally available variable application_id
    record = BtechTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'btech/btech5.html', context)

def btech6(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /btech6.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        passport_photo = request.FILES['passport_photo']
        jee_result = request.FILES['jee_result']
        marksheet_10th = request.FILES['marksheet_10th']
        marksheet_12th = request.FILES['marksheet_12th']
        aadhaar = request.FILES['aadhaar']
        pancard = request.FILES['pancard']
        ipuregistrationproof = request.FILES['ipuregistrationproof']
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BtechTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.passport_photo = passport_photo   
            existing_record.jee_result = jee_result
            existing_record.marksheet_10th = marksheet_10th
            existing_record.marksheet_12th = marksheet_12th
            existing_record.aadhaar = aadhaar
            existing_record.pancard = pancard
            existing_record.ipuregistrationproof = ipuregistrationproof
            # saving the updated record
            existing_record.save()
            # we will only redirect to payments on /btech7 if all previous steps are filled
            # so to check that, we will check whether some value on each step is filled or not
            if not existing_record.candidate_first_name:
                return redirect('btech1')
            if not existing_record.father_first_name:
                return redirect('btech2')
            if not existing_record.board_12th:
                return redirect('btech3')
            if not existing_record.jee_rollno:
                return redirect('btech4')
            if not existing_record.preference1:
                return redirect('btech5')
            # if all of these details are filled, then we can safely proceed to payment
            return redirect ('btech7')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BtechTemp(application_id=application_id, ipu_registration=ipu_registration,
                            passport_photo=passport_photo, jee_result=jee_result, marksheet_10th=marksheet_10th, marksheet_12th=marksheet_12th,
                            aadhaar=aadhaar, pancard=pancard, ipuregistrationproof=ipuregistrationproof)
            newform.save()
            # if its a new record, then we shall not allow to proceed to payment, so we are redirecting to /btech1
            return redirect ('btech1')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of btech form by clicking the step-form (progress bar)
    # or user is coming from btech5.html after saving his record
    # in all three cases we can render btech6.html with context
    # to create context we will use the globally available variable application_id
    record = BtechTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'btech/btech6.html', context)

def btech7(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /btech7.html page
    # so we shall save the data 
    if request.method == "POST" :
        transaction_id = request.POST.get('transaction_id')
        transaction_proof = request.FILES['transaction_proof']
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # (this will never be the case because we are not allowing user to come to /btech7 if he hasn't already filled previous data , but still handling this case)
        # so, let's check if a record exists or not
        existing_record = BtechTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.transaction_id = transaction_id   
            existing_record.transaction_proof = transaction_proof
            # saving the updated record
            existing_record.save()
            # all steps are completed, now redirecting to final preview where data will move from temp table to permanent table 
            return redirect ('btech')
        else:
            # saving all fields in a new object
            newform = BtechTemp(application_id=application_id, ipu_registration=ipu_registration, 
                            transaction_id=transaction_id, transaction_proof=transaction_proof)
            newform.save()
            return redirect ('btech')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of btech form by clicking the step-form (progress bar)
    # or user is coming from btech6.html after saving his record
    # we shall allow the user only in the case when he has submitted all 6 steps
    record = BtechTemp.objects.all().filter(application_id = application_id).first()
    # so to check that, we will check whether some value on each step is filled or not
    # before that we can check if record exists or not:
    if not record:
        messages.info(request, 'Please fill candidate details before payment')
        return redirect('btech1')
    if not record.candidate_first_name:
        messages.info(request, 'Please fill candidate details before payment')
        return redirect('btech1')
    if not record.father_first_name:
        messages.info(request, 'Please fill parent details before payment')
        return redirect('btech2')
    if not record.board_10th:
        messages.info(request, 'Please fill educational details before payment')
        return redirect('btech3')
    if not record.jee_rollno:
        messages.info(request, 'Please fill qualifying details before payment')
        return redirect('btech4')
    if not record.preference1:
        messages.info(request, 'Please fill choice of programme before payment')
        return redirect('btech5')
    if not record.passport_photo:
        messages.info(request, 'Please upload documents before payment')
        return redirect("btech6")
    # if all of these details are filled, then we can safely render /btech7.html
    context = {'record': record}
    return render(request, 'btech/btech7.html', context)

# Btech
def btech(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Submit" on the /btech.html page
    # so we shall save the data in permanent table and delete from temporary table
    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id')
        # category and region
        category = request.POST.get('category')
        region = request.POST.get('region')
        candidate_first_name = request.POST.get('candidate_first_name')
        candidate_middle_name = request.POST.get('candidate_middle_name')
        candidate_last_name = request.POST.get('candidate_last_name')
        #father mother details
        father_first_name = request.POST.get('father_first_name')
        father_middle_name = request.POST.get('father_middle_name')
        father_last_name = request.POST.get('father_last_name')
        mother_first_name = request.POST.get('mother_first_name')
        mother_middle_name = request.POST.get('mother_middle_name')
        mother_last_name = request.POST.get('mother_last_name')
        father_qualification = request.POST.get('father_qualification')
        mother_qualification = request.POST.get('mother_qualification')
        father_job = request.POST.get('father_job')
        mother_job = request.POST.get('mother_job')
        father_job_designation = request.POST.get('father_job_designation')
        mother_job_designation = request.POST.get('mother_job_designation')
        father_business_type = request.POST.get('father_business_type')
        mother_business_type = request.POST.get('mother_business_type')
        father_number = request.POST.get('father_number')
        mother_number = request.POST.get('mother_number')
        father_office_address = request.POST.get('father_office_address')
        mother_office_address = request.POST.get('mother_office_address')
        #other candidate details
        complete_address = request.POST.get('complete_address')
        email = request.POST.get('email')
        candidate_number = request.POST.get('candidate_number')
        gender = request.POST.get('gender')
        #guardian details
        guardian_name = request.POST.get('guardian_name')
        #candidate dob
        dob = request.POST.get('dob')
        #12th class details
        board_12th = request.POST.get('board_12th')
        year_of_12th = request.POST.get('year_of_12th')
        rollno_12th = request.POST.get('rollno_12th')
        school_12th = request.POST.get('school_12th')
        aggregate_12th = float(request.POST.get('aggregate_12th'))
        maths_12th = request.POST.get('maths_12th')
        physics_12th = request.POST.get('physics_12th')
        chemistry_12th = request.POST.get('chemistry_12th')
        english_12th = request.POST.get('english_12th')
        other_subject_12th = request.POST.get('other_subject_12th')
        other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        #10th class details
        board_10th = request.POST.get('board_10th')
        year_of_10th = request.POST.get('year_of_10th')
        rollno_10th = request.POST.get('rollno_10th')
        school_10th = request.POST.get('school_10th')
        aggregate_10th = float(request.POST.get('aggregate_10th'))
        maths_10th = request.POST.get('maths_10th')
        science_10th = request.POST.get('science_10th')
        english_10th = request.POST.get('english_10th')
        sst_10th = request.POST.get('sst_10th')
        other_subject_10th = request.POST.get('other_subject_10th')
        other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        #JEE details
        jee_rank = request.POST.get('jee_rank')
        jee_percentile = request.POST.get('jee_percentile')
        jee_rollno = request.POST.get('jee_rollno')
        #special acheivements
        special_achievements = request.POST.get('special_achievements')
        #preference list
        preference1 = request.POST.get('preference1')
        preference2 = request.POST.get('preference2')
        preference3 = request.POST.get('preference3')
        preference4 = request.POST.get('preference4')
        preference5 = request.POST.get('preference5')
        preference6 = request.POST.get('preference6')
        preference7 = request.POST.get('preference7')
        preference8 = request.POST.get('preference8')
        preference9 = request.POST.get('preference9')
        preference10 = request.POST.get('preference10')
        preference11 = request.POST.get('preference11')
        preference12 = request.POST.get('preference12')
        preference13 = request.POST.get('preference13')
        # To track IP address and other info of user coming from request.META header
        ip_address = request.META.get('REMOTE_ADDR','-1')      # return -1 if no address found
        forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR','-1')
        browser_info = request.META.get('HTTP_USER_AGENT','-1')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        # saving all fields expect files in a new object
        newform = Btech(candidate_first_name=candidate_first_name, candidate_middle_name=candidate_middle_name, candidate_last_name=candidate_last_name,
                        father_first_name=father_first_name, father_middle_name=father_middle_name, father_last_name=father_last_name,
                        mother_first_name=mother_first_name, mother_middle_name=mother_middle_name, mother_last_name=mother_last_name,
                        father_qualification=father_qualification, mother_qualification=mother_qualification,
                        father_job=father_job, mother_job=mother_job,
                        father_job_designation=father_job_designation, mother_job_designation=mother_job_designation,
                        father_business_type=father_business_type, mother_business_type=mother_business_type,
                        father_number=father_number, mother_number=mother_number,
                        father_office_address=father_office_address, mother_office_address=mother_office_address,
                        complete_address=complete_address, candidate_number=candidate_number,
                        guardian_name=guardian_name, email=email, dob=dob, gender=gender,
                        board_12th=board_12th, year_of_12th=year_of_12th, rollno_12th=rollno_12th, school_12th=school_12th,
                        maths_12th=maths_12th, physics_12th=physics_12th, chemistry_12th=chemistry_12th, english_12th=english_12th,
                        other_subject_12th=other_subject_12th, other_subject_2_12th=other_subject_2_12th, aggregate_12th=aggregate_12th, 
                        board_10th=board_10th, year_of_10th=year_of_10th, rollno_10th=rollno_10th, school_10th=school_10th,
                        maths_10th=maths_10th, science_10th=science_10th, english_10th=english_10th, sst_10th=sst_10th,
                        other_subject_10th=other_subject_10th, other_subject_2_10th=other_subject_2_10th, aggregate_10th=aggregate_10th, 
                        jee_rank=jee_rank, jee_percentile=jee_percentile, jee_rollno=jee_rollno,
                        ipu_registration=ipu_registration, special_achievements=special_achievements,
                        preference1=preference1, preference2=preference2, preference3=preference3,
                        preference4=preference4, preference5=preference5, preference6=preference6,
                        preference7=preference7, preference8=preference8, preference9=preference9, 
                        preference10=preference10, preference11=preference11, preference12=preference12, preference13=preference13,
                        application_id=application_id, transaction_id=transaction_id,
                        category=category, region=region,
                        ip_address=ip_address, forwarded_address=forwarded_address, browser_info=browser_info, created_at=created_at,)
        newform.save()
        # now saving files after instance is created
        temp_record = BtechTemp.objects.get(application_id=application_id)
        newobj = Btech.objects.get(pk=newform.pk)
        newobj.passport_photo = temp_record.passport_photo
        newobj.jee_result = temp_record.jee_result
        newobj.marksheet_10th = temp_record.marksheet_10th
        newobj.marksheet_12th = temp_record.marksheet_12th
        newobj.aadhaar = temp_record.aadhaar
        newobj.pancard = temp_record.pancard
        newobj.ipuregistrationproof = temp_record.ipuregistrationproof
        newobj.transaction_proof = temp_record.transaction_proof
        newobj.save()
        temp_record.delete()   # deleting the temporary record
        # At this point, form is submitted successfully
        return redirect('btech_preview')
    record = BtechTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'btech/btech.html', context)
    
# Btech Preview
def btech_preview(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    record = Btech.objects.filter(application_id=application_id).first()
    context = {'record': record}
    return render(request, 'btech/btech-preview.html', context)
    
# Edit Btech (after final submission)
def btech_edit(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save" on the /btech-edit.html page
    # so we shall save the data in permanent table and delete from temporary table
    if request.method == 'POST':
        record = Btech.objects.all().filter(application_id = application_id).first()
        record.transaction_id = request.POST.get('transaction_id')
        # category and region
        record.category = request.POST.get('category')
        record.region = request.POST.get('region')
        record.candidate_first_name = request.POST.get('candidate_first_name')
        record.candidate_middle_name = request.POST.get('candidate_middle_name')
        record.candidate_last_name = request.POST.get('candidate_last_name')
        #father mother details
        record.father_first_name = request.POST.get('father_first_name')
        record.father_middle_name = request.POST.get('father_middle_name')
        record.father_last_name = request.POST.get('father_last_name')
        record.mother_first_name = request.POST.get('mother_first_name')
        record.mother_middle_name = request.POST.get('mother_middle_name')
        record.mother_last_name = request.POST.get('mother_last_name')
        record.father_qualification = request.POST.get('father_qualification')
        record.mother_qualification = request.POST.get('mother_qualification')
        record.father_job = request.POST.get('father_job')
        record.mother_job = request.POST.get('mother_job')
        record.father_job_designation = request.POST.get('father_job_designation')
        record.mother_job_designation = request.POST.get('mother_job_designation')
        record.father_business_type = request.POST.get('father_business_type')
        record.mother_business_type = request.POST.get('mother_business_type')
        record.father_number = request.POST.get('father_number')
        record.mother_number = request.POST.get('mother_number')
        record.father_office_address = request.POST.get('father_office_address')
        record.mother_office_address = request.POST.get('mother_office_address')
        #other candidate details
        record.complete_address = request.POST.get('complete_address')
        record.email = request.POST.get('email')
        record.candidate_number = request.POST.get('candidate_number')
        record.gender = request.POST.get('gender')
        #guardian details
        record.guardian_name = request.POST.get('guardian_name')
        #candidate dob
        record.dob = request.POST.get('dob')
        #12th class details
        record.board_12th = request.POST.get('board_12th')
        record.year_of_12th = request.POST.get('year_of_12th')
        record.rollno_12th = request.POST.get('rollno_12th')
        record.school_12th = request.POST.get('school_12th')
        record.aggregate_12th = float(request.POST.get('aggregate_12th'))
        record.maths_12th = request.POST.get('maths_12th')
        record.physics_12th = request.POST.get('physics_12th')
        record.chemistry_12th = request.POST.get('chemistry_12th')
        record.english_12th = request.POST.get('english_12th')
        record.other_subject_12th = request.POST.get('other_subject_12th')
        record.other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        #10th class details
        record.board_10th = request.POST.get('board_10th')
        record.year_of_10th = request.POST.get('year_of_10th')
        record.rollno_10th = request.POST.get('rollno_10th')
        record.school_10th = request.POST.get('school_10th')
        record.aggregate_10th = float(request.POST.get('aggregate_10th'))
        record.maths_10th = request.POST.get('maths_10th')
        record.science_10th = request.POST.get('science_10th')
        record.english_10th = request.POST.get('english_10th')
        record.sst_10th = request.POST.get('sst_10th')
        record.other_subject_10th = request.POST.get('other_subject_10th')
        record.other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        #JEE details
        record.jee_rank = request.POST.get('jee_rank')
        record.jee_percentile = request.POST.get('jee_percentile')
        record.jee_rollno = request.POST.get('jee_rollno')
        #special acheivements
        record.special_achievements = request.POST.get('special_achievements')
        #preference list
        record.preference1 = request.POST.get('preference1')
        record.preference2 = request.POST.get('preference2')
        record.preference3 = request.POST.get('preference3')
        record.preference4 = request.POST.get('preference4')
        record.preference5 = request.POST.get('preference5')
        record.preference6 = request.POST.get('preference6')
        record.preference7 = request.POST.get('preference7')
        record.preference8 = request.POST.get('preference8')
        record.preference9 = request.POST.get('preference9')
        record.preference10 = request.POST.get('preference10')
        record.preference11 = request.POST.get('preference11')
        record.preference12 = request.POST.get('preference12')
        record.preference13 = request.POST.get('preference13')
        record.save()
        # At this point, form is submitted successfully
        return redirect('btech_preview')
    # GET request: render the filled details
    record = Btech.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'btech/btech-edit.html', context)





def btechle1(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /btechle1.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        candidate_first_name = request.POST.get('candidate_first_name')
        candidate_middle_name = request.POST.get('candidate_middle_name')
        candidate_last_name = request.POST.get('candidate_last_name')
        email = request.POST.get('email')
        candidate_number = request.POST.get('candidate_number')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        category = request.POST.get('category')
        region = request.POST.get('region')
        # To track IP address and other info of user coming from request.META header
        ip_address = request.META.get('REMOTE_ADDR','-1')      # return -1 if no address found
        forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR','-1')
        browser_info = request.META.get('HTTP_USER_AGENT','-1')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BtechLETemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.candidate_first_name = candidate_first_name   
            existing_record.candidate_middle_name = candidate_middle_name
            existing_record.candidate_last_name = candidate_last_name
            existing_record.email = email
            existing_record.candidate_number = candidate_number
            existing_record.gender = gender
            existing_record.dob = dob
            existing_record.category = category
            existing_record.region = region
            existing_record.ip_address = ip_address
            existing_record.forwarded_address = forwarded_address
            existing_record.browser_info = browser_info
            existing_record.created_at = created_at
            # saving the updated record
            existing_record.save()
            return redirect ('btechle2')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BtechLETemp(application_id=application_id, ipu_registration=ipu_registration,
                            candidate_first_name=candidate_first_name,
                            candidate_middle_name=candidate_middle_name, candidate_last_name=candidate_last_name,
                            email=email, candidate_number=candidate_number, gender=gender, dob=dob, category=category, region=region,
                            ip_address=ip_address, forwarded_address=forwarded_address, browser_info=browser_info, created_at=created_at,)
            newform.save()
            return redirect ('btechle2')
    # if the request method is not POST, then:
    # either user is coming from login page for the very first time
    # or user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of btechle form by clicking the step-form (progress bar)
    # in all three cases we can render btechle1.html with context
    # to create context we will use the globally available variable application_id
    record = BtechLETemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'btechle/btechle1.html', context)

def btechle2(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /btechle2.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        father_first_name = request.POST.get('father_first_name')
        father_middle_name = request.POST.get('father_middle_name')
        father_last_name = request.POST.get('father_last_name')
        mother_first_name = request.POST.get('mother_first_name')
        mother_middle_name = request.POST.get('mother_middle_name')
        mother_last_name = request.POST.get('mother_last_name')
        father_qualification = request.POST.get('father_qualification')
        mother_qualification = request.POST.get('mother_qualification')
        father_job = request.POST.get('father_job')
        mother_job = request.POST.get('mother_job')
        father_job_designation = request.POST.get('father_job_designation')
        mother_job_designation = request.POST.get('mother_job_designation')
        father_business_type = request.POST.get('father_business_type')
        mother_business_type = request.POST.get('mother_business_type')
        father_number = request.POST.get('father_number')
        mother_number = request.POST.get('mother_number')
        father_office_address = request.POST.get('father_office_address')
        mother_office_address = request.POST.get('mother_office_address')
        guardian_name = request.POST.get('guardian_name')
        complete_address = request.POST.get('complete_address')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BtechLETemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.father_first_name = father_first_name   
            existing_record.father_middle_name = father_middle_name
            existing_record.father_last_name = father_last_name
            existing_record.mother_first_name = mother_first_name   
            existing_record.mother_middle_name = mother_middle_name
            existing_record.mother_last_name = mother_last_name
            existing_record.father_qualification = father_qualification
            existing_record.mother_qualification = mother_qualification
            existing_record.father_job = father_job
            existing_record.mother_job = mother_job
            existing_record.father_job_designation = father_job_designation
            existing_record.mother_job_designation = mother_job_designation
            existing_record.father_business_type = father_business_type   
            existing_record.mother_business_type = mother_business_type
            existing_record.father_office_address = father_office_address
            existing_record.mother_office_address = mother_office_address   
            existing_record.father_number = father_number
            existing_record.mother_number = mother_number
            existing_record.guardian_name = guardian_name   
            existing_record.complete_address = complete_address
            # saving the updated record
            existing_record.save()
            return redirect ('btechle3')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BtechLETemp(application_id=application_id, ipu_registration=ipu_registration, 
                            father_first_name=father_first_name, father_middle_name=father_middle_name, father_last_name=father_last_name,
                            mother_first_name=mother_first_name, mother_middle_name=mother_middle_name, mother_last_name=mother_last_name,
                            father_qualification=father_qualification, mother_qualification=mother_qualification,
                            father_job=father_job, mother_job=mother_job,
                            father_job_designation=father_job_designation, mother_job_designation=mother_job_designation,
                            father_business_type=father_business_type, mother_business_type=mother_business_type,
                            father_number=father_number, mother_number=mother_number,
                            father_office_address=father_office_address, mother_office_address=mother_office_address,
                            complete_address=complete_address, guardian_name=guardian_name,)
            newform.save()
            return redirect ('btechle3')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of btechle form by clicking the step-form (progress bar)
    # or user is coming from btechle1.html after saving his record
    # in all three cases we can render btechle2.html with context
    # to create context we will use the globally available variable application_id
    record = BtechLETemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'btechle/btechle2.html', context)

def btechle3(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /btechle3.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        board_12th = request.POST.get('board_12th')
        year_of_12th = request.POST.get('year_of_12th')
        rollno_12th = request.POST.get('rollno_12th')
        school_12th = request.POST.get('school_12th')
        aggregate_12th = request.POST.get('aggregate_12th')
        maths_12th = request.POST.get('maths_12th')
        physics_12th = request.POST.get('physics_12th')
        chemistry_12th = request.POST.get('chemistry_12th')
        english_12th = request.POST.get('english_12th')
        other_subject_12th = request.POST.get('other_subject_12th')
        other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        board_10th = request.POST.get('board_10th')
        year_of_10th = request.POST.get('year_of_10th')
        rollno_10th = request.POST.get('rollno_10th')
        school_10th = request.POST.get('school_10th')
        aggregate_10th = float(request.POST.get('aggregate_10th'))
        maths_10th = request.POST.get('maths_10th')
        science_10th = request.POST.get('science_10th')
        english_10th = request.POST.get('english_10th')
        sst_10th = request.POST.get('sst_10th')
        other_subject_10th = request.POST.get('other_subject_10th')
        other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        diploma_bsc_type = request.POST.get("diploma")
        board_diploma_bsc = request.POST.get("board_diploma")
        year_of_diploma_bsc = request.POST.get("year_of_diploma")
        rollno_diploma_bsc = request.POST.get("rollno_diploma")
        school_diploma_bsc = request.POST.get("school_diploma")
        aggregate_diploma_bsc = request.POST.get("agg_diploma")
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BtechLETemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.board_12th = board_12th   
            existing_record.year_of_12th = year_of_12th
            existing_record.rollno_12th = rollno_12th
            existing_record.school_12th = school_12th
            existing_record.aggregate_12th = aggregate_12th
            existing_record.maths_12th = maths_12th
            existing_record.physics_12th = physics_12th
            existing_record.chemistry_12th = chemistry_12th
            existing_record.english_12th = english_12th
            existing_record.other_subject_12th = other_subject_12th
            existing_record.other_subject_2_12th = other_subject_2_12th
            existing_record.board_10th = board_10th   
            existing_record.year_of_10th = year_of_10th
            existing_record.rollno_10th = rollno_10th
            existing_record.school_10th = school_10th
            existing_record.aggregate_10th = aggregate_10th
            existing_record.maths_10th = maths_10th
            existing_record.science_10th = science_10th
            existing_record.english_10th = english_10th
            existing_record.sst_10th = sst_10th
            existing_record.other_subject_10th = other_subject_10th
            existing_record.other_subject_2_10th = other_subject_2_10th
            existing_record.diploma_bsc_type = diploma_bsc_type   
            existing_record.board_diploma_bsc = board_diploma_bsc
            existing_record.year_of_diploma_bsc = year_of_diploma_bsc
            existing_record.rollno_diploma_bsc = rollno_diploma_bsc
            existing_record.school_diploma_bsc = school_diploma_bsc
            existing_record.aggregate_diploma_bsc = aggregate_diploma_bsc
            # saving the updated record
            existing_record.save()
            return redirect ('btechle4')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BtechLETemp(application_id=application_id, ipu_registration=ipu_registration,
                            board_12th=board_12th, year_of_12th=year_of_12th, rollno_12th=rollno_12th, school_12th=school_12th,
                            maths_12th=maths_12th, physics_12th=physics_12th, chemistry_12th=chemistry_12th, english_12th=english_12th,
                            other_subject_12th=other_subject_12th, other_subject_2_12th=other_subject_2_12th, aggregate_12th=aggregate_12th, 
                            board_10th=board_10th, year_of_10th=year_of_10th, rollno_10th=rollno_10th, school_10th=school_10th,
                            maths_10th=maths_10th, science_10th=science_10th, english_10th=english_10th, sst_10th=sst_10th,
                            other_subject_10th=other_subject_10th, other_subject_2_10th=other_subject_2_10th, aggregate_10th=aggregate_10th,
                            diploma_bsc_type=diploma_bsc_type, board_diploma_bsc=board_diploma_bsc, year_of_diploma_bsc=year_of_diploma_bsc,
                            rollno_diploma_bsc=rollno_diploma_bsc, school_diploma_bsc=school_diploma_bsc, aggregate_diploma_bsc=aggregate_diploma_bsc,)
            newform.save()
            return redirect ('btechle4')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of btechle form by clicking the step-form (progress bar)
    # or user is coming from btechle2.html after saving his record
    # in all three cases we can render btechle3.html with context
    # to create context we will use the globally available variable application_id
    record = BtechLETemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'btechle/btechle3.html', context)

def btechle4(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /btechle4.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        cet_rank = request.POST.get('cet_rank')
        cet_rollno = request.POST.get('cet_rollno')
        special_achievements = request.POST.get('special_achievements')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BtechLETemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.cet_rank = cet_rank
            existing_record.cet_rollno = cet_rollno
            existing_record.special_achievements = special_achievements
            # saving the updated record
            existing_record.save()
            return redirect ('btechle5')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BtechLETemp(application_id=application_id, ipu_registration=ipu_registration,
                            cet_rank=cet_rank, cet_rollno=cet_rollno, special_achievements=special_achievements,)
            newform.save()
            return redirect ('btechle5')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of btechle form by clicking the step-form (progress bar)
    # or user is coming from btechle3.html after saving his record
    # in all three cases we can render btechle4.html with context
    # to create context we will use the globally available variable application_id
    record = BtechLETemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'btechle/btechle4.html', context)

def btechle5(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /btechle5.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        preference1 = request.POST.get('preference1')
        preference2 = request.POST.get('preference2')
        preference3 = request.POST.get('preference3')
        preference4 = request.POST.get('preference4')
        preference5 = request.POST.get('preference5')
        preference6 = request.POST.get('preference6')
        preference7 = request.POST.get('preference7')
        preference8 = request.POST.get('preference8')
        preference9 = request.POST.get('preference9')
        preference10 = request.POST.get('preference10')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BtechLETemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.preference1 = preference1   
            existing_record.preference2 = preference2
            existing_record.preference3 = preference3
            existing_record.preference4 = preference4
            existing_record.preference5 = preference5
            existing_record.preference6 = preference6
            existing_record.preference7 = preference7
            existing_record.preference8 = preference8
            existing_record.preference9 = preference9
            existing_record.preference10 = preference10
            # saving the updated record
            existing_record.save()
            return redirect ('btechle6')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BtechLETemp(application_id=application_id, ipu_registration=ipu_registration,
                            preference1=preference1, preference2=preference2, preference3=preference3,
                            preference4=preference4, preference5=preference5, preference6=preference6,
                            preference7=preference7, preference8=preference8, preference9=preference9, 
                            preference10=preference10,)
            newform.save()
            return redirect ('btechle6')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of btechle form by clicking the step-form (progress bar)
    # or user is coming from btechle4.html after saving his record
    # in all three cases we can render btechle5.html with context
    # to create context we will use the globally available variable application_id
    record = BtechLETemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'btechle/btechle5.html', context)

def btechle6(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /btechle6.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        passport_photo = request.FILES['passport_photo']
        marksheet_10th = request.FILES['marksheet_10th']
        cet_result = request.FILES['cet_result']
        aadhaar = request.FILES['aadhaar']
        pancard = request.FILES['pancard']
        ipuregistrationproof = request.FILES['ipuregistrationproof']
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BtechLETemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.passport_photo = passport_photo   
            existing_record.marksheet_10th = marksheet_10th
            existing_record.cet_result = cet_result
            if (existing_record.diploma_bsc_type == "Diploma") :
                existing_record.diploma_result = request.FILES['diploma_result']
            else:
                existing_record.marksheet_12th = request.FILES['marksheet_12th']
            existing_record.aadhaar = aadhaar
            existing_record.pancard = pancard
            existing_record.ipuregistrationproof = ipuregistrationproof
            # saving the updated record
            existing_record.save()
            # we will only redirect to payments on /btechle7 if all previous steps are filled
            # so to check that, we will check whether some value on each step is filled or not
            if not existing_record.candidate_first_name:
                return redirect('btechle1')
            if not existing_record.father_first_name:
                return redirect('btechle2')
            if not existing_record.board_10th:
                return redirect('btechle3')
            if not existing_record.cet_rollno:
                return redirect('btechle4')
            if not existing_record.preference1:
                return redirect('btechle5')
            # if all of these details are filled, then we can safely proceed to payment
            return redirect ('btechle7')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BtechLETemp(application_id=application_id, ipu_registration=ipu_registration,
                            passport_photo=passport_photo, marksheet_10th=marksheet_10th,
                            aadhaar=aadhaar, pancard=pancard, ipuregistrationproof=ipuregistrationproof)
            newform.save()
            # if its a new record, then we shall not allow to proceed to payment, so we are redirecting to /btechle1
            return redirect ('btechle1')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of btechle form by clicking the step-form (progress bar)
    # or user is coming from btechle5.html after saving his record
    # in all three cases we can render btechle6.html with context
    # to create context we will use the globally available variable application_id
    record = BtechLETemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'btechle/btechle6.html', context)

def btechle7(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /btechle7.html page
    # so we shall save the data 
    if request.method == "POST" :
        transaction_id = request.POST.get('transaction_id')
        transaction_proof = request.FILES['transaction_proof']
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # (this will never be the case because we are not allowing user to come to /btechle7 if he hasn't already filled previous data , but still handling this case)
        # so, let's check if a record exists or not
        existing_record = BtechLETemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.transaction_id = transaction_id   
            existing_record.transaction_proof = transaction_proof
            # saving the updated record
            existing_record.save()
            # all steps are completed, now redirecting to final preview where data will move from temp table to permanent table 
            return redirect ('btechle')
        else:
            # saving all fields in a new object
            newform = BtechLETemp(application_id=application_id, ipu_registration=ipu_registration,
                                transaction_id=transaction_id, transaction_proof=transaction_proof)
            newform.save()
            return redirect ('btechle')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of btechle form by clicking the step-form (progress bar)
    # or user is coming from btechle6.html after saving his record
    # we shall allow the user only in the case when he has submitted all 6 steps
    record = BtechLETemp.objects.all().filter(application_id = application_id).first()
    # so to check that, we will check whether some value on each step is filled or not
    # before that we can check if record exists or not:
    if not record:
        messages.info(request, 'Please fill candidate details before payment')
        return redirect('btechle1')
    if not record.candidate_first_name:
        messages.info(request, 'Please fill candidate details before payment')
        return redirect('btechle1')
    if not record.father_first_name:
        messages.info(request, 'Please fill parent details before payment')
        return redirect('btechle2')
    if not record.board_10th:
        messages.info(request, 'Please fill educational details before payment')
        return redirect('btechle3')
    if not record.cet_rollno:
        messages.info(request, 'Please fill qualifying details before payment')
        return redirect('btechle4')
    if not record.preference1:
        messages.info(request, 'Please fill choice of programme before payment')
        return redirect('btechle5')
    if not record.passport_photo:
        messages.info(request, 'Please upload documents before payment')
        return redirect("btechle6")
    # if all of these details are filled, then we can safely render /btech7.html
    context = {'record': record}
    return render(request, 'btechle/btechle7.html', context)

# BtechLE
def btechle(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Submit" on the /btech.html page
    # so we shall save the data in permanent table and delete from temporary table
    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id')
        # category and region
        category = request.POST.get('category')
        region = request.POST.get('region')
        candidate_first_name = request.POST.get('candidate_first_name')
        candidate_middle_name = request.POST.get('candidate_middle_name')
        candidate_last_name = request.POST.get('candidate_last_name')
        #father mother details
        father_first_name = request.POST.get('father_first_name')
        father_middle_name = request.POST.get('father_middle_name')
        father_last_name = request.POST.get('father_last_name')
        mother_first_name = request.POST.get('mother_first_name')
        mother_middle_name = request.POST.get('mother_middle_name')
        mother_last_name = request.POST.get('mother_last_name')
        father_qualification = request.POST.get('father_qualification')
        mother_qualification = request.POST.get('mother_qualification')
        father_job = request.POST.get('father_job')
        mother_job = request.POST.get('mother_job')
        father_job_designation = request.POST.get('father_job_designation')
        mother_job_designation = request.POST.get('mother_job_designation')
        father_business_type = request.POST.get('father_business_type')
        mother_business_type = request.POST.get('mother_business_type')
        father_number = request.POST.get('father_number')
        mother_number = request.POST.get('mother_number')
        father_office_address = request.POST.get('father_office_address')
        mother_office_address = request.POST.get('mother_office_address')
        #other candidate details
        complete_address = request.POST.get('complete_address')
        email = request.POST.get('email')
        candidate_number = request.POST.get('candidate_number')
        gender = request.POST.get('gender')
        #guardian details
        guardian_name = request.POST.get('guardian_name')
        #candidate dob
        dob = request.POST.get('dob')
        #12th class details
        board_12th = request.POST.get('board_12th')
        year_of_12th = request.POST.get('year_of_12th')
        rollno_12th = request.POST.get('rollno_12th')
        school_12th = request.POST.get('school_12th')
        aggregate_12th = request.POST.get('aggregate_12th')
        maths_12th = request.POST.get('maths_12th')
        physics_12th = request.POST.get('physics_12th')
        chemistry_12th = request.POST.get('chemistry_12th')
        english_12th = request.POST.get('english_12th')
        other_subject_12th = request.POST.get('other_subject_12th')
        other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        diploma_type = request.POST.get("diploma")
        board_diploma = request.POST.get("board_diploma")
        year_of_diploma = request.POST.get("year_of_diploma")
        rollno_diploma = request.POST.get("rollno_diploma")
        school_diploma = request.POST.get("school_diploma")
        agg_diploma = request.POST.get("agg_diploma")
        #CET details
        cet_rank = request.POST.get('cet_rank')
        cet_rollno = request.POST.get('cet_rollno')
        #10th class details
        board_10th = request.POST.get('board_10th')
        year_of_10th = request.POST.get('year_of_10th')
        rollno_10th = request.POST.get('rollno_10th')
        school_10th = request.POST.get('school_10th')
        aggregate_10th = float(request.POST.get('aggregate_10th'))
        maths_10th = request.POST.get('maths_10th')
        science_10th = request.POST.get('science_10th')
        english_10th = request.POST.get('english_10th')
        sst_10th = request.POST.get('sst_10th')
        other_subject_10th = request.POST.get('other_subject_10th')
        other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        #special acheivements
        special_achievements = request.POST.get('special_achievements')
        #preference list
        preference1 = request.POST.get('preference1')
        preference2 = request.POST.get('preference2')
        preference3 = request.POST.get('preference3')
        preference4 = request.POST.get('preference4')
        preference5 = request.POST.get('preference5')
        preference6 = request.POST.get('preference6')
        preference7 = request.POST.get('preference7')
        preference8 = request.POST.get('preference8')
        preference9 = request.POST.get('preference9')
        preference10 = request.POST.get('preference10')
        # To track IP address and other info of user coming from request.META header
        ip_address = request.META.get('REMOTE_ADDR','-1')      # return -1 if no address found
        forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR','-1')
        browser_info = request.META.get('HTTP_USER_AGENT','-1')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        # saving all fields expect files in a new object
        newform = BtechLE(candidate_first_name=candidate_first_name, candidate_middle_name=candidate_middle_name, candidate_last_name=candidate_last_name,
                            father_first_name=father_first_name, father_middle_name=father_middle_name, father_last_name=father_last_name,
                            mother_first_name=mother_first_name, mother_middle_name=mother_middle_name, mother_last_name=mother_last_name,
                            father_qualification=father_qualification, mother_qualification=mother_qualification,
                            father_job=father_job, mother_job=mother_job,
                            father_job_designation=father_job_designation, mother_job_designation=mother_job_designation,
                            father_business_type=father_business_type, mother_business_type=mother_business_type,
                            father_number=father_number, mother_number=mother_number,
                            father_office_address=father_office_address, mother_office_address=mother_office_address,
                            complete_address=complete_address, candidate_number=candidate_number,
                            guardian_name=guardian_name, email=email, dob=dob, gender=gender,
                            board_12th=board_12th, year_of_12th=year_of_12th, rollno_12th=rollno_12th, school_12th=school_12th,
                            maths_12th=maths_12th, physics_12th=physics_12th, chemistry_12th=chemistry_12th, english_12th=english_12th,
                            other_subject_12th=other_subject_12th, other_subject_2_12th=other_subject_2_12th, aggregate_12th=aggregate_12th, 
                            board_10th=board_10th, year_of_10th=year_of_10th, rollno_10th=rollno_10th, school_10th=school_10th,
                            maths_10th=maths_10th, science_10th=science_10th, english_10th=english_10th, sst_10th=sst_10th,
                            other_subject_10th=other_subject_10th, other_subject_2_10th=other_subject_2_10th, aggregate_10th=aggregate_10th, 
                            cet_rank=cet_rank, cet_rollno=cet_rollno,
                            ipu_registration=ipu_registration, special_achievements=special_achievements,
                            preference1=preference1, preference2=preference2, preference3=preference3, 
                            preference4=preference4, preference5=preference5, preference6=preference6,
                            preference7=preference7, preference8=preference8, preference9=preference9, 
                            preference10=preference10,
                            application_id=application_id, transaction_id=transaction_id, diploma_bsc_type=diploma_type, board_diploma_bsc=board_diploma,
                            year_of_diploma_bsc=year_of_diploma, rollno_diploma_bsc=rollno_diploma, school_diploma_bsc=school_diploma, aggregate_diploma_bsc=agg_diploma,
                            category=category, region=region,
                            ip_address=ip_address, forwarded_address=forwarded_address, browser_info=browser_info, created_at=created_at,)
        newform.save()
        # now saving files after instance is created
        temp_record = BtechLETemp.objects.get(application_id=application_id)
        newobj = BtechLE.objects.get(pk=newform.pk)
        newobj.passport_photo = temp_record.passport_photo
        newobj.cet_result = temp_record.cet_result
        if (newobj.diploma_bsc_type == "Diploma") :
            newobj.diploma_result = temp_record.diploma_result
        else:
            newobj.marksheet_12th = temp_record.marksheet_12th
        newobj.marksheet_10th = temp_record.marksheet_10th
        newobj.aadhaar = temp_record.aadhaar
        newobj.pancard = temp_record.pancard
        newobj.ipuregistrationproof = temp_record.ipuregistrationproof
        newobj.transaction_proof = temp_record.transaction_proof
        newobj.save()
        temp_record.delete()   # deleting the temporary record
        # At this point, form is submitted successfully
        return redirect('btechle_preview')
    record = BtechLETemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'btechle/btechle.html', context)
    
# BtechLE Preview
def btechle_preview(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    record = BtechLE.objects.filter(application_id=application_id).first()
    context = {'record': record}
    return render(request, 'btechle/btechle-preview.html', context)
    
# Edit BtechLE (after final submission)
def btechle_edit(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save" on the /btechle-edit.html page
    # so we shall save the data in permanent table and delete from temporary table
    if request.method == 'POST':
        record = BtechLE.objects.all().filter(application_id = application_id).first()
        record.transaction_id = request.POST.get('transaction_id')
        # category and region
        record.category = request.POST.get('category')
        record.region = request.POST.get('region')
        record.candidate_first_name = request.POST.get('candidate_first_name')
        record.candidate_middle_name = request.POST.get('candidate_middle_name')
        record.candidate_last_name = request.POST.get('candidate_last_name')
        #father mother details
        record.father_first_name = request.POST.get('father_first_name')
        record.father_middle_name = request.POST.get('father_middle_name')
        record.father_last_name = request.POST.get('father_last_name')
        record.mother_first_name = request.POST.get('mother_first_name')
        record.mother_middle_name = request.POST.get('mother_middle_name')
        record.mother_last_name = request.POST.get('mother_last_name')
        record.father_qualification = request.POST.get('father_qualification')
        record.mother_qualification = request.POST.get('mother_qualification')
        record.father_job = request.POST.get('father_job')
        record.mother_job = request.POST.get('mother_job')
        record.father_job_designation = request.POST.get('father_job_designation')
        record.mother_job_designation = request.POST.get('mother_job_designation')
        record.father_business_type = request.POST.get('father_business_type')
        record.mother_business_type = request.POST.get('mother_business_type')
        record.father_number = request.POST.get('father_number')
        record.mother_number = request.POST.get('mother_number')
        record.father_office_address = request.POST.get('father_office_address')
        record.mother_office_address = request.POST.get('mother_office_address')
        #other candidate details
        record.complete_address = request.POST.get('complete_address')
        record.email = request.POST.get('email')
        record.candidate_number = request.POST.get('candidate_number')
        record.gender = request.POST.get('gender')
        #guardian details
        record.guardian_name = request.POST.get('guardian_name')
        #candidate dob
        record.dob = request.POST.get('dob')
        #12th class details
        record.board_12th = request.POST.get('board_12th')
        record.year_of_12th = request.POST.get('year_of_12th')
        record.rollno_12th = request.POST.get('rollno_12th')
        record.school_12th = request.POST.get('school_12th')
        record.aggregate_12th = float(request.POST.get('aggregate_12th'))
        record.maths_12th = request.POST.get('maths_12th')
        record.physics_12th = request.POST.get('physics_12th')
        record.chemistry_12th = request.POST.get('chemistry_12th')
        record.english_12th = request.POST.get('english_12th')
        record.other_subject_12th = request.POST.get('other_subject_12th')
        record.other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        #10th class details
        record.board_10th = request.POST.get('board_10th')
        record.year_of_10th = request.POST.get('year_of_10th')
        record.rollno_10th = request.POST.get('rollno_10th')
        record.school_10th = request.POST.get('school_10th')
        record.aggregate_10th = float(request.POST.get('aggregate_10th'))
        record.maths_10th = request.POST.get('maths_10th')
        record.science_10th = request.POST.get('science_10th')
        record.english_10th = request.POST.get('english_10th')
        record.sst_10th = request.POST.get('sst_10th')
        record.other_subject_10th = request.POST.get('other_subject_10th')
        record.other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        record.diploma_bsc_type = request.POST.get("diploma")
        record.board_diploma_bsc = request.POST.get("board_diploma")
        record.year_of_diploma_bsc = request.POST.get("year_of_diploma")
        record.rollno_diploma_bsc = request.POST.get("rollno_diploma")
        record.school_diploma_bsc = request.POST.get("school_diploma")
        record.aggregate_diploma_bsc = request.POST.get("agg_diploma")
        #CET details
        record.cet_rank = request.POST.get('cet_rank')
        record.cet_rollno = request.POST.get('cet_rollno')
        #special acheivements
        record.special_achievements = request.POST.get('special_achievements')
        #preference list
        record.preference1 = request.POST.get('preference1')
        record.preference2 = request.POST.get('preference2')
        record.preference3 = request.POST.get('preference3')
        record.preference4 = request.POST.get('preference4')
        record.preference5 = request.POST.get('preference5')
        record.preference6 = request.POST.get('preference6')
        record.preference7 = request.POST.get('preference7')
        record.preference8 = request.POST.get('preference8')
        record.preference9 = request.POST.get('preference9')
        record.preference10 = request.POST.get('preference10')
        record.preference11 = request.POST.get('preference11')
        record.preference12 = request.POST.get('preference12')
        record.preference13 = request.POST.get('preference13')
        record.save()
        # At this point, form is submitted successfully
        return redirect('btechle_preview')
    # GET request: render the filled details
    record = BtechLE.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'btechle/btechle-edit.html', context)





def bba1(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bba1.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        candidate_first_name = request.POST.get('candidate_first_name')
        candidate_middle_name = request.POST.get('candidate_middle_name')
        candidate_last_name = request.POST.get('candidate_last_name')
        email = request.POST.get('email')
        candidate_number = request.POST.get('candidate_number')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        category = request.POST.get('category')
        region = request.POST.get('region')
        # To track IP address and other info of user coming from request.META header
        ip_address = request.META.get('REMOTE_ADDR','-1')      # return -1 if no address found
        forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR','-1')
        browser_info = request.META.get('HTTP_USER_AGENT','-1')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BbaTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.candidate_first_name = candidate_first_name   
            existing_record.candidate_middle_name = candidate_middle_name
            existing_record.candidate_last_name = candidate_last_name
            existing_record.email = email
            existing_record.candidate_number = candidate_number
            existing_record.gender = gender
            existing_record.dob = dob
            existing_record.category = category
            existing_record.region = region
            existing_record.ip_address = ip_address
            existing_record.forwarded_address = forwarded_address
            existing_record.browser_info = browser_info
            existing_record.created_at = created_at
            # saving the updated record
            existing_record.save()
            return redirect ('bba2')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BbaTemp(application_id=application_id, ipu_registration=ipu_registration,
                            candidate_first_name=candidate_first_name,
                            candidate_middle_name=candidate_middle_name, candidate_last_name=candidate_last_name,
                            email=email, candidate_number=candidate_number, gender=gender, dob=dob, category=category, region=region,
                            ip_address=ip_address, forwarded_address=forwarded_address, browser_info=browser_info, created_at=created_at,)
            newform.save()
            return redirect ('bba2')
    # if the request method is not POST, then:
    # either user is coming from login page for the very first time
    # or user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bba form by clicking the step-form (progress bar)
    # in all three cases we can render bba1.html with context
    # to create context we will use the globally available variable application_id
    record = BbaTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bba/bba1.html', context)

def bba2(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bba2.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        father_first_name = request.POST.get('father_first_name')
        father_middle_name = request.POST.get('father_middle_name')
        father_last_name = request.POST.get('father_last_name')
        mother_first_name = request.POST.get('mother_first_name')
        mother_middle_name = request.POST.get('mother_middle_name')
        mother_last_name = request.POST.get('mother_last_name')
        father_qualification = request.POST.get('father_qualification')
        mother_qualification = request.POST.get('mother_qualification')
        father_job = request.POST.get('father_job')
        mother_job = request.POST.get('mother_job')
        father_job_designation = request.POST.get('father_job_designation')
        mother_job_designation = request.POST.get('mother_job_designation')
        father_business_type = request.POST.get('father_business_type')
        mother_business_type = request.POST.get('mother_business_type')
        father_number = request.POST.get('father_number')
        mother_number = request.POST.get('mother_number')
        father_office_address = request.POST.get('father_office_address')
        mother_office_address = request.POST.get('mother_office_address')
        guardian_name = request.POST.get('guardian_name')
        complete_address = request.POST.get('complete_address')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BbaTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.father_first_name = father_first_name   
            existing_record.father_middle_name = father_middle_name
            existing_record.father_last_name = father_last_name
            existing_record.mother_first_name = mother_first_name   
            existing_record.mother_middle_name = mother_middle_name
            existing_record.mother_last_name = mother_last_name
            existing_record.father_qualification = father_qualification
            existing_record.mother_qualification = mother_qualification
            existing_record.father_job = father_job
            existing_record.mother_job = mother_job
            existing_record.father_job_designation = father_job_designation
            existing_record.mother_job_designation = mother_job_designation
            existing_record.father_business_type = father_business_type   
            existing_record.mother_business_type = mother_business_type
            existing_record.father_office_address = father_office_address
            existing_record.mother_office_address = mother_office_address   
            existing_record.father_number = father_number
            existing_record.mother_number = mother_number
            existing_record.guardian_name = guardian_name   
            existing_record.complete_address = complete_address
            # saving the updated record
            existing_record.save()
            return redirect ('bba3')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BbaTemp(application_id=application_id, ipu_registration=ipu_registration, 
                            father_first_name=father_first_name, father_middle_name=father_middle_name, father_last_name=father_last_name,
                            mother_first_name=mother_first_name, mother_middle_name=mother_middle_name, mother_last_name=mother_last_name,
                            father_qualification=father_qualification, mother_qualification=mother_qualification,
                            father_job=father_job, mother_job=mother_job,
                            father_job_designation=father_job_designation, mother_job_designation=mother_job_designation,
                            father_business_type=father_business_type, mother_business_type=mother_business_type,
                            father_number=father_number, mother_number=mother_number,
                            father_office_address=father_office_address, mother_office_address=mother_office_address,
                            complete_address=complete_address, guardian_name=guardian_name,)
            newform.save()
            return redirect ('bba3')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bba form by clicking the step-form (progress bar)
    # or user is coming from bba1.html after saving his record
    # in all three cases we can render bba2.html with context
    # to create context we will use the globally available variable application_id
    record = BbaTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bba/bba2.html', context)

def bba3(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bba3.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        board_12th = request.POST.get('board_12th')
        year_of_12th = request.POST.get('year_of_12th')
        rollno_12th = request.POST.get('rollno_12th')
        school_12th = request.POST.get('school_12th')
        aggregate_12th = float(request.POST.get('aggregate_12th'))
        first_subject_12th = request.POST.get('first_subject_12th')
        second_subject_12th = request.POST.get('second_subject_12th')
        third_subject_12th = request.POST.get('third_subject_12th')
        fourth_subject_12th = request.POST.get('fourth_subject_12th')
        other_subject_12th = request.POST.get('other_subject_12th')
        other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        board_10th = request.POST.get('board_10th')
        year_of_10th = request.POST.get('year_of_10th')
        rollno_10th = request.POST.get('rollno_10th')
        school_10th = request.POST.get('school_10th')
        aggregate_10th = float(request.POST.get('aggregate_10th'))
        maths_10th = request.POST.get('maths_10th')
        science_10th = request.POST.get('science_10th')
        english_10th = request.POST.get('english_10th')
        sst_10th = request.POST.get('sst_10th')
        other_subject_10th = request.POST.get('other_subject_10th')
        other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BbaTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.board_12th = board_12th   
            existing_record.year_of_12th = year_of_12th
            existing_record.rollno_12th = rollno_12th
            existing_record.school_12th = school_12th
            existing_record.aggregate_12th = aggregate_12th
            existing_record.first_subject_12th = first_subject_12th
            existing_record.second_subject_12th = second_subject_12th
            existing_record.third_subject_12th = third_subject_12th
            existing_record.fourth_subject_12th = fourth_subject_12th
            existing_record.other_subject_12th = other_subject_12th
            existing_record.other_subject_2_12th = other_subject_2_12th
            existing_record.board_10th = board_10th   
            existing_record.year_of_10th = year_of_10th
            existing_record.rollno_10th = rollno_10th
            existing_record.school_10th = school_10th
            existing_record.aggregate_10th = aggregate_10th
            existing_record.maths_10th = maths_10th
            existing_record.science_10th = science_10th
            existing_record.english_10th = english_10th
            existing_record.sst_10th = sst_10th
            existing_record.other_subject_10th = other_subject_10th
            existing_record.other_subject_2_10th = other_subject_2_10th
            # saving the updated record
            existing_record.save()
            return redirect ('bba4')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BbaTemp(application_id=application_id, ipu_registration=ipu_registration,
                            board_12th=board_12th, year_of_12th=year_of_12th, rollno_12th=rollno_12th, school_12th=school_12th,
                            first_subject_12th=first_subject_12th, second_subject_12th=second_subject_12th, third_subject_12th=third_subject_12th, fourth_subject_12th=fourth_subject_12th,
                            other_subject_12th=other_subject_12th, other_subject_2_12th=other_subject_2_12th, aggregate_12th=aggregate_12th, 
                            board_10th=board_10th, year_of_10th=year_of_10th, rollno_10th=rollno_10th, school_10th=school_10th,
                            maths_10th=maths_10th, science_10th=science_10th, english_10th=english_10th, sst_10th=sst_10th,
                            other_subject_10th=other_subject_10th, other_subject_2_10th=other_subject_2_10th, aggregate_10th=aggregate_10th,)
            newform.save()
            return redirect ('bba4')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bba form by clicking the step-form (progress bar)
    # or user is coming from bba2.html after saving his record
    # in all three cases we can render bba3.html with context
    # to create context we will use the globally available variable application_id
    record = BbaTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bba/bba3.html', context)

def bba4(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bba4.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        cet_or_cuet = request.POST.get('cet_or_cuet')
        cet_rank = request.POST.get('cet_rank')
        cet_rollno = request.POST.get('cet_rollno')
        special_achievements = request.POST.get('special_achievements')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BbaTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.cet_or_cuet = cet_or_cuet   
            existing_record.cet_rank = cet_rank
            existing_record.cet_rollno = cet_rollno
            existing_record.special_achievements = special_achievements
            # saving the updated record
            existing_record.save()
            return redirect ('bba5')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BbaTemp(application_id=application_id, ipu_registration=ipu_registration,
                            cet_rank=cet_rank, cet_rollno=cet_rollno, cet_or_cuet=cet_or_cuet,
                            special_achievements=special_achievements,)
            newform.save()
            return redirect ('bba5')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bba form by clicking the step-form (progress bar)
    # or user is coming from bba3.html after saving his record
    # in all three cases we can render bba4.html with context
    # to create context we will use the globally available variable application_id
    record = BbaTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bba/bba4.html', context)

def bba5(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bba5.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        passport_photo = request.FILES['passport_photo']
        cet_result = request.FILES['cet_result']
        marksheet_10th = request.FILES['marksheet_10th']
        marksheet_12th = request.FILES['marksheet_12th']
        aadhaar = request.FILES['aadhaar']
        pancard = request.FILES['pancard']
        ipuregistrationproof = request.FILES['ipuregistrationproof']
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = BbaTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.passport_photo = passport_photo   
            existing_record.cet_result = cet_result
            existing_record.marksheet_10th = marksheet_10th
            existing_record.marksheet_12th = marksheet_12th
            existing_record.aadhaar = aadhaar
            existing_record.pancard = pancard
            existing_record.ipuregistrationproof = ipuregistrationproof
            # saving the updated record
            existing_record.save()
            # we will only redirect to payments on /bba6 if all previous steps are filled
            # so to check that, we will check whether some value on each step is filled or not
            if not existing_record.candidate_first_name:
                return redirect('bba1')
            if not existing_record.father_first_name:
                return redirect('bba2')
            if not existing_record.board_10th:
                return redirect('bba3')
            if not existing_record.cet_rollno:
                return redirect('bba4')
            # if all of these details are filled, then we can safely proceed to payment
            return redirect ('bba6')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BbaTemp(application_id=application_id, ipu_registration=ipu_registration,
                            passport_photo=passport_photo, cet_result=cet_result, marksheet_10th=marksheet_10th, marksheet_12th=marksheet_12th,
                            aadhaar=aadhaar, pancard=pancard, ipuregistrationproof=ipuregistrationproof)
            newform.save()
            # if its a new record, then we shall not allow to proceed to payment, so we are redirecting to /bba1
            return redirect ('bba1')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bba form by clicking the step-form (progress bar)
    # or user is coming from bba4.html after saving his record
    # in all three cases we can render bba5.html with context
    # to create context we will use the globally available variable application_id
    record = BbaTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bba/bba5.html', context)

def bba6(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /bba6.html page
    # so we shall save the data 
    if request.method == "POST" :
        transaction_id = request.POST.get('transaction_id')
        transaction_proof = request.FILES['transaction_proof']
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # (this will never be the case because we are not allowing user to come to /bba6 if he hasn't already filled previous data , but still handling this case)
        # so, let's check if a record exists or not
        existing_record = BbaTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.transaction_id = transaction_id   
            existing_record.transaction_proof = transaction_proof
            # saving the updated record
            existing_record.save()
            # all steps are completed, now redirecting to final preview where data will move from temp table to permanent table 
            return redirect ('bba')
        else:
            # saving all fields in a new object
            newform = BbaTemp(application_id=application_id, ipu_registration=ipu_registration,
                            transaction_id=transaction_id, transaction_proof=transaction_proof)
            newform.save()
            return redirect ('bba')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of bba form by clicking the step-form (progress bar)
    # or user is coming from bba5.html after saving his record
    # we shall allow the user only in the case when he has submitted all 5 steps
    record = BbaTemp.objects.all().filter(application_id = application_id).first()
    # so to check that, we will check whether some value on each step is filled or not
    # before that we can check if record exists or not:
    if not record:
        messages.info(request, 'Please fill candidate details before payment')
        return redirect('bba1')
    if not record.candidate_first_name:
        messages.info(request, 'Please fill candidate details before payment')
        return redirect('bba1')
    if not record.father_first_name:
        messages.info(request, 'Please fill parent details before payment')
        return redirect('bba2')
    if not record.board_10th:
        messages.info(request, 'Please fill educational details before payment')
        return redirect('bba3')
    if not record.cet_rollno:
        messages.info(request, 'Please fill qualifying details before payment')
        return redirect('bba4')
    if not record.passport_photo:
        messages.info(request, 'Please upload documents before payment')
        return redirect("bba5")
    # if all of these details are filled, then we can safely render /bba6.html
    context = {'record': record}
    return render(request, 'bba/bba6.html', context)

# Bba
def bba(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Submit" on the /bba.html page
    # so we shall save the data in permanent table and delete from temporary table
    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id')
        # category and region
        category = request.POST.get('category')
        region = request.POST.get('region')
        candidate_first_name = request.POST.get('candidate_first_name')
        candidate_middle_name = request.POST.get('candidate_middle_name')
        candidate_last_name = request.POST.get('candidate_last_name')
        #father mother details
        father_first_name = request.POST.get('father_first_name')
        father_middle_name = request.POST.get('father_middle_name')
        father_last_name = request.POST.get('father_last_name')
        mother_first_name = request.POST.get('mother_first_name')
        mother_middle_name = request.POST.get('mother_middle_name')
        mother_last_name = request.POST.get('mother_last_name')
        father_qualification = request.POST.get('father_qualification')
        mother_qualification = request.POST.get('mother_qualification')
        father_job = request.POST.get('father_job')
        mother_job = request.POST.get('mother_job')
        father_job_designation = request.POST.get('father_job_designation')
        mother_job_designation = request.POST.get('mother_job_designation')
        father_business_type = request.POST.get('father_business_type')
        mother_business_type = request.POST.get('mother_business_type')
        father_number = request.POST.get('father_number')
        mother_number = request.POST.get('mother_number')
        father_office_address = request.POST.get('father_office_address')
        mother_office_address = request.POST.get('mother_office_address')
        #other candidate details
        complete_address = request.POST.get('complete_address')
        email = request.POST.get('email')
        candidate_number = request.POST.get('candidate_number')
        gender = request.POST.get('gender')
        #guardian details
        guardian_name = request.POST.get('guardian_name')
        #candidate dob
        dob = request.POST.get('dob')
        #12th class details
        board_12th = request.POST.get('board_12th')
        year_of_12th = request.POST.get('year_of_12th')
        rollno_12th = request.POST.get('rollno_12th')
        school_12th = request.POST.get('school_12th')
        aggregate_12th = float(request.POST.get('aggregate_12th'))
        first_subject_12th = request.POST.get('first_subject_12th')
        second_subject_12th = request.POST.get('second_subject_12th')
        third_subject_12th = request.POST.get('third_subject_12th')
        fourth_subject_12th = request.POST.get('fourth_subject_12th')
        other_subject_12th = request.POST.get('other_subject_12th')
        other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        #10th class details
        board_10th = request.POST.get('board_10th')
        year_of_10th = request.POST.get('year_of_10th')
        rollno_10th = request.POST.get('rollno_10th')
        school_10th = request.POST.get('school_10th')
        aggregate_10th = float(request.POST.get('aggregate_10th'))
        maths_10th = request.POST.get('maths_10th')
        science_10th = request.POST.get('science_10th')
        english_10th = request.POST.get('english_10th')
        sst_10th = request.POST.get('sst_10th')
        other_subject_10th = request.POST.get('other_subject_10th')
        other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        #CET details
        cet_or_cuet = request.POST.get('cet_or_cuet')
        cet_rank = request.POST.get('cet_rank')
        cet_rollno = request.POST.get('cet_rollno')
        #special acheivements
        special_achievements = request.POST.get('special_achievements')
        # To track IP address and other info of user coming from request.META header
        ip_address = request.META.get('REMOTE_ADDR','-1')      # return -1 if no address found
        forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR','-1')
        browser_info = request.META.get('HTTP_USER_AGENT','-1')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        # saving all fields expect files in a new object
        newform = Bba(candidate_first_name=candidate_first_name, candidate_middle_name=candidate_middle_name, candidate_last_name=candidate_last_name,
                        father_first_name=father_first_name, father_middle_name=father_middle_name, father_last_name=father_last_name,
                        mother_first_name=mother_first_name, mother_middle_name=mother_middle_name, mother_last_name=mother_last_name,
                        father_qualification=father_qualification, mother_qualification=mother_qualification,
                        father_job=father_job, mother_job=mother_job,
                        father_job_designation=father_job_designation, mother_job_designation=mother_job_designation,
                        father_business_type=father_business_type, mother_business_type=mother_business_type,
                        father_number=father_number, mother_number=mother_number,
                        father_office_address=father_office_address, mother_office_address=mother_office_address,
                        complete_address=complete_address, candidate_number=candidate_number,
                        guardian_name=guardian_name, email=email, dob=dob, gender=gender,
                        board_12th=board_12th, year_of_12th=year_of_12th, rollno_12th=rollno_12th, school_12th=school_12th,
                        first_subject_12th=first_subject_12th, second_subject_12th=second_subject_12th, third_subject_12th=third_subject_12th, fourth_subject_12th=fourth_subject_12th,
                        other_subject_12th=other_subject_12th, other_subject_2_12th=other_subject_2_12th, aggregate_12th=aggregate_12th, 
                        board_10th=board_10th, year_of_10th=year_of_10th, rollno_10th=rollno_10th, school_10th=school_10th,
                        maths_10th=maths_10th, science_10th=science_10th, english_10th=english_10th, sst_10th=sst_10th,
                        other_subject_10th=other_subject_10th, other_subject_2_10th=other_subject_2_10th, aggregate_10th=aggregate_10th, 
                        cet_rank=cet_rank, cet_rollno=cet_rollno, cet_or_cuet=cet_or_cuet,
                        ipu_registration=ipu_registration, special_achievements=special_achievements,
                        application_id=application_id, transaction_id=transaction_id,
                        category=category, region=region,
                        ip_address=ip_address, forwarded_address=forwarded_address, browser_info=browser_info, created_at=created_at,)
        newform.save()
        # now saving files after instance is created
        temp_record = BbaTemp.objects.get(application_id=application_id)
        newobj = Bba.objects.get(pk=newform.pk)
        newobj.passport_photo = temp_record.passport_photo
        newobj.cet_result = temp_record.cet_result
        newobj.marksheet_10th = temp_record.marksheet_10th
        newobj.marksheet_12th = temp_record.marksheet_12th
        newobj.aadhaar = temp_record.aadhaar
        newobj.pancard = temp_record.pancard
        newobj.ipuregistrationproof = temp_record.ipuregistrationproof
        newobj.transaction_proof = temp_record.transaction_proof
        newobj.save()
        temp_record.delete()   # deleting the temporary record
        # At this point, form is submitted successfully
        return redirect('bba_preview')
    record = BbaTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bba/bba.html', context)
    
# Bba Preview
def bba_preview(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    record = Bba.objects.filter(application_id=application_id).first()
    context = {'record': record}
    return render(request, 'bba/bba-preview.html', context)

# Edit Bba (after final submission)
def bba_edit(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save" on the /bba-edit.html page
    # so we shall save the data in permanent table and delete from temporary table
    if request.method == 'POST':
        record = Bba.objects.all().filter(application_id = application_id).first()
        record.transaction_id = request.POST.get('transaction_id')
        # category and region
        record.category = request.POST.get('category')
        record.region = request.POST.get('region')
        record.candidate_first_name = request.POST.get('candidate_first_name')
        record.candidate_middle_name = request.POST.get('candidate_middle_name')
        record.candidate_last_name = request.POST.get('candidate_last_name')
        #father mother details
        record.father_first_name = request.POST.get('father_first_name')
        record.father_middle_name = request.POST.get('father_middle_name')
        record.father_last_name = request.POST.get('father_last_name')
        record.mother_first_name = request.POST.get('mother_first_name')
        record.mother_middle_name = request.POST.get('mother_middle_name')
        record.mother_last_name = request.POST.get('mother_last_name')
        record.father_qualification = request.POST.get('father_qualification')
        record.mother_qualification = request.POST.get('mother_qualification')
        record.father_job = request.POST.get('father_job')
        record.mother_job = request.POST.get('mother_job')
        record.father_job_designation = request.POST.get('father_job_designation')
        record.mother_job_designation = request.POST.get('mother_job_designation')
        record.father_business_type = request.POST.get('father_business_type')
        record.mother_business_type = request.POST.get('mother_business_type')
        record.father_number = request.POST.get('father_number')
        record.mother_number = request.POST.get('mother_number')
        record.father_office_address = request.POST.get('father_office_address')
        record.mother_office_address = request.POST.get('mother_office_address')
        #other candidate details
        record.complete_address = request.POST.get('complete_address')
        record.email = request.POST.get('email')
        record.candidate_number = request.POST.get('candidate_number')
        record.gender = request.POST.get('gender')
        #guardian details
        record.guardian_name = request.POST.get('guardian_name')
        #candidate dob
        record.dob = request.POST.get('dob')
        #12th class details
        record.board_12th = request.POST.get('board_12th')
        record.year_of_12th = request.POST.get('year_of_12th')
        record.rollno_12th = request.POST.get('rollno_12th')
        record.school_12th = request.POST.get('school_12th')
        record.aggregate_12th = float(request.POST.get('aggregate_12th'))
        record.first_subject_12th = request.POST.get('first_subject_12th')
        record.second_subject_12th = request.POST.get('second_subject_12th')
        record.third_subject_12th = request.POST.get('third_subject_12th')
        record.fourth_subject_12th = request.POST.get('fourth_subject_12th')
        record.other_subject_12th = request.POST.get('other_subject_12th')
        record.other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        #10th class details
        record.board_10th = request.POST.get('board_10th')
        record.year_of_10th = request.POST.get('year_of_10th')
        record.rollno_10th = request.POST.get('rollno_10th')
        record.school_10th = request.POST.get('school_10th')
        record.aggregate_10th = float(request.POST.get('aggregate_10th'))
        record.maths_10th = request.POST.get('maths_10th')
        record.science_10th = request.POST.get('science_10th')
        record.english_10th = request.POST.get('english_10th')
        record.sst_10th = request.POST.get('sst_10th')
        record.other_subject_10th = request.POST.get('other_subject_10th')
        record.other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        #JEE details
        record.cet_rank = request.POST.get('cet_rank')
        record.cet_or_cuet = request.POST.get('cet_or_cuet')
        record.cet_rollno = request.POST.get('cet_rollno')
        #special acheivements
        record.special_achievements = request.POST.get('special_achievements')
        record.save()
        # At this point, form is submitted successfully
        return redirect('bba_preview')
    # GET request: render the filled details
    record = Bba.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'bba/bba-edit.html', context)




def mba1(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /mba1.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        candidate_first_name = request.POST.get('candidate_first_name')
        candidate_middle_name = request.POST.get('candidate_middle_name')
        candidate_last_name = request.POST.get('candidate_last_name')
        email = request.POST.get('email')
        candidate_number = request.POST.get('candidate_number')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        category = request.POST.get('category')
        region = request.POST.get('region')
        # To track IP address and other info of user coming from request.META header
        ip_address = request.META.get('REMOTE_ADDR','-1')      # return -1 if no address found
        forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR','-1')
        browser_info = request.META.get('HTTP_USER_AGENT','-1')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = MbaTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.candidate_first_name = candidate_first_name   
            existing_record.candidate_middle_name = candidate_middle_name
            existing_record.candidate_last_name = candidate_last_name
            existing_record.email = email
            existing_record.candidate_number = candidate_number
            existing_record.gender = gender
            existing_record.dob = dob
            existing_record.category = category
            existing_record.region = region
            existing_record.ip_address = ip_address
            existing_record.forwarded_address = forwarded_address
            existing_record.browser_info = browser_info
            existing_record.created_at = created_at
            # saving the updated record
            existing_record.save()
            return redirect ('mba2')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = MbaTemp(application_id=application_id, ipu_registration=ipu_registration,
                            candidate_first_name=candidate_first_name,
                            candidate_middle_name=candidate_middle_name, candidate_last_name=candidate_last_name,
                            email=email, candidate_number=candidate_number, gender=gender, dob=dob, category=category, region=region,
                            ip_address=ip_address, forwarded_address=forwarded_address, browser_info=browser_info, created_at=created_at,)
            newform.save()
            return redirect ('mba2')
    # if the request method is not POST, then:
    # either user is coming from login page for the very first time
    # or user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of mba form by clicking the step-form (progress bar)
    # in all three cases we can render mba1.html with context
    # to create context we will use the globally available variable application_id
    record = MbaTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'mba/mba1.html', context)

def mba2(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /mba2.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        father_first_name = request.POST.get('father_first_name')
        father_middle_name = request.POST.get('father_middle_name')
        father_last_name = request.POST.get('father_last_name')
        mother_first_name = request.POST.get('mother_first_name')
        mother_middle_name = request.POST.get('mother_middle_name')
        mother_last_name = request.POST.get('mother_last_name')
        father_qualification = request.POST.get('father_qualification')
        mother_qualification = request.POST.get('mother_qualification')
        father_job = request.POST.get('father_job')
        mother_job = request.POST.get('mother_job')
        father_job_designation = request.POST.get('father_job_designation')
        mother_job_designation = request.POST.get('mother_job_designation')
        father_business_type = request.POST.get('father_business_type')
        mother_business_type = request.POST.get('mother_business_type')
        father_number = request.POST.get('father_number')
        mother_number = request.POST.get('mother_number')
        father_office_address = request.POST.get('father_office_address')
        mother_office_address = request.POST.get('mother_office_address')
        guardian_name = request.POST.get('guardian_name')
        complete_address = request.POST.get('complete_address')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = MbaTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.father_first_name = father_first_name   
            existing_record.father_middle_name = father_middle_name
            existing_record.father_last_name = father_last_name
            existing_record.mother_first_name = mother_first_name   
            existing_record.mother_middle_name = mother_middle_name
            existing_record.mother_last_name = mother_last_name
            existing_record.father_qualification = father_qualification
            existing_record.mother_qualification = mother_qualification
            existing_record.father_job = father_job
            existing_record.mother_job = mother_job
            existing_record.father_job_designation = father_job_designation
            existing_record.mother_job_designation = mother_job_designation
            existing_record.father_business_type = father_business_type   
            existing_record.mother_business_type = mother_business_type
            existing_record.father_office_address = father_office_address
            existing_record.mother_office_address = mother_office_address   
            existing_record.father_number = father_number
            existing_record.mother_number = mother_number
            existing_record.guardian_name = guardian_name   
            existing_record.complete_address = complete_address
            # saving the updated record
            existing_record.save()
            return redirect ('mba3')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = MbaTemp(application_id=application_id, ipu_registration=ipu_registration, 
                            father_first_name=father_first_name, father_middle_name=father_middle_name, father_last_name=father_last_name,
                            mother_first_name=mother_first_name, mother_middle_name=mother_middle_name, mother_last_name=mother_last_name,
                            father_qualification=father_qualification, mother_qualification=mother_qualification,
                            father_job=father_job, mother_job=mother_job,
                            father_job_designation=father_job_designation, mother_job_designation=mother_job_designation,
                            father_business_type=father_business_type, mother_business_type=mother_business_type,
                            father_number=father_number, mother_number=mother_number,
                            father_office_address=father_office_address, mother_office_address=mother_office_address,
                            complete_address=complete_address, guardian_name=guardian_name,)
            newform.save()
            return redirect ('mba3')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of mba form by clicking the step-form (progress bar)
    # or user is coming from mba1.html after saving his record
    # in all three cases we can render mba2.html with context
    # to create context we will use the globally available variable application_id
    record = MbaTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'mba/mba2.html', context)

def mba3(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /mba3.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        board_12th = request.POST.get('board_12th')
        year_of_12th = request.POST.get('year_of_12th')
        rollno_12th = request.POST.get('rollno_12th')
        school_12th = request.POST.get('school_12th')
        aggregate_12th = float(request.POST.get('aggregate_12th'))
        first_subject_12th = request.POST.get('first_subject_12th')
        second_subject_12th = request.POST.get('second_subject_12th')
        third_subject_12th = request.POST.get('third_subject_12th')
        fourth_subject_12th = request.POST.get('fourth_subject_12th')
        other_subject_12th = request.POST.get('other_subject_12th')
        other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        board_10th = request.POST.get('board_10th')
        year_of_10th = request.POST.get('year_of_10th')
        rollno_10th = request.POST.get('rollno_10th')
        school_10th = request.POST.get('school_10th')
        aggregate_10th = float(request.POST.get('aggregate_10th'))
        maths_10th = request.POST.get('maths_10th')
        science_10th = request.POST.get('science_10th')
        english_10th = request.POST.get('english_10th')
        sst_10th = request.POST.get('sst_10th')
        other_subject_10th = request.POST.get('other_subject_10th')
        other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        ug_type = request.POST.get("ug_type")
        board_ug = request.POST.get("board_ug")
        year_of_ug = request.POST.get("year_of_ug")
        rollno_ug = request.POST.get("rollno_ug")
        school_ug = request.POST.get("school_ug")
        aggregate_ug = request.POST.get("aggregate_ug")
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = MbaTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.board_12th = board_12th   
            existing_record.year_of_12th = year_of_12th
            existing_record.rollno_12th = rollno_12th
            existing_record.school_12th = school_12th
            existing_record.aggregate_12th = aggregate_12th
            existing_record.first_subject_12th = first_subject_12th
            existing_record.second_subject_12th = second_subject_12th
            existing_record.third_subject_12th = third_subject_12th
            existing_record.fourth_subject_12th = fourth_subject_12th
            existing_record.other_subject_12th = other_subject_12th
            existing_record.other_subject_2_12th = other_subject_2_12th
            existing_record.board_10th = board_10th   
            existing_record.year_of_10th = year_of_10th
            existing_record.rollno_10th = rollno_10th
            existing_record.school_10th = school_10th
            existing_record.aggregate_10th = aggregate_10th
            existing_record.maths_10th = maths_10th
            existing_record.science_10th = science_10th
            existing_record.english_10th = english_10th
            existing_record.sst_10th = sst_10th
            existing_record.other_subject_10th = other_subject_10th
            existing_record.other_subject_2_10th = other_subject_2_10th
            existing_record.ug_type = ug_type
            existing_record.board_ug = board_ug
            existing_record.year_of_ug = year_of_ug
            existing_record.rollno_ug = rollno_ug
            existing_record.school_ug = school_ug
            existing_record.aggregate_ug = aggregate_ug
            # saving the updated record
            existing_record.save()
            return redirect ('mba4')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = MbaTemp(application_id=application_id, ipu_registration=ipu_registration,
                            board_12th=board_12th, year_of_12th=year_of_12th, rollno_12th=rollno_12th, school_12th=school_12th,
                            first_subject_12th=first_subject_12th, second_subject_12th=second_subject_12th, third_subject_12th=third_subject_12th, fourth_subject_12th=fourth_subject_12th,
                            other_subject_12th=other_subject_12th, other_subject_2_12th=other_subject_2_12th, aggregate_12th=aggregate_12th, 
                            board_10th=board_10th, year_of_10th=year_of_10th, rollno_10th=rollno_10th, school_10th=school_10th,
                            maths_10th=maths_10th, science_10th=science_10th, english_10th=english_10th, sst_10th=sst_10th,
                            other_subject_10th=other_subject_10th, other_subject_2_10th=other_subject_2_10th, aggregate_10th=aggregate_10th,
                            ug_type=ug_type, board_ug=board_ug, year_of_ug=year_of_ug, rollno_ug=rollno_ug, school_ug=school_ug,
                            aggregate_ug=aggregate_ug,)
            newform.save()
            return redirect ('mba4')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of mba form by clicking the step-form (progress bar)
    # or user is coming from mba2.html after saving his record
    # in all three cases we can render mba3.html with context
    # to create context we will use the globally available variable application_id
    record = MbaTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'mba/mba3.html', context)

def mba4(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /mba4.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        cat_or_cmat = request.POST.get('cat_or_cmat')
        cat_or_cmat_rank = request.POST.get('cat_or_cmat_rank')
        cat_or_cmat_rollno = request.POST.get('cat_or_cmat_rollno')
        special_achievements = request.POST.get('special_achievements')
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = MbaTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.cat_or_cmat = cat_or_cmat   
            existing_record.cat_or_cmat_rank = cat_or_cmat_rank
            existing_record.cat_or_cmat_rollno = cat_or_cmat_rollno
            existing_record.special_achievements = special_achievements
            # saving the updated record
            existing_record.save()
            return redirect ('mba5')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = BbaTemp(application_id=application_id, ipu_registration=ipu_registration,
                            cat_or_cmat=cat_or_cmat, cat_or_cmat_rank=cat_or_cmat_rank, cat_or_cmat_rollno=cat_or_cmat_rollno,
                            special_achievements=special_achievements,)
            newform.save()
            return redirect ('mba5')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of mba form by clicking the step-form (progress bar)
    # or user is coming from mba3.html after saving his record
    # in all three cases we can render mba4.html with context
    # to create context we will use the globally available variable application_id
    record = MbaTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'mba/mba4.html', context)

def mba5(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /mba5.html page
    # so we shall save the data irrespective of that fact whether there is some already submitted data or not
    if request.method == "POST" :
        passport_photo = request.FILES['passport_photo']
        cat_or_cmat_result = request.FILES['cat_or_cmat_result']
        ug_degree = request.FILES['ug_degree']
        marksheet_10th = request.FILES['marksheet_10th']
        marksheet_12th = request.FILES['marksheet_12th']
        aadhaar = request.FILES['aadhaar']
        pancard = request.FILES['pancard']
        ipuregistrationproof = request.FILES['ipuregistrationproof']
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # so, let's check if a record exists or not
        existing_record = MbaTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.passport_photo = passport_photo   
            existing_record.cat_or_cmat_result = cat_or_cmat_result
            existing_record.marksheet_10th = marksheet_10th
            existing_record.marksheet_12th = marksheet_12th
            existing_record.aadhaar = aadhaar
            existing_record.pancard = pancard
            existing_record.ipuregistrationproof = ipuregistrationproof
            existing_record.ug_degree = ug_degree
            # saving the updated record
            existing_record.save()
            # we will only redirect to payments on /mba6 if all previous steps are filled
            # so to check that, we will check whether some value on each step is filled or not
            if not existing_record.candidate_first_name:
                return redirect('mba1')
            if not existing_record.father_first_name:
                return redirect('mba2')
            if not existing_record.board_10th:
                return redirect('mba3')
            if not existing_record.cat_or_cmat_rollno:
                return redirect('mba4')
            # if all of these details are filled, then we can safely proceed to payment
            return redirect ('mba6')
        else:
            # saving all fields in a new object
            # if the record is existing then it already has application_id and ipu_registration,
            #  but if its getting saved first time then we have to save both of them
            newform = MbaTemp(application_id=application_id, ipu_registration=ipu_registration,
                            passport_photo=passport_photo, cat_or_cmat_result=cat_or_cmat_result, marksheet_10th=marksheet_10th, marksheet_12th=marksheet_12th,
                            aadhaar=aadhaar, pancard=pancard, ipuregistrationproof=ipuregistrationproof, ug_degree=ug_degree,)
            newform.save()
            # if its a new record, then we shall not allow to proceed to payment, so we are redirecting to /mba1
            return redirect ('mba1')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of mba form by clicking the step-form (progress bar)
    # or user is coming from mba4.html after saving his record
    # in all three cases we can render mba5.html with context
    # to create context we will use the globally available variable application_id
    record = MbaTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'mba/mba5.html', context)

def mba6(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save and Next" on the /mba6.html page
    # so we shall save the data 
    if request.method == "POST" :
        transaction_id = request.POST.get('transaction_id')
        transaction_proof = request.FILES['transaction_proof']
        # Now, two cases possible:
        # if a record for this application id already exists , then we will update the existing record
        # else if a record doesn't exist, we will create a new record
        # (this will never be the case because we are not allowing user to come to /mba6 if he hasn't already filled previous data , but still handling this case)
        # so, let's check if a record exists or not
        existing_record = MbaTemp.objects.all().filter(application_id = application_id).first()
        if existing_record :
            # update all fields
            existing_record.transaction_id = transaction_id   
            existing_record.transaction_proof = transaction_proof
            # saving the updated record
            existing_record.save()
            # all steps are completed, now redirecting to final preview where data will move from temp table to permanent table 
            return redirect ('mba')
        else:
            # saving all fields in a new object
            newform = MbaTemp(application_id=application_id, ipu_registration=ipu_registration,
                            transaction_id=transaction_id, transaction_proof=transaction_proof,)
            newform.save()
            return redirect ('mba')
    # if the request method is not POST, then:
    # either user is coming from login page when he has some already submitted fields and we shall display those fields
    # or user is coming from some other part of mba form by clicking the step-form (progress bar)
    # or user is coming from mba5.html after saving his record
    # we shall allow the user only in the case when he has submitted all 5 steps
    record = MbaTemp.objects.all().filter(application_id = application_id).first()
    # so to check that, we will check whether some value on each step is filled or not
    # before that we can check if record exists or not:
    if not record:
        messages.info(request, 'Please fill candidate details before payment')
        return redirect('mba1')
    if not record.candidate_first_name:
        messages.info(request, 'Please fill candidate details before payment')
        return redirect('mba1')
    if not record.father_first_name:
        messages.info(request, 'Please fill parent details before payment')
        return redirect('mba2')
    if not record.board_10th:
        messages.info(request, 'Please fill educational details before payment')
        return redirect('mba3')
    if not record.cat_or_cmat_rollno:
        messages.info(request, 'Please fill qualifying details before payment')
        return redirect('mba4')
    if not record.passport_photo:
        messages.info(request, 'Please upload documents before payment')
        return redirect("mba5")
    # if all of these details are filled, then we can safely render /mba6.html
    context = {'record': record}
    return render(request, 'mba/mba6.html', context)

# Mba
def mba(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Submit" on the /mba.html page
    # so we shall save the data in permanent table and delete from temporary table
    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id')
        # category and region
        category = request.POST.get('category')
        region = request.POST.get('region')
        candidate_first_name = request.POST.get('candidate_first_name')
        candidate_middle_name = request.POST.get('candidate_middle_name')
        candidate_last_name = request.POST.get('candidate_last_name')
        #father mother details
        father_first_name = request.POST.get('father_first_name')
        father_middle_name = request.POST.get('father_middle_name')
        father_last_name = request.POST.get('father_last_name')
        mother_first_name = request.POST.get('mother_first_name')
        mother_middle_name = request.POST.get('mother_middle_name')
        mother_last_name = request.POST.get('mother_last_name')
        father_qualification = request.POST.get('father_qualification')
        mother_qualification = request.POST.get('mother_qualification')
        father_job = request.POST.get('father_job')
        mother_job = request.POST.get('mother_job')
        father_job_designation = request.POST.get('father_job_designation')
        mother_job_designation = request.POST.get('mother_job_designation')
        father_business_type = request.POST.get('father_business_type')
        mother_business_type = request.POST.get('mother_business_type')
        father_number = request.POST.get('father_number')
        mother_number = request.POST.get('mother_number')
        father_office_address = request.POST.get('father_office_address')
        mother_office_address = request.POST.get('mother_office_address')
        #other candidate details
        complete_address = request.POST.get('complete_address')
        email = request.POST.get('email')
        candidate_number = request.POST.get('candidate_number')
        gender = request.POST.get('gender')
        #guardian details
        guardian_name = request.POST.get('guardian_name')
        #candidate dob
        dob = request.POST.get('dob')
        #12th class details
        board_12th = request.POST.get('board_12th')
        year_of_12th = request.POST.get('year_of_12th')
        rollno_12th = request.POST.get('rollno_12th')
        school_12th = request.POST.get('school_12th')
        aggregate_12th = float(request.POST.get('aggregate_12th'))
        first_subject_12th = request.POST.get('first_subject_12th')
        second_subject_12th = request.POST.get('second_subject_12th')
        third_subject_12th = request.POST.get('third_subject_12th')
        fourth_subject_12th = request.POST.get('fourth_subject_12th')
        other_subject_12th = request.POST.get('other_subject_12th')
        other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        #10th class details
        board_10th = request.POST.get('board_10th')
        year_of_10th = request.POST.get('year_of_10th')
        rollno_10th = request.POST.get('rollno_10th')
        school_10th = request.POST.get('school_10th')
        aggregate_10th = float(request.POST.get('aggregate_10th'))
        maths_10th = request.POST.get('maths_10th')
        science_10th = request.POST.get('science_10th')
        english_10th = request.POST.get('english_10th')
        sst_10th = request.POST.get('sst_10th')
        other_subject_10th = request.POST.get('other_subject_10th')
        other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        #ug details
        ug_type = request.POST.get("ug_type")
        board_ug = request.POST.get("board_ug")
        year_of_ug = request.POST.get("year_of_ug")
        rollno_ug = request.POST.get("rollno_ug")
        school_ug = request.POST.get("school_ug")
        aggregate_ug = request.POST.get("aggregate_ug")
        #CAT/CMAT details
        cat_or_cmat = request.POST.get('cat_or_cmat')
        cat_or_cmat_rank = request.POST.get('cat_or_cmat_rank')
        cat_or_cmat_rollno = request.POST.get('cat_or_cmat_rollno')
        #special acheivements
        special_achievements = request.POST.get('special_achievements')
        # To track IP address and other info of user coming from request.META header
        ip_address = request.META.get('REMOTE_ADDR','-1')      # return -1 if no address found
        forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR','-1')
        browser_info = request.META.get('HTTP_USER_AGENT','-1')
        created_at = str(datetime.datetime.now())[:19]        # only first 19 indexes so that it doesnt store microseconds
        # saving all fields expect files in a new object
        newform = Mba(candidate_first_name=candidate_first_name, candidate_middle_name=candidate_middle_name, candidate_last_name=candidate_last_name,
                        father_first_name=father_first_name, father_middle_name=father_middle_name, father_last_name=father_last_name,
                        mother_first_name=mother_first_name, mother_middle_name=mother_middle_name, mother_last_name=mother_last_name,
                        father_qualification=father_qualification, mother_qualification=mother_qualification,
                        father_job=father_job, mother_job=mother_job,
                        father_job_designation=father_job_designation, mother_job_designation=mother_job_designation,
                        father_business_type=father_business_type, mother_business_type=mother_business_type,
                        father_number=father_number, mother_number=mother_number,
                        father_office_address=father_office_address, mother_office_address=mother_office_address,
                        complete_address=complete_address, candidate_number=candidate_number,
                        guardian_name=guardian_name, email=email, dob=dob, gender=gender,
                        board_12th=board_12th, year_of_12th=year_of_12th, rollno_12th=rollno_12th, school_12th=school_12th,
                        first_subject_12th=first_subject_12th, second_subject_12th=second_subject_12th, third_subject_12th=third_subject_12th, fourth_subject_12th=fourth_subject_12th,
                        other_subject_12th=other_subject_12th, other_subject_2_12th=other_subject_2_12th, aggregate_12th=aggregate_12th, 
                        board_10th=board_10th, year_of_10th=year_of_10th, rollno_10th=rollno_10th, school_10th=school_10th,
                        maths_10th=maths_10th, science_10th=science_10th, english_10th=english_10th, sst_10th=sst_10th,
                        other_subject_10th=other_subject_10th, other_subject_2_10th=other_subject_2_10th, aggregate_10th=aggregate_10th, 
                        cat_or_cmat=cat_or_cmat, cat_or_cmat_rank=cat_or_cmat_rank, cat_or_cmat_rollno=cat_or_cmat_rollno,
                        ug_type=ug_type, board_ug=board_ug, year_of_ug=year_of_ug, rollno_ug=rollno_ug, school_ug=school_ug, aggregate_ug=aggregate_ug,
                        ipu_registration=ipu_registration, special_achievements=special_achievements,
                        application_id=application_id, transaction_id=transaction_id,
                        category=category, region=region,
                        ip_address=ip_address, forwarded_address=forwarded_address, browser_info=browser_info, created_at=created_at,)
        newform.save()
        # now saving files after instance is created
        temp_record = MbaTemp.objects.get(application_id=application_id)
        newobj = Mba.objects.get(pk=newform.pk)
        newobj.passport_photo = temp_record.passport_photo
        newobj.cat_or_cmat_result = temp_record.cat_or_cmat_result
        newobj.ug_degree = temp_record.ug_degree
        newobj.marksheet_10th = temp_record.marksheet_10th
        newobj.marksheet_12th = temp_record.marksheet_12th
        newobj.aadhaar = temp_record.aadhaar
        newobj.pancard = temp_record.pancard
        newobj.ipuregistrationproof = temp_record.ipuregistrationproof
        newobj.transaction_proof = temp_record.transaction_proof
        newobj.save()
        temp_record.delete()   # deleting the temporary record
        # At this point, form is submitted successfully
        return redirect('mba_preview')
    record = MbaTemp.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'mba/mba.html', context)
    
# Mba Preview
def mba_preview(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    record = Mba.objects.filter(application_id=application_id).first()
    context = {'record': record}
    return render(request, 'mba/mba-preview.html', context)

# Edit Mba (after final submission)
def mba_edit(request):
    # if user is not logged in, then he shall be redirected to login page
    if not logged_in:
        return redirect('login')
    # if request method is POST, then it means user has clicked on "Save" on the /mba-edit.html page
    # so we shall save the data in permanent table and delete from temporary table
    if request.method == 'POST':
        record = Mba.objects.all().filter(application_id = application_id).first()
        record.transaction_id = request.POST.get('transaction_id')
        # category and region
        record.category = request.POST.get('category')
        record.region = request.POST.get('region')
        record.candidate_first_name = request.POST.get('candidate_first_name')
        record.candidate_middle_name = request.POST.get('candidate_middle_name')
        record.candidate_last_name = request.POST.get('candidate_last_name')
        #father mother details
        record.father_first_name = request.POST.get('father_first_name')
        record.father_middle_name = request.POST.get('father_middle_name')
        record.father_last_name = request.POST.get('father_last_name')
        record.mother_first_name = request.POST.get('mother_first_name')
        record.mother_middle_name = request.POST.get('mother_middle_name')
        record.mother_last_name = request.POST.get('mother_last_name')
        record.father_qualification = request.POST.get('father_qualification')
        record.mother_qualification = request.POST.get('mother_qualification')
        record.father_job = request.POST.get('father_job')
        record.mother_job = request.POST.get('mother_job')
        record.father_job_designation = request.POST.get('father_job_designation')
        record.mother_job_designation = request.POST.get('mother_job_designation')
        record.father_business_type = request.POST.get('father_business_type')
        record.mother_business_type = request.POST.get('mother_business_type')
        record.father_number = request.POST.get('father_number')
        record.mother_number = request.POST.get('mother_number')
        record.father_office_address = request.POST.get('father_office_address')
        record.mother_office_address = request.POST.get('mother_office_address')
        #other candidate details
        record.complete_address = request.POST.get('complete_address')
        record.email = request.POST.get('email')
        record.candidate_number = request.POST.get('candidate_number')
        record.gender = request.POST.get('gender')
        #guardian details
        record.guardian_name = request.POST.get('guardian_name')
        #candidate dob
        record.dob = request.POST.get('dob')
        #12th class details
        record.board_12th = request.POST.get('board_12th')
        record.year_of_12th = request.POST.get('year_of_12th')
        record.rollno_12th = request.POST.get('rollno_12th')
        record.school_12th = request.POST.get('school_12th')
        record.aggregate_12th = float(request.POST.get('aggregate_12th'))
        record.first_subject_12th = request.POST.get('first_subject_12th')
        record.second_subject_12th = request.POST.get('second_subject_12th')
        record.third_subject_12th = request.POST.get('third_subject_12th')
        record.fourth_subject_12th = request.POST.get('fourth_subject_12th')
        record.other_subject_12th = request.POST.get('other_subject_12th')
        record.other_subject_2_12th =  request.POST.get('other_subject_2_12th')
        #10th class details
        record.board_10th = request.POST.get('board_10th')
        record.year_of_10th = request.POST.get('year_of_10th')
        record.rollno_10th = request.POST.get('rollno_10th')
        record.school_10th = request.POST.get('school_10th')
        record.aggregate_10th = float(request.POST.get('aggregate_10th'))
        record.maths_10th = request.POST.get('maths_10th')
        record.science_10th = request.POST.get('science_10th')
        record.english_10th = request.POST.get('english_10th')
        record.sst_10th = request.POST.get('sst_10th')
        record.other_subject_10th = request.POST.get('other_subject_10th')
        record.other_subject_2_10th =  request.POST.get('other_subject_2_10th')
        #ug details
        record.ug_type = request.POST.get("ug_type")
        record.board_ug = request.POST.get("board_ug")
        record.year_of_ug = request.POST.get("year_of_ug")
        record.rollno_ug = request.POST.get("rollno_ug")
        record.school_ug = request.POST.get("school_ug")
        record.aggregate_ug = request.POST.get("aggregate_ug")
        #CAT/CMAT details
        record.cat_or_cmat_rank = request.POST.get('cat_or_cmat_rank')
        record.cat_or_cmat = request.POST.get('cat_or_cmat')
        record.cat_or_cmat_rollno = request.POST.get('cat_or_cmat_rollno')
        #special acheivements
        record.special_achievements = request.POST.get('special_achievements')
        record.save()
        # At this point, form is submitted successfully
        return redirect('mba_preview')
    # GET request: render the filled details
    record = Mba.objects.all().filter(application_id = application_id).first()
    context = {'record': record}
    return render(request, 'mba/mba-edit.html', context)