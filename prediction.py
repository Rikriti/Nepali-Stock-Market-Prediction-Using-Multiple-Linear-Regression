import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
from matplotlib import style
import math
from nepse_recomand import stock_recommender,nepse_live_data
import plotly.graph_objects as go

class OrdinaryLeastSquares(object):
    
    def __init__(self):
        self.coefficients =[]

    def _reshape_x(self,X):
        return X.reshape(-1,1)
    
    def _concatenate_ones(self,X):
        ones = np.ones(shape=X.shape[0]).reshape(-1,1)
        return np.concatenate((ones,X),1)  
        
    def fit(self, X, y):
        if len(X.shape) == 1:X = self._reshape_x(X)
        
        X=self._concatenate_ones(X)
        self.coefficients=np.linalg.inv(X.transpose().dot(X)).dot(X.transpose()).dot(y) 

    
    def predict(self,entry):
        b0 = self.coefficients[0]
        other_betas = self.coefficients[1:]
        prediction = b0
        
        for xi,bi in zip(entry,other_betas):
            prediction += (bi * xi)

        return prediction
    
    
def mae(y_predicted, y_actual):
    errors = []
    for y_pred, y_act in zip(y_predicted, y_actual):
        error = abs( y_pred - y_act )
        errors.append(error)
    mean = sum(errors)/len(errors)
    return mean     
     

def main():
    df = pd.read_csv('stock_price.csv')
    st.title("Stock Prediction")
    st.sidebar.title("Stock Prediction Web App")
    st.markdown("There is a risk in everything, so be prepared for the ups and downs.")

    x = df[['High','Open','Low','Volume']].values
    y = df['Close'].values

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

    regressor = OrdinaryLeastSquares()
    regressor.fit(x_train,y_train) 
    y_pred = []
    for row in x_test:
      y_pred.append(regressor.predict(row))
    y_actual = y_test.tolist()
      
     
      
    mae_error = mae(y_pred,y_actual)
    y_pred=np.array(y_pred)
    result = pd.DataFrame({'Actual':y_test.flatten(),'Predicted':y_pred.flatten()})
    print(result)
    x = result.head(20)
    a=(x['Actual'].mean(axis = 0))
    b=(x['Predicted'].mean(axis = 0))
    High = int(st.sidebar.number_input("Enter High value: "))

    Open = int(st.sidebar.number_input("Enter Open value: "))
            
    Low = int(st.sidebar.number_input("Enter Low value: "))
    Volume = int(st.sidebar.number_input("Enter Volume value: "))

    if High <= 0 or Open <= 0 or Low <= 0 or Volume <=0:
        user_input = None   
    else:
        user_input=[High,Open,Low,Volume] 
    
    if st.sidebar.button("Predict", key='Predict'):
        st.subheader("Stock Prediction Results")
        if user_input is None:
            st.write("Invalid Input")
        else:
            regressor.fit(x_train,y_train)
            predicted_output = regressor.predict(user_input)
            st.write("Prediction: ", round(predicted_output,3))
            graph = result
            graph.plot()
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
            st.write("Mean Absolute Error :", round(mae_error,2))

    if st.sidebar.button("recommend a stock",key="recommend"):
        st.subheader("Recomended Share From Past Days Activity:" + stock_recommender())
    if st.sidebar.button("Live Trading Data",key="Live Trading Data"):
        data = nepse_live_data()
        sn=[]
        stock_id=[]
        stock_symbol=[]
        max_price=[]
        min_price=[]
        closing_price=[]
        traded_shares=[]
        previous_closing=[]
        percent_difference=[]
        date=[]

        for i,live_data in enumerate(data['live']):
            sn.append(i+1)
            stock_id.append(live_data["StockID"])
            stock_symbol.append(live_data["StockSymbol"])
            max_price.append(live_data["MaxPrice"])
            min_price.append(live_data["MinPrice"])
            closing_price.append(live_data["ClosingPrice"])
            traded_shares.append(live_data["TradedShares"])
            previous_closing.append(live_data["PreviousClosing"])
            percent_difference.append(live_data["PercentDifference"])
            date.append(live_data["Date"])
            # nepse_values.append([i+1,live_data["StockID"],live_data["StockSymbol"],live_data["MaxPrice"],live_data["MinPrice"],live_data["ClosingPrice"],live_data["TradedShares"],live_data["PreviousClosing"],live_data["PercentDifference"],live_data["Date"]])
            

        fig = go.Figure(data=[go.Table(header=dict(values=['S.N', 'Stock ID','Stock Symbol','Max Price','Min Price','Closing Price','Traded Shares','Previous Closing','Percent Difference','Date']),
                        cells=dict(values=[sn,stock_id,stock_symbol,max_price,min_price,closing_price,traded_shares,previous_closing,percent_difference,date]))
                            ])
        st.write(fig)
                
if __name__ == '__main__':
    main()



