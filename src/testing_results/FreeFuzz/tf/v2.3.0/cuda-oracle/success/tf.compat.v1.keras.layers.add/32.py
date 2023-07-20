results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      inputs_0_tensor = tf.saturate_cast(tf.random.uniform([2, 2], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint64)
      inputs_0 = tf.identity(inputs_0_tensor)
      inputs_1_tensor = tf.saturate_cast(tf.random.uniform([2, 2], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint64)
      inputs_1 = tf.identity(inputs_1_tensor)
      inputs_2_tensor = tf.saturate_cast(tf.random.uniform([1, 3], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint32)
      inputs_2 = tf.identity(inputs_2_tensor)
      inputs = [inputs_0,inputs_1,inputs_2,]
      results["res_cpu"] = tf.compat.v1.keras.layers.add(inputs=inputs,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      inputs_0 = tf.identity(inputs_0_tensor)
      inputs_0 = tf.cast(inputs_0, tf.uint64)
      inputs_1 = tf.identity(inputs_1_tensor)
      inputs_1 = tf.cast(inputs_1, tf.uint64)
      inputs_2 = tf.identity(inputs_2_tensor)
      inputs_2 = tf.cast(inputs_2, tf.uint32)
      inputs = [inputs_0,inputs_1,inputs_2,]
      results["res_gpu"] = tf.compat.v1.keras.layers.add(inputs=inputs,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)