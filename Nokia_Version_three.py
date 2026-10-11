
menu = """
 
================================================================
Welcome to Nokia 5510
================================================================
 
Select an [Option]
 
1.  Phone book
2.  Messages
3.  Chat
4.  Call register
5.  Tones
6.  Settings
7.  Call divert
8.  Music
9.  Games
10. Calculator
11. Reminders
12. Clock
13. Profiles
14. Services
15. Sim services
0.  Exit
 
================================================================
""";
 
 
def main_menu():
 
    while True:
 
        menu_choice = input(menu)
 
        match menu_choice:
 
            case "1":
                phone_book()
            case "2":
                messages()
            case "3":
                print("Chat")
            case "4":
                call_register()
            case "5":
                tones()
            case "6":
                settings()
            case "7":
                print("Call divert")
            case "8":
                music()
            case "9":
                print("Games")
            case "10":
                print("Calculator")
            case "11":
                print("Reminders")
            case "12":
                clock()
            case "13":
                print("Profiles")
            case "14":
                print("Services")
            case "15":
                print("SIM services")
            case "0":
                print("Exit")
                break
            case _:
                print("Invalid")
 
 
 
 
 
def phone_book():
 
    while True:
 
        print("Phone Book")
 
        phone_book_list = """
 
        ================================================================
        Phone Book List
        ================================================================
 
        1.  Search
        2.  Service Nos
        3.  Add name
        4.  Erase
        5.  Edit
        6.  Copy
        7.  Assign tone
        8.  Send b’card
        9.  Options
        10. Speed dials
        11. Voice tags
        0.  Back
        99. Home
 
        ================================================================
 
        """;
 
        phone_book_menu_choice = input(phone_book_list)
 
        match phone_book_menu_choice:
 
            case "1":
                print("Search")
            case "2":
                print("Service Nos")
            case "3":
                print("Add name")
            case "4":
                print("Erase")
            case "5":
                print("Edit")
            case "6":
                print("Copy")
            case "7":
                print("Assign tone")
            case "8":
                print("Send b'card")
            case "9":
 
                while True:
 
                    print("""
        ================================================================
        List of Options
        ================================================================""");
 
                    options_list = """
 
        1.  Memory in use
        2.  Type of view
        3.  Memory Status
        0.  Back
        99. Home
 
        ================================================================
 
        """;
 
                    options_menu = input(options_list)
 
                    match options_menu:
 
                        case "1":
                            print("Memory in use")
                        case "2":
                            print("Type of view")
                        case "3":
                            print("Memory Status")
                        case "0":
                            break
                        case "99":
                            return
                        case _:
                            print("Invalid")
 
            case "10":
                print("Speed dials")
            case "11":
                print("Voice tags")
            case "0":
                break
            case "99":
                return
            case _:
                print("Invalid")
 
 
 
 
 
def messages():
 
    while True:
 
        print("Messages")
 
        message_list = """
 
        ================================================================
        Messages List
        ================================================================
 
        1.  Write messages
        2.  Inbox
        3.  Outbox
        4.  Picture messages
        5.  Templates
        6.  Smileys
        7.  Message settings
        8.  Info service
        9.  Voice mailbox number
        10. Service command editor
        0.  Back
        99. Home
 
        ================================================================
 
        """;
 
        message_choice = input(message_list)
 
        match message_choice:
 
            case "1":
                print("Write message")
            case "2":
                print("Inbox")
            case "3":
                print("Outbox")
            case "4":
                print("Picture message")
            case "5":
                print("Template")
            case "6":
                print("Smileys")
            case "7":
 
                while True:
 
                    print("""
        ================================================================
        Message settings
        ================================================================""")
 
                    message_settings_list = """
 
        1.  Set
        2.  Common
        0.  Back
        99. Home
 
        ================================================================
 
        """;
 
                    message_settings_menu = input(message_settings_list)
 
                    match message_settings_menu:
 
                        case "1":
 
                            while True:
 
                                print("""
        ================================================================
        Set 1
        ================================================================""");
 
                                set_list = """
 
        1.  Message Centre number
        2.  Messages sent as
        3.  Message validity
        0.  Back
        99. Home
 
        ================================================================
 
        """;
 
                                set_menu = input(set_list)
 
                                match set_menu:
 
                                    case "1":
                                        print("Message Centre Number")
                                    case "2":
                                        print("Message Sent as")
                                    case "3":
                                        print("Message Validity")
                                    case "0":
                                        break
                                    case "99":
                                        return
                                    case _:
                                        print("Invalid")
 
                        case "2":
 
                            while True:
 
                                print("""
        ================================================================
        Common
        ================================================================""");
 
                                common_list = """
 
        1.  Delivery reports
        2.  Reply via same centre
        3.  Character support
        0.  Back
        99. Home
 
        ================================================================
 
        """;
 
                                common_menu = input(common_list)
 
                                match common_menu:
 
                                    case "1":
                                        print("Delivery reports")
                                    case "2":
                                        print("Reply via same centre")
                                    case "3":
                                        print("Character support")
                                    case "0":
                                        break
                                    case "99":
                                        return
                                    case _:
                                        print("Invalid")
 
                        case "0":
                            break
                        case "99":
                            return
                        case _:
                            print("Invalid")
 
            case "8":
                print("Info Services")
            case "9":
                print("Voice mailbox")
            case "10":
                print("Service command editor")
            case "0":
                break
            case "99":
                return
            case _:
                print("Invalid")
 
 
 
 
 
