      back = np.copy(background)

      masked_image = cv2.resize(frame, (513,384))
      masked_image[seg_image != 0] = 0

      back[seg_image == 0] = 0
  