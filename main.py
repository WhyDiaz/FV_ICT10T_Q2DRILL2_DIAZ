from pyscript import document, display

g7_members = {"Lorem Ipsum", "Twinkle Toes", "Will Harris", "Main Attraction", "Modo Olachenko", "Gloc Nine"}
g8_members = {"Kyle Felonious", "Gru Felonious", "Vector Pirkins", "Rabbidous Epidoues V", "Abdis Abbaba", "Shrek Swampingson"}
g9_members = {"Barry Benson", "Orion Jennson", "Jericho Magdalena", "Magdalena Ernesto", "Jett Fillmore"}
g10_members = {"Gerthy Bradar", "Joaqinn Castorian", "Luna Mae", "Eran Diaz"}

all_members = g7_members | g8_members | g9_members | g10_members


def club_verification_checker(e):
    global all_members

    first, last = document.getElementById("fname").value, document.getElementById("lname").value
    full_name = f"{first} {last}"

    already_exists = full_name in all_members

    messages = (
        f"{full_name} has passed registration and is now a member of the Club.",
        f"{full_name} is already a core/new member of the Club."
    )

    all_members.add(full_name)
    total_count = len(all_members)

    rows = (f"<tr><td>7</td><td class='fw-bold'>{full_name}</td><td class='fw-bold'>Member</td></tr>", "")
    document.getElementById("members-list").innerHTML += rows[already_exists]


    display(f"Total Registered Members: {total_count}", target="total_members_count", append=False)
    
    display(messages[already_exists], target="result", append=False)