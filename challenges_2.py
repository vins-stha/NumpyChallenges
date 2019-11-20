import numpy as np

np.random.seed(100)
arr = np.random.randint(1,11,size=(6, 10))
print(arr)
a = np.unique(arr,axis=1)

#Y = np.unique(arr,axis=1)

#b = np.bincount(np.array(a[0]))
#arr.shape[0]
#ind = np.array(lambda b : np.bincount(np.array(a[i] for i in arr.shape[0])))

bin_length = arr.shape[1]+1
bin_arr_sized = []
final = []
for i in range(0,arr.shape[0]):
    
    bin_arr = (np.array(a[i]))
    bin_arr_sized=np.bincount(bin_arr,minlength=bin_length)
    final =np.concatenate((final,bin_arr_sized)).astype(int)
    #print("Final",final)
  #  final = np.vstack((a,b))
   # type(bin_arr_sized)
     #ans = ans.append(np.bincount(np.array(a[i])))
        
  #  ans = np.bincount(np.array(a[i]))
final = final.reshape(6,11).astype(int)
final = final[:,1:]
print(final)

