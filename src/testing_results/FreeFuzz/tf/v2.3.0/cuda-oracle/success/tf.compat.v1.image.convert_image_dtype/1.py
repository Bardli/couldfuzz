results = dict()
import tensorflow as tf
try:
  try:
    with tf.device('/CPU'):
      image_0_0_0 = 1.0
      image_0_0_1 = 2.0
      image_0_0_2 = 3.0
      image_0_0 = [image_0_0_0,image_0_0_1,image_0_0_2,]
      image_0_1_0 = 4.0
      image_0_1_1 = 5.0
      image_0_1_2 = 6.0
      image_0_1 = [image_0_1_0,image_0_1_1,image_0_1_2,]
      image_0 = [image_0_0,image_0_1,]
      image_1_0_0 = 7.0
      image_1_0_1 = 8.0
      image_1_0_2 = 9.0
      image_1_0 = [image_1_0_0,image_1_0_1,image_1_0_2,]
      image_1_1_0 = 10.0
      image_1_1_1 = 11.0
      image_1_1_2 = 12.0
      image_1_1 = [image_1_1_0,image_1_1_1,image_1_1_2,]
      image_1 = [image_1_0,image_1_1,]
      image = [image_0,image_1,]
      dtype = 5
      saturate = 11
      name = None
      results["res_cpu"] = tf.compat.v1.image.convert_image_dtype(image=image,dtype=dtype,saturate=saturate,name=name,)
  except Exception as e:
    results["err_cpu"] = "Error:"+str(e)
  try:
    with tf.device('/GPU:0'):
      image_0_0 = [image_0_0_0,image_0_0_1,image_0_0_2,]
      image_0_1 = [image_0_1_0,image_0_1_1,image_0_1_2,]
      image_0 = [image_0_0,image_0_1,]
      image_1_0 = [image_1_0_0,image_1_0_1,image_1_0_2,]
      image_1_1 = [image_1_1_0,image_1_1_1,image_1_1_2,]
      image_1 = [image_1_0,image_1_1,]
      image = [image_0,image_1,]
      results["res_gpu"] = tf.compat.v1.image.convert_image_dtype(image=image,dtype=dtype,saturate=saturate,name=name,)
  except Exception as e:
    results["err_gpu"] = "Error:"+str(e)
except Exception as e:
  results["err"] = "Error:"+str(e)

print(results)
