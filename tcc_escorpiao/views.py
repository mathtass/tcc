from django.shortcuts import render
from .models import Escorpiao
import numpy as np
import cv2
import pdb
from django.utils import timezone

# Create your views here.
def tela(request):
    escorpiao = False
    img = cv2.imread('esc.png')
    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thrash = cv2.threshold(imgGrey, 155, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
        cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
        x = approx.ravel()[0]
        y = approx.ravel()[1] - 5

    

        if len(approx) == 24 or len(approx) == 23: 
            cv2.putText(img, "Escorpiao", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.8, (1, 0, 0))
            escorpiao = True
            Escorpiao.objects.create(presenca="Presença de escorpião detectada pelo seu formato.",data_encontro=timezone.now())
            print("Escorpiao foi encontrado")

        if (escorpiao == False):
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            lower_range = np.array([0,0,0])
            upper_range = np.array([114, 255,255])

            mask = cv2.inRange(hsv, lower_range, upper_range)

            if cv2.countNonZero(mask) > 0:
                Escorpiao.objects.create(presenca="Presença de escorpião detectada pela sua cor.",data_encontro=timezone.now())
                escorpiao = True
                # cv2.imshow('image', img)
                # cv2.imshow('mask', mask)
            else:
                print('Escorpiao nao encontrado')    



   
    # if (escorpiao == True):
    #     Escorpiao.objects.create(presenca="Presença de escorpião detectada.",data_encontro=timezone.now())
    escorpiao_query = Escorpiao.objects.all()
    # cv2.imshow("shapes", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return render(request, 'tcc_escorpiao/tela.html',  {'escorpiao': escorpiao_query})


