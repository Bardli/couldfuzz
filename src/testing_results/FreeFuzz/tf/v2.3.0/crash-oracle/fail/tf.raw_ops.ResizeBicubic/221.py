import tensorflow as tf
try:
  images_tensor = tf.random.uniform([1, 3, 6], dtype=tf.float16)
  images = tf.identity(images_tensor)
  size_0 = 3
  size_1 = 7
  size = [size_0,size_1,]
  align_corners = False
  half_pixel_centers = False
  name = None
  results["res"] = tf.raw_ops.ResizeBicubic(images=images,size=size,align_corners=align_corners,half_pixel_centers=half_pixel_centers,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
