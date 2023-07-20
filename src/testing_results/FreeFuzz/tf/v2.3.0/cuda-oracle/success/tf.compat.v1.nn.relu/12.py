results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      features_tensor = tf.random.uniform([1, 2], dtype=tf.float32)
      features = tf.identity(features_tensor)
      name = None
      results["res_cpu"] = tf.compat.v1.nn.relu(features=features,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      features = tf.identity(features_tensor)
      features = tf.cast(features, tf.float32)
      results["res_gpu"] = tf.compat.v1.nn.relu(features=features,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
