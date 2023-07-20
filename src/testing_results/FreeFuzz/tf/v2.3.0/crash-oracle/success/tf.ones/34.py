import tensorflow as tf
try:
  arg_0_0 = 1
  arg_0_1 = 8
  arg_0_2 = 12
  arg_0_3 = 64
  arg_0 = [arg_0_0,arg_0_1,arg_0_2,arg_0_3,]
  results["res"] = tf.ones(arg_0,)
except Exception as e:
  results["err"] = "Error:"+str(e)
