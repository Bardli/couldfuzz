import tensorflow as tf
try:
  images_tensor = tf.random.uniform([1, 5, 5, 0, 1], dtype=tf.float16)
  images = tf.identity(images_tensor)
  size_0 = 6
  size_1 = 6
  size = [size_0,size_1,]
  align_corners = False
  name = None
  results["res"] = tf.raw_ops.ResizeBicubic(images=images,size=size,align_corners=align_corners,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)