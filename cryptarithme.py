for u in range(1,10):
    for n in range(10):
        for e in range(10):
            for f in range(10):
                for o in range(1,10):
                    for z in range(10):
                        if u!=n and u!=e and u!=f and u!=o and u!=z :
                            if n != e and n!=f and n!=o and n!=z :
                                if e!=f and e !=o and e!=z:
                                    if f!=o and f!=z:
                                        if o!=z :
                                            if ((u*10 +n+ u*10+n+ n*1000+ e* 100 + u*10 + f) == (1000 *o + n*100 + 10 *z + e)) :
                                                print(" ", u, n)
                                                print("+",u,n)
                                                print("+",n,e,u,f)
                                                print("_______")
                                                print("=",o,n,z,e)
                                                break
                        z+=1
                    o+=1
                f+=1
            e+=1
        n+=1
    u+=1