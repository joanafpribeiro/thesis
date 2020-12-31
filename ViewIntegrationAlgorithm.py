import os
import numpy as np
from collections import OrderedDict

############################################################################
earlyQuestions = ["Who performed X?", "Where did X took place?", "When does X occur?", "In what does X consist of?"]

detailQuestions = [
"What activity triggered X to be executed?", 
"What activity does X trigger?",
"Which computing system/tool is used in the execution of X?",
"Does X require the use of information that is produced out of the scope of this process (or other executions of this process)?",
"Does X require the storing of information in a more permanent way?",
"Does X produce any documents, either in physical or digital form, that can only be assessed during the execution of the process?", 
"Does X require any documents, either in physical or digital form, that can only be assessed during the execution of the process?",
"Does X depicts any kind of visual representation of data or notes?",
"Does something else occur during the course of the process (e.g. a message, a timeout)?",
"What is the level of granularity of X?"
]

responsibilityQuestions = [
    "Are you responsible or part of team responsible for the execution of X?",
    "Do you agree with the name given to X?",
    "Do you work with anyone outside your team for the execution of X?",
    "Does X always unwind the same way?",
    "Is X a mandatory activity to guarantee a good functioning of the process?",
    "Could X be set aside while the process remained with good functioning?",
    "Does X usually happen always at the same time?",
    "Does it usually take the same amount of time to execute X?",
    "Does X usually happen always at the same place?",
    "Does X usually unfold in a standard manner?",
    "Does X happen always with the same purpose?"
]

novelQuestions = [
    "Do both X and Y have similar/equivalent names?",
    "Are both X and Y triggered by the same event?",
    "Do both X and Y trigger the same event?",
    "Do both X and Y occur simultaneously?",
    "Are both X and Y executed by the same person?",
    "Do both X and Y occur at the same location?",
    "Do both X and Y have a similar precedent activity?", 
    "Do both X and Y have a similar consequent activity?",
    "Do both X and Y have the same purpose?",
    "Do both X and Y endorse the same regulations?",
    "Do both X and Y need the same set of requirements to execute?",
    "Do both X and Y use the same IT support system to execute?",
    "Is activity X a possible composition of activities Y?"
]

earlyAnswersDict = {
    "1Assess car damage": ["Service Manager", "Garage", " ", " "],
    "Replace parts": ["Other:", "Warehouse", " ", " "],
    "Planish parts": [" ", "Garage", " ", " "],
    "1Prepare car for spraying": [" ", "Garage", " ", " "],
    "Spray and inspect paiting": ["Painter", "Greenhouse", " ", " "],
    "2Assess car damage": ["Service Manager", "Garage", " ", " "],
    "Fix Parts": ["Panel Beater", " ", " ", " "],
    "2Prepare car for spraying": ["Painter", "Greenhouse", " ", " "],
    "Spray car": ["Painter", "Greenhouse", " ", " "],
    "Inspect paiting quality": ["Service Manager", " ", " ", " "]
    }

resemblanceDict = {
    "1Assess car damage": [" ", " ", " ", " "],
    "Replace parts": ["Little SM", " ", " ", " "],
    "Planish parts": [" ", " ", " ", " "],
    "1Prepare car for spraying": [" ", " ", " ", " "],
    "Spray and inspect paiting": [" ", " ", " ", " "],
    "2Assess car damage": [" ", " ", " ", " "],
    "Fix Parts": [" ", " ", " ", " "],
    "2Prepare car for spraying": [" ", " ", " ", " "],
    "Spray car": [" ", " ", " ", " "],
    "Inspect paiting quality": [" ", " ", " ", " "]
    }

