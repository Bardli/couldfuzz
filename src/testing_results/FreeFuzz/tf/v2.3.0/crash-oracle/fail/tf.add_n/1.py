import tensorflow as tf
try:
  inputs_0_tensor = tf.random.uniform([], dtype=tf.bfloat16)
  inputs_0 = tf.identity(inputs_0_tensor)
  inputs_1_tensor = tf.random.uniform([], dtype=tf.float32)
  inputs_1 = tf.identity(inputs_1_tensor)
  inputs = [inputs_0,inputs_1,]
  name = None
  results["res"] = tf.add_n(inputs=inputs,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
