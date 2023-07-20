import tensorflow as tf
try:
  features_tensor = tf.cast(tf.random.uniform([4, 1, 2048], minval=0, maxval=2, dtype=tf.int32), dtype=tf.bool)
  features = tf.identity(features_tensor)
  name = 0.0
  results["res"] = tf.compat.v1.nn.relu(features=features,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
