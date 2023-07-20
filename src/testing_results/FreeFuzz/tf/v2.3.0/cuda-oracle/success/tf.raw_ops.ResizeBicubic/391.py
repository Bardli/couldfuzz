results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      images_tensor = tf.saturate_cast(tf.random.uniform([1, 5, 5, 1], minval=-256, maxval=257, dtype=tf.int64), dtype=tf.int16)
      images = tf.identity(images_tensor)
      size_0 = 5
      size_1 = 7
      size = [size_0,size_1,]
      align_corners = False
      name = None
      results["res_cpu"] = tf.raw_ops.ResizeBicubic(images=images,size=size,align_corners=align_corners,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      images = tf.identity(images_tensor)
      images = tf.cast(images, tf.int16)
      size = [size_0,size_1,]
      results["res_gpu"] = tf.raw_ops.ResizeBicubic(images=images,size=size,align_corners=align_corners,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
