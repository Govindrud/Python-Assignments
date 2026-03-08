import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

def Weather(Datapath):
    Border = "="*60
    #------------------------------------------------------------
    # Step 1 : Load Dataset
    #------------------------------------------------------------
    print(Border)
    print("Step 1 : Load the Dataset")
    print(Border)
    df = pd.read_csv(Datapath)
    print(df.head())
    print(df.shape)

    #------------------------------------------------------------
    # Step2: Clean , Prepare and Manipulate the Data
    #------------------------------------------------------------
    print(Border)
    print("Step 2: Clean , Prepare and Manipulate the Data ")
    print(Border)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns =['Unnamed: 0'], inplace= True)
    
    print(df.shape)
    print(df.head())
    print("Missing values columns:",df.isnull().sum())

    print(Border)
    print(df.describe())

    #Manipulate the Data 
    le = LabelEncoder()

    df['Whether']= le.fit_transform(df['Whether'])

    df['Temperature']=le.fit_transform(df['Temperature'])

    print(df.head())
    #------------------------------------------------------------
    # Step 3: Train Data 
    #------------------------------------------------------------
    print(Border)
    print("Step 3: Train Data  ")
    print(Border)

    X =df[['Whether','Temperature']]
    Y = df['Play']
    X_train,X_test,Y_train,Y_test= train_test_split(X,Y,test_size=0.2,random_state=42)
   #------------------------------------------------------------
    # Step 4: Test Data 
    #------------------------------------------------------------
    print(Border)
    print("Step 4: Test Data   ")
    print(Border)
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train,Y_train)
    Y_pred = model.predict(X_test)

   #------------------------------------------------------------
    # Step 5: Calculate Accuracy
    #------------------------------------------------------------
    print(Border)
    print("Step 5: Calculate Accuracy   ")
    print(Border)
    Accuracy = accuracy_score(Y_test ,Y_pred)
    print(Accuracy *100)

def main():
    Weather(Datapath="PlayPredictor.csv")

if __name__ == "__main__":
    main()