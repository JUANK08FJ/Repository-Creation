import re


def initial_repository():
    global repository

    # LOOP WHERE THE USER CAN'T LEAVE THE NAME EMPTY
    while True:
        repo_name = re.sub(r"\s+", " ", input("\nWrite a name for the repository: ").strip())
        if repo_name == "":
            print("\nYou can't leave the name empty.")
            continue

        # LOOP WHERE THE USER CAN'T LEAVE THE CATEGORY EMPTY
        while True:
            repo_category = re.sub(r"\s+", " ", input(f"\nWrite a category for the repository {repo_name}: ").strip())
            if repo_category == "":
                print(f"\nYou can't leave the category of {repo_name} empty.")
                continue
            else:
                break

        # CREATE THE REPOSITORY IN VARIABLE REPOSITORY
        repository = {"name": repo_name, "category": repo_category, "software": []}
        print(f"\nThe repository {repo_name} has been created with category {repo_category}.")
        break


def create_software():
    global repository

    # LOOP WHERE THE USER MUST ANSWER WITH A NUMBER OF 3 DIGITS
    while True:
        try:
            software_id = int(re.sub(r"\s+", "", input("\nWrite an id for the new software ( 0. Cancel ): ").strip()))

        # THE USER RETURN A STRING INSTEAD OF A INTEGER
        except ValueError:
            print("\nPlease enter an integer for the software creation.")
            continue

        # END THE FUNCTION TO CANCEL THE SOFTWARE CREATION
        if software_id == 0:
            return

        # THE ENTER USER'S ID CAN'T BE NEGATIVE OR HAVE MORE THAN 3 DIGITS
        elif software_id < 0 or software_id > 999:
            print("\nPlease enter an integer with 3 natural digits for the software creation.")
            continue

        # CHECK IF THE SOFTWARE LIST DON'T HAVE ANY DICTIONARY OR IF THE ID SOFTWARE DOESN'T EXIST IN THE LIST
        else:
            non_existent_id = True

            for software in repository["software"]:
                if software["id"] == software_id:
                    non_existent_id = False
                    print(f"\nThe id {software['id']} already exists for the software {software['name']}.")

            if not repository["software"] or non_existent_id:
                break

    # LOOP WHERE THE USER CAN'T LEAVE THE NAME EMPTY
    while True:
        name_software = re.sub(r"\s+", " ", input("\nWrite a name for the software ( 0. Cancel ): ").strip())
        if name_software == "":
            print("\nYou can't leave the name empty.")
            continue

        # END THE FUNCTION TO CANCEL THE SOFTWARE CREATION
        elif name_software == "0":
            return

        # BREAK THE LOOP WITH THE NAME OF THE SOFTWARE
        break

    # ADD THE SOFTWARE TO THE REPOSITORY AND PRINT THE SOFTWARE IN QUESTION
    repository["software"].append({"id": software_id, "name": name_software, "files": [], "developers": []})
    print(f"\nSoftware {name_software} has been created with id {software_id} in the software list.")


def delete_software():
    global repository

    # VARIABLE WITH THE LIST OF SOFTWARE'S AND CHECK IF THERE IS ANY SOFTWARE
    if not repository["software"]:
        return print("\nThere isn't any software created to delete.")

    # PRINT EVERY EXISTENT SOFTWARE IN THE REPOSITORY
    print("")
    for software in repository["software"]:
        print(f"Software name: {software['name']} || id: {software['id']}")

    # LOOP WHERE THE USER MUST ANSWER WITH AN EXISTENT ID SOFTWARE
    while True:
        try:
            software_id = int(
                re.sub(r"\s+", " ", input("\nWrite the id of the software you want to delete ( 0. Cancel ): ").strip()))

        # THE USER RETURN A STRING INSTEAD OF A INTEGER
        except ValueError:
            print("\nPlease enter an integer for the software deleting.")
            continue

        # END THE FUNCTION TO CANCEL THE SOFTWARE CREATION
        if software_id == 0:
            return

        # CHECK IF THE SOFTWARE ID EXIST IN THE LIST
        else:
            existent_id = False

            for software in repository["software"]:
                if software["id"] == software_id:
                    existent_id = True

            # BREAK THE LOOP IF THE ID EXIST IN THE LIST SOFTWARE
            if existent_id:
                break

        # THE USER RETURN AN NON-EXISTENT ID IN THE SOFTWARE LIST
        print("\nPlease enter an existent id for the software elimination.")

    # DELETE THE DICTIONARY WITH THE ID INSIDE THE SOFTWARE LIST
    for sw_count in range(len(repository["software"])):
        if software_id == repository["software"][sw_count]["id"]:
            print(f"\nSoftware {repository['software'][sw_count]['name']} with id {software_id} has been deleted.")
            repository["software"].pop(sw_count)
            return


