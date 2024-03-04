import random
QuestionDebut = ["Comment allez-vous ?","Pourquoi venez-vous me voir ?","Comment s'est passée votre journée ?"]
QuestionMotCle =["Comment va votre {0}", "La relation avec votre {0} vous pose t-elle problème ?","Pourquoi pensez-vous en ce moment à votre {0} ?"]
QuestionInterro = ["Pourquoi me posez-vous cette question ?","Oseriez-vous poser cette question à un humain ?","Je ne peux malheureusement pas répondre à cette question."]
PhraseVague = ["J\'entends bien.","Je sens une pointe de regret",'Est-ce une bonne nouvelle ?',"Oui, c\'est ça le problème","Pensez-vous ce que vous dites ?","Hum... Je vois"]
Mots = ['père','mère','copain','copine','maman','papa']
choix = random.randint(0,2)
rep = input(QuestionDebut[choix])
while True:
    choix = random.randint(0,2)
    for i in Mots:
        if (rep.find(i)!=-1) :
            rep=input(QuestionMotCle[choix].format(i))
            break
    if (rep.find("?")!=-1):
        rep = input(QuestionInterro[choix])
    else :
        rep = input(PhraseVague[choix])