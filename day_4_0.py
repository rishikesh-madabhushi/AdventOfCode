import re

f = open("day_4_0.txt")
#f = open("test.txt")
         
input_lines = f.readlines()

def checkPassport(passport):
    req_fields = {"ecl", "pid", "eyr", "hcl", "byr", "iyr", "cid", "hgt"}

    hcl = re.compile("[a-f,0-9]+")
    ecl = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    pid = re.compile("\d\d\d\d\d\d\d\d\d")
    
    for fldkey in passport.keys():
        if fldkey in req_fields:
            if fldkey == "byr":
                if len(passport[fldkey]) != 4:
                    return False
                try:
                    byr = int(passport[fldkey])
                    if byr < 1920 or byr > 2002:
                        return False
                except ValueError:
                    return False
            elif fldkey == "iyr":
                if len(passport[fldkey]) != 4:
                    return False
                try:
                    iyr = int(passport[fldkey])
                    if iyr < 2010 or iyr > 2020:
                        return False
                except ValueError:
                    return False
            elif fldkey == "eyr":
                if len(passport[fldkey]) != 4:
                    return False
                try:
                    eyr = int(passport[fldkey])
                    if eyr < 2020 or eyr > 2030:
                        return False
                except ValueError:
                    return False
            elif fldkey == "hgt":
                fldval = passport[fldkey]
                attrlen =len(fldval)
                if attrlen < 4:
                    return False
                try:
                    hgt = int(fldval[:attrlen - 2])
                except ValueError:
                    print(fldval[:attrlen - 2])
                    return False
                    
                if (fldval[attrlen - 2:] == "cm"):
                    if hgt < 150 or hgt > 193:
                        return False
                elif fldval[attrlen - 2:] == "in":
                    if hgt < 59 or hgt > 76:
                        return False
                else: return False
            elif fldkey == "hcl":
                fldval = passport[fldkey]
                if len(fldval) != 7:
                    return False
                if fldval[0] != '#':
                    return False
                if not hcl.fullmatch(fldval[1:]):
                    return False
            elif fldkey == "ecl":
                if not passport[fldkey] in ecl:
                    return False
            elif fldkey == "pid":
                if not pid.fullmatch(passport[fldkey]):
                    return False
            elif fldkey != "cid":
                return False
                
            req_fields.discard(fldkey)
    matched_fields = len(req_fields)
    return matched_fields == 0 or (matched_fields == 1 and "cid" in req_fields)

passport = {}
count = 0
for line in input_lines:
    if not line.strip():
        if checkPassport(passport):
            count += 1
        passport = {}
    else:
        attrs = line.strip().split()
        for attr in attrs:
            keyval = attr.split(':')
            passport[keyval[0]] = keyval[1]
print (len(passport))
print(count)


