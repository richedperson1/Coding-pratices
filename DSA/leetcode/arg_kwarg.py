s = 'foo'
t = 'bar'
print(*zip(s,t))
def check(s,t):
        
    mapping_s_t = {}
    mapping_t_s = {}
    for s1,t1 in zip(s,t):
        if s1 not in mapping_s_t and t1 not in mapping_t_s:
            mapping_t_s[t1] = s1
            mapping_s_t[s1] = t1
            
        elif mapping_t_s.get(t1) or mapping_s_t.get(s1)!=t1:
            return False
        
    return True
print(check(s,t))