detailAnswersDict = {
    "1Assess car damage": ["Starting event 'Damaged car arrives'", "Gateway 'Planishing needed'", "No", "Yes", " ", " ", " ", " ", " ", "medium"],
    "Replace parts": ["Gateway 'New parts needed'", "Gateway ' '", "No", "Yes", " ", " ", " ", " ", " ", "medium"],
    "Planish parts": ["Gateway 'Planishing needed'", "Gateway ' '", "No", "Yes", " ", " ", " ", " ", " ", "medium"],
    "1Prepare car for spraying": ["Gateway ' '", "Activity 'Spray and inspect paiting'", "No", "Yes", " ", " ", " ", " ", " ", "medium"],
    "Spray and inspect paiting": ["Activity 'Prepare car for spraying'", "End event 'Car ready to be delivered'", "No", "Yes", " ", " ", " ", " ", " ", "medium"],
    "2Assess car damage": ["Starting event 'Damaged car arrives'", "Activity 'Fix parts'", "No", "Yes", " ", " ", " ", " ", " ", "medium"],
    "Fix Parts": ["Activity '2Assess car damage", "Activity 'Prepare car for spraying'", "No", "Yes", " ", " ", " ", " ", " ", "medium"],
    "2Prepare car for spraying": ["Activity 'Fix parts'", "Gateway ' '", "No", "Yes", " ", " ", " ", " ", " ", "medium"],
    "Spray car": ["Gateway ' '", "Activity 'Inspect paiting quality'", "No", "Yes", " ", " ", " ", " ", " ", "low"],
    "Inspect paiting quality": ["Activity 'Spray Car'", "Gateway ' '", "No", "Yes", " ", " ", " ", " ", " ", "medium"]
    }

responsibilityAnswersDict = {
    "1Assess car damage": "y,y,y,y,y,y,y,y,y,y,y",
    "Replace parts": "y,y,y,y,y,y,y,y,y,y,y",
    "Planish parts": "y,y,y,y,y,y,y,y,y,y,y",
    "1Prepare car for spraying": "y,y,y,y,y,y,y,y,y,y,y",
    "Spray and inspect paiting": "y,y,y,y,y,y,y,y,y,y,y",
    "2Assess car damage": "y,y,y,y,y,y,y,y,y,y,y",
    "Fix Parts": "y,y,y,y,y,y,y,y,y,y,y",
    "2Prepare car for spraying": "y,y,y,y,y,y,y,y,y,y,y",
    "Spray car": "y,y,y,y,y,y,y,y,y,y,y",
    "Inspect paiting quality": "y,y,y,y,y,y,y,y,y,y,y"
    }
############################################################################



############################################################################
def getNovelAnswersResemblance(pair):
    answers = [pair, "y,y,y,y,y,y,y,y,y,y,y,y"]
    return answers
############################################################################



############################################################################
def getNovelAnswersComposition(key, values):
    sets = [key, values]
    answers = [sets, "y"]
    return answers
############################################################################



############################################################################
def getViewName (activity):
    if (activity=="1Assess car damage"):
        view = "Facilities"
    if (activity=="Replace parts"):
        view = "Facilities"
    if (activity=="Planish parts"): 
        view = "Facilities"
    if (activity=="1Prepare car for spraying"):
        view = "Facilities"
    if (activity=="Spray and inspect paiting"):
        view = "Facilities"
    if (activity=="2Assess car damage"):
        view = "HR"
    if (activity=="Fix Parts"):
        view = "HR"
    if (activity=="2Prepare car for spraying"):
        view = "HR"
    if (activity=="Spray car"):
        view = "HR"
    if (activity=="Inspect paiting quality"):
        view = "HR"

    return view
############################################################################



############################################################################
def getActivitiesfromBPMN (view):

    activities = []

    if(view=="Facilities"):
        activities = ["1Assess car damage", "Replace parts", "Planish parts", "1Prepare car for spraying", "Spray and inspect paiting"]

    if(view=="HR"):
        activities = ["2Assess car damage", "Fix Parts", "2Prepare car for spraying", "Spray car", "Inspect paiting quality"]

    return activities
############################################################################



