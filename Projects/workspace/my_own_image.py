import urllib.request
# import urllib2
import cv2
import numpy as np
import os

def store_raw_images():
	# neg_images_link = '/home/kaeun/Projects/workspace/animals.txt'
	# neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
	neg_image_urls = open('/home/kaeun/Projects/workspace/mountain.txt')
	#get data from:
	#google images + console (ctr+shift+f or j)
	#type in: 
	#javascript:document.body.innerHTML = `<a href="data:text/csv;charset=utf-8,${escape(Array.from(document.querySelectorAll('.rg_di .rg_meta')).map(el=>JSON.parse(el.textContent).ou).join('\n'))}" download="links.txt">download urls</a>`;

	if not os.path.exists('neg'):
		os.makedirs('neg')

	pic_num = 891
	#be sure to update this number if using a different url link

	# for i in neg_image_urls.split('\n'):
	for i in neg_image_urls.readlines():
		try:
			print(i)
			urllib.request.urlretrieve(i, "neg/"+str(pic_num)+ '.jpg')
			img = cv2.imread("neg/"+str(pic_num)+ '.jpg', cv2.IMREAD_GRAYSCALE)
			resized_img = cv2.resize(img, (100, 100))
			cv2.imwrite("neg/"+str(pic_num)+ '.jpg', resized_img)
			pic_num +=1


		except Exception as e:
			print(str(e))

def find_uglies():
	for file_type in ['neg']:
		for img in os.listdir(file_type):
			#iterate all images under the 'neg' directory
			for ugly in os.listdir('uglies'):
				try:
					current_image_path = str(file_type)+'/'+str(img)
					ugly = cv2.imread('uglies/' + str(ugly))
					question = cv2.imread(current_image_path)

					if ugly.shape == question.shape and not (np.bitwise_xor(ugly, question).any()):
						#if the shape is the same
						#and if or it is ugly
						print('damn girl you ugly')
						print(current_image_path)
						os.remove(current_image_path)

				except Exception as e:
					print(str(e))


# store_raw_images()

# find_uglies()


def create_pos_n_neg():
	for file_type in ['neg']:
		for img in os.listdir(file_type):
			if file_type == 'neg':
				line = file_type+'/'+img+'\n'
				with open('bg.txt', 'a') as f:
					f.write(line)

			# elif file_type == 'pos':
			# 	line = file_type + '/'+img+'1 0 0 50 50 \n'
			# 	with open('info.dat', 'a') as f:
			# 		f.write(line)

# create_pos_n_neg()

#mkdir data
#makdir info
#opencv_createsamples -img g_object.jpg -bg bg.txt -info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1500
#this creates positive samples
#opencv_createsamples -info info/info.lst -num 1950 -w 20 -h 20 -vec positives.vec
#positive vectors
#opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1400 -numNeg 900 -numStages 10 -w 20 -h 20
#or 
#nohup opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1400 -numNeg 900 -numStages 10 -w 20 -h 20 &