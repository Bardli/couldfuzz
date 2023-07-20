import tensorflow as tf
try:
  images_tensor = tf.complex(tf.random.uniform([1, 5, 5, 1], dtype=tf.float64),tf.random.uniform([1, 5, 5, 1], dtype=tf.float64))
  images = tf.identity(images_tensor)
  size_0 = -1
  size_1 = 6
  size = [size_0,size_1,]
  align_corners = True
  half_pixel_centers = False
  name = None
  results["res"] = tf.raw_ops.ResizeBicubic(images=images,size=size,align_corners=align_corners,half_pixel_centers=half_pixel_centers,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)