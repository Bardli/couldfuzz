results = dict()
import tensorflow as tf
import time
try:
  try:
    arg_0_0 = 201
    arg_0_1 = 81
    arg_0 = [arg_0_0,arg_0_1,]
    dtype = None
    results["res_low"] = tf.ones(arg_0,dtype=dtype,)
    t_start = time.time()
    results["res_low"] = tf.ones(arg_0,dtype=dtype,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    arg_0 = [arg_0_0,arg_0_1,]
    results["res_high"] = tf.ones(arg_0,dtype=dtype,)
    t_start = time.time()
    results["res_high"] = tf.ones(arg_0,dtype=dtype,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
