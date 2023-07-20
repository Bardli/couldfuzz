import tensorflow as tf
try:
  arg_0_0 = 1
  arg_0_1 = 80
  arg_0 = [arg_0_0,arg_0_1,]
  dtype = None
  results["res"] = tf.ones(arg_0,dtype=dtype,)
except Exception as e:
  results["err"] = "Error:"+str(e)
