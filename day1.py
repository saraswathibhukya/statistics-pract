import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r"C:\\Users\\Dell\\Downloads\\Statistics_Dataset.csv")
# print(df)
# print(df.head())
# print(df.tail())
# print(df.info())

# print("\nQ4. MEAN ORDER VALUE")
# mean_order_value = df["order_value"].mean()
# print("Mean Order Value =", mean_order_value)
# print("\nTotal records:")
# print(len(df))
# print("\nMedian:")
# print(df["order_value"].median())
# print(df["product_category"].mode()[0])
# print(df["payment_method"].mode()[0])
# print("\nOrder Value Range:")
# print(df["order_value"].max() - df["order_value"].min())
# print("Delivery Time Range:")
# print(df["delivery_time_min"].max() - df["delivery_time_min"].min())

# Q8 - Order Value
# print("\nOrder Value Variance:")
# print(df["order_value"].var())
# print("Order Value Standard Deviation:")
# print(df["order_value"].std())

# # Q9 - Delivery Time
# print("\nDelivery Time Variance:")
# print(df["delivery_time_min"].var())

# print("Delivery Time Standard Deviation:")
# print(df["delivery_time_min"].std())

# #10 - Quartiles
# print("\nQ1:")
# print(df["order_value"].quantile(0.25))

# print("Q2:")
# print(df["order_value"].quantile(0.50))

# print("Q3:")
# print(df["order_value"].quantile(0.75))


# Q11. Calculate IQR of order_value
# q1 = df["order_value"].quantile(0.25)
# q3 = df["order_value"].quantile(0.75)
# iqr = q3 - q1
# print("Q11 - IQR:", iqr)

# # Q12. Find 25th, 50th and 90th percentiles
# print("\nQ12 - Percentiles")

# print("25th:", df["order_value"].quantile(0.25))
# print("50th:", df["order_value"].quantile(0.50))
# print("90th:", df["order_value"].quantile(0.90))


# Q13. Compare mean and median
# mean = df["order_value"].mean()
# median = df["order_value"].median()

# print("\nQ13 - Mean:", mean)
# print("Q13 - Median:", median)

# if mean > median:
#     print("Mean is greater than median")
# elif mean < median:
#     print("Mean is less than median")
# else:
#     print("Mean and median are equal")


# Q14. Coefficient of Variation
# mean_order = df["order_value"].mean()
# std_order = df["order_value"].std()

# mean_delivery = df["delivery_time_min"].mean()
# std_delivery = df["delivery_time_min"].std()

# cv_order = (std_order / mean_order) * 100
# cv_delivery = (std_delivery / mean_delivery) * 100

# print("\nQ14 - CV Order Value:", cv_order, "%")
# print("Q14 - CV Delivery Time:", cv_delivery, "%")


# Q15. Average order value by product category
# print("\nQ15 - Average Order Value by Category")

# print(
#     df.groupby("product_category")["order_value"].mean()
# )


# Q16. Product category with highest median order value
# print("\nQ16 - Highest Median Category")

# median_category = df.groupby("product_category")["order_value"].median()

# print(median_category)

# print("Highest:",
    #   median_category.idxmax())

# Q17. Histogram of order_value
# print("\nQ17 - Histogram")

# plt.hist(df["order_value"], bins=10)
# plt.xlabel("Order Value")
# plt.ylabel("Number of Customers")
# plt.title("Order Value Histogram")
# plt.show()


# Q18. Histogram of delivery_time_min
# print("\nQ18 - Delivery Time Histogram")

# plt.hist(df["delivery_time_min"], bins=10)
# plt.xlabel("Delivery Time")
# plt.ylabel("Number of Customers")
# plt.title("Delivery Time Histogram")
# plt.show()

# Q19. Boxplots
# print("\nQ19 - Boxplots")

# plt.boxplot(df["order_value"])
# plt.title("Order Value Boxplot")
# plt.ylabel("Order Value")
# plt.show()

# plt.boxplot(df["delivery_time_min"])
# plt.title("Delivery Time Boxplot")
# plt.ylabel("Delivery Time")
# plt.show()

# Q20. Boxplot of order_value for each product category
# print("\nQ20 - Category Boxplot")

# sns.boxplot(
#     x="product_category",
#     y="order_value",
#     data=df
# )

# plt.title("Order Value by Product Category")
# plt.xticks(rotation=45)
# plt.show()


# Q21. Bar charts

# print("\nQ21 - Bar Charts")

