import pandas as pd
import numpy as np
import statsmodels.api as sm

INPUT_XLSX = r"C:\Users\ASUS\PyCharmMiscProject\GBS_analysis\processed_input\processed_gps_input.xlsx"  # change if needed
SHEET_NAME = 0  # or "Sheet1"
OUTPUT_XLSX = "GBS_logistic_results.xlsx"

OUTCOME_COL = "GoodOutcome"

UNIVARIATE_VARS = [
    "Hughes disability score - admission (0 to 6 ,0 is healthy least severe,6 is most severe (death)",
    "Single breath count (>30 NORMAL)",
    "Craniobulbar weakness",
    "CRP(<0.5mg/dL)",
    "Subtype_AMSAN",
    "Albumin (3.4-5.4g/dl)",
    "Facial weakness",
    "Paresthesias",
    "Subtype_AIDP",
    "Age",
    "Subtype_AMAN",
    "Truncal weakness",
    "NLR (normal <1-3,3-6 mild increase,6-9 mod increase,>9 severe increase in stress)",
    "Sex_binary",
    "PLR(Males-36.63-149.13)(Females43.36-172.68)",
]

MULTIVARIATE_VARS = [
    "Hughes disability score - admission (0 to 6 ,0 is healthy least severe,6 is most severe (death)",
    "Single breath count (>30 NORMAL)",
    "Craniobulbar weakness",
    "CRP(<0.5mg/dL)",
    "Subtype_AMSAN",
]


def fit_logit(y: pd.Series, X: pd.DataFrame):
    model = sm.Logit(y, X)
    res = model.fit(disp=False, method="lbfgs", maxiter=1000)
    return res


def univariate_table(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for var in UNIVARIATE_VARS:
        temp = df[[OUTCOME_COL, var]].copy()
        temp[OUTCOME_COL] = pd.to_numeric(temp[OUTCOME_COL], errors="coerce")
        temp[var] = pd.to_numeric(temp[var], errors="coerce")
        temp = temp.dropna()

        if len(temp) < 5:
            continue

        y = temp[OUTCOME_COL].astype(float)
        X = sm.add_constant(temp[[var]].astype(float))

        res = fit_logit(y, X)

        beta = res.params[var]
        ci_low, ci_high = res.conf_int().loc[var]
        p = res.pvalues[var]

        rows.append(
            {
                "Variable": var,
                "OR": float(np.exp(beta)),
                "CI_low": float(np.exp(ci_low)),
                "CI_high": float(np.exp(ci_high)),
                "p_value": float(p),
                "N_used": int(len(temp)),
            }
        )

    out = pd.DataFrame(rows)
    if not out.empty:
        out = out.sort_values("p_value", ascending=True).reset_index(drop=True)
    return out


def multivariable_table(df: pd.DataFrame) -> pd.DataFrame:
    cols = [OUTCOME_COL] + MULTIVARIATE_VARS
    temp = df[cols].copy()

    temp[OUTCOME_COL] = pd.to_numeric(temp[OUTCOME_COL], errors="coerce")
    for v in MULTIVARIATE_VARS:
        temp[v] = pd.to_numeric(temp[v], errors="coerce")

    temp = temp.dropna()

    y = temp[OUTCOME_COL].astype(float)
    X = sm.add_constant(temp[MULTIVARIATE_VARS].astype(float))

    res = fit_logit(y, X)

    rows = []
    for var in MULTIVARIATE_VARS:
        beta = res.params[var]
        ci_low, ci_high = res.conf_int().loc[var]
        p = res.pvalues[var]

        rows.append(
            {
                "Variable": var,
                "OR": float(np.exp(beta)),
                "CI_low": float(np.exp(ci_low)),
                "CI_high": float(np.exp(ci_high)),
                "p_value": float(p),
            }
        )

    out = pd.DataFrame(rows).sort_values("p_value", ascending=True).reset_index(drop=True)
    out.insert(1, "N_used", int(len(temp)))
    return out


def main():
    df = pd.read_excel(INPUT_XLSX, sheet_name=SHEET_NAME)

    uni = univariate_table(df)
    mv = multivariable_table(df)

    with pd.ExcelWriter(OUTPUT_XLSX, engine="openpyxl") as writer:
        uni.to_excel(writer, index=False, sheet_name="Univariate")
        mv.to_excel(writer, index=False, sheet_name="Multivariable")

    print(f"Saved: {OUTPUT_XLSX}")


if __name__ == "__main__":
    main()
