import tensorflow as tf
try:
  x_tensor = tf.saturate_cast(tf.random.uniform([10, 512], minval=0, maxval=257, dtype=tf.int64), dtype=tf.uint16)
  x = tf.identity(x_tensor)
  name_0 = 2
  name_1 = -1024
  name = [name_0,name_1,]
  results["res"] = tf.raw_ops.Asinh(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
