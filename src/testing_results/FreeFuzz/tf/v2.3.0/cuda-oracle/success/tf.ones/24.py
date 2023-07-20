results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      arg_0_0_tensor = tf.saturate_cast(tf.random.uniform([], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint64)
      arg_0_0 = tf.identity(arg_0_0_tensor)
      arg_0_1 = 3
      arg_0_2 = 1
      arg_0_3 = 510
      arg_0 = [arg_0_0,arg_0_1,arg_0_2,arg_0_3,]
      results["res_cpu"] = tf.ones(arg_0,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      arg_0_0 = tf.identity(arg_0_0_tensor)
      arg_0_0 = tf.cast(arg_0_0, tf.uint64)
      arg_0 = [arg_0_0,arg_0_1,arg_0_2,arg_0_3,]
      results["res_gpu"] = tf.ones(arg_0,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
