results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      x = 1
      y_0 = 2
      y_1 = 1
      y_2 = 0
      y = [y_0,y_1,y_2,]
      name = None
      results["res_cpu"] = tf.compat.v1.math.pow(x=x,y=y,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      y = [y_0,y_1,y_2,]
      results["res_gpu"] = tf.compat.v1.math.pow(x=x,y=y,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