# df["product_category"].value_counts().plot(kind="bar")
# plt.title("Product Category")
# plt.xlabel("Category")
# plt.ylabel("Count")
# plt.show()

# df["city"].value_counts().plot(kind="bar")
# plt.title("City")
# plt.xlabel("City")
# plt.ylabel("Count")
# plt.show()

# df["payment_method"].value_counts().plot(kind="bar")
# plt.title("Payment Method")
# plt.xlabel("Payment")
# plt.ylabel("Count")
# plt.show()


# # Q22. Scatterplot: order_value vs delivery_time_min

# print("\nQ22 - Order Value vs Delivery Time")

# plt.scatter(df["order_value"], df["delivery_time_min"])
# plt.xlabel("Order Value")
# plt.ylabel("Delivery Time")
# plt.title("Order Value vs Delivery Time")
# plt.show()

# print("Correlation:")
# print(df["order_value"].corr(df["delivery_time_min"]))


# Q23. Scatterplot: delivery_time_min vs satisfaction_score

# print("\nQ23 - Delivery Time vs Satisfaction")

# plt.scatter(df["delivery_time_min"], df["satisfaction_score"])
# plt.xlabel("Delivery Time")
# plt.ylabel("Satisfaction Score")
# plt.title("Delivery Time vs Satisfaction")
# plt.show()

# print("Correlation:")
# print(df["delivery_time_min"].corr(df["satisfaction_score"]))


# # Q24. Satisfaction for returned and non-returned

# print("\nQ24 - Satisfaction by Returned Status")

# sns.boxplot(
#     x="returned",
#     y="satisfaction_score",
#     data=df
# )

# plt.xlabel("Returned (0 = No, 1 = Yes)")
# plt.ylabel("Satisfaction Score")
# plt.title("Satisfaction by Returned Status")
# plt.show()


# Q25. P(orders_today >= 1)

# print("\nQ25 - Probability of At Least One Order")

# p = (df["orders_today"] >= 1).mean()

# print(p)


# # Q26. P(orders_today = 0)

# print("\nQ26 - P(orders_today = 0)")

# p = (df["orders_today"] == 0).mean()

# print(p)


# # Q27. P(orders_today = 1)

# print("\nQ27 - P(orders_today = 1)")

# p = (df["orders_today"] == 1).mean()

# print(p)


# # Q28. P(orders_today = 2)

# print("\nQ28 - P(orders_today = 2)")

# p = (df["orders_today"] == 2).mean()

# print(p)


# # Q29. P(orders_today = 3)

# print("\nQ29 - P(orders_today = 3)")

# p = (df["orders_today"] == 3).mean()

# print(p)


# # Q30. P(orders_today >= 2)

# print("\nQ30 - P(orders_today >= 2)")

# p = (df["orders_today"] >= 2).mean()

# print(p)


# # Q31. P(returned = 1) and P(returned = 0)

# print("\nQ31 - Returned Probability")

# p_returned = (df["returned"] == 1).mean()
# p_not_returned = (df["returned"] == 0).mean()

# print("P(returned = 1):", p_returned)
# print("P(returned = 0):", p_not_returned)


# # Q32. P(satisfaction_score >= 4)

# print("\nQ32 - P(satisfaction >= 4)")

# p = (df["satisfaction_score"] >= 4).mean()

# print(p)


# # Q33. P(order_value > 5000)

# print("\nQ33 - P(order_value > 5000)")

# p = (df["order_value"] > 5000).mean()

# print(p)


# # Q34. P(payment_method = UPI)

# print("\nQ34 - P(UPI)")

# p = (df["payment_method"] == "UPI").mean()

# print(p)


# Q35. P(product_category = Electronics)

# print("\nQ35 - P(Electronics)")

# p = (df["product_category"] == "Electronics").mean()

# print(p)


# # Q36. P(returned) + P(not returned)

# print("\nQ36 - Probability Check")

# print(p_returned + p_not_returned)


# # Q37. P(UPI AND returned)

# print("\nQ37 - P(UPI AND Returned)")

# p = (
#     (df["payment_method"] == "UPI") &
#     (df["returned"] == 1)
# ).mean()

# print(p)


# # Q38. P(returned | Fashion)

# print("\nQ38 - P(Returned | Fashion)")

# fashion = df[df["product_category"] == "Fashion"]

# p = (fashion["returned"] == 1).mean()

# print(p)


# # Q39. P(returned | Electronics)