def create_file():
    global repository

    # SELECT THE SOFTWARE ID FOR USE
    access_software = software_selection("create", "file")

    if access_software is None:
        return

    # LOOP WHERE THE USER CAN'T LEAVE THE NAME OF THE FILE EMPTY
    while True:
        file_name = re.sub(r"\s+", "",
                           input("\nWrite a name for the file inside the software ( 0. Cancel ): ").strip())
        if file_name == "":
            if file_name == "":
                print("\nYou can't leave the filename empty.")
                continue

        # END THE FUNCTION TO CANCEL THE FILE CREATION
        elif file_name == "0":
            return

        # LOOP WHERE THE USER CAN'T LEAVE THE SIZE OF THE FILE EMPTY
        while True:
            try:
                file_size = int(
                    re.sub(r"\s+", " ", input(f"\nWrite the size of the file {file_name} ( -1. Cancel ): ").strip()))

            # THE USER RETURN A STRING INSTEAD OF A INTEGER
            except ValueError:
                print("\nPlease enter an integer for the file creation.")
                continue

            # END THE FUNCTION TO CANCEL THE FILE CREATION
            if file_size == -1:
                return

            # BREAK THE LOOP WITH THE NAME AND THE SIZE OF THE FILE
            else:
                break
        break

    # ENTER THE SOFTWARE SELECTED
    for sw_count in range(len(repository["software"])):
        if access_software == repository["software"][sw_count]["id"]:
            selected_id = sw_count
            selected_sw = repository["software"][sw_count]

    # ENTER THE FILES LIST WITH THE SOFTWARE ID
    if not selected_sw["files"]:
        repository["software"][selected_id]["files"].append({"name": file_name, "size": file_size})
        print(f"\nFile {file_name} with {file_size} bytes has been successfully created.")

    # CHECK IF THE FILENAME DON'T EXIST
    else:
        count = 0
        while count == 0:
            count = 1

            for file in selected_sw["files"]:

                if file["name"] == file_name:
                    print(f"\nFile with name {file_name} already exists.")

                    # LOOP UNTIL THE USER RETURN A NEW NAME FOR THE FILE
                    while True:
                        file_name = re.sub(r"\s+", " ", input(
                            f"\nWrite a new name for the file inside the software {selected_sw['name']} ( 0. Cancel ): ").strip())

                        if file_name == "":
                            print("\nYou can't leave the filename empty.")
                            continue

                        # END THE FUNCTION TO CANCEL THE FILE CREATION
                        elif file_name == "0":
                            return

                        count = 0
                        break

        repository["software"][selected_id]["files"].append({"name": file_name, "size": file_size})
        print(
            f"\nFile {file_name} with {file_size} bytes has been successfully created inside the software {selected_sw['name']}.")


