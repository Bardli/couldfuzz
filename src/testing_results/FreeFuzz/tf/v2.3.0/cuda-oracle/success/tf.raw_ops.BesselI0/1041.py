results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      x_0 = -58.0
      x_1 = -19.1
      x_2 = -43.9
      x_3 = 40.0
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
