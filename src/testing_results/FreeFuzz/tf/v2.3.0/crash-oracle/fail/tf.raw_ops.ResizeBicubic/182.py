import tensorflow as tf
try:
  images_tensor = tf.random.uniform([0, 5, 5, 16], minval=-256, maxval=257, dtype=tf.int64)
  images = tf.identity(images_tensor)
  size_0 = 5
  size_1 = 7
  size = [size_0,size_1,]
  align_corners = True
  half_pixel_centers = True
  name = None
  results["res"] = tf.raw_ops.ResizeBicubic(images=images,size=size,align_corners=align_corners,half_pixel_centers=half_pixel_centers,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
