results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      features_tensor = tf.cast(tf.random.uniform([4, 1, 2048], minval=0, maxval=2, dtype=tf.int32), dtype=tf.bool)
      features = tf.identity(features_tensor)
      name = 0.0
      results["res_cpu"] = tf.compat.v1.nn.relu(features=features,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      features = tf.identity(features_tensor)
      features = tf.cast(features, tf.bool)
      results["res_gpu"] = tf.compat.v1.nn.relu(features=features,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
