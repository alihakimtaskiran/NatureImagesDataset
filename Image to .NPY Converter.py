from google.colab import drive
drive.mount('/content/gdrive')
%cd /content/gdrive/My Drive/Image Dataset/100OLYMP
import cv2
import os
from PIL import Image
import numpy as np

save_directory="/content/gdrive/My Drive/Image Dataset"
liste=[0,0,0,0,0,0,0,0,0,0]
liste[0]=os.listdir()[0:50]
liste[1]=os.listdir()[50:100]
liste[2]=os.listdir()[100:150]
liste[3]=os.listdir()[150:200]
liste[4]=os.listdir()[200:250]
liste[5]=os.listdir()[250:300]
liste[6]=os.listdir()[300:350]
liste[7]=os.listdir()[350:400]
liste[8]=os.listdir()[400:450]
liste[9]=os.listdir()[450:(len(os.listdir())-1)]

for i in range(6,10):
  out_array=[]
  for tmp in liste[i]:
      print(tmp)
      im=cv2.resize(np.array(Image.open(tmp)),(992,744))
      out_array.append(im)
  out_array=np.array(out_array).astype(np.uint8)
  print(out_array.shape)
  np.save(save_directory+"/foo"+str(i), out_array)
  del out_array
