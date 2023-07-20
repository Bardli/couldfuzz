results = dict()
import tensorflow as tf
import time
try:
  try:
    arg_0_0 = 1
    arg_0_1 = 7
    arg_0_2 = 3
    arg_0_3 = 0
    arg_0 = [arg_0_0,arg_0_1,arg_0_2,arg_0_3,]
    results["res_low"] = tf.ones(arg_0,)
    t_start = time.time()
    results["res_low"] = tf.ones(arg_0,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    arg_0 = [arg_0_0,arg_0_1,arg_0_2,arg_0_3,]
    results["res_high"] = tf.ones(arg_0,)
    t_start = time.time()
    results["res_high"] = tf.ones(arg_0,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
