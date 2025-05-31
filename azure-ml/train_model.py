# Placeholder for ML training script
# Replace with Isolation Forest training code as shown earlier.

# Additional ML Model: Local Outlier Factor
from sklearn.neighbors import LocalOutlierFactor
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.05)
lof.fit(features)
joblib.dump(lof, "lof_model.pkl")
print("LOF model trained and saved.")

# Additional ML Model: One-Class SVM
from sklearn.svm import OneClassSVM
ocsvm = OneClassSVM(kernel='rbf', nu=0.05)
ocsvm.fit(features)
joblib.dump(ocsvm, "ocsvm_model.pkl")
print("One-Class SVM model trained and saved.")
