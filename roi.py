import cv2
import numpy as np
import tensorflow
#[y1,y2,x1,x2]
roi_values = [[33, 95, 150, 279],[91, 158, 149, 279],[153, 220, 149, 278],[214, 282, 146, 278],[274, 341, 149, 278],[335, 402, 147, 277],[398, 464, 146, 273],[461, 527, 144, 274],[523, 620, 145, 273],[614, 711, 145, 275],[32,93,274,399],[92, 156, 272, 396],[214,277,272,397],[153, 216, 272, 398],[274, 339, 271, 397],[337, 401, 271, 396],[400, 465, 271, 397],[460, 526, 270, 398],[521, 619, 270, 401],[614, 712, 269, 398],[616, 715, 564, 696],[525, 619, 565, 694],[462, 528, 565, 695],[399, 465, 565, 693],[339, 400, 565, 693],[275, 342, 563, 694],[212, 279, 565, 694],[151, 217, 565, 695],[90, 153, 563, 693],[27, 93, 563, 692],[29, 91, 688, 816],[89, 153, 687, 817],[150, 218, 690, 817],[213, 279, 689, 821],[277, 344, 690, 818],[337, 404, 689, 818],[399, 465, 690, 818],[461, 530, 689, 821],[524, 624, 689, 823],[618, 712, 689, 822],[649, 717, 966, 1094],[587, 653, 965, 1095],[525, 591, 964, 1095],[465, 528, 966, 1094],[401, 466, 965, 1093],[336, 405, 964, 1091],[277, 341, 964, 1092],[213, 279, 964, 1091],[149, 217, 963, 1090],[89, 155, 963, 1091],[26, 94, 962, 1091],[29, 95, 1085, 1218],[88, 156, 1087, 1215],[150, 217, 1084, 1219],[214, 280, 1088, 1219],[277, 343, 1089, 1216],[337, 406, 1090, 1219],[401, 469, 1088, 1218],[462, 532, 1089, 1221],[526, 589, 1089, 1220],[587, 654, 1090, 1220],[651, 714, 1091, 1220]]

model = tensorflow.keras.models.load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
img = cv2.imread("parking_lot_top.jpg")
ori = img.copy()
counter =1
for y1,y2,x1,x2 in roi_values:
     slot =ori[y1:y2, x1:x2]
     image= cv2.resize(slot, (224, 224))
# image = ImageOps.fit(slot,(224,224), Image.ANTIALIAS)
     image_array = np.asarray(image)
     normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
     data[0] = normalized_image_array
     probablity = model.predict(data)
     print(probablity)
     prediction = np.argmax(probablity)
     if prediction == 0:
     	img2 = cv2.rectangle(img, (x1,y1),(x2,y2), (0, 0, 255), 2)
     else:
     	img2 = cv2.rectangle(img, (x1,y1),(x2,y2), (255, 0, 0), 2)
    
    # pre = model.predict_classes(cv2.resize(slot, (32, 28)).reshape(1, 32, 28, 3))[0][0]
     #cv2.imwrite("C:\\Users\\deadl\\Downloads\\Parking_system-master\\Driver_safety\\data\\"+str(counter)+".jpg",slot)
     cv2.putText(img2,str(counter), (x1+30, y1+30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)
    # cv2.putText(img2, str(prediction), (x1 + 50, y1 + 30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 225), 1)
     counter += 1

cv2.imshow("w",img)
#cv2.imshow("c",)
cv2.waitKey(0)
cv2.destroyAllWindows()
