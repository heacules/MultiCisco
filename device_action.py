import netmiko
import yaml
import getpass

class my_device ():

    def __init__(self, filepath):
        with open(filepath, 'r') as file:
            self.yaml_device_list = yaml.safe_load(file)
            self.connection = []
            self.username = ""
            self.password = ""
            #print(yaml_input)
            #return yaml_input

    def ssh_conection(self):
        #missing to write this function
        for device in self.yaml_device_list:
            connection_info = { 
                "device_type" : "cisco_ios",
                "host" : device["ip"],
                "username" : self.username,
                "password" : self.password,
            }
            #print(connection_info)
            connection = netmiko.ConnectHandler(**connection_info)
            self.connection.append(connection)
        #print(self.connection)
        #return self.connection

    def nice_print (self):
        return yaml.safe_dump(self.yaml_device_list)
    
    def credtianls_information (self):
        self.username = input("enter the username to use for all device: ")
        self.password = getpass.getpass("enter the password for alle the device: ")
    
    def print_arp(self):
        print(self.connection)
        for device in self.connection:
            print(device.send_command("show arp"))


def main():
    #do nofthing here
    pass    

if __name__ == "__main__":
    main()