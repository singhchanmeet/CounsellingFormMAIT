# This file contains utility functions
# (rename functions for file upload)
# we are renaming everything by ipu_registration because that is unique for every candidate
import os

#Btech rename functions
def btech_photo_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/btech/photographs')):
            if (each_file == new_name):
                os.remove(os.path.join('media/btech/photographs', new_name))
        return os.path.join('btech/photographs', new_name)
    else:
        return filename
    
def btech_jeeresult_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/btech/jeeresult')):
            if (each_file == new_name):
                os.remove(os.path.join('media/btech/jeeresult', new_name))
        return os.path.join('btech/jeeresult', new_name)
    else:
        return filename
    
def btech_10thmarksheet_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/btech/marksheet10th')):
            if (each_file == new_name):
                os.remove(os.path.join('media/btech/marksheet10th', new_name))
        return os.path.join('btech/marksheet10th', new_name)
    else:
        return filename    
    
def btech_12thmarksheet_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file
        for each_file in os.listdir(os.path.join('media/btech/marksheet12th')):
            if (each_file == new_name):
                os.remove(os.path.join('media/btech/marksheet12th', new_name))
        return os.path.join('btech/marksheet12th', new_name)
    else:
        return filename
    
def btech_aadhar_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file
        for each_file in os.listdir(os.path.join('media/btech/aadhar')):
            if (each_file == new_name):
                os.remove(os.path.join('media/btech/aadhar', new_name))
        return os.path.join('btech/aadhar', new_name)
    else:
        return filename

def btech_pancard_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/btech/pancard')):
            if (each_file == new_name):
                os.remove(os.path.join('media/btech/pancard', new_name))
        return os.path.join('btech/pancard', new_name)
    else:
        return filename
    
def btech_ipuregistration_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/btech/ipuregistration')):
            if (each_file == new_name):
                os.remove(os.path.join('media/btech/ipuregistration', new_name))
        return os.path.join('btech/ipuregistration', new_name)
    else:
        return filename

def btech_transaction_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/btech/transactions')):
            if (each_file == new_name):
                os.remove(os.path.join('media/btech/transactions', new_name))
        return os.path.join('btech/transactions', new_name)
    else:
        return filename
    
def btech_counselling_transaction_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/btech/counselling_transactions')):
            if (each_file == new_name):
                os.remove(os.path.join('media/btech/counselling_transactions', new_name))
        return os.path.join('btech/counselling_transactions', new_name)
    else:
        return filename
    


#Btech LE rename functions
def btech_le_photo_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # If we change a already uploaded file or image from admin panel
        # then to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/btechle/photographs')):
            if (each_file == new_name):
                os.remove(os.path.join('media/btechle/photographs', new_name))
        return os.path.join('btechle/photographs', new_name)
    else:
        return filename
    
def btech_le_cetresult_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # If we change a already uploaded file or image from admin panel
        # then to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/btechle/cetresult')):
            if (each_file == new_name):
                os.remove(os.path.join('media/btechle/cetresult', new_name))
        return os.path.join('btechle/cetresult', new_name)
    else:
        return filename
    
def btech_le_diplomaresult_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # If we change a already uploaded file or image from admin panel
        # then to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/btechle/diplomaresult')):
            if (each_file == new_name):
                os.remove(os.path.join('media/btechle/diplomaresult', new_name))
        return os.path.join('btechle/diplomaresult', new_name)
    else:
        return filename

def btech_le_10thmarksheet_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # If we change a already uploaded file or image from admin panel
        # then to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/btechle/marksheet10th')):
            if (each_file == new_name):
                os.remove(os.path.join('media/btechle/marksheet10th', new_name))
        return os.path.join('btechle/marksheet10th', new_name)
    else:
        return filename    
    
def btech_le_12thmarksheet_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # If we change a already uploaded file or image from admin panel
        # then to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/btechle/marksheet12th')):
            if (each_file == new_name):
                os.remove(os.path.join('media/btechle/marksheet12th', new_name))
        return os.path.join('btechle/marksheet12th', new_name)
    else:
        return filename
    
def btech_le_aadhar_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # If we change a already uploaded file or image from admin panel
        # then to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/btechle/aadhar')):
            if (each_file == new_name):
                os.remove(os.path.join('media/btechle/aadhar', new_name))
        return os.path.join('btechle/aadhar', new_name)
    else:
        return filename

def btech_le_pancard_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # If we change a already uploaded file or image from admin panel
        # then to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/btechle/pancard')):
            if (each_file == new_name):
                os.remove(os.path.join('media/btechle/pancard', new_name))
        return os.path.join('btechle/pancard', new_name)
    else:
        return filename
    
def btech_le_ipuregistration_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # If we change a already uploaded file or image from admin panel
        # then to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/btechle/ipuregistration')):
            if (each_file == new_name):
                os.remove(os.path.join('media/btechle/ipuregistration', new_name))
        return os.path.join('btechle/ipuregistration', new_name)
    else:
        return filename

def btech_le_transaction_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # If we change a already uploaded file or image from admin panel
        # then to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/btechle/transactions')):
            if (each_file == new_name):
                os.remove(os.path.join('media/btechle/transactions', new_name))
        return os.path.join('btechle/transactions', new_name)
    else:
        return filename
        
