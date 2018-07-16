class A(object):
  def foo(self,x):
    print("executing foo(%s,%s)"%(self,x))
 
  @classmethod
  def class_foo(cls,x):
    print("executing class_foo(%s,%s)"%(cls,x))
 
  @staticmethod
  def static_foo(x):
    print("executing static_foo(%s)"%x)

class B(A):
    def foo1(self,x):
        print("executing foo(%s,%s)"%(self,x))
    def class_foo(self):
        print(self.class_foo(88))

if __name__ == '__main__':
    a=A()
    a.foo(3)
    #A.foo(4)
    a.class_foo(5)
    A.class_foo(6)
    a.static_foo(7)
    A.static_foo(8)
    b = B()
    b.class_foo()