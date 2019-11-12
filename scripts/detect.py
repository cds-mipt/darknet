import os
from tqdm import tqdm


images_folder = '/home/k_andrei/darknet/data/Augmentated_NKBVS_selected_joined/images/test'
images_files = sorted(os.listdir(images_folder))
for image_file in tqdm(images_files):
    os.system('./darknet detector test Augmentated_NKBVS_selected_joined/config/dataset.data Augmentated_NKBVS_selected_joined/config/yolov3.cfg Augmentated_NKBVS_selected_joined/epoch_18.weights ' + os.path.join(images_folder, image_file) + ' -thresh 0.3')
    os.system('mv predictions.jpg predictions/test/' + image_file)

