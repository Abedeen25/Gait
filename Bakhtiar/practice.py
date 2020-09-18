import json

data = {}
data['UTKinect'] = []
data['UPCV'] = []
data['general'] = []

data['UPCV'].append(
    {
        'SpanDivide' : 5,
        'Head' : 1,
        'ShoulderCenter' : 2,
        'ShoulderLeft' : 3,
        'ShoulderRight' : 4,
        'ElbowLeft' : 5,
        'ElbowRight' : 6,
        'WristLeft' : 7,
        'WristRight' : 8,
        'HandLeft' : 9,
        'HandRight' : 10,
        'Spine' : 11,
        'HipCenter' : 12,
        'HipLeft' : 13,
        'HipRight' : 14,
        'KneeLeft' : 15,
        'KneeRight' : 16,
        'AnkleLeft' : 17,
        'AnkleRight' : 18,
        'FootLeft' : 19,
        'FootRight' : 20
    })

data['UTKinect'].append(
    {
        'SpanDivide' : 10,
        'HipCenter' : 1,
        'Spine' : 2,
        'ShoulderCenter' : 3,
        'Head' : 4,
        'ShoulderLeft' : 5,
        'ElbowLeft' : 6,
        'WristLeft' : 7,
        'HandLeft' : 8,
        'ShoulderRight' : 9,
        'ElbowRight' : 10,
        'WristRight' : 11,
        'HandRight' : 12,
        'HipLeft' : 13,
        'KneeLeft' : 14,
        'AnkleLeft' : 15,
        'FootLeft' : 16,
        'HipRight' : 17,
        'KneeRight' : 18,
        'AnkleRight' : 19,
        'FootRight' : 20
    }
)

data['general'].append(
    {
        'TotalJoints' : 20,
        'xCord' : 0,
        'yCord' : 1,
        'zCord' : 2,
        'MinBin' : 20,
        'DatasetFolder' : 'DataSet/',
        'UPCVFolder' : 'UPCV',
        'UTKinectFolder' : 'UTKinect',
        'TrainingSetFolder' : 'TrainingSet/',
        'TestSetFolder' : 'TestSet/',
        'TrainingFileNamePrefix' : 'User_Information_'
    }
)

with open('constants.json', 'w') as outfile:
    json.dumps(data, outfile)