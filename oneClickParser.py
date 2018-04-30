import xml.etree.ElementTree as ET
import os
import cv2

manuscripts = ['3157556', '3158466', '3249138', '3368132', '3426930']
paddings = ['00', '_0', '00', '_00', '00']
ranges = [[3, 100], [5, 72] , [7, 57] , [4, 50] , [10, 79]]
root_path = '/DATA/majeek/dataset/'

for manuscript, padding, one_range in zip(manuscripts, paddings, ranges):
    print('parsing manuscript ', manuscript)
    path = root_path + manuscript + '/'
    current = one_range[0]
    while current <= one_range[1]:
        perm = 1
        while perm < 3:
            if current < 10:
                curImgName = padding + '0' + str(current) + '-' + str(perm)
            elif current < 100:
                curImgName = padding + str(current) + '-' + str(perm)
            else:
                curImgName = '0' + str(current) + '-' + str(perm)

            img = cv2.imread(path + curImgName + '.png')
            tree = ET.parse(path + curImgName + '.xml')
            root = tree.getroot()

            idx = 0
            pixelPadding = 3
            annotations = []
            idxList = []
            for documentElement in root:  # list of bounding boxes
                elementType = documentElement.find('ElementType').text
                # make folder of image name + CCs folder
                d = os.path.dirname(path + 'segments/' + curImgName + '/')
                if not os.path.exists(d):
                    os.makedirs(d)
                e = os.path.dirname(path + 'segments/' + curImgName + '/CCs/')
                if not os.path.exists(e):
                    os.makedirs(e)
                if elementType == 'PartOfWord':
                    x = documentElement.find('X').text
                    y = documentElement.find('Y').text
                    width = documentElement.find('Width').text
                    height = documentElement.find('Height').text

                    try:
                        roi = img[
                              int(y) - pixelPadding:int(y) + int(height) + pixelPadding,
                              int(x) - pixelPadding:int(x) + int(width) + pixelPadding
                              ]
                        transcript = documentElement.find('Transcript').text
                        annotations += [transcript]
                        idxList += [idx]
                        cv2.imwrite(path + 'segments/' + curImgName + '/CCs/' +
                                    manuscript + '-' + curImgName + '-' + str(idx) + '.png', roi)
                    except (TypeError, AttributeError) as e:
                        print('error', idx, curImgName, e)
                    finally:
                        idx += 1
            # write annotations to file
            idx = 0
            with open(path + 'segments/' + curImgName + '/' + curImgName + '.txt', 'w') as outFile:
                for annotation in annotations:
                    outFile.write((str(idxList[idx]) + '\t' + annotation + '\n').encode('utf-8'))
                    idx += 1
            perm += 1
        current += 1
