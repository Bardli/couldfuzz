import tensorflow as tf
try:
  features_tensor = tf.random.uniform([1, 21, 2048], dtype=tf.float32)
  features = tf.identity(features_tensor)
  name = 0.0
  results["res"] = tf.compat.v1.nn.relu(features=features,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)