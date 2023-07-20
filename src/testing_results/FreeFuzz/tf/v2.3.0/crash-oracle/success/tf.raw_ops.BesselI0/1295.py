import tensorflow as tf
try:
  x_0 = -1.0
  x_1 = -0.5
  x_2 = 0.5
  x_3 = 1.0
  x = [x_0,x_1,x_2,x_3,]
  name_tensor = tf.random.uniform([1, 1], dtype=tf.float64)
  name = tf.identity(name_tensor)
  results["res"] = tf.raw_ops.BesselI0(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
