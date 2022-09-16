
import json
import os, cv2, time

pwd = 'D:\\test\\ARCH\\cat-arch-013482'
# pwd = 'D:\\test\\BODYSHAKE\\20201202_dog-bodyshake-010101.mp4'
json_path = os.path.join(os.getcwd(), pwd + '.json')



with open(json_path, encoding="UTF-8") as f:
    data = json.load(f)
    for i in range(len(data['annotations']) ):
    # for i in range(3):
        print(i)
        frame_number = data['annotations'][i]['frame_number']
        timestamp = data['annotations'][i]['timestamp']
        bounding_box = data['annotations'][i]['bounding_box']
        keypoints = data['annotations'][i]['keypoints']
        x, y, width, height = bounding_box['x'], bounding_box['y'], bounding_box['width'], bounding_box['height']
        
        image_path = os.path.join(os.getcwd(),
        pwd + '\\frame_%s_timestamp_%s.jpg'
        %(frame_number,timestamp))
        image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

        for j in keypoints:
            if keypoints[j] is not None:
                key_x, key_y = keypoints[j]['x'], keypoints[j]['y']
                cv2.line(image,(key_x,key_y),(key_x,key_y),(0,0,255),10)
        
        cv2.rectangle(image, (x,y), (x+width, y+height),(0,255,0) ,5)
        re_img = cv2.resize(image, (1300,700))
        cv2.imshow("picture", re_img)
        # time.sleep(100)
        cv2.waitKey()
        cv2.destroyAllWindows()







        
# import json
# import os, cv2, time

# pwd = 'D:\\test\\BODYSHAKE\\20201118_dog-bodyshake-001668.mp4'
# # pwd = 'D:\\test\\BODYSHAKE\\20201202_dog-bodyshake-010101.mp4'
# json_path = os.path.join(os.getcwd(), pwd + '.json')



# with open(json_path, encoding="UTF-8") as f:
#     data = json.load(f)
#     # for i in range(len(data['annotations']) + 1):
#     for i in range(3):
#         print(i)
#         frame_number = data['annotations'][i]['frame_number']
#         timestamp = data['annotations'][i]['timestamp']
#         bounding_box = data['annotations'][i]['bounding_box']
#         keypoints = data['annotations'][i]['keypoints']
#         x, y, width, height = bounding_box['x'], bounding_box['y'], bounding_box['width'], bounding_box['height']
#    
#         image_path = os.path.join(os.getcwd(),
#         pwd + '\\frame_%s_timestamp_%s.jpg'
#         %(frame_number,timestamp))

#         image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
#         image = cv2.rectangle(image, (x,y), (x+width, y+height),(0,255,0) ,5)

#         cv2.imshow("picture", image)
#         # time.sleep(100)
#         cv2.waitKey()
#         cv2.destroyAllWindows()