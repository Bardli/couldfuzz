results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      array_tensor = tf.random.uniform([4, 1], dtype=tf.float32)
      array = tf.identity(array_tensor)
      shape_0 = 3
      shape_1 = 1
      shape = [shape_0,shape_1,]
      results["res_cpu"] = tf.experimental.numpy.broadcast_to(array=array,shape=shape,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      array = tf.identity(array_tensor)
      array = tf.cast(array, tf.float32)
      shape = [shape_0,shape_1,]
      results["res_gpu"] = tf.experimental.numpy.broadcast_to(array=array,shape=shape,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
