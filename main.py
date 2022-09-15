import cv2
import face_recognition
from flask import Flask, render_template, request

 
def working():
    imgElon = face_recognition.load_image_file('elon.jpg')
    imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
    imgTest = face_recognition.load_image_file('bill.jpg')
    imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)
    
    faceLoc = face_recognition.face_locations(imgElon)[0]
    encodeElon = face_recognition.face_encodings(imgElon)[0]
    cv2.rectangle(imgElon,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)
    
    faceLocTest = face_recognition.face_locations(imgTest)[0]
    encodeTest = face_recognition.face_encodings(imgTest)[0]
    cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)
    
    results = face_recognition.compare_faces([encodeElon],encodeTest)
    faceDis = face_recognition.face_distance([encodeElon],encodeTest)
    print(results,faceDis)
    cv2.putText(imgTest,f'{results}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
 
    # cv2.imshow('Elon Musk',imgElon)
    # cv2.imshow('Elon Test',imgTest)
    cv2.imwrite('imgTest.jpg',imgTest)
    return results

# from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
         f = request.files['file']
         f.save('google.png')

#    response=working('google.png')
   response=working()
   return response
   

if __name__ == '__main__':
   app.run(debug = True)