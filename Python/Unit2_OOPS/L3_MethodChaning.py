#  Method Chaning:   Calling Multiple Methods sequentially
#                  each call performs an action on the same object and return self.

class MultipleName:
    def name1(self):
        print("Hi,My Name is Shailesh")
        return self
    
    def name2(self):
        print("Hi,My Name is Raju")
        return self

    def name3(self):
        print("Hi,My Name is Roshni")
        return self
    
    def name4(self):
        print("Hi,My Name is Preeti")
        return self   #When Call One object two method then required self attributes show step2 & step3
    

obj = MultipleName()
# Step1 :  Find Multiple Methods Calling Tips
# obj.name1()
# obj.name2()
# obj.name3()
# obj.name4()

# Step2 :  Find Multiple Methods Calling Tips

# obj.name1().name2()
# obj.name3().name4()

# Step3 :  Find Multiple Methods Calling Tips

obj.name1().name2().name3().name4()