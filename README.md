# Nature Images Dataset
This repository includes image to npy converter and link for converted npy files

  NPY is a file format to store numpy arrays. How to work Image to NPY converter? Firstly it imports necessary python modules.(numpy, cv2, pillow, matplotlib.pyplot, os, sys and google.cloab(optional)). If you run this code in your computer you don't need google.colab module.

  You have to copy all images into a folder. After that copy the python script into same folder. Script will get list of all files of the folder.
  
  Caution! there is an error may be occured. If you try to proccess large images, your RAM may not enough to this process and you get error.
If you don't have large RAM, I recommend Google Colab or another cloud service. I've used Google Colab,but there wasn't enogh RAM. 
I've splited image list and I reduced image size. So at the end of the process I got 10 files.

  Pillow module reads image and numpy module converts image into ndarray. After that all images are appends into a ndarray. Finally numpy saves ndarray as npy file.

  You can restore images with np.load("npy file") function. This function returns ndarray.

########TR########

 Bu depo resimleri npy formatına dönüştürücü ve dönüştürülmüş npy dosyalarına ulaşmanızı sağlayan bir bağlantı içermektedir.
 NPY, numpy array'lerini depolamak için kullanılan bir dosya formatıdır. NPY dönüştürücü nasıl çalışır? Öncelikle gerekli python modüllerini import eder.
 Bunlar numpy, cv2, pillow, matplotlib.pyplot, os, sys ve google.cloab(isteğe bağlı)'dır. 
 Eğer kodu bilgisayarınızda çalıştıracaksanız google.colab modülüne ihtiyacınız yoktur.
 
 Tüm resimleri bir klasörün içine eklemelisiniz. Bundan sonra aynı klasöre python kodunu kopyalayın. Kod, klasördeki tüm dosyaların listesini alacaktır.
 
 Dikkat! Bir hata meydana gelebilir.Eğer büyük resimler üzerinde işlem yapıyorsanız RAM'iniz bu iş için yetmeyebilir ve hata alırsınız. 
 Eğer yeterince büyük RAM'iniz yoksa Google Colab ya da başka bir bulut servisi kullanmanızı tavsiye ederim. Ben Google Colab kullandım fakat onun RAM'i de bana yetmedi. 
 Bu yüzden resim listesini parçalara ayırdım ve resim boyutunu azalttım. Böylece işlemin sonunda 10 adet dosya aldım.
 
 Pillow modülü resimleri okur ve numpy resimleri ndarray'e dönüştürür. Bundan sonra tüm resimler bir adte ndarray'e ekleir. Son olarak numpy, ndarray'i npy dosyası olarak kaydeder.
 
 np.load("npy dosyası") fonksiyonu ile npy dosyasını tekrar ndarray'e çevirebilirsiniz. Bu fonksiyon ndarray cinsinden değer döndürür.
