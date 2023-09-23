import ua_generator

amount = int(input("How many >> "))
times = int(input("Times >> "))

with open("ua.txt", "a+") as f:
    for x in range(times):
        ua = ua_generator.generate()
        uaS = str(ua) + "\n"  # Convert ua to a string before concatenating
        f.write(uaS)

print("Generated and saved user agents successfully.")
