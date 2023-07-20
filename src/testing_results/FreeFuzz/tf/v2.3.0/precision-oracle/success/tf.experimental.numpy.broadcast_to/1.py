results = dict()
import tensorflow as tf
import time
try:
  try:
    array_0 = 1
    array_1 = 2
    array_2 = 3
    array = [array_0,array_1,array_2,]
    shape_0 = 3
    shape_1 = 0
    shape_2 = 1
    shape = [shape_0,shape_1,shape_2,]
    results["res_low"] = tf.experimental.numpy.broadcast_to(array=array,shape=shape,)
    t_start = time.time()
    results["res_low"] = tf.experimental.numpy.broadcast_to(array=array,shape=shape,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    array = [array_0,array_1,array_2,]
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
