import  pandas 
import  numpy  
from  sklearn.linear_model  import  LinearRegression

db = pandas.read_csv('weight-height.csv')
y = db["Weight"]
x = db["Height"]
x = x.values
x = x.reshape(10000,1)
y = y.values
y = y.reshape(10000,1)
from sklearn.linear_model import LinearRegression 
mind = LinearRegression()
mind.fit(x,y)

while True:
            input1 = float(input("enter height for which you want to predict weight: "))
            print("Your estimated Salary:", mind.predict( [[ input1 ]] ) )
            quit = input("\nPress q to exit & to continue press Enter:")
	    if quit == "q":
	 	   break
            

