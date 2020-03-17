# Make an objective function for optimization of italian data to SIR model first version
def SIR_model_without_R(t, y,beta,gamma,N):
    S=y[0]
    I=y[1]
    dSdt=-beta*I*S/N
    dIdt=beta*I*S/N-gamma*I    
    return [dSdt,dIdt]

#Improved version where I is integrated along (before cumsum which explains low R0, at least partially)

# Make an objective function for optimization of italian data to SIR model
def SIR_model_without_R(t, y,beta,gamma,N):
    S=y[0]
    I=y[1]
    Icum=y[2]
    dSdt=-beta*I*S/N
    dIdt=beta*I*S/N-gamma*I
    dIcumdt=beta*I*S/N
    return [dSdt,dIdt,dIcumdt]

def fit_function(t,beta,gamma,S0,I0,N):
    sol= solve_ivp(lambda t,y: SIR_model_without_R(t,y,beta,gamma,N), 
                   [0, max(t)],(S0,I0,I0),teval=np.arange(0,max(t),1e-3),
                   dense_output=True,rtol=1e-10,atol=1e-20)
    y=sol.sol(t)
    return y[2]
