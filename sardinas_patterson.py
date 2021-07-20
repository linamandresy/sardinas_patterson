def quotien_residuel(prefixe, langage):
    prefixe = str(prefixe)
    result = []
    for mot in langage:
        mot = str(mot)
        started = False
        while mot.startswith(prefixe):
            mot = mot[len(prefixe): len(mot)]
            started = True
        if started:
            result.append(mot)
    return result


def enlever_mot_vide(langage):
    result = []
    for mot in langage:
        if mot != "":
            result.append(mot)
    return result


def contien_mot_vide(langage):
    for mot in langage:
        mot = str(mot)
        if mot == "":
            return True
    return False


def quotien(ln0, ln1):
    result = []
    for prefixe in ln0:
        result.extend(quotien_residuel(prefixe, ln1))
    return result

def sd_pt(ln,langage):
    result = []
    result.extend(quotien(ln,langage))
    result.extend(quotien(langage,ln))
    return result

def periodic(u,n):
    for l in u:
        identic = True
        if len(l)==len(n):
            if len(l)==0:
                return True
            for i in range(0,len(u)):
                if l[i]!=n[i]:
                    identic=False
                    break
        else:
            identic=False
        if identic:
            return True
    return False
        

def sardinas_patterson(langage):
    if contien_mot_vide(langage):
        return False
    else:
        u = []
        u.append(langage)
        u1=[]
        u1.extend(quotien(langage,langage))
        u.append(enlever_mot_vide(u1))
        while True:
            lnext=sd_pt(u[len(u)-1],langage)
            if contien_mot_vide(lnext):
                return False
            else:
                if periodic(u,lnext):
                    return True
                elif contien_mot_vide(lnext):
                    return False
                else:
                    u.append(lnext)
