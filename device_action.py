import netmiko
import yaml

class my_device ():

    def __init__(self, filepath):
        with open(filepath, 'r') as file:
            yaml_input = yaml.safe_load(file)
            print(yaml_input)


def main():
    #do nofthing here
    pass    

if __name__ == "__main__":
    main()