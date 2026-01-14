Problem statement

This project analyzes clinical data from patients diagnosed with Guillain-Barré Syndrome to identify factors associated with functional recovery at hospital discharge.

Functional outcome is measured using the Hughes disability score at discharge. A good outcome is defined as a Hughes score of 2 or less, indicating independent or near-independent function. A poor outcome is defined as a score greater than 2.

The objective is not to predict future outcomes, but to determine which admission-time demographic, clinical, laboratory, and electrophysiological variables are associated with recovery by discharge.

Statistical analysis overview

All analyses are performed using classical statistical methods commonly used in clinical research.

Descriptive statistics

Continuous variables are summarized using mean and standard deviation.

Categorical variables are summarized using counts and percentages.

Group comparisons

Student’s t-test is used for normally distributed continuous variables.

Mann–Whitney U test is used for non-normally distributed continuous variables.

Chi-square test or Fisher’s exact test is used for categorical variables.

These analyses compare patients with good versus poor discharge outcomes.

Logistic regression analysis

Logistic regression is used to identify factors associated with discharge outcome.

Outcome variable

GoodOutcome

Defined as Hughes disability score ≤ 2 at discharge.

Binary variable: 1 = good outcome, 0 = poor outcome.

Univariate logistic regression

Each admission-time variable is analyzed individually against the outcome.

Odds ratios with 95 percent confidence intervals and p values are calculated.

This step is used to screen variables for potential association with outcome.

Multivariable logistic regression

Variables showing significant or near-significant association in univariate analysis are entered into a multivariable model.

This model identifies independent predictors of discharge outcome after adjusting for other variables.

Results are reported as adjusted odds ratios with 95 percent confidence intervals and p values.

Interpretation

Odds ratio greater than 1 indicates higher odds of good recovery.

Odds ratio less than 1 indicates lower odds of good recovery.

Statistical significance is assessed using a p-value threshold of 0.05.