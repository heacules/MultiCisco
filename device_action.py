import netmiko
import yaml

class my_device ():

    def __init__(self, filepath):
        with open(filepath, 'r') as file:
            self.yaml_device_list = yaml.safe_load(file)
            connection = []
            #print(yaml_input)
            #return yaml_input

    def ssh_conection(self):
        for device in self.yaml_device_list[0]['device']:
            pass

    def nice_print (self):
        return yaml.safe_dump(self.yaml_device_list)
    
    def print_arp(self):
        pass


def main():
    #do nofthing here
    pass    

if __name__ == "__main__":
    main()