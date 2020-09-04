from google.colab import drive
drive.mount('/content/gdrive')
!ls /content/gdrive/My Drive
model_save_name = 'model.h5'
path = F"/content/gdrive/My Drive/{model_save_name}" 
torch.save(model.state_dict(), path)
