
t n=foldr(\x ((a,b,d),c)->((b,c,x),a+b+c))((0,1,0),2)[3..(n+1)]
c m=foldr(\x a->a/(x+1)*(4*x-2))1[1..m]
ohno=(floor.logBase 2.c.snd.t)