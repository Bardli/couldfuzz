results = dict()
import tensorflow as tf
import time
try:
  try:
    x_0 = -64.0
    x_1 = -49.5
    x_2 = 3.5
    x_3 = 50.0
    x = [x_0,x_1,x_2,x_3,]
    name_0 = -1
    name_1 = 1
    name = (name_0,name_1,)
    results["res_low"] = tf.raw_ops.BesselI0(x=x,name=name,)
    t_start = time.time()
    results["res_low"] = tf.raw_ops.BesselI0(x=x,name=name,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    x = [x_0,x_1,x_2,x_3,]
    name = (name_0,name_1,)
    results["res_high"] = tf.raw_ops.BesselI0(x=x,name=name,)
    t_start = time.time()
    results["res_high"] = tf.raw_ops.BesselI0(x=x,name=name,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)