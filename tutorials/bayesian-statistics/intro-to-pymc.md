# Introduction to PyMC

## Initial Setup

### Required Imports

```python
import pymc as pm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import arviz as az

# Optional: set random seed for reproducibility
np.random.seed(42)
```

### Loading Data

```python
# Example: Simple linear regression dataset
# Generate synthetic data
n_samples = 100
true_intercept = 2.0
true_slope = 1.5
true_sigma = 0.5

x = np.linspace(0, 10, n_samples)
y = true_intercept + true_slope * x + np.random.normal(0, true_sigma, n_samples)

# Create DataFrame
data = pd.DataFrame({'x': x, 'y': y})

# Basic data exploration
print(data.head())
print(data.describe())
```

## Building Models

### Model Context and Structure

```python
with pm.Model() as linear_model:
    # Priors for unknown model parameters
    intercept = pm.Normal('intercept', mu=0, sigma=10)
    slope = pm.Normal('slope', mu=0, sigma=10)
    sigma = pm.HalfNormal('sigma', sigma=1)

    # Expected value of outcome
    mu = intercept + slope * x

    # Likelihood (sampling distribution) of observations
    y_obs = pm.Normal('y_obs', mu=mu, sigma=sigma, observed=y)
```

### Random Variables

```python
with pm.Model() as model:
    # Continuous distributions
    normal_rv = pm.Normal('normal_param', mu=0, sigma=1)
    uniform_rv = pm.Uniform('uniform_param', lower=0, upper=10)
    beta_rv = pm.Beta('beta_param', alpha=2, beta=5)

    # Discrete distributions
    poisson_rv = pm.Poisson('poisson_param', mu=3)
    binomial_rv = pm.Binomial('binomial_param', n=10, p=0.3)

    # Positive-only distributions
    exponential_rv = pm.Exponential('exp_param', lam=1)
    gamma_rv = pm.Gamma('gamma_param', alpha=2, beta=1)
```

### Adding in Observed Data

```python
with pm.Model() as model:
    # Parameters
    mu = pm.Normal('mu', mu=0, sigma=1)
    sigma = pm.HalfNormal('sigma', sigma=1)

    # Observed data
    obs = pm.Normal('observations', mu=mu, sigma=sigma, observed=data['y'])
```

### Deterministic Transformations

```python
with pm.Model() as model:
    # Parameters
    a = pm.Normal('a', mu=0, sigma=1)
    b = pm.Normal('b', mu=0, sigma=1)

    # Deterministic transformations
    sum_ab = pm.Deterministic('sum', a + b)
    product_ab = pm.Deterministic('product', a * b)

    # More complex transformations
    transformed = pm.Deterministic('transformed',
                                 pm.math.exp(a) / (1 + pm.math.exp(a)))
```

#### Some More Advanced Transformations

```python
with pm.Model() as model:
    x = pm.Normal('x', mu=0, sigma=1)

    # PyMC math functions
    exp_x = pm.Deterministic('exp_x', pm.math.exp(x))
    log_x = pm.Deterministic('log_x', pm.math.log(pm.math.abs(x) + 1e-8))
    sin_x = pm.Deterministic('sin_x', pm.math.sin(x))

    # Conditional logic
    positive_x = pm.Deterministic('positive_x', pm.math.switch(x > 0, x, 0))
```

## Sampling

### Basics

```python
with linear_model:
    # Sample from posterior
    trace = pm.sample(
        draws=2000,           # Number of samples per chain
        tune=1000,            # Number of tuning samples
        chains=4,             # Number of chains
        cores=4,              # Number of CPU cores
        random_seed=42        # For reproducibility
    )
```

### Additional Options

```python
with linear_model:
    # More control over sampling
    trace = pm.sample(
        draws=2000,
        tune=1000,
        chains=4,
        target_accept=0.95,   # Higher acceptance rate
        max_treedepth=12,     # Deeper trees for complex models
        return_inferencedata=True
    )

    # Check sampling diagnostics
    print(az.summary(trace))
    print(f"R-hat values: {az.rhat(trace)}")
```

## Model Validation

### Prior Predictive Checks

```python
with linear_model:
    # Sample from prior
    prior_predictive = pm.sample_prior_predictive(samples=1000)

# Plot prior predictions
fig, ax = plt.subplots(figsize=(10, 6))
for i in range(50):
    ax.plot(x, prior_predictive.prior_predictive['y_obs'][0, i, :],
            alpha=0.1, color='blue')
ax.scatter(x, y, alpha=0.5, color='red')
ax.set_title('Prior Predictive Check')
plt.show()
```

### Posterior Predictive Checks

```python
with linear_model:
    # Sample from posterior predictive
    posterior_predictive = pm.sample_posterior_predictive(
        trace,
        samples=1000
    )

# Plot posterior predictions
fig, ax = plt.subplots(figsize=(10, 6))
for i in range(50):
    ax.plot(x, posterior_predictive.posterior_predictive['y_obs'][0, i, :],
            alpha=0.1, color='blue')
ax.scatter(x, y, alpha=0.5, color='red')
ax.set_title('Posterior Predictive Check')
plt.show()
```

## An Example Hierarchical Model

```python
# Generate hierarchical data
n_groups = 5
n_per_group = 20
group_means = np.random.normal(0, 2, n_groups)
groups = np.repeat(np.arange(n_groups), n_per_group)
y_hierarchical = np.concatenate([
    np.random.normal(group_means[i], 1, n_per_group)
    for i in range(n_groups)
])

with pm.Model() as hierarchical_model:
    # Hyperpriors
    mu_global = pm.Normal('mu_global', mu=0, sigma=10)
    sigma_global = pm.HalfNormal('sigma_global', sigma=2)

    # Group-level parameters
    mu_group = pm.Normal('mu_group',
                        mu=mu_global,
                        sigma=sigma_global,
                        shape=n_groups)

    # Individual-level parameters
    sigma_individual = pm.HalfNormal('sigma_individual', sigma=2)

    # Likelihood
    y_pred = pm.Normal('y_pred',
                      mu=mu_group[groups],
                      sigma=sigma_individual,
                      observed=y_hierarchical)

    # Sample
    hierarchical_trace = pm.sample(2000, tune=1000, chains=4)
```
