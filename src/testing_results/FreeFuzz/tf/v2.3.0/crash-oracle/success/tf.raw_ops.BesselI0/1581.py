import tensorflow as tf
try:
  x_0 = 0.5
  x_1 = 1.0
  x_2 = 2.0
  x_3 = 4.0
  x = [x_0,x_1,x_2,x_3,]
  name_tensor = tf.random.uniform([1, 1], dtype=tf.float32)
  name = tf.identity(name_tensor)
  results["res"] = tf.raw_ops.BesselI0(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
