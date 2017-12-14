import sqlite3
import pandas as pd

def main():

    database_name = 'iris.db'
    table_name = 'iris'
    file_name = 'iris.data'

    # db = sqlite3.connect(':memory:')  # in memory database
    db = sqlite3.connect(database_name)  # file based database

    # download the example dataset
    # dataset_location = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    dataset_location = './{}'.format(file_name)
    dataset = pd.read_csv(dataset_location, names=['slength', 'swidth', 'pheight', 'pwidth', 'class'])
    print(dataset.describe())
    # dataset.to_csv('iris.data', index=False)  # save to disk

    # dump existing table, and save to database
    cursor = db.cursor()
    cursor.execute('DROP TABLE {}'.format(table_name))
    db.commit()
    dataset.to_sql(table_name, con=db, index=False)

    # retrieve from database
    dataset = pd.read_sql_query("SELECT * FROM {}".format(table_name), db)
    print(dataset.describe())

    # and finally we close the db
    db.close()


if __name__ == "__main__":
    main()