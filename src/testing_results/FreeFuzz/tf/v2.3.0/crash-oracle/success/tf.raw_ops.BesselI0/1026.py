import tensorflow as tf
try:
  x_0 = -1.0
  x_1 = -0.1
  x_2 = 0.1
  x_3 = 1.0
  x = [x_0,x_1,x_2,x_3,]
  name_tensor = tf.random.uniform([2, 1], minval=-256, maxval=257, dtype=tf.int32)
  name = tf.identity(name_tensor)
  name = tf.Variable(name)
  results["res"] = tf.raw_ops.BesselI0(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
