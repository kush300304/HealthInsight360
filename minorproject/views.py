from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from doctor.models import *
from patient.models import *
import pandas as pd
# import matplotlib.pyplot as plt
from datetime import datetime
import time
from .models import *


def home(request):
    key = request.session.get('key')
    context = {
        'key': key
    }
    return render(request,'minorproject/home.html',context)

def encounters(request):
    # key = request.session.get('key')
    # context = {
    #     'key': key
    # }
    return render(request,'minorproject/encounters.html')

def profile(request, user):
	key = request.session.get('key')
	print(request.user)
	userid = User.objects.get(username=request.user)
	print(userid)
	# if request.user:
	# 	status = request.user
	if request.method == "POST":
		print(request.POST['name'])
		if key == "P":
			update = Patient.objects.get(username=userid)
			update.name = request.POST['name']
			update.phone = request.POST['phone']
			update.email = request.POST['email']
			update.gender = request.POST['gender']
			update.age = request.POST['age']
			update.blood = request.POST['blood']
			update.address = request.POST['address']
			userid.username=request.POST['name']
			userid.save()
			update.save()
			return redirect('minor-home')
		else:
			update = Doctor.objects.get(username=userid)
			update.name = request.POST['name']
			update.phone = request.POST['phone']
			update.email = request.POST['email']
			update.gender = request.POST['gender']
			update.age = request.POST['age']
			update.department=request.POST['department']     
			update.address = request.POST['address']
			update.Specializations=request.POST['specializations']
			userid.username=request.POST['name']
			userid.save()
			update.save()
			return redirect('minor-home')


	if key == "P":
		userdata = Patient.objects.get(username=userid)
		return render(request  , 'patient/profile.html',{'userdata' : userdata , 'user':user})

	else:
		userdata  = Doctor.objects.get(username=userid)
		return render(request  , 'doctor/profile.html',{'userdata' : userdata , 'user':user})


	return redirect('minor-home')

def dashboard(request,user):
    key = request.session.get('key')
    if request.method=="GET":
        if key=="D":
            return render(request,"doctor/dashboard.html")
        else:
            return render(request,"patient/dashboard.html")
    else:
        return HttpResponse("Error 404!")
    
def logins(request):
    return render(request,'minorproject/logins.html')

def search(request):
    return render(request,'minorproject/search.html')


# Function to strip double quotes from a string
def strip_double_quotes(s):
    if isinstance(s, str):
        return s.strip('"')
    else:
        return s


# Function to update plot
def update_plot():
    try:
        # Read CSV file 'patients.csv'
        df = pd.read_csv(r"C:\Users\kusha\Desktop\healthinsight\Python\files\`patients`.csv")

        # Strip double quotes from the 'BIRTHDATE' column
        df['BIRTHDATE'] = df['BIRTHDATE'].apply(strip_double_quotes)

        # Convert 'BIRTHDATE' strings to datetime objects
        df['BIRTHDATE'] = pd.to_datetime(df['BIRTHDATE'], format='%Y-%m-%d')

        # Calculate age for each patient
        now = pd.Timestamp('now')
        df['AGE'] = (now - df['BIRTHDATE']).dt.days / 365.25  # Divide by number of days in a year

        # Plot age distribution
        # plt.clf()  # Clear existing plot
        # plt.hist(df['AGE'], bins=20, color='skyblue', edgecolor='black')
        # plt.xlabel('Age')
        # plt.ylabel('Frequency')
        # plt.title('Age Distribution of Patients')
        # plt.grid(True)
        # plt.savefig(r'C:\Users\kusha\Desktop\healthinsight\minorproject\static\img\plot.png')  # Save plot image
    except Exception as e:
        print("Error:", e)


def insights(request):
      update_plot()
      #Render the page with the plot
      return render(request,'minorproject/insights.html')

def search_medicines(request):
    query = request.GET.get('query', '')
    if len(query) < 3:
        return render(request, 'minorproject/searchmed.html', {'error': 'Query too short'})

    medicines = Medication.objects.filter(name__icontains=query)
    results = set()  # Initialize results as a set

    for med in medicines:
        result = (
            med.name,
            tuple([med.substitute0, med.substitute1, med.substitute2, med.substitute3, med.substitute4]),
            tuple([med.sideeffect0, med.sideeffect1, med.sideeffect2, med.sideeffect3, med.sideeffect4, med.sideeffect5, med.sideeffect6, med.sideeffect7, med.sideeffect8, med.sideeffect9, med.sideeffect10, med.sideeffect11, med.sideeffect12, med.sideeffect13, med.sideeffect14]),
            tuple([med.use0, med.use1, med.use2, med.use3, med.use4]),
            med.chemical_class,
            med.therapeutic_class
        )
        results.add(result)

    # Convert results back to list of dictionaries
    results = [
        {
            'name': med[0],
            'substitutes': list(med[1]),
            'sideEffects': list(med[2]),
            'uses': list(med[3]),
            'chemicalClass': med[4],
            'therapeuticClass': med[5]
        }
        for med in results
    ]

    return render(request, 'minorproject/searchmed.html', {'results': results})


def autocomplete(request):
    term = request.GET.get('term')
    suggestions = list(Medication.objects.filter(name__istartswith=term)[:10].values_list('name', flat=True))
    return JsonResponse({'suggestions': suggestions})
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

def send_email(request):
    subject = request.POST.get("subject", "")
    message = request.POST.get("message", "")
    from_email = request.POST.get("from_email", "")
    
    if subject and message and from_email:
        try:
            send_mail(
                subject,
                message, 
                settings.EMAIL_HOST_USER,  # Use the actual value of EMAIL_HOST_USER
                [from_email]  # Use the actual value of from_email
            )
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        return render(request,'minorproject/send_email.html')  # Correct the redirection URL
    else:
        # In reality, we'd use a form class to get proper validation errors.
        return HttpResponse("Make sure all fields are entered and valid.")
    
def reports(request,user):
    # key = request.session.get('key')
    # context = {
    #     'key': key
    # }

    return render(request,"minorproject/reports.html")

from datetime import datetime

def encounters(request):
    query = request.GET.get('query', '')
    query = f'"{query}'
    encounters = Encounters.objects.filter(patient__startswith=query)
    return render(request,"minorproject/encounters.html",{'encounters':encounters})


def records(request,encount_id):
    query = encount_id
    results = {}
    print(query)
    # studies = {}
    
    # # Filter encounters for the given patient ID
    encounters = Encounters.objects.filter(id=query)#enco class
    print(encounters)
    
    for encounter in encounters: 
        print(f"Fetching records for Encounter ID: {encounter.id}")
        
        # Fetch related records from other tables for the current encounter
        imaging_studies = ImagingStudies.objects.filter(encounter=encount_id) #bodysite_des sop_des
        medications = Medications.objects.filter(encounter=encounter.id)#reasondes totalcost
        immunizations = Immunizations.objects.filter(encounter=encounter.id)#descrip
        conditions = Conditions.objects.filter(encounter=encounter.id)#description
        allergies = Allergies.objects.filter(encounter=encounter.id)#des
        careplans = Careplans.objects.filter(encounter=encounter.id)#reasondes
        observations = Observations.objects.filter(encounter=encounter.id)#desc
        procedures = Procedures.objects.filter(encounter=encounter.id)#reason

        # Fetch organization name for the current encounter
        organizations = Organizations.objects.filter(id=encounter.organization) #hos name hos city phone no
        # org_name = organization_name.name if organization_name else None

        # Add the related records to the results dictionary
        result = {
            'encounter': encounter,
            'imaging_studies':imaging_studies,
            'medications': medications,
            'immunizations': immunizations,
            'conditions': conditions,
            'allergies': allergies,
            'careplans': careplans,
            'observations': observations,
            'procedures': procedures,
            'organizations':organizations,
        }
        results[encounter.id] = result

        # Add imaging studies to the studies dictionary
        # for study in imaging_studies:
        #     print(f"Adding imaging study {study.id} to studies dictionary")
        #     hello = {
        #         'study_date' : study.date,
        #         'study_bodysite_code' : study.bodysite_code,
        #         'study_bodysite_description' : study.bodysite_description,
        #         'study_modality_code' : study.modality_code,
        #         'study_modality_description' : study.modality_description,
        #         'study_sop_code' : study.sop_code,
        #         'study_sop_description' :  study.sop_description
        #     }
        #     studies[study.id] = hello

    return render(request, 'minorproject/records.html', {'results': results.values()})


# def records(request):
#     query = request.GET.get('query', '')
#     desc=[]
#     results=[]
#     studies=[]
    
#     # Filter medicines whose name starts with the first 8 digits of the query
#     encount = Encounters.objects.filter(patient__startswith=query)
#     studd   = ImagingStudies.objects.filter(patient__startswith=query)
#     print(studd)
#     print(encount)
#     for med in encount:
#         desc.append(med.description)
#         # print(med.organization)
#         obs=Organizations.objects.filter(id=med.organization)
#         # print(obs)
#         for obbb in obs:
             
#             result={
#                 'desc': med.description,
#                 'name': obbb.name,
#                 'city': obbb.city,
#                 'phone':obbb.phone
#             }
#             results.append(result)
#         for study in studd:
#              stud={
#               'study_id': study.id,
#              'study_date': study.date
#          }
#              print(stud)
#              studies.append(stud)

         
         
         


#     # print(results)
#     return render(request, 'minorproject/records.html', {'results': results, 'studies': studies})
