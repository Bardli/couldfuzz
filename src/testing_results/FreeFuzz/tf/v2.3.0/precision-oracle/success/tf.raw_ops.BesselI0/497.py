results = dict()
import tensorflow as tf
import time
try:
  try:
    x_0 = -35.0
    x_1 = 0.5
    x_2 = -11.5
    x_3 = -53.0
    x = [x_0,x_1,x_2,x_3,]
    name = None
    results["res_low"] = tf.raw_ops.BesselI0(x=x,name=name,)
    t_start = time.time()
    results["res_low"] = tf.raw_ops.BesselI0(x=x,name=name,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    x = [x_0,x_1,x_2,x_3,]
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
