import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from .yolo_xml_generator import xml_fill
import re

#ImagePath is directory of directories with first folder as image(countaining .jpeg) and second as masks containing binary masks , like stage1_test_solution
def get_xml_combined_mask(ImagePath, Textpath, classname, save_image_path , save_annot_path , image_shape = (512 , 512)):
	try:
		os.mkdir(save_image_path)
	except:
		pass
	try:
		os.mkdir(save_annot_path)
	except:
		pass
	image_list = os.listdir(ImagePath)
	for i,elem in enumerate(os.listdir(ImagePath)):
		if elem == '.DS_Store':
			image_list.pop(i)
			break

	for images in image_list:
		filler = xml_fill(save_annot_path+ images+'.xml', image_shape[0] , image_shape[1])
		coordinates_list = []
		if images == ".DS_Store":
			continue
		else:
			temp = plt.imread(ImagePath + '/' + images)
			prev_shape = temp.shape
			final_image = cv2.resize(temp , (512,512))
			if re.search(".*\.jpg",images):
				if images[:-3] + 'txt' in os.listdir(Textpath):
					file = images[:-3] + 'txt'
					with open(Textpath + images[:-3] + 'txt') as f:
						k = f.read()[:-1]
						for coords in k.split(' '):
								coordinates_list.append(float(coords))
					x,y,w,h = ((coordinates_list[1]*512) , (coordinates_list[2]*512), (coordinates_list[3]*512) , (coordinates_list[4]*512))
					im = Image.fromarray(final_image)
					im.save(save_image_path+ '/' + images)
					filler.addBox('0',x,y,w,h)
					filler.save(save_annot_path + images[:-3] + 'xml')
				else:
	  				pass
			elif re.search(".*\.jpeg",images):
				if images[:-4] + 'txt' in os.listdir(Textpath):
					file = images[:-4] + 'txt'
					with open(Textpath + images[:-4] + 'txt') as f:
						k = f.read()[:-1]
						for coords in k.split(' '):
								coordinates_list.append(float(coords))
					x,y,w,h = ((coordinates_list[1]*512) , (coordinates_list[2]*512), (coordinates_list[3]*512) , (coordinates_list[4]*512))
					im = Image.fromarray(final_image)
					im.save(save_image_path+ '/' + images)
					filler.addBox('0',x,y,w,h)
					filler.save(save_annot_path + images[:-4] + 'xml')
				else:
					pass
			else:
					pass