# print("\nQ39 - P(Returned | Electronics)")

# electronics = df[df["product_category"] == "Electronics"]

# p = (electronics["returned"] == 1).mean()

# print(p)


# Q40. P(purchase_today | UPI)

# print("\nQ40 - P(Purchase Today | UPI)")

# upi = df[df["payment_method"] == "UPI"]

# p = (upi["purchase_today"] == 1).mean()

# print(p)

# Q41. P(purchase_today | COD)

print("\nQ41 - P(Purchase Today | COD)")

cod = df[df["payment_method"] == "COD"]

p = (cod["purchase_today"] == 1).mean()

print(p)


# Q42. P(satisfaction >= 4 | returned = 0)

print("\nQ42 - P(Satisfaction >= 4 | Not Returned)")

not_returned = df[df["returned"] == 0]

p = (not_returned["satisfaction_score"] >= 4).mean()

print(p)


# Q43. P(satisfaction >= 4 | returned = 1)

print("\nQ43 - P(Satisfaction >= 4 | Returned)")

returned = df[df["returned"] == 1]

p = (returned["satisfaction_score"] >= 4).mean()

print(p)


# Q44. P(UPI | returned = 1)

print("\nQ44 - P(UPI | Returned)")

p = (returned["payment_method"] == "UPI").mean()

print(p)


# Q45. P(returned = 1 | UPI)

print("\nQ45 - P(Returned | UPI)")

upi = df[df["payment_method"] == "UPI"]

p = (upi["returned"] == 1).mean()

print(p)


# Q46. Why are Q44 and Q45 different?

print("\nQ46")

print("P(UPI | Returned) means:")
print("Among returned customers, how many used UPI.")

print("P(Returned | UPI) means:")
print("Among UPI customers, how many returned.")


# Q47. Contingency table: payment_method and returned

print("\nQ47 - Payment Method and Returned")

table = pd.crosstab(df["payment_method"], df["returned"])

print(table)


# Q48. Contingency table: product_category and purchase_today

print("\nQ48 - Product Category and Purchase")

table = pd.crosstab(
    df["product_category"],
    df["purchase_today"]
)

print(table)


# Q49. Check independence of UPI and returned

print("\nQ49 - Independence Check")

p_upi = (df["payment_method"] == "UPI").mean()
p_returned = (df["returned"] == 1).mean()

p_both = (
    (df["payment_method"] == "UPI") &
    (df["returned"] == 1)
).mean()

print("P(UPI) =", p_upi)
print("P(Returned) =", p_returned)
print("P(UPI and Returned) =", p_both)

print("P(UPI) * P(Returned) =", p_upi * p_returned)


# Q50. Multiplication rule

print("\nQ50 - Multiplication Rule")

p_returned_given_upi = (upi["returned"] == 1).mean()

print("P(UPI) =", p_upi)
print("P(Returned | UPI) =", p_returned_given_upi)

print("P(UPI) * P(Returned | UPI) =",
      p_upi * p_returned_given_upi)

print("Actual P(UPI and Returned) =", p_both)


# Q51. Bayes theorem concept

print("\nQ51 - Bayes Theorem")

print("Bayes theorem helps calculate:")
print("P(Returned | Fashion)")

print("using reverse conditional probabilities.")


# Q52. Possible values of orders_today

print("\nQ52 - Possible Values")

print(df["orders_today"].unique())


# Q53. PMF of orders_today

print("\nQ53 - PMF")

pmf = df["orders_today"].value_counts(normalize=True).sort_index()

print(pmf)


# Q54. PMF probabilities add to 1

print("\nQ54 - PMF Sum")

print(pmf.sum())


# Q55. P(X <= 1)

print("\nQ55 - P(X <= 1)")

p = (df["orders_today"] <= 1).mean()

print(p)


# Q56. P(X >= 2)

print("\nQ56 - P(X >= 2)")

p = (df["orders_today"] >= 2).mean()

print(p)


# Q57. CDF

print("\nQ57 - CDF")

cdf = pmf.cumsum()

print(cdf)


# Q58. CDF at X = 1

print("\nQ58 - CDF at X = 1")

print(cdf.loc[1])


# Q59. Expected value

print("\nQ59 - Expected Value")

expected = (pmf.index * pmf).sum()

print(expected)


# Q60. Expected value vs ordinary mean

print("\nQ60")

print("Expected Value =", expected)

print("Ordinary Mean =",
      df["orders_today"].mean())


# Q61. Variance

print("\nQ61 - Variance")