############################################################################
def classifyEarly(view):
    if (view=="Facilities"):
        earlyElements = [["Warehouse", "where"], ["Garage", "where"], ["Greenhouse", "where"], ["Headquarters", "who"], ["Facilities Department", "who"]] 
    if (view=="HR"):
        earlyElements = [["Panel Beater", "who"], ["Service Manager", "who"], ["Painter", "who"], ["HR Department", "who"], ["ACME", "where"]]
    return earlyElements

def classifyDetail(view):
    if (view=="Facilities"):
        detailElements = [["Starting event 'Damaged car arrives'", "trigger"], ["Gateway 'Planishing needed'", "trigger"], ["End event 'Car ready to be delivered'", "trigger"]] 
    if (view=="HR"):
        detailElements = [["Starting event 'Damaged car arrives'", "trigger"], ["End event 'Car ready to be delivered'", "trigger"]] 
    
    return detailElements

def classifyBPMNElements (view):
    
    elements = [[[]],[[]]] 

    earlyElements = classifyEarly(view)

    detailElements = classifyDetail(view) 
    
    elements[0] = earlyElements
    
    elements[1] = detailElements
    
    return elements
############################################################################



############################################################################
def generateEarlyQuestions (activity, earlyelements):

    global earlyQuestions

    whoOptions = []
    whereOptions= []
    whenOptions = []
    whatOptions = []
   
    for element in earlyelements:
        
        if (element[1] == "who"):
            whoOptions.append(element[0])
        if (element[1] == "where"):
            whereOptions.append(element[0])
        if (element[1] == "when"):
            whenOptions.append(element[0])
        if (element[1] == "what"):
            whatOptions.append(element[0])

    earlyquestions = []

    for question in earlyQuestions:
        earlyquestions.append((question.replace("X", activity)))

    dictEarly = {
        earlyquestions[0]:whoOptions,
        earlyquestions[1]:whereOptions,
        earlyquestions[2]:whenOptions,
        earlyquestions[3]:whatOptions
    }
 
    return dictEarly
############################################################################



############################################################################
def generateResponsibilityQuestions (activity):

    global responsibilityQuestions

    responsibilityOptions = ["yes", "no"]

    responsibilityquestions = []

    for question in responsibilityQuestions:
        responsibilityquestions.append((question.replace("X", activity)))

    dictResponsibility = {
        responsibilityquestions[0]:responsibilityOptions,
        responsibilityquestions[1]:responsibilityOptions,
        responsibilityquestions[2]:responsibilityOptions,
        responsibilityquestions[3]:responsibilityOptions,
        responsibilityquestions[4]:responsibilityOptions,
        responsibilityquestions[5]:responsibilityOptions,
        responsibilityquestions[6]:responsibilityOptions,
        responsibilityquestions[7]:responsibilityOptions,
        responsibilityquestions[8]:responsibilityOptions,
        responsibilityquestions[9]:responsibilityOptions,
        responsibilityquestions[10]:responsibilityOptions
    }
    
    return dictResponsibility
############################################################################



############################################################################
def generateDetailQuestions (activity, detailelements):

    global detailQuestions

    triggerOptions = []
    systemOptions= ["yes", "no"]
    manualOptions = ["yes", "no"]
    datastoreOptions = []
    artefactOptions = []
    dataobjectOptions = []
    granularityOptions = ["low", "medium", "high"]

    for element in detailelements:
        if (element[1] == "trigger"):
            triggerOptions.append(element[0])
        if (element[1] == "system"):
            systemOptions.append(element[0])
        if (element[1] == "manual"):
            manualOptions.append(element[0])
        if (element[1] == "datastore"):
            datastoreOptions.append(element[0])
        if (element[1] == "artefact"):
            artefactOptions.append(element[0])
        if (element[1] == "dataobject"):
            dataobjectOptions.append(element[0])
        if (element[1] == "granularity"):
            granularityOptions.append(element[0])

    detailquestions = []

    for question in detailQuestions:
        detailquestions.append((question.replace("X", activity)))

    detailquestions = []

    for question in detailQuestions:
        detailquestions.append((question.replace("X", activity)))

    dictDetail = {
        detailquestions[0]:triggerOptions,
        detailquestions[1]:triggerOptions,
        detailquestions[2]:systemOptions,
        detailquestions[3]:manualOptions,
        detailquestions[4]:datastoreOptions,
        detailquestions[5]:artefactOptions,
        detailquestions[6]:artefactOptions,
        detailquestions[7]:dataobjectOptions,
        detailquestions[8]:dataobjectOptions,
        detailquestions[9]:granularityOptions
    }

    return dictDetail    

