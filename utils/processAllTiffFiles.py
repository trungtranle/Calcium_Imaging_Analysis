from calciumImaging import timePropsToJSON
import os

#props = exportFrameTimeStamp('/Users/letrung/Documents/Schwartz_lab_random_codes/072023A_Calcium_img_with_OGB/072023Ac4_multipulse_00004.tif')

FILE_DIR = '/Users/letrung/Documents/Schwartz_lab_random_codes/111023A_Gcamp_Gramicidin'

img_files = os.listdir(FILE_DIR)

[timePropsToJSON(os.path.join(FILE_DIR, x)) for x in img_files]

#timePropsToJSON('/Users/letrung/Documents/Schwartz_lab_random_codes/072023A_Calcium_img_with_OGB/072023Ac4_multipulse_00004.tif')