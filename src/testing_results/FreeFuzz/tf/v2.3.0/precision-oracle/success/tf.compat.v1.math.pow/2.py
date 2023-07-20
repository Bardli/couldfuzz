results = dict()
import tensorflow as tf
import time
try:
  try:
    x = 0
    y_0 = 3
    y_1 = 2
    y_2 = 0
    y = [y_0,y_1,y_2,]
    name = None
    results["res_low"] = tf.compat.v1.math.pow(x=x,y=y,name=name,)
    t_start = time.time()
    results["res_low"] = tf.compat.v1.math.pow(x=x,y=y,name=name,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    y = [y_0,y_1,y_2,]
    results["res_high"] = tf.compat.v1.math.pow(x=x,y=y,name=name,)
    t_start = time.time()
    results["res_high"] = tf.compat.v1.math.pow(x=x,y=y,name=name,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
