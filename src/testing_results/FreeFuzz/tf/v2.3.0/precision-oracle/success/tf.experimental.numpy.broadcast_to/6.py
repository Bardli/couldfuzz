results = dict()
import tensorflow as tf
import time
try:
  try:
    array_tensor = tf.random.uniform([4, 1], dtype=tf.float16)
    array = tf.identity(array_tensor)
    shape_0 = 3
    shape_1 = 1
    shape = [shape_0,shape_1,]
    results["res_low"] = tf.experimental.numpy.broadcast_to(array=array,shape=shape,)
    t_start = time.time()
    results["res_low"] = tf.experimental.numpy.broadcast_to(array=array,shape=shape,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    array = tf.identity(array_tensor)
    array = tf.cast(array, tf.float32)
    shape = [shape_0,shape_1,]
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
