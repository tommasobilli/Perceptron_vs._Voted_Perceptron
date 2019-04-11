# Perceptron vs. Voted Perceptron

Questo progetto è stato realizzato per l'esame di Intelligenza Artificiale del corso di laurea in Ingegneria Informatica presso l'Università degli Studi di Firenze.

In questo progetto sono stati implementati gli algoritmi Perceptron e Voted Perceptron con l'obiettivo di confrontarne le prestazioni analizzando la matrice di confusione e l'accuratezza su Dataset con almeno 1000 esempi ciascuno.

I 3 dataset utilizzati sono i seguenti:

- [Banknote Authentication](https://archive.ics.uci.edu/ml/machine-learning-databases/00267/);
- [HTRU 2](https://archive.ics.uci.edu/ml/machine-learning-databases/00372/) (file 'HTRU_2.arff' all'interno del pacchetto .zip);
- [Phishing Websites](http://archive.ics.uci.edu/ml/machine-learning-databases/00327/) (file 'Training Dataset.arff').

Per costruire un oggetto DataSet è sufficiente passare al costruttore il percorso del dataset stesso (esempio: `DataSet(filename="DataSets/data_banknote_authentication.txt")`).

Il file `Test` implementa sia il metodo `holdoutValidation()` che il metodo `kFoldCrossValidation()`. Per un'analisi più approfondita, si è scelto di usare per i test la k-fold cross validation.

Sono indicate nel file alcune linee di codice modificabili per cambiare la suddivisione fra training test e test set nella funzione `holdoutValidation()` mentre nella funzione `test()` si può aggiustare il numero di massime iterazioni per Perceptron e Voted Perceptron.

Per chiamare i due metodi di test è sufficiente passare l'oggetto DataSet, e nel caso di k-fold cross validation si passa anche il numero k di iterazioni (esempio: `kFoldCrossValidation(5, banknote_auth_dataset)`).

Nelle classi Perceptron e Voted Perceptron sono implementati i rispettivi metodi `train()` e `predict()`.
