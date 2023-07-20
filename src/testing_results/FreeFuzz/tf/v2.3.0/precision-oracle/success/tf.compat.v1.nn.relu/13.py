results = dict()
import tensorflow as tf
import time
try:
  try:
    features_0_tensor = tf.random.uniform([], dtype=tf.float16)
    features_0 = tf.identity(features_0_tensor)
    features_1_tensor = tf.random.uniform([], dtype=tf.float16)
    features_1 = tf.identity(features_1_tensor)
    features_2_tensor = tf.random.uniform([], dtype=tf.float16)
    features_2 = tf.identity(features_2_tensor)
    features_3_tensor = tf.random.uniform([], dtype=tf.float16)
    features_3 = tf.identity(features_3_tensor)
    features = [features_0,features_1,features_2,features_3,]
    name = None
    results["res_low"] = tf.compat.v1.nn.relu(features=features,name=name,)
    t_start = time.time()
    results["res_low"] = tf.compat.v1.nn.relu(features=features,name=name,)
    t_end = time.time()
    results["time_low"] = t_end - t_start
  except Exception as e:
    results["err_low"] = "Error:"+str(e)
  try:
    features_0 = tf.identity(features_0_tensor)
    features_0 = tf.cast(features_0, tf.float32)
    features_1 = tf.identity(features_1_tensor)
    features_1 = tf.cast(features_1, tf.float32)
    features_2 = tf.identity(features_2_tensor)
    features_2 = tf.cast(features_2, tf.float32)
    features_3 = tf.identity(features_3_tensor)
    features_3 = tf.cast(features_3, tf.float32)
    features = [features_0,features_1,features_2,features_3,]
    results["res_high"] = tf.compat.v1.nn.relu(features=features,name=name,)
    t_start = time.time()
    results["res_high"] = tf.compat.v1.nn.relu(features=features,name=name,)
    t_end = time.time()
    results["time_high"] = t_end - t_start
  except Exception as e:
    results["err_high"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
