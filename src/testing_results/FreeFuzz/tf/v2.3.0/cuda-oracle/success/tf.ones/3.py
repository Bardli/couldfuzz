results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      arg_0_0 = 3
      arg_0_1 = 12
      arg_0_2 = 7
      arg_0_3 = 0
      arg_0_4 = 4
      arg_0 = [arg_0_0,arg_0_1,arg_0_2,arg_0_3,arg_0_4,]
      results["res_cpu"] = tf.ones(arg_0,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      arg_0 = [arg_0_0,arg_0_1,arg_0_2,arg_0_3,arg_0_4,]
      results["res_gpu"] = tf.ones(arg_0,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
