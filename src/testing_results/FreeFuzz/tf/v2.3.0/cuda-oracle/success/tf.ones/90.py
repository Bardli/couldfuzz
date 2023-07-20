results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      arg_0 = 1
      results["res_cpu"] = tf.ones(arg_0,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      results["res_gpu"] = tf.ones(arg_0,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
