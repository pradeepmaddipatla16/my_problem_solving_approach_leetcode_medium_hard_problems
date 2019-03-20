buf_dict={}
def function1(log_message,timestamp):
    if log_message in buf_dict:
        if (timestamp - buf_dict[log_message]) < 10:return False
    buf_dict[log_message]=timestamp
    return True

print(function1('foo',1))
print(function1('bar',2))
print(function1('foo',3))