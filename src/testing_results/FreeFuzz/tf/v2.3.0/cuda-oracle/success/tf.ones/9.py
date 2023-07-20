results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      arg_0_0 = 5
      arg_0_1 = 0
      arg_0 = [arg_0_0,arg_0_1,]
      results["res_cpu"] = tf.ones(arg_0,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      arg_0 = [arg_0_0,arg_0_1,]
      results["res_gpu"] = tf.ones(arg_0,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
