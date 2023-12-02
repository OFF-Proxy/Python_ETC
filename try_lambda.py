def execute_param_fn(args, hosei, fn):
    result=fn(args, hosei)
    return result

print (execute_param_fn([1,2,3],4,lambda a, b: max(a)+b))
print (execute_param_fn([1,2,3],4,lambda a, b: min(a)-b))
