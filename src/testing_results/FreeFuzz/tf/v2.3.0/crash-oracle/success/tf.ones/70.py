import tensorflow as tf
try:
  arg_0_0 = 5
  arg_0_1 = 22
  arg_0 = [arg_0_0,arg_0_1,]
  results["res"] = tf.ones(arg_0,)
except Exception as e:
  results["err"] = "Error:"+str(e)
