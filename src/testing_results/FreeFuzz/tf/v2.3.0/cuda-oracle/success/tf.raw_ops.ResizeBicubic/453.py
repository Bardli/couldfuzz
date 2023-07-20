results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      images_tensor = tf.saturate_cast(tf.random.uniform([1, 5, 5, 1], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint16)
      images = tf.identity(images_tensor)
      size = []
      align_corners = False
      name = None
      results["res_cpu"] = tf.raw_ops.ResizeBicubic(images=images,size=size,align_corners=align_corners,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      images = tf.identity(images_tensor)
      images = tf.cast(images, tf.uint16)
      size = []
      results["res_gpu"] = tf.raw_ops.ResizeBicubic(images=images,size=size,align_corners=align_corners,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
