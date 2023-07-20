results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      features_tensor = tf.saturate_cast(tf.random.uniform([4, 1, 3072], minval=-128, maxval=128, dtype=tf.int64), dtype=tf.int8)
      features = tf.identity(features_tensor)
      name = 0.0
      results["res_cpu"] = tf.compat.v1.nn.relu(features=features,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      features = tf.identity(features_tensor)
      features = tf.cast(features, tf.int8)
      results["res_gpu"] = tf.compat.v1.nn.relu(features=features,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
