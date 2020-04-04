import os
list_path="/home/flu2/PyTorch-YOLOv3/data/custom/valid_original.txt"
with open(list_path, "r") as file:
    img_files = file.readlines()
# rgb_path = "data/custom/images/"+img_path[:-6] + "visible/" + img_path[-6:]+ ".jpg"
# thermal_path = "data/custom/images/"+img_path[:-6] + "lwir/" + img_path[-6:]+ ".jpg"
img_rgb_path = ["/home/flu2/PyTorch-YOLOv3/data/custom/images/"+path.rstrip()[:-6] + "visible/" + path.rstrip()[-6:]+".jpg" for path in img_files]
img_thermal_path = ["/home/flu2/PyTorch-YOLOv3/data/custom/images/"+path.rstrip()[:-6] + "lwir/" + path.rstrip()[-6:]+".jpg" for path in img_files]
lb_path = ["/home/flu2/PyTorch-YOLOv3/data/custom/labels/"+path.rstrip()[:-6] + path.rstrip()[-6:]+".txt" for path in img_files]
newfile=[]
for path in img_files:
    lb_path="/home/flu2/PyTorch-YOLOv3/data/custom/labels/"+path.rstrip()[:-6] + path.rstrip()[-6:]+".txt"
    if os.stat(lb_path).st_size > 1:
        newfile.append(path)
with open('/home/flu2/PyTorch-YOLOv3/data/custom/valid.txt', 'w') as filehandle:
    for listitem in newfile:
        filehandle.write('%s' % listitem)
