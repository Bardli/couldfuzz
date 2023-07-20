import tensorflow as tf
try:
  inputs_0_tensor = tf.random.uniform([2, 2], minval=-256, maxval=257, dtype=tf.int32)
  inputs_0 = tf.identity(inputs_0_tensor)
  inputs_1_tensor = tf.saturate_cast(tf.random.uniform([2, 2], minval=-128, maxval=128, dtype=tf.int64), dtype=tf.int8)
  inputs_1 = tf.identity(inputs_1_tensor)
  inputs_2_tensor = tf.cast(tf.random.uniform([2, 2], minval=0, maxval=2, dtype=tf.int32), dtype=tf.bool)
  inputs_2 = tf.identity(inputs_2_tensor)
  inputs = [inputs_0,inputs_1,inputs_2,]
  results["res"] = tf.compat.v1.keras.layers.add(inputs=inputs,)
except Exception as e:
  results["err"] = "Error:"+str(e)
