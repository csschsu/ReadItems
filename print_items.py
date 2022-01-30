filler = "                                                                                  "
def am_codes(code):
    if code == "AM1": return (code + ":Dörr,Balkong" + filler)[0:25]
    elif code == "AM2": return (code + ":Dörr,Fransk Balkong" + filler)[0:25]
    elif code == "AM3": return (code + ":Dörr,Entre" + filler)[0:25]
    elif code == "AM4": return (code + ":Dörr,Inner" + filler)[0:25]
    elif code == "AM5": return (code + ":Dörr,Garderob" + filler)[0:25]
    elif code == "AM6": return (code + ":Toalett,kakel" + filler)[0:25]
    elif code == "AM7": return (code + ":Toalett,lutning golv" + filler)[0:25]
    elif code == "AM8": return (code + ":Toalett,handfat, stol" + filler)[0:25]
    elif code == "AM9": return (code + ":Toalett,blandare" + filler)[0:25]
    elif code == "AM10": return (code + ":Toalett,tork" + filler)[0:25]
    elif code == "AM11": return (code + ":Toalett,Lukt" + filler)[0:25]
    elif code == "AM12": return (code + ":Toalett,Mögel" + filler)[0:25]
    elif code == "AM13": return (code + ":Toalett,duschvägg" + filler)[0:25]
    elif code == "AM14": return (code + ":Toalett,skåp" + filler)[0:25]
    elif code == "AM15": return (code + ":Kök,diskho" + filler)[0:25]
    elif code == "AM16": return (code + ":Kök,spisfläkt" + filler)[0:25]
    elif code == "AM17": return (code + ":Kök,skåp,bänkar" + filler)[0:25]
    elif code == "AM18": return (code + ":Källare" + filler)[0:25]
    elif code == "AM19": return (code + ":Sedumtak" + filler)[0:25]
    elif code == "AM20": return (code + ":Fasad" + filler)[0:25]
    elif code == "AM21": return (code + ":Balkong,inglasning" + filler)[0:25]
    elif code == "AM24": return (code + ":Fönster,kondens" + filler)[0:25]
    elif code == "AM25": return (code + ":Fönster,drag, list" + filler)[0:25]
    elif code == "AM26": return (code + ":Fönster,vatten" + filler)[0:25]
    elif code == "AM27": return (code + ":Fönster, repor" + filler)[0:25]
    elif code == "AM28": return (code + ":Fönsterlås" + filler)[0:25]
    elif code == "AM29": return (code + ":El" + filler)[0:25]
    elif code == "AM31": return (code + ":Hiss" + filler)[0:25]
    elif code == "AM32": return (code + ":Ventilation lukt" + filler)[0:25]
    elif code == "AM33": return (code + ":Ventilation kyla" + filler)[0:25]
    elif code == "AM34": return (code + ":Temperatur" + filler)[0:25]
    elif code == "AM37": return (code + ":Ljud, ute" + filler)[0:25]
    elif code == "AM38": return (code + ":Skador golv lister" + filler)[0:25]
    elif code == "AM39": return (code + ":Knarrande golv" + filler)[0:25]
    elif code == "AM40": return (code + ":Sprickor" + filler)[0:25]
    elif code == "AM41": return (code + ":Målning, yta" + filler)[0:25]
    elif code == "AM42": return (code + ":Gård" + filler)[0:25]
    elif code == "AM43": return (code + ":Energiförbrukning" + filler)[0:25]
    elif code == "AM44": return (code + ":Ej entreprenör" + filler)[0:25]
    else:
        return (code + ":unknown code" + filler)[0:25]

#
# Main
#
resultfile= open ( "out.txt", "w")

fd = open("Felanmälningar_5års_besiktning - Felanmälningar.tsv", "r")
line = fd.readline()
while line:

    items = line.split("\t")
    lgh = items[2]
    resultfile.write(filler[0:74] + items[2])
    resultfile.write("\nLägenhet " + items[2] + "\n\n")

    resultfile.write((items[1]+ "    ")[0:8] + am_codes(items[7]) + items[12] + "\n\n")
    line = fd.readline()
    items_nextline = line.split("\t")
    while line and items[2] == items_nextline[2]:
        resultfile.write((items_nextline[1] + "    ")[0:8] + am_codes(items_nextline[7]) + items_nextline[12] + "\n\n")
        line = fd.readline()
        items_nextline = line.split("\t")
    resultfile.write( "\f")

resultfile.close()