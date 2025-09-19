def greeting(times = 1,names = None ):
    for i in range(times):
        if names:
            print(f"hello {names}")
        else:
            print("hello")
        pass
greeting(5)
greeting(1, "Harvey")

