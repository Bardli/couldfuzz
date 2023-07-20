results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      arg_0_0 = 3
      arg_0 = [arg_0_0,]
      dtype = "float64"
      results["res_cpu"] = tf.ones(arg_0,dtype=dtype,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      arg_0 = [arg_0_0,]
      results["res_gpu"] = tf.ones(arg_0,dtype=dtype,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)