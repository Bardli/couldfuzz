import tensorflow as tf
try:
  x_0 = 109.0
  x_1 = -29.1
  x_2 = 9.100000000000001
  x_3 = 52.0
  x = [x_0,x_1,x_2,x_3,]
  name = None
  results["res"] = tf.raw_ops.BesselI0(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
