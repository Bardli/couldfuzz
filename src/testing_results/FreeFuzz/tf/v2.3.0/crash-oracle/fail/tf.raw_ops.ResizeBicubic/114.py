import tensorflow as tf
try:
  images_tensor = tf.saturate_cast(tf.random.uniform([2, 5, 5], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint64)
  images = tf.identity(images_tensor)
  size_0 = False
  size_1 = 7
  size = [size_0,size_1,]
  align_corners = True
  name = None
  results["res"] = tf.raw_ops.ResizeBicubic(images=images,size=size,align_corners=align_corners,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
