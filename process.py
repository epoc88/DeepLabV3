      cv2_im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      pil_im = Image.fromarray(cv2_im)
      
      # DeepLAb model output
      resized_im, seg_map = MODEL.run(pil_im)
      arr = np.asarray(seg_map)

      seg_image = label_to_color_image(seg_map).astype(np.uint8)