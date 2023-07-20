results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      arg_0_0_tensor = tf.random.uniform([], minval=-256, maxval=257, dtype=tf.int32)
      arg_0_0 = tf.identity(arg_0_0_tensor)
      arg_0_1 = 1
      arg_0_2 = 1
      arg_0_3 = 1
      arg_0 = [arg_0_0,arg_0_1,arg_0_2,arg_0_3,]
      results["res_cpu"] = tf.ones(arg_0,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      arg_0_0 = tf.identity(arg_0_0_tensor)
      arg_0_0 = tf.cast(arg_0_0, tf.int32)
      arg_0 = [arg_0_0,arg_0_1,arg_0_2,arg_0_3,]
      results["res_gpu"] = tf.ones(arg_0,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
