results = dict()
import tensorflow as tf
import time
try:
  try:
    array_tensor = tf.saturate_cast(tf.random.uniform([1, 1, 20], minval=-256, maxval=257, dtype=tf.int64), dtype=tf.int8)
    array = tf.identity(array_tensor)
    shape_0 = -1024
    shape_1 = 4
    shape_2 = 20
    shape = [shape_0,shape_1,shape_2,]
    results["res_low"] = tf.experimental.numpy.broadcast_to(array=array,shape=shape,)
    t_start = time.time()
    results["res_low"] = tf.experimental.numpy.broadcast_to(array=array,shape=shape,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    array = tf.identity(array_tensor)
    array = tf.cast(array, tf.int32)
    shape = [shape_0,shape_1,shape_2,]
    results["res_high"] = tf.experimental.numpy.broadcast_to(array=array,shape=shape,)
    t_start = time.time()
    results["res_high"] = tf.experimental.numpy.broadcast_to(array=array,shape=shape,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
