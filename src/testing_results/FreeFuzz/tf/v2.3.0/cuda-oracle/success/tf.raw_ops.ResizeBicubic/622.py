results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      images_tensor = tf.random.uniform([1, 5, 5, 1], minval=-256, maxval=257, dtype=tf.int32)
      images = tf.identity(images_tensor)
      size_0 = 5
      size_1 = 7
      size = [size_0,size_1,]
      align_corners = False
      half_pixel_centers = False
      name_tensor = tf.random.uniform([1, 1], dtype=tf.float32)
      name = tf.identity(name_tensor)
      results["res_cpu"] = tf.raw_ops.ResizeBicubic(images=images,size=size,align_corners=align_corners,half_pixel_centers=half_pixel_centers,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      images = tf.identity(images_tensor)
      images = tf.cast(images, tf.int32)
      size = [size_0,size_1,]
      name = tf.identity(name_tensor)
      name = tf.cast(name, tf.float32)
      results["res_gpu"] = tf.raw_ops.ResizeBicubic(images=images,size=size,align_corners=align_corners,half_pixel_centers=half_pixel_centers,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
