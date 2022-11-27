import os
import glob
from PIL import Image
import shutil

# make output directory 
dest_folder = 'c:\\Temp\sortedByDate'
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

# read photo
for fpath in glob.glob('C:\\Temp\\photo\\*.jpg'):
    img = Image.open(fpath)
    exifData = img.getexif()
    img.close()

    # 사진 정보 추출 (https://exiv2.org/tags.html)
    try:
        # key:306 = 이미지 생성일
        # split output = array
        date = exifData[306].split()[0].replace(':','-')
        fname = fpath.split('\\')[-1]
    except KeyError:
        print('Skip:', fpath)
        continue

    # 날짜별 저장 폴더
    folder2save = os.path.join(dest_folder, date)
    if not os.path.exists(folder2save):
        os.makedirs(folder2save)
    # 파일 경로
    fpath2save = os.path.join(folder2save, fname)    
    
    # 파일 복사
    shutil.copyfile(fpath, fpath2save)
