# importing os module 
import os 
  
# Function to rename multiple files 
def main(): 
    i = 0
    e = '1'
      
    for filename in os.listdir('C:/Users/63917/Documents/Jigo/Thesis/images/testingmodel/species'+e+'/'): 
        dst ='model_test'+e+'.' + str(i) + '.jpg'
        src ='C:/Users/63917/Documents/Jigo/Thesis/images/testingmodel/species'+e+'/'+ filename 
        dst ='C:/Users/63917/Documents/Jigo/Thesis/images/testingmodel/species'+e+'/'+ dst 
        
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 