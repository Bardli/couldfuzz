import tensorflow as tf
try:
  inputs_0_tensor = tf.random.uniform([2, 2], minval=-256, maxval=257, dtype=tf.int32)
  inputs_0 = tf.identity(inputs_0_tensor)
  inputs_1_tensor = tf.random.uniform([2, 2], minval=-256, maxval=257, dtype=tf.int32)
  inputs_1 = tf.identity(inputs_1_tensor)
  inputs_2_tensor = tf.random.uniform([2, 2], minval=-256, maxval=257, dtype=tf.int32)
  inputs_2 = tf.identity(inputs_2_tensor)
  inputs = [inputs_0,inputs_1,inputs_2,]
  name = None
  results["res"] = tf.add_n(inputs=inputs,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