def delete_file():
    global repository

    # SELECT THE SOFTWARE ID FOR USE
    access_software = software_selection("delete", "file")

    if access_software is None:
        return

    # ENTER THE SOFTWARE SELECTED
    for sw_count in range(len(repository["software"])):
        if access_software == repository["software"][sw_count]["id"]:
            selected_id = sw_count
            selected_sw = repository["software"][sw_count]

    # CHECK IF THERE IS ANY FILE
    if not selected_sw["files"]:
        return print(f"\nThere isn't any file created to delete in software {selected_sw['name']}.")

    # PRINT EVERY EXISTENT FILE IN THE SOFTWARE LIST
    print("")
    for file in selected_sw["files"]:
        print(f"Software name: {file['name']} || size: {file['size']}")

    # CHECK IF THE FILENAME EXISTS INSIDE THE SOFTWARE
    count = 0
    while count == 0:
        file_name = re.sub(r"\s+", " ", input("\nWrite the name of the file to be deleted ( 0. Cancel ): ").strip())

        if file_name == "":
            print("\nYou can't leave the filename empty.")
            continue

        for file in selected_sw["files"]:
            if file_name == file["name"]:
                count = 1

        # END THE FUNCTION TO CANCEL THE FILE CREATION
        if file_name == "0":
            return

        elif count == 0:
            print("\nPlease enter an existent name for the file deletion.")

    # DELETE THE DICTIONARY WITH THE ID INSIDE THE SOFTWARE LIST
    for count_file in range(len(selected_sw["files"])):
        if file_name == selected_sw["files"][count_file]["name"]:
            print(
                f"\nFile with name {selected_sw['files'][count_file]['name']} with size {selected_sw['files'][count_file]['size']} deleted from the software {selected_sw['name']}.")
            repository["software"][selected_id]["files"].pop(count_file)
            return


def modify_file():
    global repository

    # SELECT THE SOFTWARE ID FOR USE
    access_software = software_selection("modify", "file")

    if access_software is None:
        return

    # ENTER THE SOFTWARE SELECTED
    for sw_count in range(len(repository["software"])):
        if access_software == repository["software"][sw_count]["id"]:
            selected_id = sw_count
            selected_sw = repository["software"][sw_count]

    # CHECK IF THERE IS ANY FILE
    if not selected_sw["files"]:
        return print(f"\nThere isn't any file created to modify in the software {selected_sw['name']}.")

    # PRINT EVERY EXISTENT FILE IN THE SOFTWARE LIST
    print("")
    for file in selected_sw["files"]:
        print(f"Software name: {file['name']} || size: {file['size']}")

    # CHECK IF THE FILENAME EXISTS INSIDE THE SOFTWARE
    count = 0
    while count == 0:
        file_name = re.sub(r"\s+", " ", input("\nWrite the name of the file to be modified ( 0. Cancel ): ").strip())

        if file_name == "":
            print("\nYou can't leave the filename empty.")
            continue

        if file_name == "0":
            return

        # END THE FUNCTION TO CANCEL THE FILE CREATION
        for file in selected_sw["files"]:
            if file_name == file["name"]:
                count = 1
                break

        if count == 0:
            print("\nPlease enter an existent name for the file modification.")

    # THE USER MUST SAY WHAT PARAMETER HE WANTS TO MODIFY OF THE SELECTED FILE
    while True:
        try:
            modify_file = int(input(
                f"\nWhat do you want to modify inside the file {file_name} ( 1. Name || 2. Size || 0. Cancel ): "))

            # CALL A FUNCTION TO CREATE A SOFTWARE
            if modify_file == 1:
                while True:
                    new_filename = re.sub(r"\s+", " ",
                                          input(
                                              f"\nWrite the new name for the file {file_name} ( 0. Cancel ): ").strip())

                    if new_filename == "":
                        print("\nYou can't leave the filename empty.")
                        continue

                    if new_filename == "0":
                        return

                    nonexistent_name = True

                    for file in selected_sw["files"]:
                        if new_filename == file["name"]:
                            nonexistent_name = False

                    if nonexistent_name:
                        for file_count in range(len(selected_sw["files"])):
                            if selected_sw["files"][file_count]["name"] == file_name:
                                repository["software"][selected_id]["files"][file_count]["name"] = new_filename
                                print(f"\nThe name of the file {file_name} has been updated to {new_filename}.")
                                return

                    print(f"\nThe filename {new_filename} already exists try another name for the file {file_name}.")

            # CALL A FUNCTION TO DELETE A SOFTWARE
            elif modify_file == 2:

                # LOOP WHERE THE USER CAN'T LEAVE THE SIZE OF THE FILE EMPTY
                while True:
                    try:
                        new_file_size = int(re.sub(r"\s+", "", input(
                            f"\nWrite the new size of the file {file_name} ( -1. Cancel ): ").strip()))

                    # THE USER RETURN A STRING INSTEAD OF A INTEGER
                    except ValueError:
                        print("\nPlease enter an integer for the file creation.")
                        continue

                    # END THE FUNCTION TO CANCEL THE FILE CREATION
                    if new_file_size == -1:
                        return

                    # BREAK THE LOOP WITH THE NAME AND THE SIZE OF THE FILE
                    else:
                        for file_count in range(len(selected_sw["files"])):
                            if selected_sw["files"][file_count]["name"] == file_name:
                                repository["software"][selected_id]["files"][file_count]["size"] = new_file_size
                                print(f"\nFile {file_name} now has a size of {new_file_size}.")
                                return

            # BREAK THE LOOP TO CANCEL THE SOFTWARE ACTION
            elif modify_file == 0:
                return

            # THE ACTION ISN'T IN THE LIST OF FUNCTIONS FOR SOFTWARE
            else:
                print("\nYour answer isn't on the list of actions.")

        # THE USER RETURN A STRING INSTEAD OF A INTEGER
        except ValueError:
            print("\nYour answer must be a number.")