############################################################################



############################################################################
def generatePrimaryQuestions(view):

    primaryQuestions = [[], [], []]

    activities = getActivitiesfromBPMN(view) 
    elements = classifyBPMNElements (view) 

    earlyquestions = []
    detailquestions = []
    responsibilityquestions = []

    for activity in activities:

        earlyquestions.append(generateEarlyQuestions(activity, elements[0]))

        detailquestions.append(generateDetailQuestions(activity, elements[1]))

        responsibilityquestions.append(generateResponsibilityQuestions(activity))

    primaryQuestions[0] = earlyquestions
    primaryQuestions[1] = detailquestions
    primaryQuestions[2] = responsibilityquestions

    return primaryQuestions

############################################################################



############################################################################
def askEarlyQuestions(equestions, view):
    global earlyAnswersDict

    earlyAnswers = []

    activities = getActivitiesfromBPMN(view) 

    if (view=="Facilities"):
        for activity in activities:
            earlyAnswers.append({activity:[earlyAnswersDict.get(activity)]})

    if (view=="HR"):
        for activity in activities:
            earlyAnswers.append({activity:[earlyAnswersDict.get(activity)]})

    return earlyAnswers
############################################################################



############################################################################
def askDetailQuestions(dquestions, view):
    global detailAnswersDict

    detailAnswers = []

    activities = getActivitiesfromBPMN(view) 

    if (view=="Facilities"):
        for activity in activities:
            detailAnswers.append({activity:[detailAnswersDict.get(activity)]})

    if (view=="HR"):
        for activity in activities:
            detailAnswers.append({activity:[detailAnswersDict.get(activity)]})

    return detailAnswers
############################################################################



############################################################################
def askResponsibilityQuestions(rquestions, view):

    global responsibilityAnswersDict

    responsibilityAnswers = []

    activities = getActivitiesfromBPMN(view) 

    if (view=="Facilities"):
        for activity in activities:
            responsibilityAnswers.append({activity:[responsibilityAnswersDict.get(activity)]})

    if (view=="HR"):
        for activity in activities:
            responsibilityAnswers.append({activity:[responsibilityAnswersDict.get(activity)]})

    return responsibilityAnswers
############################################################################



############################################################################
def askNovelQuestionsResemblance(nquestions):

    novelAnswers = []

    for pair in nquestions[0]:
        novelAnswers.append(getNovelAnswersResemblance(pair))
  
    return novelAnswers
############################################################################

############################################################################
def askNovelQuestionsComposition(compostionsets):

    novelAnswers = []

    for key in compostionsets[0]:
        novelAnswers.append(getNovelAnswersComposition(key, compostionsets[0][key]))
  
    return novelAnswers
############################################################################

############################################################################
def askPrimaryQuestions(questions, view): #fazer as primary questions para 1 vista
    
    earlyAnswers = []
    detailAnswers = []
    responsibilityAnswers = []

    primaryAnswers = [[[]], [[]], [[]]]

    earlyAnswers = askEarlyQuestions(questions[0], view) 
    detailAnswers = askDetailQuestions(questions[1], view) 
    responsibilityAnswers = askResponsibilityQuestions(questions[2], view) 

    primaryAnswers[0] = earlyAnswers #resposta early de todas as atividades duma dada vista
    primaryAnswers[1] = detailAnswers #resposta detail de todas as atividades duma dada vista
    primaryAnswers[2] = responsibilityAnswers 

    return primaryAnswers