mean = expected

variance = (
    ((pmf.index - mean) ** 2) * pmf
).sum()

print(variance)


# Q62. Standard deviation

print("\nQ62 - Standard Deviation")

print(variance ** 0.5)


# Q63. Decimal expected value

print("\nQ63")

print("Expected value can be decimal because it is an average.")


# Q64. Bernoulli variable

print("\nQ64 - Bernoulli")

print("Success = purchase_today = 1")
print("Failure = purchase_today = 0")


# Q65. Bernoulli probability p

print("\nQ65 - Bernoulli p")

p = df["purchase_today"].mean()

print("p =", p)


# Q66. Bernoulli expected value

print("\nQ66 - E(X)")

print("E(X) =", p)


# Q67. Bernoulli variance

print("\nQ67 - Bernoulli Variance")

bernoulli_variance = p * (1 - p)

print(bernoulli_variance)


# Q68. Theoretical vs empirical variance

print("\nQ68 - Variance Comparison")

empirical_variance = df["purchase_today"].var()

print("Theoretical Variance =", bernoulli_variance)

print("Empirical Variance =", empirical_variance)


# Q69. Continuous variable

print("\nQ69")

print("delivery_time_min is treated as a continuous variable.")
print("orders_today is a discrete variable.")


# Q70. PMF vs PDF

print("\nQ70")

print("PMF is used for discrete variables.")
print("PDF is used for continuous variables.")


# Q71. Continuous variable

print("\nQ71")

print("Continuous variables are usually studied over intervals.")


# Q72. Histogram of delivery time

print("\nQ72 - Delivery Time Histogram")

plt.hist(df["delivery_time_min"], bins=10)

plt.xlabel("Delivery Time")
plt.ylabel("Frequency")
plt.title("Delivery Time Distribution")

plt.show()


# Q73. Empirical probability distribution
# Using payment_method

print("\nQ73 - Payment Method Distribution")

distribution = df["payment_method"].value_counts(normalize=True)

print(distribution)


# Q74. Mean, variance and standard deviation

print("\nQ74 - Order Value Statistics")

print("Mean =", df["order_value"].mean())

print("Variance =", df["order_value"].var())

print("Standard Deviation =", df["order_value"].std())


# Q75. Ten random samples of 50

print("\nQ75 - Ten Sample Means")

for i in range(10):

    sample = df.sample(50)

    mean = sample["order_value"].mean()

    print("Sample", i + 1, "Mean =", mean)


# Q76. Compare sample means with population mean

print("\nQ76")

population_mean = df["order_value"].mean()

print("Population Mean =", population_mean)

for i in range(10):

    sample = df.sample(50)

    sample_mean = sample["order_value"].mean()

    print(
        "Sample", i + 1,
        "Mean =", sample_mean
    )


# Q77. Convenience sample

print("\nQ77 - Convenience Sample")

city = df["city"].mode()[0]

convenience = df[df["city"] == city]

random_sample = df.sample(50)

print("City used =", city)

print(
    "Convenience Sample Mean =",
    convenience["order_value"].mean()
)

print(
    "Random Sample Mean =",
    random_sample["order_value"].mean()
)


# Q78. Five business findings

print("\nQ78 - Business Findings")

print("1. Average order value =",
      df["order_value"].mean())

print("2. Average delivery time =",
      df["delivery_time_min"].mean())

print("3. Average satisfaction =",
      df["satisfaction_score"].mean())

print("4. Return probability =",
      df["returned"].mean())

print("5. Purchase probability =",
      df["purchase_today"].mean())


# Q79. Business question

print("\nQ79 - Business Question")

print("Question:")
print("Does delivery time affect customer satisfaction?")

print("Average Delivery Time =",
      df["delivery_time_min"].mean())

print("Average Satisfaction =",
      df["satisfaction_score"].mean())

print("Correlation =",
      df["delivery_time_min"].corr(
          df["satisfaction_score"]
      ))


# Q80. Short statistical report

print("\nQ80 - STATISTICAL REPORT")

print("Total Customers =", len(df))

print("Mean Order Value =",
      df["order_value"].mean())

print("Median Order Value =",
      df["order_value"].median())

print("P(Purchase Today) =",
      df["purchase_today"].mean())

print("P(Returned) =",
      df["returned"].mean())

print("P(Returned | UPI) =",
      p_returned_given_upi)

print("Mean Orders Today =",
      df["orders_today"].mean())

print("\nReport completed.")