def create_developer():
    global repository

    access_software = software_selection("create", "developer")

    if access_software is None:
        return

    while True:
        developer_name = re.sub(r"\s+", " ",
                                input("\nWrite a name for the developer inside the software ( 0. Cancel ): ").strip())

        if developer_name == "":
            print("\nYou can't leave the developer name empty.")
            continue

        elif developer_name == "0":
            return

        break

    while True:
        freelance_status = re.sub(r"\s+", " ", input(
            f"\nIs the freelance of the developer {developer_name} active now? (0. Cancel): ").strip()).lower()

        if freelance_status == "":
            print("\nYou can't leave the freelance status empty.")
            continue

        elif freelance_status == "yes":
            freelance_status = True
            break

        elif freelance_status == "no":
            freelance_status = False
            break

        elif freelance_status == "0":
            return

        print("\nYour answer must be ( yes | no )")

    while True:
        website = re.sub(r"\s+", "", input(
            f"\nWrite the website of the developer {developer_name} (0. Cancel): ").strip())

        if website == "":
            print("\nYou can't leave the website empty.")
            continue

        elif website == "0":
            return

        patron_url = re.compile(
            r'(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        patron_url = bool(re.match(patron_url, website))

        if patron_url:
            break
        else:
            print("\nThe website don't have structure of website")

    for sw_count in range(len(repository["software"])):
        if access_software == repository["software"][sw_count]["id"]:
            selected_id = sw_count
            selected_sw = repository["software"][sw_count]

    if not selected_sw["developers"]:
        repository["software"][selected_id]["developers"].append(
            {"name": developer_name, "freelance": freelance_status, "website": website})
        print(
            f"\nDeveloper {developer_name}, with freelance status {freelance_status} and website {website} has been successfully created.")

    else:
        count = 0
        while count == 0:
            count = 1

            for dev in selected_sw["developers"]:
                if dev["name"] == developer_name:
                    print(f"\nDeveloper with name {developer_name} already exists.")

                    while True:
                        developer_name = re.sub(r"\s+", " ", input(
                            f"\nWrite a new name for the developer inside the software {selected_sw['name']} ( 0. Cancel ): ").strip())

                        if developer_name == "":
                            print("\nYou can't leave the developer name empty.")
                            continue

                        elif developer_name == "0":
                            return

                        count = 0
                        break

        repository["software"][selected_id]["developers"].append(
            {"name": developer_name, "freelance": freelance_status, "website": website})
        print(
            f"\nDeveloper {developer_name}, with freelance status {freelance_status} and website {website} has been successfully created.")


def delete_developer():
    global repository

    access_software = software_selection("delete", "developer")

    if access_software is None:
        return

    for sw_count in range(len(repository["software"])):
        if access_software == repository["software"][sw_count]["id"]:
            selected_id = sw_count
            selected_sw = repository["software"][sw_count]

    if not selected_sw["developers"]:
        return print(f"\nThere isn't any developer created for the software {selected_sw['name']}.")

    print("")
    for dev in selected_sw["developers"]:
        print(f"Developer name: {dev['name']} || Freelance: {dev['freelance']} || Website: {dev['website']}")

    count = 0
    while count == 0:
        developer_name = re.sub(r"\s+", " ",
                                input("\nWrite the name of the developer to be deleted ( 0. Cancel ): ").strip())

        if developer_name == " ":
            print("\nYou can't leave the developer name empty.")
            continue

        elif developer_name == "0":
            return

        for dev in selected_sw["developers"]:
            if developer_name == dev["name"]:
                count = 1

        if count == 0:
            print("\nPlease enter an existent name for the developer deletion.")

    for count_dev in range(len(selected_sw["developers"])):
        if developer_name == selected_sw["developers"][count_dev]["name"]:
            print(
                f"\nDeveloper with name {selected_sw['developers'][count_dev]['name']} deleted from the software {selected_sw['name']}.")
            repository["software"][selected_id]["developers"].pop(count_dev)
            return


def modify_developer():
    global repository

    # SELECT THE SOFTWARE ID FOR USE
    access_software = software_selection("modify", "developer")

    if access_software is None:
        return

    # ENTER THE SOFTWARE SELECTED
    for sw_count in range(len(repository["software"])):
        if access_software == repository["software"][sw_count]["id"]:
            selected_id = sw_count
            selected_sw = repository["software"][sw_count]

    # CHECK IF THERE IS ANY DEVELOPER
    if not selected_sw["developers"]:
        return print(f"\nThere isn't any developer created to modify in the software {selected_sw['name']}.")

    # PRINT EVERY EXISTENT DEVELOPER IN THE SOFTWARE LIST
    print("")
    for dev in selected_sw["developers"]:
        print(f"Developer name: {dev['name']} || Freelance: {dev['freelance']} || Website: {dev['website']}")

    # CHECK IF THE DEVELOPER NAME EXISTS INSIDE THE SOFTWARE
    count = 0
    while count == 0:
        dev_name = re.sub(r"\s+", " ",
                          input("\nWrite the name of the developer to be modified ( 0. Cancel ): ").strip())

        if dev_name == "":
            print("\nYou can't leave the developer name empty.")
            continue

        if dev_name == "0":
            return

        # END THE FUNCTION TO CANCEL THE FILE CREATION
        for dev in selected_sw["developers"]:
            if dev_name == dev["name"]:
                count = 1
                break

        if count == 0:
            print("\nPlease enter an existent name for the developer modification.")

    # THE USER MUST SAY WHAT PARAMETER HE WANTS TO MODIFY OF THE SELECTED SOFTWARE
    while True:
        try:
            modify_dev = int(input(
                f"\nWhat do you want to modify inside the developer {dev_name} ( 1. Name || 2. Freelance  || 3. Website || 0. Cancel ): "))

            if modify_dev == 1:

                while True:
                    new_dev_name = re.sub(r"\s+", " ", input(
                        f"\nWrite the new name for the developer {dev_name} ( 0. Cancel ): ").strip())

                    if new_dev_name == "":
                        print("\nYou can't leave the developer name empty.")
                        continue

                    if new_dev_name == "0":
                        return

                    nonexistent_name = True

                    for dev in selected_sw["developers"]:
                        if new_dev_name == dev["name"]:
                            nonexistent_name = False

                    if nonexistent_name:
                        for dev_count in range(len(selected_sw["developers"])):
                            if selected_sw["developers"][dev_count]["name"] == dev_name:
                                repository["software"][selected_id]["developers"][dev_count]["name"] = new_dev_name
                                print(f"\nThe developer name {dev_name} has been updated to {new_dev_name}.")
                                return

                    print(f"\nThe filename {new_dev_name} already exists try another name for the file {dev_name}.")

            elif modify_dev == 2:

                while True:
                    new_freelance_status = re.sub(r"\s+", " ", input(
                        f"\nWrite a new freelance status for the developer {dev_name} (0. Cancel): ").strip()).lower()

                    if new_freelance_status == "":
                        print("\nYou can't leave the freelance status empty.")
                        continue

                    elif new_freelance_status == "yes":
                        new_freelance_status = True

                    elif new_freelance_status == "no":
                        new_freelance_status = False

                    elif new_freelance_status == "0":
                        return

                    if isinstance(new_freelance_status, bool):
                        for dev_count in range(len(selected_sw["developers"])):
                            if selected_sw["developers"][dev_count]["name"] == dev_name:
                                repository["software"][selected_id]["developers"][dev_count][
                                    "freelance"] = new_freelance_status
                                print(f"\nDeveloper {dev_name} now has a freelance status of {new_freelance_status}.")
                                return

                    print("\nYour answer must be ( yes | no )")

            elif modify_dev == 3:

                while True:
                    new_website = re.sub(r"\s+", "", input(
                        f"\nWrite a new website for the developer {dev_name} (0. Cancel): ").strip())

                    if new_website == "":
                        print("\nYou can't leave the website empty.")
                        continue

                    elif new_website == "0":
                        return

                    patron_url = re.compile(
                        r'(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
                        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'
                        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

                    patron_url = bool(re.match(patron_url, new_website))

                    if patron_url:
                        for dev_count in range(len(selected_sw["developers"])):
                            if selected_sw["developers"][dev_count]["name"] == dev_name:
                                repository["software"][selected_id]["developers"][dev_count]["website"] = new_website
                                print(f"\nDeveloper {dev_name} now has the website {new_website}.")
                                return

                    else:
                        print("\nThe website don't have structure of website")

            # BREAK THE LOOP TO CANCEL THE SOFTWARE ACTION
            elif modify_file == 0:
                return

            # THE ACTION ISN'T IN THE LIST OF FUNCTIONS FOR SOFTWARE
            else:
                print("\nYour answer isn't on the list of actions.")

        # THE USER RETURN A STRING INSTEAD OF A INTEGER
        except ValueError:
            print("\nYour answer must be a number.")


def software_selection(use, dev_or_file):
    global repository

    # CHECK IF THERE IS ANY SOFTWARE
    if not repository["software"]:
        print(f"\nThere isn't any software created to {use} a {dev_or_file}.")
        return None

    # VARIABLE WITH THE LIST OF SOFTWARE'S AND PRINT EVERY EXISTENT SOFTWARE IN THE REPOSITORY
    print("")
    for software in repository["software"]:
        print(f"Software name: {software['name']} || id: {software['id']}")

    # LOOP WHERE THE USER MUST ANSWER WITH AN EXISTENT ID SOFTWARE
    while True:
        try:
            access_software = int(re.sub(r"\s+", "", input(
                f"\nWrite the id of the software where do you want to {use} a {dev_or_file} ( 0. Cancel ): ").strip()))

        # THE USER RETURN A STRING INSTEAD OF A INTEGER
        except ValueError:
            print("\nPlease enter an integer for the software selection.")
            continue

        # END THE FUNCTION TO CANCEL THE SOFTWARE SELECTION
        if access_software == 0:
            return None

        # CHECK IF THE SOFTWARE ID EXIST IN THE SOFTWARE LIST
        else:
            existent_id = False

            for software in repository["software"]:
                if software["id"] == access_software:
                    existent_id = True

            # BREAK THE LOOP WITH THE NAME OF THE SOFTWARE
            if existent_id:
                return access_software

        # THE USER RETURN AN NON-EXISTENT ID IN THE SOFTWARE LIST
        print("\nPlease enter an existent id for the software selection.")


# REPOSITORY VARIABLE CREATION
repository = ""

# CALL THE FUNCTION TO CREATE A REPOSITORY
initial_repository()

while True:
    # THE USER MUST ANSWER WITH A NUMBER BETWEEN 0-4
    try:
        answer = int(input(
            "\nWhat would you like to do?: ( 1. Software || 2. File || 3. Developer || 4. View all || 0. Exit ): "))
    except ValueError:
        print("\nYour answer must be an integer.")
        continue

    if answer == 1:

        # THE USER MUST SAY WHAT ACTION HE WANTS TO DO WITH A SOFTWARE
        while True:
            try:
                software_function = int(
                    input("\nWhat would you like to do with a software? ( 1. Create || 2. Delete || 0. Exit ): "))

                # CALL A FUNCTION TO CREATE A SOFTWARE
                if software_function == 1:
                    create_software()
                    break

                # CALL A FUNCTION TO DELETE A SOFTWARE
                elif software_function == 2:
                    delete_software()
                    break

                # BREAK THE LOOP TO CANCEL THE SOFTWARE ACTION
                elif software_function == 0:
                    break

                # THE ACTION ISN'T IN THE LIST OF FUNCTIONS FOR SOFTWARE
                else:
                    print("\nYour answer isn't on the list of actions.")

            # THE USER RETURN A STRING INSTEAD OF A INTEGER
            except ValueError:
                print("\nYour answer must be a number.")

    elif answer == 2:

        # THE USER MUST SAY WHAT ACTION HE WANTS TO DO WITH A FILE
        while True:
            try:
                file_function = int(input(
                    "\nWhat would you like to do with a file? ( 1. Create || 2. Delete || 3. Modify || 0. Exit ): "))

                # CALL A FUNCTION TO CREATE A FILE
                if file_function == 1:
                    create_file()
                    break

                # CALL A FUNCTION TO DELETE A FILE
                elif file_function == 2:
                    delete_file()
                    break

                # CALL A FUNCTION TO MODIFY A FILE
                elif file_function == 3:
                    modify_file()
                    break

                # BREAK THE LOOP TO CANCEL THE FILE ACTION
                elif file_function == 0:
                    break

                # THE ACTION ISN'T IN THE LIST OF FUNCTIONS FOR FILE
                else:
                    print("\nYour answer isn't on the list of actions.")

            # THE USER RETURN A STRING INSTEAD OF A INTEGER
            except ValueError:
                print("\nYour answer must be a number.")

    elif answer == 3:

        # THE USER MUST SAY WHAT ACTION HE WANTS TO DO WITH A FILE
        while True:
            try:
                dev_function = int(input(
                    "\nWhat would you like to do with a developer? ( 1. Create || 2. Delete || 3. Modify || 0. Cancel ): "))

                # CALL A FUNCTION TO CREATE A FILE
                if dev_function == 1:
                    create_developer()
                    break

                # CALL A FUNCTION TO DELETE A FILE
                elif dev_function == 2:
                    delete_developer()
                    break

                # CALL A FUNCTION TO MODIFY A FILE
                elif dev_function == 3:
                    modify_developer()
                    break

                # BREAK THE LOOP TO CANCEL THE FILE ACTION
                elif dev_function == 0:
                    break

                # THE ACTION ISN'T IN THE LIST OF FUNCTIONS FOR FILE
                else:
                    print("\nYour answer isn't on the list of actions.")

            # THE USER RETURN A STRING INSTEAD OF A INTEGER
            except ValueError:
                print("\nYour answer must be a number.")

    elif answer == 4:
        # PRINT THE REPOSITORY NAME AND THE CATEGORY
        print("\nRepository:")
        print(f"Name: {repository['name']}  ||  Category: {repository['category']}")

        # PRINT IF THERE ISN'T A SOFTWARE
        if not repository["software"]:
            print("\nThere isn't any software created in the repository.")

        else:
            # PRINT EVERY SOFTWARE
            for sw in repository["software"]:
                print("\nSoftware:")
                print(f"ID: {sw['id']}  ||  Software Name: {sw['name']}")

                # PRINT IF THERE ISN'T A FILE IN THE SOFTWARE
                if not sw["files"]:
                    print(f"\nThere isn't any file created for the software {sw['name']}.")

                # PRINT EVERY FILE
                else:
                    print("\nFiles:")
                    for file_count in range(len(sw["files"])):
                        print(
                            f"Filename: {sw['files'][file_count]['name']}  ||  Size: {sw['files'][file_count]['size']}")

                # PRINT IF THERE ISN'T A DEVELOPER IN THE SOFTWARE
                if not sw["developers"]:
                    print(f"\nThere isn't any developer created for the software {sw['name']}.")

                # PRINT EVERY DEVELOPER
                else:
                    print("\nDevelopers:")
                    for dev_count in range(len(sw["developers"])):
                        print(
                            f"Developer name: {sw['developers'][dev_count]['name']}  ||  Freelance: {sw['developers'][dev_count]['freelance']}  ||  Website: {sw['developers'][dev_count]['website']}")

    # END THE SCRIPT
    elif answer == 0:
        print("\nGoodbye!!! :-)")
        break

    # THE ANSWER IS NOT A NUMBER BETWEEN 0-4
    else:
        print("\nYour answer isn't on the list of actions.")
