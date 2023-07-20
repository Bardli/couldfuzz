results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      condition_0 = True
      condition_1 = False
      condition_2 = False
      condition_3 = True
      condition = [condition_0,condition_1,condition_2,condition_3,]
      data_0 = 1
      data_1 = 2
      data_2 = 3
      data_3 = 4
      data = [data_0,data_1,data_2,data_3,]
      summarize_0 = 16
      summarize_1 = -1024
      summarize_2 = 1
      summarize_3 = 402
      summarize = [summarize_0,summarize_1,summarize_2,summarize_3,]
      name = None
      results["res_cpu"] = tf.Assert(condition=condition,data=data,summarize=summarize,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      condition = [condition_0,condition_1,condition_2,condition_3,]
      data = [data_0,data_1,data_2,data_3,]
      summarize = [summarize_0,summarize_1,summarize_2,summarize_3,]
      results["res_gpu"] = tf.Assert(condition=condition,data=data,summarize=summarize,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
