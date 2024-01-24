#example 1
print(bool("Hi"))
print(bool(12))
True
True

#example 2
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
True
True
True

#example 3
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
False
False
False
False
False
False
False

#example 4
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
False


