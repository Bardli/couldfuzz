import tensorflow as tf
try:
  images_tensor = tf.random.uniform([0, 5, 16, 1], dtype=tf.float16)
  images = tf.identity(images_tensor)
  size_0 = 1
  size_1 = 1
  size = [size_0,size_1,]
  align_corners = True
  half_pixel_centers = False
  name = None
  results["res"] = tf.raw_ops.ResizeBicubic(images=images,size=size,align_corners=align_corners,half_pixel_centers=half_pixel_centers,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
