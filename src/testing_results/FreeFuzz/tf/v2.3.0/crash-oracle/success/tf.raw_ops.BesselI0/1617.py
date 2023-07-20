import tensorflow as tf
try:
  x_0 = -8.0
  x_1 = 44.5
  x_2 = -56.5
  x_3 = 40.0
  x = [x_0,x_1,x_2,x_3,]
  name = tf.int8
  results["res"] = tf.raw_ops.BesselI0(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
