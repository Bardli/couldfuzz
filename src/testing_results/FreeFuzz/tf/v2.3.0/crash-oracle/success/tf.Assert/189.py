import tensorflow as tf
try:
  condition_0 = True
  condition_1 = False
  condition_2 = False
  condition_3 = True
  condition = [condition_0,condition_1,condition_2,condition_3,]
  data_0 = -17
  data_1 = 2
  data_2 = 4
  data_3 = 1025
  data = [data_0,data_1,data_2,data_3,]
  summarize_0 = -1
  summarize_1 = 201
  summarize_2 = -1024
  summarize_3 = 398
  summarize = [summarize_0,summarize_1,summarize_2,summarize_3,]
  name = None
  results["res"] = tf.Assert(condition=condition,data=data,summarize=summarize,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)