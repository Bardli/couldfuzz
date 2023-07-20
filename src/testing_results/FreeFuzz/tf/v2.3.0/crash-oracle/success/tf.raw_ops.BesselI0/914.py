import tensorflow as tf
try:
  x_0 = -64.0
  x_1 = -49.5
  x_2 = 3.5
  x_3 = 50.0
  x = [x_0,x_1,x_2,x_3,]
  name_0 = -1
  name_1 = 1
  name = (name_0,name_1,)
  results["res"] = tf.raw_ops.BesselI0(x=x,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
