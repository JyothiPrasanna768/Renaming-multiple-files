# import drive and files in google colaboratory
from google.colab import drive
from google.colab import files
drive.mount('/content/drive')
data = "/content/drive/My Drive/data_label/"

#import os module
import os 
ldseg=np.array(os.listdir(data))

#define a function for renaming the files
def main(): 
  i = 0
  for filename in ldseg: 
  dst =filename.split('_')[0] + ".png"
  src =data+ filename 
  dst =data+ dst 
  os.rename(src, dst) 
  i += 1
  
#call the main function  
if __name__ == '__main__': 
  main()
