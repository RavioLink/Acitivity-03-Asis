import math
from sympy import *
import asis_script_1_stat as statcalc
import asis_script_2_EV as evcalc

while True:
    age = 1
    CalcChoice = input("Stat or EV Calculation?(Type Stat or EV): ")
    if CalcChoice == "Stat":
        age = 5
        Level = int(input("Pokemon Level: "))
        BasePkmn = int(input("Base HP stat: "))
        NaturePkmn = input("Nature of your Pokemon: ")
        IVHP = int(input("IV of HP(0-31): "))
        EVHP = int(input("EV given to HP(0-255): "))
        
        IVattack = int(input("IV of Attack(0-31): "))
        IVDef = int(input("IV of Defense(0-31): "))
        IVSpecAtk = int(input("IV of Special Attack(0-31): "))
        IVSpecDef = int(input("IV of Special Defense(0-31): "))
        IVSpd = int(input("IV of Speed(0-31): "))
        
        EVAtk = int(input("EV given to Attack(0-255): "))
        EVDef = int(input("EV given to Defense(0-255): "))
        EVSpecAtk = int(input("EV given to Special Attack(0-255): "))
        EVSpecDef = int(input("EV given to Special Defense(0-255): "))
        EVSpd = int(input("EV given to Speed(0-255): "))
      
        resultHP = int(statcalc.StatCalc.HPStatCalc(Level,BasePkmn,IVHP,EVHP))
        resultAttackStat = int(statcalc.StatCalc.attackStatCalc(Level,BasePkmn,IVattack,EVAtk,NaturePkmn))
        resultDefStat = int(statcalc.StatCalc.defStatCalc(Level,BasePkmn,IVDef,EVDef,NaturePkmn))
        resultSpecAtkStat = int (statcalc.StatCalc.specAttackCalc(Level,BasePkmn,IVSpecAtk,EVSpecAtk,NaturePkmn))
        resultSpecDefStat = int(statcalc.StatCalc.specDefCalc(Level,BasePkmn,IVSpecDef,EVSpecDef,NaturePkmn))
        resultSpdStat = int(statcalc.StatCalc.spdCalc(Level,BasePkmn,IVSpd,EVSpd,NaturePkmn))
        
        print(round(resultHP))
        print(round(resultAttackStat))
        print(round(resultDefStat))
        print(round(resultSpecAtkStat))
        print(round(resultSpecDefStat))
        print(round(resultSpdStat))
        
    elif CalcChoice == "EV":
        evChoice = input("Single stat or for All Stats?(Single/All) ")
        if evChoice == "Single":
            usrStatChoice = input("For which are you going to do a calculation for?(Attack/Defense/Special Attack/Special Defense/Speed): ")
            if usrStatChoice == "Attack":
                desIncStat = int(input("Desired increase in Attack Stat: "))
                evNature = input("Pokemon nature: ")
                evLevel = int(input("Level of Pokemon: "))
                evBase = int(input("Base stats value: "))
                evIVAtk = int(input("IV for this stat(0-31): "))
                evEVAtk = int(input("EV for this stat(0-255): "))
                
                resultEVAtk = int(evcalc.EVCalc.evCalcAtk(desIncStat,evNature,evLevel,evBase,evIVAtk,evEVAtk))
                print(round(resultEVAtk))
            elif usrStatChoice == "Defense":
                desIncStat = int(input("Desired increase in Def Stat: "))
                evNature = input("Pokemon nature: ")
                evLevel = int(input("Level of Pokemon: "))
                evBase = int(input("Base stats value: "))
                evIVDef = int(input("IV for this stat(0-31): "))
                evEVDef = int(input("EV for this stat(0-255): "))
                
                resultEVDef = int(evcalc.EVCalc.evCalcDef(desIncStat,evNature,evLevel,evBase,evIVDef,evEVDef))
                print(round(resultEVDef))
            elif usrStatChoice == "Special Attack":
                desIncStat = int(input("Desired increase in Def Stat: "))
                evNature = input("Pokemon nature: ")
                evLevel = int(input("Level of Pokemon: "))
                evBase = int(input("Base stats value: "))
                evIVSpecAtk = int(input("IV for this stat(0-31): "))
                evEVSpecAtk = int(input("EV for this stat(0-255): "))
                
                resultEvSpecAtk = int(evcalc.EVCalc.evCalcSpecAtk(desIncStat,evNature,evLevel,evBase,evIVSpecAtk,evEVSpecAtk))
                print(round(resultEvSpecAtk))
                
            elif usrStatChoice == "Special Defense":
                desIncStat = int(input("Desired increase in Def Stat: "))
                evNature = input("Pokemon nature: ")
                evLevel = int(input("Level of Pokemon: "))
                evBase = int(input("Base stats value: "))
                evIVSpecDef = int(input("IV for this stat(0-31): "))
                evEVSpecDef = int(input("EV for this stat(0-255): "))
                
                resultEVSpecDef = int(evcalc.EVCalc.evCalcSpecDef(desIncStat,evNature,evLevel,evBase,evIVSpecDef,evEVSpecDef))
                print(round(resultEVSpecDef))
            elif usrStatChoice == "Speed":
                desIncStat = int(input("Desired increase in Def Stat: "))
                evNature = input("Pokemon nature: ")
                evLevel = int(input("Level of Pokemon: "))
                evBase = int(input("Base stats value: "))
                evIVSpd = int(input("IV for this stat(0-31): "))
                evEVSpd = int(input("EV for this stat(0-255): "))
                
                resultEVSpd = int(evcalc.EVCalc.evCalcSpd(desIncStat,evNature,evLevel,evBase,evIVSpd,evEVSpd))
                print(round(resultEVSpd))
            else:
                print("Selection not recognized will start from the beginning: ")
                continue
        elif evChoice == "All":
            pass
        age = 0
    else:
        print("Cannot recognize input! Will ask you again.")
        continue
    
    
    checkFunction = input("Do another calculation(Y/N)? ")
    if checkFunction == 'N' or checkFunction == 'n':
        break
    if checkFunction == 'Y' or checkFunction == 'y':
        continue