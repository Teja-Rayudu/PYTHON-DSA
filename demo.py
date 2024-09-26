from sklearn import tree # type: ignore
#[height, weight, shoe size]
X = [[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[159,55,77],[171,75,42],[181,85,43]]

Y= ['male','female','male','female','female','male','female','male','male','female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([140,50,42])

print(prediction)