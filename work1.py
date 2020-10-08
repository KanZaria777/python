from sys import argv

name_script, working_hours, rate_per_hour, award = argv

def salary(*argv):
    print((int(working_hours) * int(rate_per_hour)) + int(award))

salary(*argv)



