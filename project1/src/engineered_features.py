def add_engineered_features(data):
    data = data.copy()

    data["Cholesterol_Age_Ratio"] = (
        data["Cholesterol"] / (data["Age"] + 1)
    )

    data["MaxHR_Age_Ratio"] = (
        data["MaxHR"] / (data["Age"] + 1)
    )

    data["BP_Age_Ratio"] = (
        data["RestingBP"] / (data["Age"] + 1)
    )

    data["Heart_Stress"] = (
        data["Oldpeak"] * data["FastingBS"]
    )

    return data