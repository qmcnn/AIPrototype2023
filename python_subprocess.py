import subprocess #สำหรับรัน terminal command

def print_():
    print("-----------------------------------------")
if __name__ == "__main__":
    #basic terminal command
    subprocess.run(["ls","-ltr"])
    print("first run num=100 XX=90")
    subprocess.run(["python", "firstpy.py", "--num", "100","--XX", "90"])
    print_()
    print("second run num=-10 XX=-90")
    subprocess.run(["python", "firstpy.py", "--num", "-10","--XX", "-90"])
    print_()
    print("third run num=0")
    subprocess.run(["python", "firstpy.py", "--num", "0"])
    print_()
 

#use output from other program
process_output = subprocess.Popen(["python", "firstpy.py", "--num", "0"],
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
out, err = process_output.communicate()
print(out.decode('utf-8'))
print(len(out.decode('utf-8')))

##HW เขียน subprocess sum output ทั้งหมดของ command 3 อันข้างบน (ตัวเลขก่อน hello world!)

sum_output = 0

output1 = subprocess.check_output(["python", "firstpy.py", "--num", "100", "--XX", "90"]).decode('utf-8')
value1 = int(output1.split('\n')[3]) 
sum_output += value1

output2 = subprocess.check_output(["python", "firstpy.py", "--num", "-10", "--XX", "-90"]).decode('utf-8')
value2 = int(output2.split('\n')[3])  
sum_output += value2

output3 = subprocess.check_output(["python", "firstpy.py", "--num", "0"]).decode('utf-8')
value3 = int(output3.split('\n')[3])  
sum_output += value3

print("sum output")
print(sum_output)

