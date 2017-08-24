import sys, cv2, os
import numpy as np

def get_images_and_labels(path):
    # Append all the absolute image paths in a list image_paths
    # We will not read the image with the .sad extension in the training set
    # Rather, we will use them to test our accuracy of the training
    image_paths = [os.path.join(path, f) for f in os.listdir(path) if not f.endswith('.sad')]
    # images will contains face images
    images = []
    # labels will contains the label that is assigned to the image
    labels = []
    for image_path in image_paths:
        # Read the image and convert to grayscale
        image_pil = cv2.imread(image_path, 0)
        # Convert the image format into numpy array
        image = np.array(image_pil, 'uint8')
        # Get the label of the image
        nbr = int(os.path.split(image_path)[1].split(".")[0])
        #nbr = os.path.split(image_path)[1].split(".")[0]
        # Detect the face in the image
        faces = faceCascade.detectMultiScale(image, 
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        # If face is detected, append the face to images and the label to labels
        for (x, y, w, h) in faces:
            print "adding ", nbr
            images.append(image[y: y + h, x: x + w])
            labels.append(nbr)
            #cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
            #cv2.waitKey(50)
    # return the images list and labels list
    return images, labels



cascadePath = "C:\Programagic\OpenCV\A-FaceDetection\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
recognizer = cv2.face.createLBPHFaceRecognizer()

if os.path.exists('trainer.yml'):
    print 'loading recognizer'
    recognizer.load('trainer.yml')
else:
    print 'training recognizer'
    path = 'C:\Programagic\OpenCV\A-FaceDetection\Faces' 
    images, labels = get_images_and_labels(path)
    recognizer.train(images, np.array(labels))
    recognizer.save('trainer.yml')

#capture video
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    font = cv2.FONT_HERSHEY_SIMPLEX
    roi = None
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        gray = cv2.cvtColor(frame[y:y+h, x:x+w], cv2.COLOR_BGR2GRAY)
        nbr_predicted, conf = recognizer.predict(gray)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (100, 250, 100), 2)
        name = None

        
        if conf < 100:
            if nbr_predicted == 5:
                name = "neymar {0}".format(int(conf))
            elif nbr_predicted == 4:
                name = "papi {0}".format(int(conf))
            elif nbr_predicted == 3:
                name = "mami {0}".format(int(conf))
            elif nbr_predicted == 2:
                name = "kwikwi {0}".format(int(conf))
            elif nbr_predicted == 1:
                name = "rishi {0}".format(int(conf))
        else:
            name = "intruder {0}".format(int(conf))

        #print name, conf
        cv2.putText(frame,name,(int(x), int(y)), font, 1,(255,255,255),2)

        if (w > 0 and h > 0):
            roi = frame[y:y+h, x:x+w]

    # Display the resulting frame
    cv2.imshow('Video', frame) 

    #display the cropped
    #if roi is not None:
    #    if roi.size:
    #        cv2.imshow('Cropped', roi)
        

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()