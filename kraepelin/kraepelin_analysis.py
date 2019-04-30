def number_of_trials(dataframe):
    return dataframe['Blocks'].value_counts().sort_index()

def work_curve_charactor(dataframe):
    for i in range(1,11):
        print("".join(['O' if row['answer']==row['cor_answer'] else 'X' for idx,row in df[df['Blocks']==i].iterrows()]))
