import pandas as pd # Pandas reads CSV files into tables
from sklearn.model_selection import train_test_split
# Gets the train_test_split function that splits data into train (80%) + test (20%)
from sklearn.ensemble import RandomForestClassifier
# Gets the RandomForestClassifier class that learns hand pose
from sklearn.svm import SVC  # SVM model for comparison
import joblib # Library for saving/loading trained models

hand_dataset = pd.read_csv("data/sign_data.csv") 
# Reads the CSV into a table called hand_dataset
X = hand_dataset.iloc[:, :-1]  # 63 landmark values
# all rows (:), all columns except last (:-1)
y = hand_dataset.iloc[:, -1]   # labels
# all rows, only last column

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# Split data: 80% to train (learn patterns), 20% to test (check accuracy on unseen data)

# train both Random Forest and SVM models side-by-side
rf_model = RandomForestClassifier(random_state=42) # Random Forest: handles complex patterns well
svm_model = SVC(kernel='rbf', random_state=42, probability=True) # SVM: good for hand gesture boundaries


rf_model.fit(X_train, y_train) # Train RF
svm_model.fit(X_train, y_train)  # Train SVM (same data)

# Compare accuracy of both models
rf_accuracy = rf_model.score(X_test, y_test)
svm_accuracy = svm_model.score(X_test, y_test)
print(f"RF Accuracy: {rf_accuracy:.2%}") # shows RF performance
print(f"SVM Accuracy: {svm_accuracy:.2%}") # shows SVM performance 
# % correct predictions on unseen test data, .2f = show 2 decimal places

# save both models separately for dual demo
joblib.dump(rf_model, "rf_model.pkl")    # RF model for left screen
joblib.dump(svm_model, "svm_model.pkl")  # SVM model for right screen