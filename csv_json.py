import csv
import pandas



def main():
    filename = "tasks.csv"
   

    print("-- TASKS LIST --")
    data = []
    try:
        data = pandas.read_csv(filename)
        print(data)
    except pandas.errors.EmptyDataError:
        print("List is empty")





    print("Enter new task or delete task(delete): ")
    task = input()
    if task == "delete":
        print("Enter task name: ")
        name = input()
        data = pandas.read_csv(filename)
        data = pandas.DataFrame(data)
        data.drop(data[data['Task'] == name].index, inplace=True)
        data.to_csv(filename,index=False,header=True)
        print("-- TASKS LIST --")
        try:
            data = pandas.read_csv(filename)
            print(data)
        except pandas.errors.EmptyDataError:
            print("List is empty")

        return
    row = task.split()

    data1 = {
        'Task': [row[0]],
        'Date': [row[1]],
        'Person': [row[2]]
    }

    dataFrame = pandas.DataFrame(data1)
    dataFrame.to_csv(filename, mode='a', index=False, header=False)
    try:
        data = pandas.read_csv(filename)
        print(data)
    except pandas.errors.EmptyDataError:
        print("List is empty")

if __name__ == '__main__':
    main()