############################################################################



############################################################################
def append_value(dict_obj, key, value):
    if key in dict_obj:
        if not isinstance(dict_obj[key], list):
            dict_obj[key] = [dict_obj[key]]
        dict_obj[key].append(value)
    else:
        dict_obj[key] = value
############################################################################



############################################################################
def getGranularity(activity):
    return detailAnswersDict[activity][9]
############################################################################



############################################################################
def comparePrimaryAnswersComposition(prevanswers, answers, view, prevview):

    similarAnswers = OrderedDict()
    answersToIgnore = []
    granularity = {}
    compositionDict = {}

    earlyAnswersFirstView = prevanswers[0]
    earlyAnswersSecondView = answers[0]

    allAnswers = earlyAnswersFirstView + earlyAnswersSecondView

    for answer in allAnswers:   
        if str(list(answer.values())[0]) in list(similarAnswers.keys()):
            similarAnswers[str(list(answer.values())[0])].append(list(answer.keys())[0])
        else:
            similarAnswers[str(list(answer.values())[0])] = list(answer.keys())

    for answersKey in similarAnswers:
        activities = similarAnswers[answersKey]
        nameOfViews = [getViewName(activity) for activity in activities]
        NameOfViewsWithoutDuplicates = list(set(nameOfViews))

        if(len(NameOfViewsWithoutDuplicates) == 1):
            answersToIgnore.append(answersKey)

    for answersKey in answersToIgnore:
        del similarAnswers[answersKey]

    for activitySet in list(similarAnswers.values()):
        for activity in activitySet:
            granularity.update({activity:getGranularity(activity)})
   
    highGranularity = []
    lowGranularity = []

    for activity in granularity:
        if (granularity[activity] == "high" or granularity[activity] == "medium"):
            highGranularity.append(activity)
        else:
            lowGranularity.append(activity)
    
    highGranularitySetsWithSameAnswers = []
    for answer in similarAnswers:
        activitiesWithSameAnswersAndGranularity = []
        for activity in similarAnswers[answer]:
            if activity in highGranularity:
                activitiesWithSameAnswersAndGranularity.append(activity)
        highGranularitySetsWithSameAnswers.append(activitiesWithSameAnswersAndGranularity)

    lowGranularitySetsWithSameAnswers = []
    for answer in similarAnswers:
        activitiesWithSameAnswersAndGranularity = []
        for activity in similarAnswers[answer]:
            if activity in lowGranularity:
                activitiesWithSameAnswersAndGranularity.append(activity)
        lowGranularitySetsWithSameAnswers.append(activitiesWithSameAnswersAndGranularity)
    
    for index, highActivity in enumerate(highGranularitySetsWithSameAnswers):
        compositionDict[repr(highActivity)] = lowGranularitySetsWithSameAnswers[index]

    actToIgnore = []

    for key in compositionDict:
        if compositionDict[key]==[]:
            actToIgnore.append(key)

    for key in actToIgnore:
        del compositionDict[key]
    
    return compositionDict
############################################################################  



