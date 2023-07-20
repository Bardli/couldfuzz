import tensorflow as tf
try:
  features_tensor = tf.random.uniform([3, 256], dtype=tf.float32)
  features = tf.identity(features_tensor)
  name = None
  results["res"] = tf.compat.v1.nn.relu(features=features,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
