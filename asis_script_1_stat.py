class StatCalc():
    def HPStatCalc(Level,BasePkmn,IVHP,EVHP):
        return (((((2*BasePkmn+IVHP+(EVHP/4))*(Level))/100)+Level)+10)
    def attackStatCalc(Level,BasePkmn,IVattack,EVAtk,NaturePkmn):
        natureFlag = 1
        if NaturePkmn == "Lonely" or NaturePkmn == "Brave" or NaturePkmn == "Adamant" or NaturePkmn == "Naughty":
            natureFlag = 1.1
        elif NaturePkmn == "Bold" or NaturePkmn == "Calm":
            natureFlag = 0.9
        else:
            natureFlag = 1
        return ((((2*BasePkmn+IVattack+(EVAtk/4))*(Level)/100)+5)*natureFlag)
    def defStatCalc(Level,BasePkmn,IVDef,EVDef,NaturePkmn):
        natureFlag = 1
        if NaturePkmn == "Bold" or NaturePkmn == "Relaxed" or NaturePkmn == "Impish" or NaturePkmn == "Lax":
            natureFlag = 1.1
        elif NaturePkmn == "Lonely" or NaturePkmn == "Hasty" or NaturePkmn == "Mild" or NaturePkmn == "Gentle":
            natureFlag = 0.9
        else:
            natureFlag = 1
        return ((((2*BasePkmn+IVDef+(EVDef/4))*(Level)/100)+5)*natureFlag)
    def specAttackCalc(Level,BasePkmn,IVSpecAtk,EVSpecAtk,NaturePkmn):
        natureFlag = 1
        if NaturePkmn == "Modest" or NaturePkmn == "Mild" or NaturePkmn == "Quiet" or NaturePkmn == "Rash":
            natureFlag = 1.1
        elif NaturePkmn == "Adamant" or NaturePkmn == "Impish" or NaturePkmn == "Jolly" or NaturePkmn == "Careful":
            natureFlag = 0.9
        else:
            natureFlag = 1
        return ((((2*BasePkmn+IVSpecAtk+(EVSpecAtk/4))*(Level)/100)+5)*natureFlag)
    def specDefCalc(Level,BasePkmn,IVSpecDef,EVSpecDef,NaturePkmn):
        natureFlag = 1
        if NaturePkmn == "Calm" or NaturePkmn == "Gentle" or NaturePkmn == "Sassy" or NaturePkmn == "Careful":
            natureFlag = 1.1
        elif NaturePkmn == "Naughty" or NaturePkmn == "Lax" or NaturePkmn == "Naive" or NaturePkmn == "Rash":
            natureFlag = 0.9
        else:
            natureFlag = 1
        return ((((2*BasePkmn+IVSpecDef+(EVSpecDef/4))*(Level)/100)+5)*natureFlag)
    def spdCalc(Level,BasePkmn,IVSpd,EVSpd,NaturePkmn):
        natureFlag = 1
        if NaturePkmn == "Timid" or NaturePkmn == "Hasty" or NaturePkmn == "Jolly" or NaturePkmn == "Naive":
            natureFlag = 1.1
        elif NaturePkmn == "Brave" or NaturePkmn == "Relaxed" or NaturePkmn == "Quiet" or NaturePkmn == "Sassy":
            natureFlag = 0.9
        else:
            natureFlag = 1
        return ((((2*BasePkmn+IVSpd+(EVSpd/4))*(Level)/100)+5)*natureFlag)
        