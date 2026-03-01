#user_system.py

def check_age(age):
    if age>=18:
       return "you are an adult!"
    else:
       return "you are underage."

def main():
   name = input("Enter your name:")
   age = int(input("Enter your age:"))
   print(f"Hello {name}, {check_age(age)}")

if __name__ == "__main__":
     main()
