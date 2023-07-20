import tensorflow as tf
try:
  inputs_0_tensor = tf.random.uniform([2, 2], dtype=tf.float64)
  inputs_0 = tf.identity(inputs_0_tensor)
  inputs_1_tensor = tf.random.uniform([2, 2, 1], dtype=tf.bfloat16)
  inputs_1 = tf.identity(inputs_1_tensor)
  inputs_2_tensor = tf.saturate_cast(tf.random.uniform([2, 2, 0], minval=0, maxval=256, dtype=tf.int64), dtype=tf.uint8)
  inputs_2 = tf.identity(inputs_2_tensor)
  inputs = [inputs_0,inputs_1,inputs_2,]
  results["res"] = tf.compat.v1.keras.layers.add(inputs=inputs,)
except Exception as e:
  results["err"] = "Error:"+str(e)
