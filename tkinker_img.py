import tkinter as tk
import cv2
import PIL
import PIL.Image, PIL.ImageTk
from keras.models import load_model
LARGE_FONT = ("Verdana", 12)
model = load_model("aaas_v4.h5")

class SeaofBTCapp(tk.Tk):


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.state("zoomed")
        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Smart Parking System", font=LARGE_FONT)
        label.pack(pady=50, padx=10)
        self.delay = 5

        self.btn_dis = {}

        cam_frame = tk.Frame(self)
        self.canvas = tk.Canvas(cam_frame, width=500, height=500, bg="black", bd=2)
        self.canvas.pack(padx=100, pady=5)
        self.vid = cv2.imread("s1\\p2.jpg")
        self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv2.resize(self.vid,(500,500))))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        cam_frame.pack(side="left")



        button_frame = tk.Frame(self)
        for i in range(1,11):
            self.btn_dis[i] = tk.Button(button_frame, text=str(i),height=4,width=4,bg="red")
            self.btn_dis[i].pack(side="left", padx=10)
        button_frame.pack(anchor="nw",padx=50)

        button_frame2 = tk.Frame(self)
        for i in range(11,21):
            self.btn_dis[i] = tk.Button(button_frame2, text=str(i), height=4,
                               width=4, bg="green")
            self.btn_dis[i].pack(side="left", padx=10,pady=10)
        button_frame2.pack(anchor="nw",padx=50)

        button_frame3 = tk.Frame(self)
        for i in range(30, 20,-1):
            self.btn_dis[i] = tk.Button(button_frame3, text= str(i), height=4,
                                        width=4, bg="green")
            self.btn_dis[i].pack(side="left", padx=10, pady=10)
        button_frame3.pack(anchor="nw",padx=50)

        button_frame4 = tk.Frame(self)
        for i in range(31, 41):
            self.btn_dis[i] = tk.Button(button_frame4, text=str(i), height=4,
                                        width=4, bg="green")
            self.btn_dis[i].pack(side="left", padx=10, pady=10)
        button_frame4.pack(anchor="nw",padx=50)

        button_frame5 = tk.Frame(self)
        for i in range(51, 40,-1):
            self.btn_dis[i] = tk.Button(button_frame5, text= str(i), height=4,
                                        width=4, bg="green")
            self.btn_dis[i].pack(side="left", padx=10, pady=10)
        button_frame5.pack(anchor="nw",padx=50)

        button_frame6 = tk.Frame(self)
        for i in range(52, 63):
            self.btn_dis[i] = tk.Button(button_frame6, text= str(i), height=4,
                                        width=4, bg="green")
            self.btn_dis[i].pack(side="left", padx=10, pady=10)
        button_frame6.pack(anchor="nw",padx=50)

        self.btn_dis[9].config(bg="light green",width=8)
        self.btn_dis[10].config(bg="light green",width=8)
        self.btn_dis[19].config(bg="light green",width=8)
        self.btn_dis[20].config(bg="light green",width=8)
        self.btn_dis[21].config(bg="light green",width=8)
        self.btn_dis[22].config(bg="light green",width=8)
        self.btn_dis[39].config(bg="light green",width=8)
        self.btn_dis[40].config(bg="light green",width=8)

        self.slot_checker()

    def update(self):
            self.ret, self.frame = self.vid.get_frame()
            if self.ret:
                self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(self.frame))
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
            self.after(self.delay, self.update)

    def slot_checker(self):
        roi_values = [[33, 95, 150, 279], [91, 158, 149, 279], [153, 220, 149, 278], [214, 282, 146, 278],
                      [274, 341, 149, 278], [335, 402, 147, 277], [398, 464, 146, 273], [461, 527, 144, 274],
                      [523, 620, 145, 273], [614, 711, 145, 275], [32, 93, 274, 399], [92, 156, 272, 396],
                      [214, 277, 272, 397], [153, 216, 272, 398], [274, 339, 271, 397], [337, 401, 271, 396],
                      [400, 465, 271, 397], [460, 526, 270, 398], [521, 619, 270, 401], [614, 712, 269, 398],
                      [616, 715, 564, 696], [525, 619, 565, 694], [462, 528, 565, 695], [399, 465, 565, 693],
                      [339, 400, 565, 693], [275, 342, 563, 694], [212, 279, 565, 694], [151, 217, 565, 695],
                      [90, 153, 563, 693], [27, 93, 563, 692], [29, 91, 688, 816], [89, 153, 687, 817],
                      [150, 218, 690, 817], [213, 279, 689, 821], [277, 344, 690, 818], [337, 404, 689, 818],
                      [399, 465, 690, 818], [461, 530, 689, 821], [524, 624, 689, 823], [618, 712, 689, 822],
                      [649, 717, 966, 1094], [587, 653, 965, 1095], [525, 591, 964, 1095], [465, 528, 966, 1094],
                      [401, 466, 965, 1093], [336, 405, 964, 1091], [277, 341, 964, 1092], [213, 279, 964, 1091],
                      [149, 217, 963, 1090], [89, 155, 963, 1091], [26, 94, 962, 1091], [29, 95, 1085, 1218],
                      [88, 156, 1087, 1215], [150, 217, 1084, 1219], [214, 280, 1088, 1219], [277, 343, 1089, 1216],
                      [337, 406, 1090, 1219], [401, 469, 1088, 1218], [462, 532, 1089, 1221], [526, 589, 1089, 1220],
                      [587, 654, 1090, 1220], [651, 714, 1091, 1220]]
        img = self.vid
        counter = 1
        for y1, y2, x1, x2 in roi_values:
            # img2 = cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
            # cv2.putText(img2, str(counter), (x1 + 30, y1 + 30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)
            slot = img[y1:y2,x1:x2]
            pre = model.predict_classes(cv2.resize(slot, (32, 28)).reshape(1, 32, 28, 3))[0][0]
            print(pre)
            if pre == 0:
                self.btn_dis[counter].config(bg="red")
            else:
                self.btn_dis[counter].config(bg="green")
            counter += 1

class MyVideoCapture:

    def __init__(self,video_link):
        self.vid1 = cv2.VideoCapture(video_link)
        self.width = self.vid1.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid1.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.video_link = video_link

    def start_video(self):
        if not self.vid1.isOpened():
            print("start_video_capture")
            self.vid1 = cv2.VideoCapture(self.video_link)

    def stop_video(self):
        if self.vid1.isOpened():
            print("stop_video_capture")
            self.vid1.release()

    def get_frame(self):
        if self.vid1.isOpened():
            ret, frame = self.vid1.read()
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
app = SeaofBTCapp()
app.mainloop()