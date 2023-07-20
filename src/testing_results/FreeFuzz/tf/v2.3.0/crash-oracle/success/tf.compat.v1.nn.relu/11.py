import tensorflow as tf
try:
  features_0_tensor = tf.random.uniform([], dtype=tf.float32)
  features_0 = tf.identity(features_0_tensor)
  features_1_tensor = tf.random.uniform([], dtype=tf.float32)
  features_1 = tf.identity(features_1_tensor)
  features_2_tensor = tf.random.uniform([], dtype=tf.float32)
  features_2 = tf.identity(features_2_tensor)
  features_3_tensor = tf.random.uniform([], dtype=tf.float32)
  features_3 = tf.identity(features_3_tensor)
  features = [features_0,features_1,features_2,features_3,]
  name = None
  results["res"] = tf.compat.v1.nn.relu(features=features,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
