from speedtest import Speedtest

Download = int(input("""
        Hello , Sir 
            Do You Want Test 
                1 => Speed Download ?
                2 => Speed Upload ?
                3 => Download and Upload ? 
""").strip())

wifi = Speedtest()
def test_down():
        down = wifi.download()
        print(f"The Download Speed Is {down / 1024 / 1024 :.2f} Mbs")
        trying_func = input("""
        Do you Want Speed The Upload ?                            
        """).strip()
        if trying_func == 'yes' or trying_func == 'y':
            test_upload()
        else:
            print("Thank You For Used My Program")
def test_upload():
        upload = wifi.upload()
        print(f"The Upload Speed Is {upload / 1024 / 1024 :.2f} Mbs")
        trying_func = input("""
        Do you Want Speed The Download ?                            
        """).strip()
        if trying_func == 'yes' or trying_func == 'y':
            test_upload()
        else:
            print("Thank You For Used My Program")


if Download == 1 :
    test_down()
elif Download == 2 :
    test_upload()   
elif Download == 3 :
    test_down()
    test_upload()   


