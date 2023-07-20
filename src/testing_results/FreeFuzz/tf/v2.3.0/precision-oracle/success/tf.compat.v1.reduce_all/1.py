results = dict()
import tensorflow as tf
import time
try:
  try:
    input_tensor_tensor = tf.random.uniform([1, 512], dtype=tf.float16)
    input_tensor = tf.identity(input_tensor_tensor)
    axis = None
    keepdims = False
    name = None
    results["res_low"] = tf.compat.v1.reduce_all(input_tensor=input_tensor,axis=axis,keepdims=keepdims,name=name,)
    t_start = time.time()
    results["res_low"] = tf.compat.v1.reduce_all(input_tensor=input_tensor,axis=axis,keepdims=keepdims,name=name,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    input_tensor = tf.identity(input_tensor_tensor)
    input_tensor = tf.cast(input_tensor, tf.float16)
    results["res_high"] = tf.compat.v1.reduce_all(input_tensor=input_tensor,axis=axis,keepdims=keepdims,name=name,)
    t_start = time.time()
    results["res_high"] = tf.compat.v1.reduce_all(input_tensor=input_tensor,axis=axis,keepdims=keepdims,name=name,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
