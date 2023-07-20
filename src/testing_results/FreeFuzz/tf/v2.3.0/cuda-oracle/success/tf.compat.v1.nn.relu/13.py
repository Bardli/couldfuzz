results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
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
      results["res_cpu"] = tf.compat.v1.nn.relu(features=features,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      features_0 = tf.identity(features_0_tensor)
      features_0 = tf.cast(features_0, tf.float32)
      features_1 = tf.identity(features_1_tensor)
      features_1 = tf.cast(features_1, tf.float32)
      features_2 = tf.identity(features_2_tensor)
      features_2 = tf.cast(features_2, tf.float32)
      features_3 = tf.identity(features_3_tensor)
      features_3 = tf.cast(features_3, tf.float32)
      features = [features_0,features_1,features_2,features_3,]
      results["res_gpu"] = tf.compat.v1.nn.relu(features=features,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
