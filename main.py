import device_action


main_menu = [
    "show all device",
    "show all arp",
]

def menu(menu_option):
    make_a_chois = True
    while make_a_chois:
        for N in range(len(menu_option) ):
            #print(N)
            print(f'press {N} for "{menu_option[N]}"')
        user_choise = input("make your chois and press enter: ")
        if int(user_choise) >= 0 and int(user_choise) <= len(menu_option):
            return user_choise
        else:
            print("not a valid answer, try again \n \n")


def main():
    device_info = device_action.my_device('device_list.yaml')
    print(device_info)
    user_chois = menu(main_menu)
    if user_chois == 0:
        pass
    elif user_chois == 1:
        pass
    print(user_chois)
if __name__ == "__main__":
    main()