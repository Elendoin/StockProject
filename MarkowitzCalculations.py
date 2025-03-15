import numpy as np
from scipy.optimize import minimize


def calculate_returns(data):
    returns = data.pct_change().dropna()
    return returns


def portfolio_exp_return(weights, returns_avg):
    return np.dot(weights.T, returns_avg)


def portfolio_stddev(weights, cov_matrix):
    return np.sqrt(max(np.dot(np.dot(cov_matrix, weights), weights.T), 1e-10))


def markowitz_optimization(returns, risk_free_rate):
    num_assets = len(returns.columns)
    returns_avg = returns.mean()
    cov_matrix = returns.cov()

    print("Average Returns:\n", returns_avg)
    print("Covariance Matrix:\n", cov_matrix)

    def sharpe_ratio(weights):
        expected_return = portfolio_exp_return(weights, returns_avg)
        risk = portfolio_stddev(weights, cov_matrix)
        return -((expected_return - risk_free_rate) / risk)

    def weight_constraint(weights):
        return np.sum(weights) - 1

    start_weights = np.ones(num_assets) / num_assets
    bounds = [(0, 1) for _ in range(num_assets)]
    constraints = [{'type': 'eq', 'fun': weight_constraint}]

    result = minimize(
        sharpe_ratio,
        start_weights,
        method='SLSQP',
        bounds=bounds,
        constraints=constraints
    )

    if result.success:
        optimized_weights = result.x
        return optimized_weights
    else:
        raise RuntimeError(f"Optimization failed: {result.message}")