def call_register():
 
    while True:
 
        print("Call register")
 
        call_register_list = """
 
        ================================================================
        Call Register Menu
        ================================================================
 
        1.  Missed calls
        2.  Received calls
        3.  Dialled numbers
        4.  Erase recent call lists
        5.  Show call duration
        6.  Show call costs
        7.  Call cost settings
        8.  Prepaid credit
        0.  Back
        99. Home
 
        ================================================================
 
        """;
 
        call_register_menu = input(call_register_list)
 
        match call_register_menu:
 
            case "1":
                print("Missed calls")
            case "2":
                print("Received calls")
            case "3":
                print("Dialled numbers")
            case "4":
                print("Erase recent call lists")
            case "5":
 
                while True:
 
                    print("""
        ================================================================
        Show call duration
        ================================================================""");
 
                    call_duration_list = """
 
        1.  Last call duration
        2.  All calls duration
        3.  Received calls’ duration
        4.  Dialled calls’ duration
        5.  Clear timers
        0.  Back
        99. Home
 
        ================================================================
 
        """;
 
                    call_duration_menu = input(call_duration_list)
 
                    match call_duration_menu:
 
                        case "1":
                            print("Last call duration")
                        case "2":
                            print("All calls duration")
                        case "3":
                            print("Received calls’ duration")
                        case "4":
                            print("Dialled calls’ duration")
                        case "5":
                            print("Clear timers")
                        case "0":
                            break
                        case "99":
                            return
                        case _:
                            print("Invalid")
 
            case "6":
 
                while True:
 
                    print("""
        ================================================================
        Show call costs
        ================================================================""");
 
                    call_cost_list = """
 
        1.  Last call cost
        2.  All calls cost
        3.  Clear counters
        0.  Back
        99. Home
 
        ================================================================
 
        """;
 
                    call_cost_menu = input(call_cost_list)
 
                    match call_cost_menu:
 
                        case "1":
                            print("Last call cost")
                        case "2":
                            print("All calls cost")
                        case "3":
                            print("Clear counters")
                        case "0":
                            break
                        case "99":
                            return
                        case _:
                            print("Invalid")
 
            case "7":
 
                while True:
 
                    print("""
        ================================================================
        Call cost settings
        ================================================================""");
 
                    call_cost_settings_list = """
 
        1.  Call cost limit
        2.  Show costs in
        0.  Back
        99. Home
 
        ================================================================
 
        """;
 
                    call_cost_settings_menu = input(call_cost_settings_list)
 
                    match call_cost_settings_menu:
 
                        case "1":
                            print("Call cost limit")
                        case "2":
                            print("Show costs in")
                        case "0":
                            break
                        case "99":
                            return
                        case _:
                            print("Invalid")
 
            case "8":
                print("Prepaid credit")
            case "0":
                break
            case "99":
                return
            case _:
                print("Invalid")
 
 
 
 
 
def tones():
 
    while True:
 
        print("Tones")
 
        tones_list = """
 
        ================================================================
        Tones List
        ================================================================
 
        1.  Ringing tone
        2.  Ringing volume
        3.  Incoming call alert
        4.  Message alert tone
        5.  Keypad tones
        6.  Warning tones
        7.  Vibrating alert
        8.  Screen saver
        0.  Back
        99. Home
 
        ================================================================
 
        """;
 
        tones_menu = input(tones_list)
 
        match tones_menu:
 
            case "1":
                print("Ringing tone")
            case "2":
                print("Ringing volume")
            case "3":
                print("Incoming call alert")
            case "4":
                print("Message alert tone")
            case "5":
                print("Keypad tones")
            case "6":
                print("Warning tones")
            case "7":
                print("Vibrating alert")
            case "8":
                print("Screen saver")
            case "0":
                break
            case "99":
                return
            case _:
                print("Invalid")
 
 
 
 
 
