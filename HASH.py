dict = { 'teja' : { 'age': 20,
                    'cgpa' : 8.24,
                    'branch' : 'cse',},
         'Rakesh' : {
             'age' : 20,
             'cgpa' : 9.3,
             'branch' : 'ece',
         }
}

for key , value in dict.items():
    print(key.title(), 'has' ,value['cgpa'], 'cgpa')