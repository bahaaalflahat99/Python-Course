import os
path= r"C:\Users\3mmar\Desktop\Python Course\Week 3\photos"
files= os.listdir(path)
i=1
for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.jpg'))
i = i+1
