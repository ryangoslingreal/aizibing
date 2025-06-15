def linear(d_avg, m_min=0.01, m_max=0.3):
    return m_max - (m_max - m_min) * d_avg

def exponential(d_avg, m_min=0.01, m_max=0.3, alpha=5):
    from math import exp
    return m_min + (m_max - m_min) * exp(-alpha * d_avg)

def sigmoid(d_avg, m_min=0.01, m_max=0.3, steepness=10):
    from math import exp
    sig = 1 / (1 + exp(steepness * (d_avg - 0.5)))
    return m_min + (m_max - m_min) * sig