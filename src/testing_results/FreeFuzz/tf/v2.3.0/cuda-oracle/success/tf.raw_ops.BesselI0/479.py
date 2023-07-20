results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      x_0 = 51.0
      x_1 = 0
      x_2 = 63.0
      x_3 = -25.0
      x = [x_0,x_1,x_2,x_3,]
      name = None
      results["res_cpu"] = tf.raw_ops.BesselI0(x=x,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      x = [x_0,x_1,x_2,x_3,]
      results["res_gpu"] = tf.raw_ops.BesselI0(x=x,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