def settings():
 
    while True:
 
        print("Settings")
 
        settings_list = """
 
        ================================================================
        Settings Menu
        ================================================================
 
        1.  Call settings
        2.  Phone settings
        3.  Security settings
        4.  Restore factory settings
        0.  Back
        99. Home
 
        ================================================================
 
        """;
 
        settings_menu = input(settings_list)
 
        match settings_menu:
 
            case "1":
 
                while True:
 
                    print("""
        ================================================================
        Call settings
        ================================================================""");
 
                    call_settings_list = """
 
        1.  Automatic redial
        2.  Speed dialling
        3.  Call waiting options
        4.  Own number sending
        5.  Phone line in use
        6.  Automatic answer
        0.  Back
        99. Home
 
        ================================================================
 
        """;
 
                    call_settings_menu = input(call_settings_list)
 
                    match call_settings_menu:
 
                        case "1":
                            print("Automatic redial")
                        case "2":
                            print("Speed dialling")
                        case "3":
                            print("Call waiting options")
                        case "4":
                            print("Own number sending")
                        case "5":
                            print("Phone line in use")
                        case "6":
                            print("Automatic answer")
                        case "0":
                            break
                        case "99":
                            return
                        case _:
                            print("Invalid")
 
            case "2":
 
                while True:
 
                    print("""
        ================================================================
        Phone Settings
        ================================================================""");
 
                    phone_settings_list = """
 
        1.  Language
        2.  Cell info display
        3.  Welcome note
        4.  Network selection
        5.  Confirm SIM service actions
        0.  Back
        99. Home
 
        ================================================================
 
        """;
 
                    phone_settings_menu = input(phone_settings_list)
 
                    match phone_settings_menu:
 
                        case "1":
                            print("Language")
                        case "2":
                            print("Cell info display")
                        case "3":
                            print("Welcome note")
                        case "4":
                            print("Network selection")
                        case "5":
                            print("Confirm SIM service actions")
                        case "0":
                            break
                        case "99":
                            return
                        case _:
                            print("Invalid")
 
            case "3":
 
                while True:
 
                    print("""
        ================================================================
        Security settings
        ================================================================""");
 
                    security_settings_list = """
 
        1.  PIN code request
        2.  Call barring service
        3.  Fixed dialling
        4.  Closed user group
        5.  Security level
        6.  Change access codes
        0.  Back
        99. Home
 
        ================================================================
 
        """;
 
                    security_settings_menu = input(security_settings_list)
 
                    match security_settings_menu:
 
                        case "1":
                            print("PIN code request")
                        case "2":
                            print("Call barring service")
                        case "3":
                            print("Fixed dialling")
                        case "4":
                            print("Closed user group")
                        case "5":
                            print("Security level")
                        case "6":
                            print("Change access codes")
                        case "0":
                            break
                        case "99":
                            return
                        case _:
                            print("Invalid")
 
            case "4":
                print("Restore factory settings")
            case "0":
                break
            case "99":
                return
            case _:
                print("Invalid")
 
 
 
 
 
def music():
 
    while True:
 
        print("Music")
 
        music_list = """
 
        ================================================================
        Music List
        ================================================================
 
        1.  Music player
        2.  Radio
        3.  Recorder
        4.  Track list
        0.  Back
        99. Home
 
        ================================================================
 
        """;
 
        music_menu = input(music_list)
 
        match music_menu:
 
            case "1":
                print("Music player")
            case "2":
                print("Radio")
            case "3":
                print("Recorder")
            case "4":
                print("Track list")
            case "0":
                break
            case "99":
                return
            case _:
                print("Invalid")
 
 
 
 
 
def clock():
 
    while True:
 
        print("Clock")
 
        clock_list = """
 
        ================================================================
        Clock List
        ================================================================
 
        1.  Alarm clock
        2.  Clock settings
        3.  Date setting
        4.  Stopwatch
        5.  Countdown timer
        6.  Auto update of date and time
        0.  Back
        99. Home
 
        ================================================================
 
        """;
 
        clock_menu = input(clock_list)
 
        match clock_menu:
 
            case "1":
                print("Alarm clock")
            case "2":
                print("Clock settings")
            case "3":
                print("Date setting")
            case "4":
                print("Stopwatch")
            case "5":
                print("Countdown timer")
            case "6":
                print("Auto update of date and time")
            case "0":
                break
            case "99":
                return
            case _:
                print("Invalid")
 
 
 
 
 
main_menu()