############################################################################
def comparePrimaryAnswersResemblance(prevanswers, answers): #tem de sugerir pares de semelhança e conjuntos de composição

    similarPairs = [[]]

    earlyAnswersFirstView = prevanswers[0]
    detailAnswersFirstView = prevanswers[1]
    responsibilityAnswersFirstView = prevanswers[2]

    earlyAnswersSecondView = answers[0]
    detailAnswersSecondView = answers[1]
    responsibilityAnswersSecondView = answers[2]

    for earlyFirst in earlyAnswersFirstView:
        for earlySecond in earlyAnswersSecondView:

            earlykey1 = list(earlyFirst.keys())[0]
            earlykey2 = list(earlySecond.keys())[0]
            earlyvalues1 = earlyFirst[earlykey1]
            earlyvalues2 = earlySecond[earlykey2]

            if(earlyvalues1 == earlyvalues2):
                similarPairs.append([earlykey1, earlykey2])
    
  
    for detailFirst in detailAnswersFirstView:
        for detailSecond in detailAnswersSecondView:
            detailkey1 = list(detailFirst.keys())[0]
            detailkey2 = list(detailSecond.keys())[0]
            detailvalues1 = detailFirst[detailkey1]
            detailvalues2 = detailSecond[detailkey2]

            if(detailkey1 in similarPairs and detailkey2 in similarPairs):
                if(detailvalues1 == detailvalues2):
                    similarPairs.append([detailkey1, detailkey2])

    for responsibilityFirst in responsibilityAnswersFirstView:
        for responsibilitySecond in responsibilityAnswersSecondView:
            responsibilitykey1 = list(responsibilityFirst.keys())[0]
            responsibilitykey2 = list(responsibilitySecond.keys())[0]
            responsibilityvalues1 = responsibilityFirst[responsibilitykey1]
            responsibilityvalues2 = responsibilitySecond[responsibilitykey2]

            if(responsibilitykey1 in similarPairs and responsibilitykey2 in similarPairs):
                if(responsibilityvalues1 == responsibilityvalues2):
                    similarPairs.append([responsibilitykey1, responsibilitykey2])

    return similarPairs
############################################################################



############################################################################
def generateNovelQuestionsComposition(compositionsets):

    global novelQuestions

    granularityquestion = novelQuestions[12]

    novelquestions = []

    novelOptions = ["yes", "no"]

    dictNovel = {}   

    for key in compositionsets:
        novelquestions.append((granularityquestion.replace("X", key)).replace("Y", str(compositionsets[key])))
    
    for novel in novelquestions:
        dictNovel.update({novel: novelOptions})

    composition = [compositionsets, dictNovel]

    return composition
############################################################################



############################################################################
def generateNovelQuestionsResemblance(similarpairs): 

    global novelQuestions

    novelPairs = []

    novelOptions = ["yes", "no"]

    novelquestions = []

    dictNovel = {}
    
    for pair in similarpairs:
        if (pair != []):
            novelPairs.append(pair)    

    for question in novelQuestions:
        for pair in novelPairs:
            novelquestions.append((question.replace("X", pair[0])).replace("Y", pair[1]))

    for novel in novelquestions:
        dictNovel.update({novel: novelOptions})

    novel = [novelPairs, dictNovel]

    return novel
    
############################################################################



############################################################################
def produceConsolidatedModel (novelanswerssimilar, novelanswerscomposition):

    finalSimilarPairs = []
    finalCompositionSets = []

    outputSimilarPairs = {}
    outputCompositionSets = {}

    consolidatedModel = 0 
    
    for novelAnswer in novelanswerssimilar:
        if (novelAnswer[1] == 'y,y,y,y,y,y,y,y,y,y,y,y'):
            finalSimilarPairs.append(novelAnswer[0])
            consolidatedModel = 1
   
    for pair in finalSimilarPairs:
        if (pair[0] > pair[1]):
            outputSimilarPairs.update({pair[0]:pair[1]})
        outputSimilarPairs.update({pair[1]:pair[0]}) #testar
    
    for novelAnswer in novelanswerscomposition:
        if (novelAnswer[1] == 'y'):
            finalCompositionSets.append(novelAnswer[0])
            consolidatedModel = 1
    
    for pair in finalCompositionSets:
        outputCompositionSets.update({pair[0]:pair[1]})
    
    output = [consolidatedModel, outputSimilarPairs, outputCompositionSets]

    return output
############################################################################



############################################################################
def getResemblanceQuestionsAnswers(question):
    answers = ["contains", " ", " ", " "]
    return answers
############################################################################