def btechle_ug_degree_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.rollno_diploma_bsc, ext)
        # If we change a already uploaded file or image from admin panel
        # then to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/btechle/ug-degree')):
            if (each_file == new_name):
                os.remove(os.path.join('media/btechle/ug-degree', new_name))
        return os.path.join('btechle/ug-degree', new_name)
    else:
        return filename

def btechle_counselling_transaction_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/btech/counselling_transactions')):
            if (each_file == new_name):
                os.remove(os.path.join('media/btech/counselling_transactions', new_name))
        return os.path.join('btech/counselling_transactions', new_name)
    else:
        return filename
    



#BBA rename functions
def bba_photo_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bba/photographs')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bba/photographs', new_name))
        return os.path.join('bba/photographs', new_name)
    else:
        return filename
    
def bba_cetresult_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bba/cetresult')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bba/cetresult', new_name))
        return os.path.join('bba/cetresult', new_name)
    else:
        return filename
    
def bba_10thmarksheet_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bba/marksheet10th')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bba/marksheet10th', new_name))
        return os.path.join('bba/marksheet10th', new_name)
    else:
        return filename    
    
def bba_12thmarksheet_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file
        for each_file in os.listdir(os.path.join('media/bba/marksheet12th')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bba/marksheet12th', new_name))
        return os.path.join('bba/marksheet12th', new_name)
    else:
        return filename
    
def bba_aadhar_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file
        for each_file in os.listdir(os.path.join('media/bba/aadhar')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bba/aadhar', new_name))
        return os.path.join('bba/aadhar', new_name)
    else:
        return filename

def bba_pancard_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bba/pancard')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bba/pancard', new_name))
        return os.path.join('bba/pancard', new_name)
    else:
        return filename
    
def bba_ipuregistration_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bba/ipuregistration')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bba/ipuregistration', new_name))
        return os.path.join('bba/ipuregistration', new_name)
    else:
        return filename

def bba_transaction_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bba/transactions')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bba/transactions', new_name))
        return os.path.join('bba/transactions', new_name)
    else:
        return filename
    
def bba_counselling_transaction_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/bba/counselling_transactions')):
            if (each_file == new_name):
                os.remove(os.path.join('media/bba/counselling_transactions', new_name))
        return os.path.join('bba/counselling_transactions', new_name)
    else:
        return filename
    



#MBA rename functions
def mba_photo_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/mba/photographs')):
            if (each_file == new_name):
                os.remove(os.path.join('media/mba/photographs', new_name))
        return os.path.join('mba/photographs', new_name)
    else:
        return filename
    
def mba_cat_or_cmat_result_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/mba/cat-cmat-result')):
            if (each_file == new_name):
                os.remove(os.path.join('media/mba/cat-cmat-result', new_name))
        return os.path.join('mba/cat-cmat-result', new_name)
    else:
        return filename
    
def mba_10thmarksheet_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/mba/marksheet10th')):
            if (each_file == new_name):
                os.remove(os.path.join('media/mba/marksheet10th', new_name))
        return os.path.join('mba/marksheet10th', new_name)
    else:
        return filename    
    
def mba_12thmarksheet_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file
        for each_file in os.listdir(os.path.join('media/mba/marksheet12th')):
            if (each_file == new_name):
                os.remove(os.path.join('media/mba/marksheet12th', new_name))
        return os.path.join('mba/marksheet12th', new_name)
    else:
        return filename
    
def mba_aadhar_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file
        for each_file in os.listdir(os.path.join('media/mba/aadhar')):
            if (each_file == new_name):
                os.remove(os.path.join('media/mba/aadhar', new_name))
        return os.path.join('mba/aadhar', new_name)
    else:
        return filename

def mba_pancard_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/mba/pancard')):
            if (each_file == new_name):
                os.remove(os.path.join('media/mba/pancard', new_name))
        return os.path.join('mba/pancard', new_name)
    else:
        return filename
    
def mba_ipuregistration_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/mba/ipuregistration')):
            if (each_file == new_name):
                os.remove(os.path.join('media/mba/ipuregistration', new_name))
        return os.path.join('mba/ipuregistration', new_name)
    else:
        return filename

def mba_transaction_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/mba/transactions')):
            if (each_file == new_name):
                os.remove(os.path.join('media/mba/transactions', new_name))
        return os.path.join('mba/transactions', new_name)
    else:
        return filename
    
def mba_counselling_transaction_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/mba/counselling_transactions')):
            if (each_file == new_name):
                os.remove(os.path.join('media/mba/counselling_transactions', new_name))
        return os.path.join('mba/counselling_transactions', new_name)
    else:
        return filename
    
def mba_ug_degree_rename(instance, filename):
    ext = filename.split('.')[-1]
    if instance.pk:
        new_name = '{}.{}'.format(instance.ipu_registration, ext)
        # 1) When we move the record from temporary to permanent table
        # 2) If we change a already uploaded file or image from admin panel
        # then in both cases to avoid naming conflict, we first remove the already uploaded file 
        for each_file in os.listdir(os.path.join('media/mba/ug-degree')):
            if (each_file == new_name):
                os.remove(os.path.join('media/mba/ug-degree', new_name))
        return os.path.join('mba/ug-degree', new_name)
    else:
        return filename