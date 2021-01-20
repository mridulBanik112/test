import cv2
import uuid

def seg_ui_json(img_org):
    im1 = cv2.cvtColor(img_org, cv2.COLOR_BGR2GRAY)
    shapes=[]
    pages=[{"shapes":shapes}]
    pages_dict={"pages":pages}
    try : 
        #m1 = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_UNCHANGED) # BGR
#        im1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #im1 = cv2.imread(path.encode('utf-8', 'surrogateescape').decode('utf-8', 'surrogateescape'))

        ret,thresh1 = cv2.threshold(im1,180,255,cv2.THRESH_BINARY_INV)
        #plt.subplot(2,3,4+1),plt.imshow(thresh1,'gray')
        #plt.show()
        #kernel = np.ones((5,5),np.uint8)
        dilated = cv2.dilate(thresh1,None,iterations = 3)
        contours, hierarchy = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cordinates = []
        ROI_number = 0
        Area=[]
        for cnt in contours:
            area = cv2.contourArea(cnt)
            Area.append(area)
            if area > 100 :
                x,y,w,h = cv2.boundingRect(cnt)
                if w>50:
                    cordinates.append([x,y,x+w,y+h])
        
        list1=sorted(cordinates, key = lambda x: x[1],reverse=False)
        
        p_list=[]
        c_list=[]
        for i in range (len(list1)):
            if((i+1)<len(list1)) and (list1[i+1][1]-list1[i][1]<15):
                c_list.append(list1[i])
            else:
                c_list.append(list1[i])
                c_list1=sorted(c_list, key = lambda x: x[0],reverse=False)
                p_list.append(c_list1)
                c_list=[]
        
        ROI_number=0
        for j in p_list:
            flag=0
            for index,i in enumerate(j):
                
                
                
                if (flag!=1):
                    x=i[0]
                    y=i[1]
                    x1=i[2]
                    y1=i[3]
                
        
                if((index+1)<(len(j))):
                    
                    
                    
                    
                    x2=j[index+1][0]
                    y2=j[index+1][1]
                    x3=j[index+1][2]
                    y3=j[index+1][3]
                    
                    
                    if(x2-x1)<2 :
                        
                        #print("hello")
                        x=x
                        #x1=x3
                        
                        if (x3<x1):
                            x1=x1
                        else:
                            x1=x3
        #                
                        if(y>y2):
                            y=y2
                        elif(y2>y):
                            y=y
                        if (y3>y1):
                            y1=y3
                        elif(y1>y3):
                            y1=y1
                            
                        #i=i+1
                        flag=1
                    else:
                        flag=0
                        
                if(flag==0):
                    
                    
                    ROI = img_org[y:y1, x:x1] 
                    
                    if (ROI.nbytes > 100 and ROI.shape[1]>50):
                        

                        #cv2.rectangle(im1,(x,y),(x1,y1),(0,255,0),2)
                        ROI_number =ROI_number+1
                        unique_id = str(uuid.uuid1())
                        shapes_dict=  {
                          "id" : unique_id,
                          "x" : x,
                          "y" : y,
                          "width" : x1-x,
                          "height" : y1-y,
                          "type" : "PARAGRAPH"
                        }
                        shapes.append(shapes_dict)
                        c=0
                    #imS = cv2.resize(im1, (1920,1080))
        #             cv2.imshow("image",imS)
        #             if cv2.waitKey(0) & 0xFF == ord('q'): 
        #                 cv2.destroyAllWindows()
                    
            if c!=0:
                ROI = img_org[y:y1, x:x1] 
                if (ROI.nbytes > 100 and ROI.shape[1]>50 and ROI.shape[0]>50 ):
                    

                    #cv2.rectangle(im1,(x,y),(x1,y1),(0,255,0),2)
                    #cv2.imwrite('Output_word/ROI_{}.png'.format(ROI_number), ROI)
                
                    ROI_number=ROI_number+1
                    unique_id = str(uuid.uuid1())
                    shapes_dict=  {
                          "id" : unique_id,
                          "x" : x,
                          "y" : y,
                          "width" : x1-x,
                          "height" : y1-y,
                          "type" : "PARAGRAPH"
                        }
                    shapes.append(shapes_dict)
                    
#                with open(path_to_file, 'w') as file:
#                    json_string = json.dumps(sample, default=lambda o: o.__dict__, sort_keys=True, indent=2)
#                    file.write(json_string)
            return pages_dict



        
                    
            


        #imS = cv2.resize(im1, (1920,1080 ))
        #cv2.imshow("image",imS)
    #    if cv2.waitKey(0) & 0xFF == ord('q'): 
    #        cv2.destroyAllWindows()
        #out_full= 'output_full/'+input_
        #cv2.imwrite(out_full+'.png', im1)
        
        #         print(i)
        # #         print(j[index])
        #         cv2.rectangle(im1,(i[0],i[1]),(i[2],i[3]),(0,255,0),1)
        #         cv2.imshow("image",im1)
        #         if cv2.waitKey(0) & 0xFF == ord('q'): 
        #cv2.destroyAllWindows()  
    except Exception as e:
        print(e)
