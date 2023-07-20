import tensorflow as tf
try:
  images_tensor = tf.saturate_cast(tf.random.uniform([1, 5, 5, 1], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint16)
  images = tf.identity(images_tensor)
  size = []
  align_corners = False
  name = None
  results["res"] = tf.raw_ops.ResizeBicubic(images=images,size=size,align_corners=align_corners,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
