import tensorflow as tf
try:
  features_tensor = tf.saturate_cast(tf.random.uniform([4, 1, 3072], minval=-128, maxval=128, dtype=tf.int64), dtype=tf.int8)
  features = tf.identity(features_tensor)
  name = 0.0
  results["res"] = tf.compat.v1.nn.relu(features=features,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
