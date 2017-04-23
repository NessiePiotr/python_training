from model.address_element import Contact
import os.path
import random
import string
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone(prefix, maxlen):
    symbols = string.digits + "(" + ")" + "+" + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + "@"*5 + "."*5 + "_" + "-"
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(first_name="",  middle_name="", last_name="", nick_name="",
                    homephone="", mobilephone="", workphone="", secondaryphone="",
                    e_mail = "", e_mail2 = "", e_mail3 = "", address="")] + [
            Contact(first_name=random_string("Fname", 10), middle_name=random_string("Mname", 10),
                    last_name=random_string("Lname", 10), nick_name=random_string("Nname", 10),
                    homephone=random_phone("HP", 10), mobilephone=random_phone("MP", 10),
                    workphone=random_phone("WP", 10), secondaryphone=random_phone("SP", 10),
                    e_mail = random_email("1", 10), e_mail2 = random_email("2", 10), e_mail3 = random_email("3", 10),
                    address=random_string("Adr", 20))
            for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent = 2)
    out.write(jsonpickle.encode(testdata))