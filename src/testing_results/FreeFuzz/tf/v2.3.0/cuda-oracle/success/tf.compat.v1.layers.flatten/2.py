results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      inputs_tensor = tf.random.uniform([2, 2], dtype=tf.float32)
      inputs = tf.identity(inputs_tensor)
      name = False
      results["res_cpu"] = tf.compat.v1.layers.flatten(inputs=inputs,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      inputs = tf.identity(inputs_tensor)
      inputs = tf.cast(inputs, tf.float32)
      results["res_gpu"] = tf.compat.v1.layers.flatten(inputs=inputs,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
