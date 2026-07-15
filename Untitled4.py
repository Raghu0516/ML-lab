#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd

data = pd.read_csv("MLlab2.csv")

target = data.columns[-1]


classes = data[target].unique()
priors = {}

for c in classes:
    priors[c] = len(data[data[target] == c]) / len(data)

print("Prior Probabilities:")
for c in priors:
    print(f"P({c}) = {priors[c]:.4f}")

def predict(sample):
    probabilities = {}

    for c in classes:

        prob = priors[c]

        class_data = data[data[target] == c]
        for feature in sample:
            count = len(class_data[class_data[feature] == sample[feature]])


            feature_values = data[feature].nunique()
            cond_prob = (count + 1) / (len(class_data) + feature_values)

            prob *= cond_prob

        probabilities[c] = prob

    print("\nPosterior Probabilities:")
    for c in probabilities:
        print(f"P({c}|X) = {probabilities[c]:.8f}")

    prediction = max(probabilities, key=probabilities.get)
    return prediction


test_sample = {
    "age": "senior",
    "income": "low",
    "student": "no",
    "credit_rating": "excellent"
}

result = predict(test_sample)

print("\nTest Sample:", test_sample)
print("Predicted Class:", result)


# In[ ]:




