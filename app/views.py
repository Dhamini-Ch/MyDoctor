import cv2
import keras
import pickle
import numpy as np
from PIL import Image
import tensorflow as tf
import keras.utils as image
from django.template import loader
from django.shortcuts import render
from keras.preprocessing import image
from sklearn.preprocessing import StandardScaler
from django.views.decorators.csrf import csrf_exempt
from tensorflow.python.keras.models import load_model
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
sc = StandardScaler()


def home(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def heartview(request):
    template = loader.get_template('heartHTML.html')
    return HttpResponse(template.render())

def strokeview(request):
    template = loader.get_template('strokeHTML.html')
    return HttpResponse(template.render())

@csrf_exempt
def predictStroke(request):
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    hp = request.POST.get('hp')
    hd = request.POST.get('hd')
    m = request.POST.get('m')
    work = request.POST.get('work')
    resi = request.POST.get('resi')
    glucose = request.POST.get('glucose')
    smk = request.POST.get('smk')

    file_path = "C:/Users/aksha_fhy2u73/Downloads/strokePickle.pkl"
    with open(file_path, 'rb') as f:
        strokemodel = pickle.load(f)
    b = np.array([age]).reshape(1, -1)
    b = sc.fit_transform(b)
    bool1 = [gender, hp, hd, m, work, resi, glucose, smk]
    b = np.append(b, bool1).reshape(1, -1)
    prediction = strokemodel.predict(b)

    if prediction == 1:
        msg = "You must be careful as there are chances of you getting a stroke. Kindly better consult a doctor"
    else:
        msg = "The results indicate that you are not at risk of getting stroke!"
    context = {
        'msg': msg,
    }
    return render(request, 'strokeHTML.html', context)

@csrf_exempt
def predictHeart(request):
    age = request.POST.get('AGE')
    cigar = request.POST.get('CIGAR')
    cholestrol = request.POST.get('CHOLESTROL')
    sysbp = request.POST.get('SYSBP')
    diabp = request.POST.get('DIABP')
    bmi = request.POST.get('BMI')
    heartrate = request.POST.get('HEARTRATE')
    glucose = request.POST.get('GLUCOSE')
    smoker = request.POST.get('SMOKER')
    gender = request.POST.get('GENDER')
    bpmeds = request.POST.get('BPMEDS')
    stroke = request.POST.get('STROKE')
    diabetes = request.POST.get('DIABETES')

    file_path = 'C:/Users/aksha_fhy2u73/Downloads/heartPickle.pkl'
    with open(file_path, 'rb') as f:
        heartmodel = pickle.load(f)
    a = np.array([age, cigar, cholestrol, sysbp, diabp, bmi, heartrate, glucose]).reshape(1, -1)
    a = sc.fit_transform(a)
    bool1 = [gender, smoker, bpmeds, stroke, diabetes]
    a = np.append(a, bool1).reshape(1, -1)
    prediction = heartmodel.predict(a)
    if prediction > 0.5:
        msg ='You must be careful as there are chances of you getting a heart disease. Kindly better consult a doctor'
    else:
        msg= "You have come up negative for heart diseases!"
    context = {
        'msg': msg,
    }
    return render(request, 'heartHTML.html', context)


def prescriptionview(request):
    template = loader.get_template('prescriptionHTML.html')
    return HttpResponse(template.render())

@csrf_exempt
def predictPrescription(request):
    cold = request.POST.get('cold')
    fever = request.POST.get('fever')
    nau = request.POST.get('nau')
    head = request.POST.get('head')
    sore = request.POST.get('sore')

    file_path = "C:/Users/aksha_fhy2u73/Downloads/Hack24thon/drugPickle.pkl"
    with open(file_path, 'rb') as f:
        prescriptionmodel = pickle.load(f)
    x2 = np.array([fever, head, sore, nau, cold]).reshape(1, -1)
    prediction = prescriptionmodel.predict(x2)
    if ((prediction) == 0):
        msg1 = "Acetaminophen"
    elif ((prediction) == 1):
        msg1 = "Asprin"
    elif ((prediction) == 2):
        msg1 ="Bismol"
    elif ((prediction) == 3):
        msg1 ="Bismuth subsalicylate"
    elif ((prediction) == 4):
        msg1 ="Cetirizine"
    elif ((prediction) == 5):
        msg1 ="Diphenhydramine"
    elif ((prediction) == 6):
        msg1 ="Ibuprofen"
    elif ((prediction) == 7):
        msg1 ="Naproxen"
    elif ((prediction) == 8):
        msg1 ="Paracetamol"
    elif (prediction == 9):
        msg1 ="Promethazine"

    context = {
        'msg1': msg1,
    }
    return render(request, 'prescriptionHTML.html', context)


def lungview(request):
    template = loader.get_template('lungHTML.html')
    return HttpResponse(template.render())

@csrf_exempt
def predictlung(request):
    fileObj = request.FILES['filePath']
    fs = FileSystemStorage()
    filePathName = fs.save(fileObj.name, fileObj)
    filePathName = fs.url(filePathName)
    testimage = '.' + filePathName


    img = image.load_img(testimage, target_size=(150, 150))
    x = image.img_to_array(img)
    x = x / 255
    x = x.reshape(1, 150, 150, 3)
    model = load_model("C:/Users/aksha_fhy2u73/Downloads/Hack24thon/cnn.h5", compile=False)
    pred = model.predict(x)
    print(pred)
    if pred[0][0] > pred[0][1]:
        predictedLabel = "COVID"
    else:
        predictedLabel = 'PNEUMONIA'

    context = {
        'predictedLabel': predictedLabel,
    }
    return render(request, 'lungHTML.html', context)


# arc = request.POST.get('arc')
#     global predictedLabel, filePathName
#     fileObj = request.FILES['filePath']
#
#     fs = FileSystemStorage()
#     filePathName= fs.save(fileObj.name, fileObj)
#     filePathName = fs.url(filePathName)
#     testimage = '.'+filePathName
#     if arc =='cnn':
#         img = image.load_img(testimage, target_size=(128, 128))
#         x = image.img_to_array(img)
#         x = x / 255
#         x = x.reshape(1, img_height, img_width, 3)
#         predi = (cnn_model.predict(x) > 0.5).astype("int32")
#         if predi == 0:
#             predictedLabel = 'Benign'
#         elif predi == 1:
#             predictedLabel = 'Malignant'


def diabetesview(request):
    template = loader.get_template('diabetesHTML.html')
    return HttpResponse(template.render())

@csrf_exempt
def predictdiabetes(request):
    age = request.POST.get('AGE')
    gender = request.POST.get('gender')
    ployu = request.POST.get('polyu')
    polyd = request.POST.get('polyd')
    weightloss = request.POST.get('weightloss')
    weak = request.POST.get('weak')
    ployphagia = request.POST.get('polyphagia')
    thrush = request.POST.get('thrush')
    vision = request.POST.get('vision')
    itch = request.POST.get('itch')
    iritable = request.POST.get('iritable')
    heal = request.POST.get('heal')
    parasis = request.POST.get('parasis')
    stiff = request.POST.get('stiff')
    alo = request.POST.get('alo')
    obese = request.POST.get('obese')

    file_path = "C:/Users/aksha_fhy2u73/Downloads/Hack24thon/diabetesPickle.pkl"
    with open(file_path, 'rb') as f:
        diamodel = pickle.load(f)

    x = np.array([age,gender,ployu,polyd,weightloss,weak,ployphagia,thrush,vision,itch,iritable,heal,parasis,stiff,alo,obese]).reshape(1, -1)
    x = sc.fit_transform(x)
    pred = diamodel.predict(x)

    print(pred)
    if pred ==0:
        p = "You have come up negative for diabetes!"
    else:
        p = 'You must be careful as there are chances of you getting diabetes. Kindly better consult a doctor.'

    context = {
        'p': p,
    }
    return render(request, 'diabetesHTML.html', context)