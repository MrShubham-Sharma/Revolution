github = ['for loop','variable','block']
github.sort()
print(github)

#for sorting in desending use the (reverse=true)
github = ['for loop','variable','block']
github.sort(reverse=True)
print(github)


#sorting by the closest number of 50
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)