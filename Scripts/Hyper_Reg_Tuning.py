import numpy as np

def hyper_tuner(model,x_train_data,y_train_data,x_val_data,y_val_data,n,start,end,step):
    # Model, regressor model that is being fine-tuned
    # x_data, this is the feature dataset will use to train model
    # y_data, this is the target dataset will use to train model
    # x_val_data, this is the feature dataset will use to validate the model
    # y_val_data, this is the target dataset will use to validate the model
    # n, is the numbe rof iterations for the training process of the model
    # start, starting value of for list of alphas
    # end, end value of for list of alphas
    # step, how much you want each value in the alpha to increase with each step

    # Initalize all the metrics with appropriate values
    current_alpha=None
    current_MSE_score=float('inf')
    current_RMSE_score=None
    current_MAE_score=None
    current_R2_score=None

    # Let's train the model on given training data and test on the given validation data
    for a in np.arange(start,end,step):
        model.fit(x_train_data,y_train_data,a,n)
        MSE_value=model.MSE(x_val_data,y_val_data)
        RMSE_value=model.RMSE(x_val_data,y_val_data)
        MAE_value=model.MAE(x_val_data,y_val_data)
        R2_value=model.R_2(x_val_data,y_val_data)

        # THe best MSE metric is continuously tracked and updated
        if( ( MSE_value < current_MSE_score  )):
            current_alpha=a
            current_MSE_score=MSE_value
            current_RMSE_score=RMSE_value
            current_MAE_score=MAE_value
            current_R2_score=R2_value
    
    
    # Best metrics for the given range of learning rates is returned
    return [current_alpha,current_MSE_score,current_RMSE_score,current_MAE_score,current_R2_score]
        
        