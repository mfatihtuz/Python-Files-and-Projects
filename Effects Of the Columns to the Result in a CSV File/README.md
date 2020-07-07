[EN]
# Finding out which column affects the result most in a csv file

Simplest to use is XGBoost library (XGBRegressor or XGBClassifier depending on your task), train it and look at the feature_importance. This will directly tell you which columns were most used to create the classifier.

If the user have a table with one result column, and X column whice are affects the result. Then this method is very basic method to use, for newbie in Machine Learning.

[TR]
# Bir csv dosyasındaki sonucu en çok hangi sütunun etkilediğini bulma

Kullanımı en basit olanı XGBoost kütüphanesidir (görevinize bağlı olarak XGBRegressor veya XGBClassifier), eğitin ve feature_importance'a bakın. Bu, sınıflandırıcıyı oluşturmak size en çok hangi sütunların kullanıldığını doğrudan söyleyecektir.

Diyelim ki, kullanıcının bir sonuç sütunu ve X sayıda da sonucu etkileyen sütunu var. Bu basit metod sayesinde Machine Learning yeni başlayanlar için kullanılabilecek en ideal yöntemlerden birisidir.
