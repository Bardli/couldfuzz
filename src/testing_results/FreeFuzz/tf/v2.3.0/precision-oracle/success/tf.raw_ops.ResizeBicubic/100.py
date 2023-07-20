results = dict()
import tensorflow as tf
import time
try:
  try:
    images_tensor = tf.saturate_cast(tf.random.uniform([1, 5, 5, 1], minval=-256, maxval=257, dtype=tf.int64), dtype=tf.int8)
    images = tf.identity(images_tensor)
    size_0 = 16
    size_1 = 1024
    size = [size_0,size_1,]
    align_corners = False
    half_pixel_centers = False
    name = None
    results["res_low"] = tf.raw_ops.ResizeBicubic(images=images,size=size,align_corners=align_corners,half_pixel_centers=half_pixel_centers,name=name,)
    t_start = time.time()
    results["res_low"] = tf.raw_ops.ResizeBicubic(images=images,size=size,align_corners=align_corners,half_pixel_centers=half_pixel_centers,name=name,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    images = tf.identity(images_tensor)
    images = tf.cast(images, tf.int32)
    size = [size_0,size_1,]
    results["res_high"] = tf.raw_ops.ResizeBicubic(images=images,size=size,align_corners=align_corners,half_pixel_centers=half_pixel_centers,name=name,)
    t_start = time.time()
    results["res_high"] = tf.raw_ops.ResizeBicubic(images=images,size=size,align_corners=align_corners,half_pixel_centers=half_pixel_centers,name=name,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
