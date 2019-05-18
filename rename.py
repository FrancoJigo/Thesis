# importing os module 
import os 
  
# Function to rename multiple files 
def main(): 
    i = 0
      
    for filename in os.listdir("C:/Users/Jigu/OneDrive/Documents/Thesis/Thesis/Square-implementation/images/Species9/20pics/"): 
        dst ="test9." + str(i) + ".jpg"
        src ='C:/Users/Jigu/OneDrive/Documents/Thesis/Thesis/Square-implementation/images/Species9/20pics/'+ filename 
        dst ='C:/Users/Jigu/OneDrive/Documents/Thesis/Thesis/Square-implementation/images/Species9/20pics/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 