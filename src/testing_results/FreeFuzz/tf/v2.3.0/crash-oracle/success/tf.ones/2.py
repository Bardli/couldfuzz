import tensorflow as tf
try:
  arg_0_0 = 8
  arg_0_1 = 6
  arg_0 = [arg_0_0,arg_0_1,]
  results["res"] = tf.ones(arg_0,)
except Exception as e:
  results["err"] = "Error:"+str(e)
