results = dict()
import tensorflow as tf
import time
try:
  try:
    trainable = True
    name = None
    dtype_0 = -16
    dtype_1 = 0
    dtype = (dtype_0,dtype_1,)
    results["res_low"] = tf.compat.v1.layers.Layer(trainable=trainable,name=name,dtype=dtype,)
    t_start = time.time()
    results["res_low"] = tf.compat.v1.layers.Layer(trainable=trainable,name=name,dtype=dtype,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    dtype = (dtype_0,dtype_1,)
    results["res_high"] = tf.compat.v1.layers.Layer(trainable=trainable,name=name,dtype=dtype,)
    t_start = time.time()
    results["res_high"] = tf.compat.v1.layers.Layer(trainable=trainable,name=name,dtype=dtype,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