############################################################################
def askResemblance(key,index,view):

    global resemblanceDict

    resemblanceAnswers = []
    resemblanceQuestions = []
    resemblanceOptions = " contains or is contained in "
    resemblancePairs = []

    resemblanceAnswers.append({key:[resemblanceDict.get(key)]})

    elements = classifyEarly(view)

    if(index==0):
        for element in elements:
            if(element[1]=="who"):
                resemblanceQuestions.append([resemblanceDict[key][0],resemblanceOptions,element[0],"?"])

    if(index==1):
        for element in elements:
            if(element[1]=="where"):
                resemblanceQuestions.append([resemblanceDict[key][1],resemblanceOptions,element[0],"?"])
    
    if(index==2):
        for element in elements:
            if(element[1]=="when"):
                resemblanceQuestions.append([resemblanceDict[key][2],resemblanceOptions,element[0],"?"])

    if(index==3):
        for element in elements:
            if(element[1]=="what"):
                resemblanceQuestions.append([resemblanceDict[key][3],resemblanceOptions,element[0],"?"])            

    for ind, question in enumerate(resemblanceQuestions):

        answers = getResemblanceQuestionsAnswers(question)
        answer = answers[ind]
           
        if (answer == "contains"):
            resemblancePairs.append([question[0],"contains",question[2]])

        if (answer == "is contained in"):
            resemblancePairs.append([question[0],"is contained in",question[2]])
    
    return resemblancePairs
############################################################################



############################################################################
def generateResemblanceStructure(output,view):

    global earlyAnswersDict

    consolidatedModel = output[0]
    similarPairs = output[1]

    dimensions = []
    if consolidatedModel != 0:
        for pair in similarPairs:

            key = pair
            value = similarPairs[pair]

            if(earlyAnswersDict[key][0] != ' '):
                dimensions.append([key, value, "WHO", earlyAnswersDict[key][0]])
            
            if(earlyAnswersDict[key][1] != ' '):
                dimensions.append([key, value, "WHERE", earlyAnswersDict[key][1]])
            
            if(earlyAnswersDict[key][2] != ' '):
                dimensions.append([key, value, "WHEN", earlyAnswersDict[key][2]])
            
            if(earlyAnswersDict[key][3] != ' '): #does not contain other
                dimensions.append([key, value, "WHAT", earlyAnswersDict[key][3]])
    
    if consolidatedModel != 0:
        for key in earlyAnswersDict: #aqui estão todas as atividades
            for index, answer in enumerate(earlyAnswersDict[key]):
                if answer == "Other:":
                    resemblancePairs = askResemblance(key,index,view)

    return [dimensions, resemblancePairs]
        
############################################################################



############################################################################
def integrateSTKViews(views):
    consolidatedModel = 0

    previousView = views[0]
    views.remove(previousView)

    previousViewQuestions = generatePrimaryQuestions(previousView)
    previousViewAnswers = askPrimaryQuestions(previousViewQuestions, previousView)

    for view in views:
                
        questions = generatePrimaryQuestions(view)

        answers = askPrimaryQuestions(questions,view)

        similarActivitiesPairs = comparePrimaryAnswersResemblance(previousViewAnswers, answers)

        compositionActivitiesSets = comparePrimaryAnswersComposition(previousViewAnswers, answers, view, previousView)
        
        novelquestionssimilar = generateNovelQuestionsResemblance(similarActivitiesPairs)

        novelquestionscomposition = generateNovelQuestionsComposition(compositionActivitiesSets)

        novelanswerssimilar = askNovelQuestionsResemblance(novelquestionssimilar)
        
        novelanswerscomposition = askNovelQuestionsComposition(novelquestionscomposition)
        
        output = produceConsolidatedModel(novelanswerssimilar, novelanswerscomposition)
 
        resemblanceStructure = generateResemblanceStructure(output,view)


    if output[0] != 0:
        print("The similar pairs are", output[1])
        print("The composition pairs are", output[2])
    

    return consolidatedModel
############################################################################



############################################################################
def main():

    views = ["Facilities",  "HR"]

    consolidatedModel = integrateSTKViews(views)

    return consolidatedModel

if __name__ == "__main__":
    main()
############################################################################