def SIR_function(y, t, N, beta, gamma, mu, nu):
        # -- zunächst die Anfangsdaten - S, I, R:
        S = y[0]
        I = y[1]
        R = y[2]
        
        r1 = nu*N - beta*(S/N)*I - mu*S
        r2 = beta*(S/N)*I -gamma*I - mu*I
        r3 = gamma*I - mu*R
        
        return [r1, r2, r3]
    

def SIRD_function(y, t, N, beta, gamma, mu, nu, mu_d):
    # -- zunächst die Anfangsdaten - S, I, R:
    S = y[0]
    I = y[1]
    R = y[2]
    D = y[3]
    
    r1 = nu*N - beta*(S/N)*I - mu*S
    r2 = beta*(S/N)*I - gamma*I - (mu+mu_d)*I
    r3 = gamma*I - mu*R
    r4 = mu_d*I
    
    return [r1, r2, r3, r4]


def SEIR_function(y, t, N, beta, gamma, mu, nu, a):
    # -- zunächst die Anfangsdaten - S, I, R:
    S = y[0]
    E = y[1]
    I = y[2]
    R = y[3]
    
    r1 = nu*N - beta*(S/N)*I - mu*S
    r2 = beta*(S/N)*I - a*E - mu*E
    r3 = a*E - gamma*I - mu*I
    r4 = gamma*I - mu*R
    
    return [r1, r2, r3, r4]


def SEIRD_function(y, t, N, beta, gamma, mu, nu, a, mu_d):
    # -- zunächst die Anfangsdaten - S, I, R:
    S = y[0]
    E = y[1]
    I = y[2]
    R = y[3]
    R = y[4]
    
    r1 = nu*N - beta*(S/N)*I - mu*S
    r2 = beta*(S/N)*I - a*E - mu*E
    r3 = a*E - gamma*I - (mu+mu_d)*I
    r4 = gamma*I - mu*R
    r5 = mu_d*I
    
    return [r1, r2, r3, r4, r5]