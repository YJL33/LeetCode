"""
Operational testing model for LEETCODE
"""
#import _146_LRU_cache as mod146
import _155_min_stack as mod155

#sol146 = mod146.LRUCache(3)
#test = [sol146.set(1,1),sol146.set(2,2),sol146.set(3,3),sol146.set(4,4),sol146.get(4),sol146.get(3),sol146.get(2),sol146.get(1),sol146.set(5,5),sol146.get(1),sol146.get(2),sol146.get(3),sol146.get(4),sol146.get(5)]
#for method in test: print method

ops = ["MinStack", "push","push","push","getMin","pop","top","getMin","push","push","push","getMin","pop","getMin","pop","getMin","pop"]
args = [[], [-2],  [-1], [-3],  [],      [],   [],   [],      [-4],  [-5],  [-6], [],      [],   [],      [],   [],      []]
sol155 = mod155.MinStack()

for i in xrange(1,len(ops)):
    op, arg = ops[i], args[i]
    methodToCall = getattr(sol155, op)
    if arg:
        res = methodToCall(arg[0])
    else:
        res = methodToCall()
    print res
