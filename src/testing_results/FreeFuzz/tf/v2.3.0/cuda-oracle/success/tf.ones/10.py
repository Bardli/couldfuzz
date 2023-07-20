results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      shape_0 = 16
      shape_1 = 0
      shape = [shape_0,shape_1,]
      results["res_cpu"] = tf.ones(shape=shape,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      shape = [shape_0,shape_1,]
      results["res_gpu"] = tf.ones(shape=shape,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
