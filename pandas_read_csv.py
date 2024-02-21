import pandas
import argparse

def csv(filename):
    df = pandas.read_csv(filename)
    # print(df) # or print(df.items)
    # print(df.shape)
    # print(df.keys())
    # print(df['operator_no'])
    print(df.iloc[304])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('excel_file', help='The path of the excel file', type=str)
    args = parser.parse_args()
    csv(args.excel_file)