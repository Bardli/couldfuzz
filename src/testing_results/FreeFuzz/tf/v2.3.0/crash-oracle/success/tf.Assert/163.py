import tensorflow as tf
try:
  condition_0 = False
  condition_1 = True
  condition_2 = False
  condition_3 = True
  condition = [condition_0,condition_1,condition_2,condition_3,]
  data_0 = -1
  data_1 = -1024
  data_2 = -25.0
  data_3 = -1
  data = [data_0,data_1,data_2,data_3,]
  summarize_0 = 100
  summarize_1 = 200
  summarize_2 = 300
  summarize_3 = 400
  summarize = [summarize_0,summarize_1,summarize_2,summarize_3,]
  name = None
  results["res"] = tf.Assert(condition=condition,data=data,summarize=summarize,name=name,)
except Exception as e:
  results["err"] = "Error:"+str(e)
