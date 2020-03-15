# Make an objective function for optimization of italian data to SIR model
def SIR_model_without_R(t, y,beta,gamma,N):
    S=y[0]
    I=y[1]
    dSdt=-beta*I*S/N
    dIdt=beta*I*S/N-gamma*I    
    return [dSdt,dIdt]