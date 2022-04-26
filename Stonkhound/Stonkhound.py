from format_data import *

def main():
    print("=========================================")
    print("         WELCOME TO STONKHOUND!")
    print("=========================================")

    data = get_dataset()    
    
    for dp in data:
        print(dp)

if __name__ == "__main__":
    main()