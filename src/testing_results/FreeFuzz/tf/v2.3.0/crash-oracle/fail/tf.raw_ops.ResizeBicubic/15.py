import tensorflow as tf
try:
  images_tensor = tf.saturate_cast(tf.random.uniform([1, 5, 5, 1], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint32)
  images = tf.identity(images_tensor)
  size_0 = -1
  size_1 = 4
  size = [size_0,size_1,]
  align_corners = False
  half_pixel_centers = True
  name = None
  results["res"] = tf.raw_ops.ResizeBicubic(images=images,size=size,align_corners=align_corners,half_pixel_centers=half_pixel_centers,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
