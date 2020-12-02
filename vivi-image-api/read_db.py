import dbm
db = dbm.open('img_type','c')

for key in db.keys():
    print(key, ' | ', db[key])