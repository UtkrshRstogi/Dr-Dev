from keras.models import load_model
new_model = load_model("/content/chest-xray-pneumonia.h5")

def get_rez(pic):
  img = image.load_img(pic, target_size=(224,224))
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  x = preprocess_input(x)
  p_good,p_ill = np.around(new_model.predict(x), decimals=2)[0]
  return{'p_good':p_good,'p_ill':p_ill}

ill_path = "/content/chest_xray/train/PNEUMONIA/" 
good_path = "/content/chest_xray/train/NORMAL/" 

ill_pic = ill_path + os.listdir(ill_path)[0]
good_pic = good_path + os.listdir(good_path)[0]

print(get_rez(ill_pic))
print(get_rez(good_pic))