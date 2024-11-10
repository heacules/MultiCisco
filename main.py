import device_action


main_menu = [
    "Quit",
    "Show all device info in yaml file",
    "Enter credential for alle device",
    "Open a SSH session to all device",
    "Show all arp",
]

def menu(menu_option):
    make_a_chois = True
    while make_a_chois:
        for N in range(len(menu_option) ):
            print(f'press {N} for "{menu_option[N]}"')
        user_choise = input("make your chois and press enter: ")
        if user_choise.isdigit():
            if int(user_choise) >= 0 and int(user_choise) <= len(menu_option):
                return int(user_choise)
            else:
                print("not a valid answer, try again \n \n")
        else:
            print("not a valid answer, try again \n \n")

def main():
    #print(devices_ssh_1.yaml_input)
    user_chois = menu(main_menu)
    #print(type(user_chois))
    if user_chois == 0:
        exit()
    elif user_chois == 1:
        print(devices_ssh_1.nice_print())
        print(devices_ssh_1.username)
        main()
    elif user_chois == 2:
        devices_ssh_1.credtianls_information()
        main()
    elif user_chois == 3:
        devices_ssh_1.ssh_conection()
        #print(devices_ssh_1.connection)
        main()
    elif user_chois == 4:
        devices_ssh_1.print_arp()
        main()
    print(user_chois)
if __name__ == "__main__":
    devices_ssh_1 = device_action.my_device('device_list.yaml')
    main()