class EVCalc():
    def evCalcAtk(desIncStat,evNature,evLevel,evBase,evIVAtk,evEVAtk):
        intD = ((2*evBase+evIVAtk+(evEVAtk/4))*(evLevel/100))
        evnatureFlag = 1
        if evNature == "Lonely" or evNature == "Brave" or evNature == "Adamant" or evNature == "Naughty":
            evnatureFlag = 1.1
        elif evNature == "Bold" or evNature == "Calm":
            evnatureFlag = 0.9
        else:
            evnatureFlag = 1
        return (((((desIncStat/evnatureFlag)-(intD)*400)/evLevel)/4)*4)
    def evCalcDef(desIncStat,evNature,evLevel,evBase,evIVDef,evEVDef):
        intD = ((2*evBase+evIVDef+(evEVDef/4))*(evLevel/100))
        evnatureFlag = 1
        if evNature == "Bold" or evNature == "Relaxed" or evNature == "Impish" or evNature == "Lax":
            evnatureFlag = 1.1
        elif evNature == "Lonely" or evNature == "Hasty" or evNature == "Mild" or evNature == "Gentle":
            evnatureFlag = 0.9
        else:
            evnatureFlag = 1
        return (((((desIncStat/evnatureFlag)-(intD)*400)/evLevel)/4)*4)
    def evCalcSpecAtk(desIncStat,evNature,evLevel,evBase,evIVSpecAtk,evEVSpecAtk):
        intD = ((2*evBase+evIVSpecAtk+(evEVSpecAtk/4))*(evLevel/100))
        evnatureFlag = 1
        if evNature == "Modest" or evNature == "Mild" or evNature == "Quiet" or evNature == "Rash":
            evnatureFlag = 1.1
        elif evNature == "Adamant" or evNature == "Impish" or evNature == "Jolly" or evNature == "Careful":
            evnatureFlag = 0.9
        else:
            evnatureFlag = 1
        return (((((desIncStat/evnatureFlag)-(intD)*400)/evLevel)/4)*4)
    def evCalcSpecDef(desIncStat,evNature,evLevel,evBase,evIVSpecDef,evEVSpecDef):
        intD = ((2*evBase+evIVSpecDef+(evEVSpecDef/4))*(evLevel/100))
        evnatureFlag = 1
        if evNature == "Calm" or evNature == "Gentle" or evNature == "Sassy" or evNature == "Careful":
            evnatureFlag = 1.1
        elif evNature == "Naughty" or evNature == "Lax" or evNature == "Naive" or evNature == "Rash":
            evnatureFlag = 0.9
        else:
            evnatureFlag = 1
        return (((((desIncStat/evnatureFlag)-(intD)*400)/evLevel)/4)*4)
    def evCalcSpd(desIncStat,evNature,evLevel,evBase,evIVSpd,evEVSpd):
        intD = ((2*evBase+evIVSpd+(evEVSpd/4))*(evLevel/100))
        evnatureFlag = 1
        if evNature == "Timid" or evNature == "Hasty" or evNature == "Jolly" or evNature == "Naive":
            evnatureFlag = 1.1
        elif evNature == "Brave" or evNature == "Relaxed" or evNature == "Quiet" or evNature == "Sassy":
            evnatureFlag = 0.9
        else:
            evnatureFlag = 1
        return (((((desIncStat/evnatureFlag)-(intD)*400)/evLevel)/4)*4)
    