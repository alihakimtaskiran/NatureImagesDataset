im=np.load("/content/gdrive/My Drive/Image Dataset/foo1.npy")[0].astype(np.uint8)
print(im.shape)
print(sys.getsizeof(im))
plt.imshow(im)
plt.show()
