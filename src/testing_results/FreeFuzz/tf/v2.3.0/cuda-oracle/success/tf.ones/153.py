results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      shape_0_tensor = tf.random.uniform([], minval=-256, maxval=257, dtype=tf.int64)
      shape_0 = tf.identity(shape_0_tensor)
      shape_1 = -1
      shape = [shape_0,shape_1,]
      dtype = "int64"
      results["res_cpu"] = tf.ones(shape=shape,dtype=dtype,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      shape_0 = tf.identity(shape_0_tensor)
      shape_0 = tf.cast(shape_0, tf.int64)
      shape = [shape_0,shape_1,]
      results["res_gpu"] = tf.ones(shape=shape,dtype=dtype,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
