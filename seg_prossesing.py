      seg_image = seg_image[:,:,0] > 100 
      seg_image = np.uint8(seg_image)*255
      seg_image = cv2.cvtColor(seg_image, cv2.COLOR_GRAY2BGR)
      seg_image = 255 - seg_image