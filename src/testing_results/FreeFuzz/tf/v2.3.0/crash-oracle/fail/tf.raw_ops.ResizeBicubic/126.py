import tensorflow as tf
try:
  images_tensor = tf.random.uniform([0, 5, 5, 1], dtype=tf.float16)
  images = tf.identity(images_tensor)
  size_0 = -16
  size_1 = 5
  size = [size_0,size_1,]
  align_corners = False
  name = None
  results["res"] = tf.raw_ops.ResizeBicubic(images=images,size=size,align_corners=align_corners,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)