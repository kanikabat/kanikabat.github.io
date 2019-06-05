greeting = input("Hello, possible pirate! What's the password?")
if greeting in ["Arrr!"]:
	print("Go away, pirate.")
else:
    print("Greetings, hater of pirates!")



authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}

for author, date in authors.items():
    print("%s" % author + " died in " + "%s." % date)



year = int(input("Greetings! What is your year of origin? "))

if year <= 1900:
    print ("Woah, that's the past!")
elif year > 1900 and year < 2020:
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")
    
